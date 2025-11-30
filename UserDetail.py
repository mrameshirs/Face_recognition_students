class UserDetail:
    def __init__(self, user_data):
        """
        Initialize user detail with dictionary of data
        user_data can be either a dict with all fields or legacy parameters
        """
        if isinstance(user_data, dict):
            # New format with all fields
            self.name = user_data.get('name', '')
            self.dob = user_data.get('dob', '')
            self.gender = user_data.get('gender', '')
            self.class_std = user_data.get('class', '')
            self.blood_group = user_data.get('blood_group', '')
            self.special_talent = user_data.get('special_talent', '')
            self.address = user_data.get('address', '')
            self.area = user_data.get('area', '')
            self.city = user_data.get('city', '')
            self.pincode = user_data.get('pincode', '')
            self.parent_name = user_data.get('parent_name', '')
            self.parent_relation = user_data.get('parent_relation', '')
            self.parent_contact = user_data.get('parent_contact', '')
            self.parent_occupation = user_data.get('parent_occupation', '')
            self.parent_email = user_data.get('parent_email', '')
            self.emergency_contact = user_data.get('emergency_contact', '')
            self.previous_school = user_data.get('previous_school', '')
            self.achievements = user_data.get('achievements', '')
            self.admission_date = user_data.get('admission_date', '')
            self.medical_conditions = user_data.get('medical_conditions', '')
            self.additional_notes = user_data.get('additional_notes', '')
        else:
            # Legacy format for backward compatibility
            self.name = user_data
            self.dob = ''
            self.class_std = ''
