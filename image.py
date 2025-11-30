import os
import streamlit as st
from dropbox_utils import (
    get_dropbox_client,
    upload_image_to_dropbox,
    download_image_from_dropbox,
    list_all_user_images
)
from io import BytesIO
from PIL import Image

# Use DeepFace instead of face_recognition (faster on Streamlit Cloud)
try:
    from deepface import DeepFace
    USE_DEEPFACE = True
except ImportError:
    # Fallback to face_recognition if available
    import face_recognition as fr
    USE_DEEPFACE = False


def save_image_locally(picture, directory, filename):
    """Save image locally (for temporary processing)"""
    if not os.path.exists(directory):
        os.makedirs(directory)

    if picture:
        with open(os.path.join(directory, filename + ".jpg"), "wb") as f:
            f.write(picture.getvalue())


def save_image_to_dropbox(picture, user_id):
    """Save image directly to Dropbox"""
    dbx = get_dropbox_client()
    if not dbx:
        st.error("Could not connect to Dropbox")
        return False
    
    try:
        # Get the image bytes
        if hasattr(picture, 'getvalue'):
            image_bytes = picture.getvalue()
        else:
            image_bytes = picture
        
        # Upload to Dropbox
        return upload_image_to_dropbox(dbx, image_bytes, user_id)
    except Exception as e:
        st.error(f"Error saving image to Dropbox: {e}")
        return False


def delete_image(image_path):
    """Delete local image file"""
    if os.path.exists(image_path):
        os.remove(image_path)


def get_all_images(directory):
    """Get all local images"""
    if not os.path.exists(directory):
        return []
    return [file for file in os.listdir(directory) if file.endswith('.jpg') or file.endswith('.png')]


def compare_face_with_dropbox(unknown_image):
    """
    Compare an unknown face with all faces stored in Dropbox.
    Uses DeepFace for better cloud compatibility.
    Returns (is_match, user_id) tuple.
    """
    dbx = get_dropbox_client()
    if not dbx:
        st.error("Could not connect to Dropbox")
        return False, -1
    
    try:
        # Get all user IDs from Dropbox
        user_ids = list_all_user_images(dbx)
        
        if not user_ids:
            st.warning("No registered users found in Dropbox")
            return False, -1
        
        # Save unknown image temporarily
        if hasattr(unknown_image, 'getvalue'):
            unknown_image_bytes = unknown_image.getvalue()
        else:
            unknown_image_bytes = unknown_image
        
        temp_unknown = "temp_unknown.jpg"
        with open(temp_unknown, 'wb') as f:
            f.write(unknown_image_bytes)
        
        if USE_DEEPFACE:
            # Use DeepFace for comparison
            return compare_with_deepface(dbx, user_ids, temp_unknown)
        else:
            # Fallback to face_recognition
            return compare_with_face_recognition(dbx, user_ids, unknown_image_bytes, temp_unknown)
        
    except Exception as e:
        st.error(f"Error during face comparison: {e}")
        # Clean up
        if os.path.exists(temp_unknown):
            os.remove(temp_unknown)
        return False, -1


def compare_with_deepface(dbx, user_ids, temp_unknown):
    """Compare faces using DeepFace"""
    try:
        # Compare with each user
        for user_id in user_ids:
            known_image_bytes = download_image_from_dropbox(dbx, user_id)
            
            if not known_image_bytes:
                continue
            
            # Save known image temporarily
            temp_known = f"temp_known_{user_id}.jpg"
            with open(temp_known, 'wb') as f:
                f.write(known_image_bytes)
            
            try:
                # Use DeepFace to verify
                result = DeepFace.verify(
                    temp_unknown, 
                    temp_known,
                    model_name='VGG-Face',  # Fast and accurate
                    enforce_detection=False,  # More lenient
                    distance_metric='cosine'
                )
                
                # Clean up temp file
                os.remove(temp_known)
                
                # If match found (threshold can be adjusted)
                if result['verified'] or result['distance'] < 0.4:
                    os.remove(temp_unknown)
                    st.success(f"Match found! User ID: {user_id}")
                    return True, user_id
                    
            except Exception as e:
                # Clean up and continue to next user
                if os.path.exists(temp_known):
                    os.remove(temp_known)
                continue
        
        # No match found
        if os.path.exists(temp_unknown):
            os.remove(temp_unknown)
        return False, -1
        
    except Exception as e:
        st.error(f"Error in DeepFace comparison: {e}")
        if os.path.exists(temp_unknown):
            os.remove(temp_unknown)
        return False, -1


def compare_with_face_recognition(dbx, user_ids, unknown_image_bytes, temp_unknown):
    """Fallback: Compare faces using face_recognition library"""
    try:
        unknown_img = Image.open(BytesIO(unknown_image_bytes))
        unknown_img_array = fr.load_image_file(BytesIO(unknown_image_bytes))
        
        # Find face encodings in unknown image
        unknown_face_encodings = fr.face_encodings(unknown_img_array)
        
        if len(unknown_face_encodings) == 0:
            st.error("No face detected in the uploaded image")
            os.remove(temp_unknown)
            return False, -1
        
        unknown_face_encoding = unknown_face_encodings[0]
        
        # Compare with each user in Dropbox
        for user_id in user_ids:
            known_image_bytes = download_image_from_dropbox(dbx, user_id)
            
            if not known_image_bytes:
                continue
            
            # Load and encode the known image
            known_img_array = fr.load_image_file(BytesIO(known_image_bytes))
            known_face_encodings = fr.face_encodings(known_img_array)
            
            if len(known_face_encodings) == 0:
                continue
            
            known_face_encoding = known_face_encodings[0]
            
            # Calculate similarity
            similarity = fr.face_distance([unknown_face_encoding], known_face_encoding)
            
            # Set threshold
            threshold = 0.4
            
            if similarity[0] < threshold:
                st.success(f"Match found! User ID: {user_id}")
                os.remove(temp_unknown)
                return True, user_id
        
        # No match found
        os.remove(temp_unknown)
        return False, -1
        
    except Exception as e:
        st.error(f"Error in face_recognition comparison: {e}")
        if os.path.exists(temp_unknown):
            os.remove(temp_unknown)
        return False, -1


def compare_faces_in_directory(known_image_dir, unknown_image_dir):
    """
    Legacy function for local directory comparison.
    Kept for backward compatibility.
    """
    if not USE_DEEPFACE:
        # Use face_recognition if available
        known_image_files = get_all_images(known_image_dir)
        unknown_image_files = get_all_images(unknown_image_dir)

        if not unknown_image_files:
            return False, -1

        for j, known_image_file in enumerate(known_image_files):
            unknown_img_path = os.path.join(unknown_image_dir, unknown_image_files[0])
            known_img_path = os.path.join(known_image_dir, known_image_file)
            image1 = fr.load_image_file(unknown_img_path)
            image2 = fr.load_image_file(known_img_path)

            face_encodings1 = fr.face_encodings(image1)
            face_encodings2 = fr.face_encodings(image2)

            if len(face_encodings1) > 0 and len(face_encodings2) > 0:
                face_encoding1 = face_encodings1[0]
                face_encoding2 = face_encodings2[0]
                similarity = fr.face_distance([face_encoding1], face_encoding2)
                threshold = 0.4
                user_id = os.path.splitext(known_image_file)[0]
                if similarity[0] < threshold:
                    return True, user_id

    return False, -1
