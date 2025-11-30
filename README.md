# 🎓 AI NANBAN - Face Recognition App

**AI Personalized Coach Application for CBSE Students using Face Recognition with Dropbox Cloud Storage**

---

## 🌟 Features

### Core Features
- ✅ **Face Detection & Recognition** - Automatic student identification using facial recognition
- ☁️ **Cloud Storage** - All data stored securely in Dropbox (unlimited scalability)
- 📝 **Student Registration** - Easy registration with photo capture or upload
- 🔐 **Secure Login** - Facial recognition-based authentication
- 📊 **Activity Logging** - Automatic tracking of registrations and logins
- 🧹 **Admin Controls** - Data management and clearing capabilities

### Future Features (Planned)
- 📚 Customized Quiz Generation based on CBSE Class notes
- 📈 Personalized Score Tracking for student progress
- 📧 Email notifications for parents/teachers
- 📱 Multi-class support

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Dropbox account
- Dropbox App credentials (see setup guide)

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd ai-nanban
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Generate Dropbox credentials**
```bash
python generate_dropbox_token.py
```
Follow the prompts to get your refresh token.

4. **Configure secrets**

Create `.streamlit/secrets.toml`:
```toml
DROPBOX_APP_KEY = "your_app_key_here"
DROPBOX_APP_SECRET = "your_app_secret_here"
DROPBOX_REFRESH_TOKEN = "your_refresh_token_here"
```

5. **Run the app**
```bash
streamlit run app.py
```

---

## 📖 Detailed Setup

For complete setup instructions including:
- Dropbox App creation
- OAuth token generation
- Streamlit Cloud deployment
- Troubleshooting

See **[SETUP_GUIDE.md](SETUP_GUIDE.md)**

---

## 📁 Project Structure

```
ai-nanban/
├── app.py                          # Main Streamlit app
├── config.py                       # Configuration management
├── dropbox_utils.py                # Dropbox integration functions
├── db.py                           # Database operations
├── image.py                        # Face recognition logic
├── register.py                     # Student registration UI
├── login.py                        # Student login UI
├── clear.py                        # Admin data clearing
├── home.py                         # Home page
├── UserDetail.py                   # User data model
├── encdec.py                       # Password utilities
├── requirements.txt                # Python dependencies
├── generate_dropbox_token.py       # Token generation helper
├── SETUP_GUIDE.md                  # Detailed setup instructions
└── .streamlit/
    └── secrets.toml.template       # Secrets template
```

---

## 🔒 Security

### Important Security Practices
- ✅ Never commit `.streamlit/secrets.toml` to Git
- ✅ Use environment variables or Streamlit secrets for credentials
- ✅ Enable 2FA on your Dropbox account
- ✅ Regularly monitor activity logs
- ✅ Change default admin password in production
- ✅ Restrict Dropbox app permissions to minimum required

### Data Privacy
⚠️ **Important**: This application processes biometric data (facial images). Ensure compliance with:
- GDPR (European Union)
- COPPA (US - Children's data)
- Local privacy regulations in your jurisdiction

---

## 🎯 Usage

### Register a New Student
1. Navigate to **Register Student** tab
2. Choose camera or upload method
3. Capture/upload a clear facial photo
4. Fill in student details (Name, DOB, Class)
5. Submit - data is saved to Dropbox automatically

### Student Login
1. Navigate to **Student Login** tab
2. Capture photo using camera
3. System matches face with registered students
4. Login activity is logged

### Admin Functions
1. Navigate to **Clear** tab
2. Enter admin password
3. Clear all data if needed (⚠️ irreversible!)

---

## 🛠️ Technologies Used

- **Framework**: Streamlit
- **Face Recognition**: face_recognition (dlib)
- **Cloud Storage**: Dropbox API
- **Data Storage**: Excel files (pandas, openpyxl)
- **Image Processing**: OpenCV, Pillow
- **Authentication**: Cryptography (Fernet)

---

## 📊 Dropbox Storage Structure

```
/AI_NANBAN/
├── known_users/
│   ├── 1.jpg           # Student ID 1's photo
│   ├── 2.jpg           # Student ID 2's photo
│   └── ...
├── user_data.xlsx      # Student information database
└── activity_log.xlsx   # Login/registration activity logs
```

---

## 🐛 Troubleshooting

### Common Issues

**"Dropbox credentials not found"**
- Check `.streamlit/secrets.toml` exists
- Verify secret key names match exactly
- For Streamlit Cloud, check secrets settings

**"Authentication Error"**
- Verify App Key and App Secret are correct
- Check refresh token is valid
- Ensure app permissions are set correctly

**"No face detected"**
- Use clear, well-lit photos
- Ensure face is front-facing
- Try different lighting conditions

**Slow face recognition**
- First comparison loads models (slower)
- Subsequent comparisons are faster
- Consider limiting to <500 students

For more troubleshooting, see [SETUP_GUIDE.md](SETUP_GUIDE.md)

---

## 📈 Performance

- **Image Size**: ~100KB per student photo
- **Database**: ~1KB per student record
- **Tested**: Up to 500 students
- **Face Comparison**: ~1-2 seconds average

---

## 🤝 Contributing

This is an educational project initiated by **Koodapakkam School**. Suggestions and contributions are welcome!

To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📧 Contact & Support

For questions or suggestions, please contact Koodapakkam School through the application's feedback system.

---

## 📜 License

This project is created for educational purposes. Please ensure compliance with all applicable privacy laws when deploying.

---

## 🙏 Credits

- **Face Recognition**: [face_recognition library](https://github.com/ageitgey/face_recognition) by Adam Geitgey
- **Cloud Storage**: [Dropbox API](https://www.dropbox.com/developers)
- **Web Framework**: [Streamlit](https://streamlit.io/)
- **Initiative**: Koodapakkam School

---

## ⭐ Star this repository

If you find this project useful, please consider giving it a star!

---

**Version**: 2.0 (Dropbox Integration)  
**Last Updated**: 2024
