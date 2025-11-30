import streamlit as st
from deepface import DeepFace
import numpy as np
from PIL import Image
from io import BytesIO
from UserDetail import UserDetail
from db import Database
import datetime
import image
from dropbox_utils import log_activity, get_dropbox_client


def register():
    st.markdown("""
        <style>
        .reg-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="reg-header">
            <h2 style="margin:0;">📝 Student Registration Form</h2>
            <p style="margin:5px 0 0 0;">Government High School Suthukeny</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Photo capture section
    st.markdown("### 📸 Student Photograph")
    st.info("📌 Please take a clear, front-facing photo with good lighting")
    
    options = ["Upload", "Camera"]
    method = st.radio("Method", options, horizontal=True)
    
    picture = None
    
    if method == "Camera":
        picture = st.camera_input("Capture photo", key="regCamera", label_visibility='collapsed')
    else:
        picture = st.file_uploader("Upload photo", type=["jpg", "jpeg", "png"], key="regUpload")

    if picture:

        # Display uploaded photo
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(picture, caption="Student Photo", width=200)
        
        with col2:
            # Validate face
            try:
                if hasattr(picture, 'getvalue'):
                    image_bytes = picture.getvalue()
                else:
                    image_bytes = picture.read()
                
                img = Image.open(BytesIO(image_bytes))
                img_array = np.array(img)
                
                with st.spinner("Validating photo..."):
                    try:
                        faces = DeepFace.extract_faces(img_path=img_array, enforce_detection=False)
                        
                        if len(faces) == 0:
                            st.error("⚠️ No face detected! Please upload a clear photo.")
                            return
                        elif len(faces) > 1:
                            st.warning("⚠️ Multiple faces detected. Only the first face will be used.")
                        else:
                            st.success("✅ Face detected successfully!")
                    except Exception as e:
                        st.warning(f"⚠️ Face validation uncertain. You may proceed.")
                        
            except Exception as e:
                st.error(f"Error processing image: {e}")
                return
        
        st.divider()
        
        # Registration Form
        st.markdown("### 📋 Student Information")
        
        with st.form("student_registration_form"):
            # Personal Information
            st.markdown("#### 👤 Personal Details")
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Full Name *", placeholder="Enter student's full name")
                dob = st.date_input(
                    "Date of Birth *",
                    min_value=datetime.datetime(2000, 1, 1),
                    max_value=datetime.datetime.today(),
                    value=datetime.datetime(2010, 1, 1)
                )
                gender = st.selectbox("Gender *", ["Select", "Male", "Female", "Other"])
            
            with col2:
                class_std = st.selectbox(
                    "Class *",
                    ["Select"] + [f"Class {i}" for i in range(1, 13)]
                )
                blood_group = st.selectbox(
                    "Blood Group",
                    ["Select", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
                )
                special_talent = st.text_input("Special Talent", placeholder="e.g., Sports, Music, Art")
            
            # Contact Information
            st.markdown("#### 📍 Contact Details")
            col1, col2 = st.columns(2)
            
            with col1:
                address = st.text_area("Address *", placeholder="Door No, Street Name", height=100)
                area = st.text_input("Area/Locality *", placeholder="Area or Locality name")
            
            with col2:
                city = st.text_input("City *", placeholder="City name", value="Suthukeny")
                pincode = st.text_input("Pincode", placeholder="6-digit pincode")
            
            # Parent/Guardian Information
            st.markdown("#### 👨‍👩‍👧‍👦 Parent/Guardian Details")
            col1, col2 = st.columns(2)
            
            with col1:
                parent_name = st.text_input("Parent/Guardian Name *", placeholder="Full name")
                parent_relation = st.selectbox("Relation *", ["Select", "Father", "Mother", "Guardian"])
                parent_contact = st.text_input("Contact Number *", placeholder="10-digit mobile number")
            
            with col2:
                parent_occupation = st.text_input("Occupation", placeholder="Parent's occupation")
                parent_email = st.text_input("Email Address", placeholder="parent@example.com")
                emergency_contact = st.text_input("Emergency Contact", placeholder="Alternative contact number")
            
            # Academic Information
            st.markdown("#### 🎓 Academic Details")
            col1, col2 = st.columns(2)
            
            with col1:
                previous_school = st.text_input("Previous School", placeholder="If applicable")
                achievements = st.text_area(
                    "Achievements/Awards",
                    placeholder="List any academic or extracurricular achievements",
                    height=100
                )
            
            with col2:
                admission_date = st.date_input(
                    "Date of Admission",
                    min_value=datetime.datetime(2020, 1, 1),
                    max_value=datetime.datetime.today(),
                    value=datetime.datetime.today()
                )
                medical_conditions = st.text_area(
                    "Medical Conditions (if any)",
                    placeholder="Any medical conditions we should know about",
                    height=100
                )
            
            # Additional Notes
            additional_notes = st.text_area(
                "Additional Notes",
                placeholder="Any other information you'd like to share",
                height=80
            )
            
            # Submit Button
            st.markdown("---")
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                submit = st.form_submit_button("✅ Register Student", use_container_width=True)
=======
        # Validate that the image contains a face using DeepFace
        try:
            if hasattr(picture, 'getvalue'):
                image_bytes = picture.getvalue()
            else:
                image_bytes = picture.read()
            
            # Convert to numpy array for DeepFace
            img = Image.open(BytesIO(image_bytes))
            img_array = np.array(img)
            
            # Try to extract faces using DeepFace
            try:
                faces = DeepFace.extract_faces(img_path=img_array, enforce_detection=False)
                
                if len(faces) == 0:
                    st.error("⚠️ No face detected in the image. Please upload a clear photo showing your face.")
                    return
                elif len(faces) > 1:
                    st.warning("⚠️ Multiple faces detected. Please upload a photo with only one person.")
                    # Continue anyway, we'll use the first face
            except Exception as e:
                # If face detection fails, show warning but allow to continue
                st.warning(f"⚠️ Face validation uncertain. Proceeding anyway...")
                
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
>>>>>>> b3979ae0ae713a63f890ee71494a09e7efcf8416
        
        # Form Validation and Submission
        if submit:
            # Validate required fields
            errors = []
            
            if not name or len(name.strip()) < 2:
                errors.append("Please enter a valid name")
            if gender == "Select":
                errors.append("Please select gender")
            if class_std == "Select":
                errors.append("Please select class")
            if not address or len(address.strip()) < 5:
                errors.append("Please enter a valid address")
            if not area:
                errors.append("Please enter area/locality")
            if not city:
                errors.append("Please enter city")
            if not parent_name or len(parent_name.strip()) < 2:
                errors.append("Please enter parent/guardian name")
            if parent_relation == "Select":
                errors.append("Please select parent relation")
            if not parent_contact or len(parent_contact) < 10:
                errors.append("Please enter a valid contact number")
            
            if errors:
                for error in errors:
                    st.error(f"❌ {error}")
            else:
                with st.spinner("Registering student..."):
                    # Create user detail object with all fields
                    user_data = {
                        'name': name.strip(),
                        'dob': str(dob),
                        'gender': gender,
                        'class': class_std,
                        'blood_group': blood_group if blood_group != "Select" else "",
                        'special_talent': special_talent.strip(),
                        'address': address.strip(),
                        'area': area.strip(),
                        'city': city.strip(),
                        'pincode': pincode.strip(),
                        'parent_name': parent_name.strip(),
                        'parent_relation': parent_relation,
                        'parent_contact': parent_contact.strip(),
                        'parent_occupation': parent_occupation.strip(),
                        'parent_email': parent_email.strip(),
                        'emergency_contact': emergency_contact.strip(),
                        'previous_school': previous_school.strip(),
                        'achievements': achievements.strip(),
                        'admission_date': str(admission_date),
                        'medical_conditions': medical_conditions.strip(),
                        'additional_notes': additional_notes.strip()
                    }
                    
                    # Insert user details
                    user_id = insert_user_detail(user_data)
                    
                    if user_id:
                        # Save image to Dropbox
                        if image.save_image_to_dropbox(picture, str(user_id)):
                            st.success(f"🎉 Student registered successfully! Student ID: {user_id}")
                            st.balloons()
                            
                            # Show summary
                            with st.expander("📄 Registration Summary", expanded=True):
                                st.markdown(f"""
                                **Student ID:** {user_id}  
                                **Name:** {name}  
                                **Class:** {class_std}  
                                **Parent/Guardian:** {parent_name} ({parent_relation})  
                                **Contact:** {parent_contact}  
                                **Admission Date:** {admission_date}
                                """)
                            
                            # Log activity
                            dbx = get_dropbox_client()
                            if dbx:
                                log_activity(dbx, name, "Student Registration")
                        else:
                            st.error("❌ Failed to save photo. Please try again.")
                    else:
                        st.error("❌ Registration failed. Please try again.")


def insert_user_detail(user_data):
    """Insert user details and return user ID"""
    try:
        db = Database()
        user_id = db.insert_user_detail(user_data)
        return user_id
    except Exception as e:
        st.error(f"Error inserting user detail: {e}")
        return None
