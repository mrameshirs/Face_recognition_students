import streamlit as st
import os

# Dropbox Configuration
# For local development, use environment variables
# For Streamlit Cloud, use st.secrets

def get_secret(key, default=None):
    """Get secret from Streamlit secrets or environment variable"""
    try:
        return st.secrets.get(key, os.getenv(key, default))
    except:
        return os.getenv(key, default)

# Dropbox credentials
DROPBOX_APP_KEY = get_secret("DROPBOX_APP_KEY", "")
DROPBOX_APP_SECRET = get_secret("DROPBOX_APP_SECRET", "")
DROPBOX_REFRESH_TOKEN = get_secret("DROPBOX_REFRESH_TOKEN", "")

# Dropbox paths
IMAGES_FOLDER = "/AI_NANBAN/known_users"
USER_DATA_FILE = "/AI_NANBAN/user_data.xlsx"
LOG_FILE_PATH = "/AI_NANBAN/activity_log.xlsx"
