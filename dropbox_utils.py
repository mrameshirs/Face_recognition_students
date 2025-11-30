import streamlit as st
import dropbox
from dropbox.exceptions import AuthError, ApiError
from io import BytesIO
import pandas as pd
from datetime import datetime
from config import (
    DROPBOX_APP_KEY, 
    DROPBOX_APP_SECRET, 
    DROPBOX_REFRESH_TOKEN, 
    LOG_FILE_PATH,
    IMAGES_FOLDER,
    USER_DATA_FILE
)


def get_dropbox_client():
    """Initializes and returns the Dropbox client using a refresh token."""
    try:
        if not all([DROPBOX_APP_KEY, DROPBOX_APP_SECRET, DROPBOX_REFRESH_TOKEN]):
            st.error("Dropbox credentials are not found. Please configure them in Streamlit secrets.")
            return None

        dbx = dropbox.Dropbox(
            app_key=DROPBOX_APP_KEY,
            app_secret=DROPBOX_APP_SECRET,
            oauth2_refresh_token=DROPBOX_REFRESH_TOKEN
        )
        
        # Test the connection
        dbx.users_get_current_account()
        return dbx
        
    except AuthError as e:
        st.error(f"Authentication Error: Please check your Dropbox credentials. Details: {e}")
        return None
    except Exception as e:
        st.error(f"Failed to connect to Dropbox: {e}")
        return None


def create_folder(dbx, folder_path):
    """Creates a folder in Dropbox if it doesn't already exist."""
    try:
        dbx.files_create_folder_v2(folder_path)
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_conflict():
            pass  # Folder already exists
        else:
            st.error(f"Dropbox API error during folder creation: {e}")


def upload_image_to_dropbox(dbx, image_content, user_id):
    """Uploads a user image to Dropbox."""
    try:
        # Ensure the images folder exists
        create_folder(dbx, IMAGES_FOLDER)
        
        # Create the file path
        dropbox_path = f"{IMAGES_FOLDER}/{user_id}.jpg"
        
        # Upload the image
        dbx.files_upload(
            image_content, 
            dropbox_path, 
            mode=dropbox.files.WriteMode('overwrite')
        )
        return True
    except ApiError as e:
        st.error(f"Error uploading image to Dropbox: {e}")
        return False


def download_image_from_dropbox(dbx, user_id):
    """Downloads a user image from Dropbox."""
    try:
        dropbox_path = f"{IMAGES_FOLDER}/{user_id}.jpg"
        _, res = dbx.files_download(path=dropbox_path)
        return res.content
    except ApiError as e:
        if isinstance(e.error, dropbox.files.DownloadError):
            return None
        st.error(f"Error downloading image from Dropbox: {e}")
        return None


def list_all_user_images(dbx):
    """Lists all user image IDs stored in Dropbox."""
    try:
        result = dbx.files_list_folder(IMAGES_FOLDER)
        user_ids = []
        
        for entry in result.entries:
            if isinstance(entry, dropbox.files.FileMetadata):
                # Extract user_id from filename (remove .jpg extension)
                user_id = entry.name.replace('.jpg', '')
                user_ids.append(user_id)
        
        return user_ids
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_not_found():
            # Folder doesn't exist yet
            return []
        st.error(f"Error listing images from Dropbox: {e}")
        return []


def read_user_data_from_dropbox(dbx):
    """Reads user data Excel file from Dropbox."""
    try:
        _, res = dbx.files_download(path=USER_DATA_FILE)
        return pd.read_excel(BytesIO(res.content))
    except ApiError as e:
        if isinstance(e.error, dropbox.files.DownloadError):
            # File doesn't exist, return empty DataFrame
            return pd.DataFrame(columns=['id', 'name', 'dob', 'class'])
        st.error(f"Error reading user data from Dropbox: {e}")
        return pd.DataFrame(columns=['id', 'name', 'dob', 'class'])


def save_user_data_to_dropbox(dbx, df):
    """Saves user data DataFrame to Dropbox as Excel file."""
    try:
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Users')
        
        processed_data = output.getvalue()
        
        dbx.files_upload(
            processed_data, 
            USER_DATA_FILE, 
            mode=dropbox.files.WriteMode('overwrite')
        )
        return True
    except Exception as e:
        st.error(f"Error saving user data to Dropbox: {e}")
        return False


def log_activity(dbx, username, role="Student"):
    """Logs user login activity to Dropbox."""
    try:
        # Read existing log
        try:
            _, res = dbx.files_download(path=LOG_FILE_PATH)
            df_logs = pd.read_excel(BytesIO(res.content))
        except:
            # Create new log file
            df_logs = pd.DataFrame(columns=['Timestamp', 'Username', 'Role'])
        
        # Add new entry
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_log = pd.DataFrame([{
            'Timestamp': timestamp, 
            'Username': username, 
            'Role': role
        }])
        df_logs = pd.concat([df_logs, new_log], ignore_index=True)
        
        # Save back to Dropbox
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_logs.to_excel(writer, index=False, sheet_name='Activity Log')
        
        processed_data = output.getvalue()
        dbx.files_upload(
            processed_data, 
            LOG_FILE_PATH, 
            mode=dropbox.files.WriteMode('overwrite')
        )
        return True
    except Exception as e:
        st.warning(f"Could not log activity: {e}")
        return False


def delete_user_from_dropbox(dbx, user_id):
    """Deletes a user's image from Dropbox."""
    try:
        dropbox_path = f"{IMAGES_FOLDER}/{user_id}.jpg"
        dbx.files_delete_v2(dropbox_path)
        return True
    except ApiError as e:
        st.error(f"Error deleting image from Dropbox: {e}")
        return False


def clear_all_data(dbx):
    """Clears all user data from Dropbox (use with caution!)"""
    try:
        # Delete the entire AI_NANBAN folder
        dbx.files_delete_v2("/AI_NANBAN")
        
        # Recreate empty folders
        create_folder(dbx, "/AI_NANBAN")
        create_folder(dbx, IMAGES_FOLDER)
        
        # Create empty user data file
        empty_df = pd.DataFrame(columns=['id', 'name', 'dob', 'class'])
        save_user_data_to_dropbox(dbx, empty_df)
        
        return True
    except Exception as e:
        st.error(f"Error clearing data: {e}")
        return False
