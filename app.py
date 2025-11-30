import streamlit as st

# Import all modules
import clear
import home_new as home
import register_new as register
import login
import reports
import graphs

# Page configuration
st.set_page_config(
    page_title="Government High School Suthukeny - Student Management",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        background-color: #f0f2f6;
        border-radius: 10px 10px 0 0;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Create tabs
homeTab, registerTab, loginTab, reportsTab, graphsTab, clearTab = st.tabs([
    "🏠 Home",
    "📝 Register Student", 
    "🔐 Student Login",
    "📊 Reports",
    "📈 Graphs",
    "🗑️ Clear Data"
])

with homeTab:
    home.home()

with registerTab:
    register.register()

with loginTab:
    login.login()

with reportsTab:
    reports.reports()

with graphsTab:
    graphs.graphs()

with clearTab:
    clear.clear()
