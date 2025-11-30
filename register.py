import streamlit as st
from deepface import DeepFace  # ✅ ADD THIS
import numpy as np
from PIL import Image
from io import BytesIOfrom UserDetail import UserDetail
from db import Database
import datetime
import image
from dropbox_utils import log_activity, get_dropbox_client


def register():
    st.write('Take a closeup and legible photo of student face')
    options = ["Camera", "Upload"]
    initial_selection = options.index("Upload")
    method = st.radio("Method", options, index=initial_selection)
    
    picture = None
    
    if method == "Camera":
        picture = st.camera_input("picture", key="loginPic", label_visibility='hidden')
    if method == "Upload":
        picture = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

    if picture:
        # Validate that the image contains a face
        try:
            if hasattr(picture, 'getvalue'):
                image_bytes = picture.getvalue()
            else:
                image_bytes = picture.read()
            
            from io import BytesIO
            import face_recognition as fr
            
            img_array = fr.load_image_file(BytesIO(image_bytes))
            face_encodings = fr.face_encodings(img_array)
            
            if len(face_encodings) == 0:
                st.error("⚠️ No face detected in the image. Please upload a clear photo showing your face.")
                return
            elif len(face_encodings) > 1:
                st.warning("⚠️ Multiple faces detected. Please upload a photo with only one person.")
                # Continue anyway, we'll use the first face
        except Exception as e:
            st.error(f"Error validating image: {e}")
            return
        
        form = st.form("Register")
        name = form.text_input("Student name")
        min_date = datetime.datetime(1900, 1, 1)
        max_date = datetime.datetime.today()
        dob = form.date_input("Date of Birth", min_value=min_date, max_value=max_date)
        city = form.text_input("Class")
        submit = form.form_submit_button("submit")
        
        if submit:
            if not name or not dob or not city:
                st.error("Please enter your name, DOB and class")
            else:
                with st.spinner("Registering student..."):
                    # Insert user details into database
                    user_id = insert_user_detail(city, dob, name)
                    
                    if user_id:
                        # Save image to Dropbox
                        if image.save_image_to_dropbox(picture, str(user_id)):
                            st.success(f"✅ Student registered successfully! User ID: {user_id}")
                            
                            # Log the registration activity
                            dbx = get_dropbox_client()
                            if dbx:
                                log_activity(dbx, name, "Student Registration")
                        else:
                            st.error("Failed to save image to Dropbox. Please try again.")
                    else:
                        st.error("Failed to register student. Please try again.")


def insert_user_detail(city, dob, name):
    """Insert user details and return user ID"""
    try:
        user_detail = UserDetail(name, dob, city)
        db = Database()
        user_id = db.insert_user_detail(user_detail)
        return user_id
    except Exception as e:
        st.error(f"Error inserting user detail: {e}")
        return None
