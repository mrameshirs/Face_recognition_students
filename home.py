import streamlit as st

def home():
    # Custom CSS for colorful school homepage
    st.markdown("""
        <style>
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            color: white;
            margin-bottom: 30px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        }
        .school-name {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .subtitle {
            font-size: 24px;
            margin-bottom: 5px;
            color: #ffd700;
        }
        .tagline {
            font-size: 18px;
            font-style: italic;
            margin-top: 10px;
        }
        .feature-card {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 25px;
            border-radius: 12px;
            margin: 15px 0;
            color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        .feature-card h3 {
            margin-top: 0;
            font-size: 22px;
        }
        .info-box {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            color: white;
        }
        .credits {
            background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-top: 30px;
            color: white;
            font-size: 16px;
        }
        .emoji {
            font-size: 40px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Main Header
    st.markdown("""
        <div class="main-header">
            <div class="school-name">🏫 Government High School Suthukeny</div>
            <div class="subtitle">Student Management Information System</div>
            <div class="tagline">✨ AI-Based Facial Recognition System ✨</div>
        </div>
    """, unsafe_allow_html=True)

    # Welcome Section with columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <div class="emoji">🎓</div>
                <h3>Smart Registration</h3>
                <p>Quick and secure student registration with facial recognition technology</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-card">
                <div class="emoji">📊</div>
                <h3>Analytics & Reports</h3>
                <p>Comprehensive student data analysis and visual insights</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="feature-card">
                <div class="emoji">🔐</div>
                <h3>Secure Access</h3>
                <p>Face-based authentication for enhanced security</p>
            </div>
        """, unsafe_allow_html=True)

    # System Features
    st.markdown("""
        <div class="info-box">
            <h2 style="margin-top:0;">🌟 System Features</h2>
            <ul style="font-size: 16px; line-height: 1.8;">
                <li><strong>AI-Powered Face Recognition:</strong> Instant student identification using advanced deep learning</li>
                <li><strong>Comprehensive Student Profiles:</strong> Detailed information including academics, talents, and achievements</li>
                <li><strong>Smart Search & Filtering:</strong> Find student records quickly using multiple search criteria</li>
                <li><strong>Visual Analytics:</strong> Interactive charts and graphs for data-driven insights</li>
                <li><strong>Cloud Storage:</strong> Secure data storage with Dropbox integration</li>
                <li><strong>Real-time Updates:</strong> Instant synchronization across all devices</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # About the System
    st.markdown("## 📖 About This System")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            This cutting-edge **Student Management Information System** leverages artificial intelligence 
            to provide seamless student registration, authentication, and management capabilities.
            
            **Key Technologies:**
            - 🤖 **DeepFace AI** for facial recognition
            - ☁️ **Dropbox Cloud** for secure data storage
            - 📊 **Advanced Analytics** for insights
            - 🎨 **Modern UI/UX** for easy navigation
            
            **Benefits:**
            - ⚡ Fast registration process
            - 🔒 Enhanced security through biometric authentication
            - 📈 Data-driven decision making
            - 🌐 Accessible from anywhere
        """)
    
    with col2:
        # School logo or image placeholder
        st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 30px; border-radius: 15px; text-align: center; color: white;">
                <div style="font-size: 80px;">🏫</div>
                <h3>Excellence in Education</h3>
                <p>Empowering Students with Technology</p>
            </div>
        """, unsafe_allow_html=True)

    # Credits Section
    st.markdown("""
        <div class="credits">
            <h3 style="margin-top: 0;">👨‍🎓 Developed by Students</h3>
            <p style="font-size: 18px; margin: 10px 0;">
                <strong>An initiative by the Students of Government High School Suthukeny</strong>
            </p>
            <p style="font-size: 14px; margin-top: 15px;">
                💡 Innovation | 🎯 Excellence | 🚀 Future-Ready
            </p>
            <p style="font-size: 12px; margin-top: 10px; opacity: 0.9;">
                For queries and suggestions, contact: school@suthukeny.edu
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Quick Start Guide
    with st.expander("📘 Quick Start Guide", expanded=False):
        st.markdown("""
            ### For Students:
            1. **Registration:** Click on "Register Student" tab and complete the form
            2. **Upload Photo:** Capture or upload a clear face photo
            3. **Login:** Use the "Student Login" tab for face-based authentication
            
            ### For Administrators:
            1. **View Reports:** Access the "Reports" tab to search and view student records
            2. **Analytics:** Check the "Graphs" tab for visual insights
            3. **Manage Data:** Use filters to find specific student information
            
            ### Tips:
            - 📸 Ensure good lighting for photo capture
            - 😊 Face the camera directly
            - 🎯 Fill all required fields during registration
        """)
