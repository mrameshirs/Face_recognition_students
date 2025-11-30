import pandas as pd
import streamlit as st
from UserDetail import UserDetail
from dropbox_utils import (
    get_dropbox_client,
    read_user_data_from_dropbox,
    save_user_data_to_dropbox
)


class Database:
    def __init__(self):
        """Initialize database connection to Dropbox"""
        self.dbx = get_dropbox_client()
        if self.dbx:
            self.df = read_user_data_from_dropbox(self.dbx)
        else:
            # Fallback to empty DataFrame if Dropbox is not available
            self.df = pd.DataFrame(columns=['id', 'name', 'dob', 'class'])

    def insert_user_detail(self, userDetail):
        """Insert a new user and return the user ID"""
        try:
            # Generate new user ID
            if len(self.df) == 0:
                user_id = 1
            else:
                user_id = int(self.df['id'].max()) + 1
            
            # Create new user record
            new_user = pd.DataFrame([{
                'id': user_id,
                'name': userDetail.student_name,
                'dob': str(userDetail.dob),
                'class': userDetail.class_std
            }])
            
            # Add to DataFrame
            self.df = pd.concat([self.df, new_user], ignore_index=True)
            
            # Save to Dropbox
            if self.dbx:
                save_user_data_to_dropbox(self.dbx, self.df)
            
            return user_id
        except Exception as e:
            st.error(f"Error inserting user: {e}")
            return None

    def get_user_detail(self, user_id):
        """Get user details by user ID"""
        try:
            # Convert user_id to int for comparison
            user_id = int(user_id)
            
            # Filter the DataFrame
            user_row = self.df[self.df['id'] == user_id]
            
            if len(user_row) == 0:
                return None
            
            # Extract user data
            row = user_row.iloc[0]
            name = row['name']
            dob = row['dob']
            class_std = row['class']
            
            # Create UserDetail object
            user_detail = UserDetail(name, dob, class_std)
            return user_detail
            
        except Exception as e:
            st.error(f"Error getting user detail: {e}")
            return None

    def get_all_users(self):
        """Get all users"""
        return self.df

    def delete_user(self, user_id):
        """Delete a user by ID"""
        try:
            user_id = int(user_id)
            self.df = self.df[self.df['id'] != user_id]
            
            # Save to Dropbox
            if self.dbx:
                save_user_data_to_dropbox(self.dbx, self.df)
            
            return True
        except Exception as e:
            st.error(f"Error deleting user: {e}")
            return False

    def update_user_detail(self, user_id, userDetail):
        """Update user details"""
        try:
            user_id = int(user_id)
            
            # Update the row
            self.df.loc[self.df['id'] == user_id, 'name'] = userDetail.student_name
            self.df.loc[self.df['id'] == user_id, 'dob'] = str(userDetail.dob)
            self.df.loc[self.df['id'] == user_id, 'class'] = userDetail.class_std
            
            # Save to Dropbox
            if self.dbx:
                save_user_data_to_dropbox(self.dbx, self.df)
            
            return True
        except Exception as e:
            st.error(f"Error updating user: {e}")
            return False
