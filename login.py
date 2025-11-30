import streamlit as st
import image
from db import Database
from dropbox_utils import log_activity, get_dropbox_client


def login():
    st.write("📸 Capture your photo to login")
    
    picture = st.camera_input("picture", key="registercam", label_visibility='hidden')

    if picture:
        with st.spinner("Verifying your identity..."):
            # Compare face with images stored in Dropbox
            is_match, user_id = image.compare_face_with_dropbox(picture)

            if is_match:
                # Get user details from database
                db = Database()
                user_detail = db.get_user_detail(user_id)
                
                if user_detail:
                    st.success(f"✅ Welcome back, {user_detail.student_name}!")
                    
                    # Display user information
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Name", user_detail.student_name)
                    with col2:
                        st.metric("Class", user_detail.class_std)
                    with col3:
                        st.metric("Date of Birth", user_detail.dob)
                    
                    # Log the login activity
                    dbx = get_dropbox_client()
                    if dbx:
                        log_activity(dbx, user_detail.student_name, "Student Login")
                    
                    # Store login state in session
                    st.session_state['logged_in'] = True
                    st.session_state['user_id'] = user_id
                    st.session_state['user_name'] = user_detail.student_name
                    st.session_state['user_class'] = user_detail.class_std
                    
                else:
                    st.error("User details not found in database")
            else:
                st.error("❌ No matching face found. Please register first or try again.")
