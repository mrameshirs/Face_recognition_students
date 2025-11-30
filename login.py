import streamlit as st
import image
from db import Database
from dropbox_utils import log_activity, get_dropbox_client, download_image_from_dropbox
from PIL import Image
from io import BytesIO


def login():
    st.markdown("""
        <style>
        .login-header {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="login-header">
            <h2 style="margin:0;">🔐 Student Login</h2>
            <p style="margin:5px 0 0 0;">Face Recognition Authentication</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("📸 Please position your face clearly in the camera frame")
    
    picture = st.camera_input("Capture your photo", key="loginCamera", label_visibility='collapsed')

    if picture:
        with st.spinner("🔍 Verifying your identity..."):
            # Compare face with images stored in Dropbox
            is_match, user_id = image.compare_face_with_dropbox(picture)

            if is_match:
                # Get user details from database
                db = Database()
                user_detail = db.get_user_detail(user_id)
                
                if user_detail:
                    # user_detail is now a dictionary, not an object
                    student_name = user_detail.get('name', 'Unknown')
                    student_class = user_detail.get('class', 'N/A')
                    student_dob = user_detail.get('dob', 'N/A')
                    student_gender = user_detail.get('gender', 'N/A')
                    student_city = user_detail.get('city', 'N/A')
                    
                    st.success(f"✅ Welcome back, {student_name}!")
                    st.balloons()
                    
                    # Display student photo at the top
                    st.markdown("### 📸 Student Photo")
                    photo_col1, photo_col2, photo_col3 = st.columns([1, 2, 1])
                    
                    with photo_col2:
                        if dbx:
                            try:
                                img_bytes = download_image_from_dropbox(dbx, str(user_id))
                                if img_bytes and len(img_bytes) > 0:
                                    img_buffer = BytesIO(img_bytes)
                                    img = Image.open(img_buffer)
                                    st.image(img, caption=f"{student_name} - ID: {user_id}", use_column_width=True)
                                else:
                                    st.info("📷 Photo not available in database")
                            except Exception as e:
                                st.info("📷 Photo not available")
                        else:
                            st.info("📷 Photo not available")
                    
                    st.markdown("---")
                    
                    # Display user information in a nice card
                    st.markdown("### 👤 Student Information")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("📛 Name", student_name)
                    with col2:
                        st.metric("📚 Class", student_class)
                    with col3:
                        st.metric("🎂 Date of Birth", student_dob)
                    with col4:
                        st.metric("🆔 Student ID", user_id)
                    
                    # Additional details in expander
                    with st.expander("📋 More Details", expanded=True):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown("**Personal Information:**")
                            st.markdown(f"- **Gender:** {student_gender}")
                            st.markdown(f"- **Blood Group:** {user_detail.get('blood_group', 'N/A')}")
                            st.markdown(f"- **Special Talent:** {user_detail.get('special_talent', 'N/A')}")
                            st.markdown(f"- **City:** {student_city}")
                        
                        with col2:
                            st.markdown("**Contact Information:**")
                            st.markdown(f"- **Parent:** {user_detail.get('parent_name', 'N/A')}")
                            st.markdown(f"- **Relation:** {user_detail.get('parent_relation', 'N/A')}")
                            st.markdown(f"- **Contact:** {user_detail.get('parent_contact', 'N/A')}")
                            st.markdown(f"- **Emergency:** {user_detail.get('emergency_contact', 'N/A')}")
                    
                    # Log the login activity
                    dbx = get_dropbox_client()
                    if dbx:
                        log_activity(dbx, student_name, "Student Login")
                    
                    # Store login state in session
                    st.session_state['logged_in'] = True
                    st.session_state['user_id'] = user_id
                    st.session_state['user_name'] = student_name
                    st.session_state['user_class'] = student_class
                    st.session_state['login_time'] = st.session_state.get('login_time', 
                                                                          str(st.session_state.get('login_time', 'Just now')))
                    
                    st.success("✅ Login successful! Session active.")
                    
                else:
                    st.error("❌ User details not found in database")
            else:
                st.error("❌ No matching face found. Please register first or try again.")
                st.info("💡 Tip: Make sure you're registered and your face is clearly visible")










































