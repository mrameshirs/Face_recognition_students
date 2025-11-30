import pandas as pd
import streamlit as st
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
            # Ensure all required columns exist
            self._ensure_columns()
        else:
            self.df = self._get_empty_dataframe()

    def _get_empty_dataframe(self):
        """Create empty dataframe with all required columns"""
        return pd.DataFrame(columns=[
            'id', 'name', 'dob', 'gender', 'class', 'blood_group', 'special_talent',
            'address', 'area', 'city', 'pincode',
            'parent_name', 'parent_relation', 'parent_contact', 'parent_occupation',
            'parent_email', 'emergency_contact',
            'previous_school', 'achievements', 'admission_date',
            'medical_conditions', 'additional_notes'
        ])

    def _ensure_columns(self):
        """Ensure all required columns exist in the dataframe"""
        required_columns = [
            'id', 'name', 'dob', 'gender', 'class', 'blood_group', 'special_talent',
            'address', 'area', 'city', 'pincode',
            'parent_name', 'parent_relation', 'parent_contact', 'parent_occupation',
            'parent_email', 'emergency_contact',
            'previous_school', 'achievements', 'admission_date',
            'medical_conditions', 'additional_notes'
        ]
        
        for col in required_columns:
            if col not in self.df.columns:
                self.df[col] = ''

    def insert_user_detail(self, user_data):
        """
        Insert a new user and return the user ID
        user_data should be a dictionary with all user fields
        """
        try:
            # Generate new user ID
            if len(self.df) == 0:
                user_id = 1
            else:
                user_id = int(self.df['id'].max()) + 1
            
            # Create new user record
            new_user = {
                'id': user_id,
                'name': user_data.get('name', ''),
                'dob': user_data.get('dob', ''),
                'gender': user_data.get('gender', ''),
                'class': user_data.get('class', ''),
                'blood_group': user_data.get('blood_group', ''),
                'special_talent': user_data.get('special_talent', ''),
                'address': user_data.get('address', ''),
                'area': user_data.get('area', ''),
                'city': user_data.get('city', ''),
                'pincode': user_data.get('pincode', ''),
                'parent_name': user_data.get('parent_name', ''),
                'parent_relation': user_data.get('parent_relation', ''),
                'parent_contact': user_data.get('parent_contact', ''),
                'parent_occupation': user_data.get('parent_occupation', ''),
                'parent_email': user_data.get('parent_email', ''),
                'emergency_contact': user_data.get('emergency_contact', ''),
                'previous_school': user_data.get('previous_school', ''),
                'achievements': user_data.get('achievements', ''),
                'admission_date': user_data.get('admission_date', ''),
                'medical_conditions': user_data.get('medical_conditions', ''),
                'additional_notes': user_data.get('additional_notes', '')
            }
            
            # Add to DataFrame
            self.df = pd.concat([self.df, pd.DataFrame([new_user])], ignore_index=True)
            
            # Save to Dropbox
            if self.dbx:
                save_user_data_to_dropbox(self.dbx, self.df)
            
            return user_id
        except Exception as e:
            st.error(f"Error inserting user: {e}")
            return None

    def get_user_detail(self, user_id):
        """Get user details by user ID - returns dictionary"""
        try:
            user_id = int(user_id)
            user_row = self.df[self.df['id'] == user_id]
            
            if len(user_row) == 0:
                return None
            
            # Return as dictionary
            return user_row.iloc[0].to_dict()
            
        except Exception as e:
            st.error(f"Error getting user detail: {e}")
            return None

    def get_all_students(self):
        """Get all students as DataFrame"""
        return self.df.copy()

    def get_all_users(self):
        """Get all users - alias for backward compatibility"""
        return self.get_all_students()

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

    def update_user_detail(self, user_id, user_data):
        """Update user details"""
        try:
            user_id = int(user_id)
            
            # Update the row
            for key, value in user_data.items():
                if key in self.df.columns and key != 'id':
                    self.df.loc[self.df['id'] == user_id, key] = value
            
            # Save to Dropbox
            if self.dbx:
                save_user_data_to_dropbox(self.dbx, self.df)
            
            return True
        except Exception as e:
            st.error(f"Error updating user: {e}")
            return False

    def search_students(self, **kwargs):
        """
        Search students by various criteria
        Example: db.search_students(class='Class 10', city='Mumbai')
        """
        result = self.df.copy()
        
        for key, value in kwargs.items():
            if key in result.columns and value:
                result = result[result[key].str.contains(str(value), case=False, na=False)]
        
        return result
