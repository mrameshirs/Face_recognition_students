import os
import streamlit as st
import encdec
from dropbox_utils import get_dropbox_client, clear_all_data


def clear():
    st.warning("⚠️ This will delete ALL user data from Dropbox!")
    password = st.text_input("Enter admin password", type="password")
    clearbtn = st.button("Clear All Data")
    
    if clearbtn and password == encdec.encdec():
        with st.spinner("Clearing all data from Dropbox..."):
            try:
                # Get Dropbox client
                dbx = get_dropbox_client()
                
                if dbx:
                    # Clear all data from Dropbox
                    if clear_all_data(dbx):
                        st.success("✅ All data cleared from Dropbox successfully!")
                    else:
                        st.error("Failed to clear data from Dropbox")
                else:
                    st.error("Could not connect to Dropbox")
                
            except Exception as e:
                st.error(f"Error: {e}")
    
    elif clearbtn and password != encdec.encdec():
        st.error("❌ Password entered is incorrect")
