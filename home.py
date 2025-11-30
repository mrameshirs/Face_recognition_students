import streamlit as st

def home():
    st.markdown("""
        <style>
        .title {
            color: purple;
            font-size: 30px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Load GIF image from a trusted source
    gif_url = "https://articleft.com/wp-content/uploads/2023/06/040823_chatgpt_feat.gif"
    st.image(gif_url, width=400)  # Adjust width as needed

    # Split markdown for separate rendering
    intro_text = """
        <h1 class="title">AI NANBAN</h1>
        <p>AI Personalised Coach application for CBSE Classs using face recognition.</p>
    """

    features_text = """
        <h2>Features</h2>
        <ul>
            <li>Face detection and recognition of Students</li>
            <li>Customised Quiz Generation for Students based on CBSE Class notes</li>
            <li>Personalised Score tracking of students for progress tracking</li>
        </ul>
        <p>An Initiative by Koodapakkam school, Suggestions are Welcome to email id</p>
    """

    st.markdown(intro_text, unsafe_allow_html=True)
    st.markdown("""<h2>Introduction</h2>""", unsafe_allow_html=True)
    st.markdown(features_text, unsafe_allow_html=True)