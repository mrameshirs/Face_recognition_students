# AI NANBAN - Face Recognition App with Dropbox Integration

## Overview
This is an AI-powered personalized coaching application for CBSE students using face recognition, now with **Dropbox cloud storage integration** for scalable data management.

## New Features with Dropbox Integration

### ✨ What's New
- **Cloud Storage**: All student photos and data stored in Dropbox
- **Scalability**: No local storage limits - store unlimited student records
- **Accessibility**: Access data from anywhere, perfect for cloud deployment
- **Activity Logging**: Automatic logging of registrations and logins
- **Data Management**: Easy backup and recovery of student data

### 📁 File Structure in Dropbox
```
/AI_NANBAN/
├── known_users/          # Student face images (user_id.jpg)
├── user_data.xlsx        # Student information database
└── activity_log.xlsx     # Login/registration activity logs
```

## Setup Instructions

### 1. Dropbox App Setup

#### Step 1: Create a Dropbox App
1. Go to https://www.dropbox.com/developers/apps
2. Click "Create app"
3. Choose:
   - API: Scoped access
   - Access: Full Dropbox
   - Name: "AI-NANBAN" (or your preferred name)
4. Click "Create app"

#### Step 2: Configure App Permissions
In your app settings, go to the "Permissions" tab and enable:
- `files.metadata.write`
- `files.metadata.read`
- `files.content.write`
- `files.content.read`

Click "Submit" to save permissions.

#### Step 3: Get App Credentials
1. Go to the "Settings" tab
2. Note down your **App key** and **App secret**

#### Step 4: Generate Refresh Token
Use the following Python script to generate a refresh token:

```python
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

APP_KEY = 'your_app_key_here'
APP_SECRET = 'your_app_secret_here'

auth_flow = DropboxOAuth2FlowNoRedirect(
    APP_KEY, 
    APP_SECRET,
    token_access_type='offline'
)

authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click 'Allow' (you might have to log in first)")
print("3. Copy the authorization code.")

auth_code = input("Enter the authorization code here: ").strip()

try:
    oauth_result = auth_flow.finish(auth_code)
    print("\nRefresh Token:", oauth_result.refresh_token)
    print("\nSave this refresh token securely!")
except Exception as e:
    print('Error: %s' % (e,))
```

Save this refresh token - you'll need it for deployment.

### 2. Local Development Setup

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Configure Secrets
1. Create `.streamlit/secrets.toml` file in your project root:
```toml
DROPBOX_APP_KEY = "your_app_key_here"
DROPBOX_APP_SECRET = "your_app_secret_here"
DROPBOX_REFRESH_TOKEN = "your_refresh_token_here"
```

2. Add `.streamlit/secrets.toml` to your `.gitignore` to prevent committing secrets

#### Run the App
```bash
streamlit run app.py
```

### 3. Streamlit Cloud Deployment

#### Step 1: Push to GitHub
1. Create a new repository on GitHub
2. Add all project files EXCEPT `.streamlit/secrets.toml`
3. Make sure `.gitignore` includes:
```
.streamlit/secrets.toml
*.pyc
__pycache__/
db.sqlite
known_user/
unknown_user/
```

#### Step 2: Deploy to Streamlit Cloud
1. Go to https://share.streamlit.io/
2. Click "New app"
3. Connect your GitHub repository
4. Select the repository and branch
5. Set main file path to `app.py`

#### Step 3: Add Secrets in Streamlit Cloud
1. In your deployed app dashboard, click "Settings"
2. Go to "Secrets" section
3. Add your secrets in TOML format:
```toml
DROPBOX_APP_KEY = "your_app_key_here"
DROPBOX_APP_SECRET = "your_app_secret_here"
DROPBOX_REFRESH_TOKEN = "your_refresh_token_here"
```
4. Click "Save"

#### Step 4: Reboot the App
Click "Reboot" to apply the secrets.

## Usage Guide

### Register a New Student
1. Go to "Register Student" tab
2. Choose "Camera" or "Upload" method
3. Capture/upload a clear face photo
4. Fill in student details:
   - Name
   - Date of Birth
   - Class
5. Click "Submit"
6. The photo and data are automatically saved to Dropbox

### Student Login
1. Go to "Student Login" tab
2. Capture your photo using the camera
3. The system will match your face with registered students
4. If matched, your details will be displayed
5. Login activity is logged automatically

### Admin Functions
**Clear All Data** (use with caution!)
1. Go to "Clear" tab
2. Enter admin password
3. Click "Clear All Data"
4. This removes all student data from Dropbox

## File Descriptions

### Core Files
- `app.py` - Main Streamlit application entry point
- `config.py` - Configuration and secrets management
- `dropbox_utils.py` - Dropbox integration functions
- `db.py` - Database operations using Dropbox storage
- `image.py` - Image processing and face recognition
- `register.py` - Student registration interface
- `login.py` - Student login interface
- `clear.py` - Admin data clearing interface
- `home.py` - Home page interface

### Supporting Files
- `UserDetail.py` - User data model
- `encdec.py` - Password encryption utilities
- `requirements.txt` - Python dependencies

## Security Notes

⚠️ **Important Security Practices:**

1. **Never commit secrets** to version control
2. **Use environment variables** or Streamlit secrets for credentials
3. **Restrict Dropbox app permissions** to only what's needed
4. **Change default admin password** in production
5. **Enable 2FA** on your Dropbox account
6. **Regularly rotate** refresh tokens
7. **Monitor activity logs** for unauthorized access

## Troubleshooting

### "Dropbox credentials not found"
- Ensure secrets are properly configured in `.streamlit/secrets.toml` or Streamlit Cloud settings
- Verify the secret keys match exactly: `DROPBOX_APP_KEY`, `DROPBOX_APP_SECRET`, `DROPBOX_REFRESH_TOKEN`

### "Authentication Error"
- Check that your App Key and App Secret are correct
- Verify your refresh token is valid (tokens don't expire but can be revoked)
- Ensure app permissions are properly set

### "No face detected"
- Use a clear, well-lit photo
- Ensure the face is clearly visible and front-facing
- Try different lighting conditions

### Face recognition is slow
- This is normal for the first comparison (loading models)
- Subsequent comparisons should be faster
- For many users (100+), consider optimizing face encoding storage

## Performance Considerations

- **Image Storage**: Images are stored as JPG files (~100KB each)
- **Database**: Excel file grows with each student (~1KB per record)
- **Recommended Limits**: Tested up to 500 students (may work with more)
- **Face Comparison**: ~1-2 seconds per comparison on average hardware

## Future Enhancements

Potential improvements:
- [ ] Quiz generation and tracking
- [ ] Score management system
- [ ] Student progress analytics
- [ ] Batch student registration
- [ ] Export activity reports
- [ ] Multi-class support
- [ ] Teacher/Admin dashboard
- [ ] Email notifications
- [ ] SMS integration

## Support

For issues or questions:
- Check the troubleshooting section above
- Review Dropbox API documentation: https://www.dropbox.com/developers/documentation
- Review Streamlit documentation: https://docs.streamlit.io

## License

This project is created for educational purposes as an initiative by Koodapakkam School.

## Credits

- Face Recognition: face_recognition library by Adam Geitgey
- Cloud Storage: Dropbox API
- Web Framework: Streamlit
- School Initiative: Koodapakkam School

---

**Note**: This application processes and stores biometric data (facial images). Ensure compliance with local privacy laws and regulations (GDPR, COPPA, etc.) when deploying in production.
