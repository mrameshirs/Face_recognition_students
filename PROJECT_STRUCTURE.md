# 📁 AI NANBAN - Project Structure

## 🗂️ Complete File Structure

```
ai-nanban/
│
├── 📄 Core Application Files
│   ├── app.py                      # Main Streamlit entry point
│   ├── home.py                     # Home page interface
│   ├── register.py                 # Student registration UI
│   ├── login.py                    # Student login UI
│   ├── clear.py                    # Admin data clearing
│   └── UserDetail.py               # User data model class
│
├── 🔧 Configuration & Integration
│   ├── config.py                   # Configuration management
│   ├── dropbox_utils.py            # Dropbox API integration
│   ├── db.py                       # Database operations
│   ├── image.py                    # Face recognition & image handling
│   └── encdec.py                   # Password encryption utilities
│
├── 📚 Documentation
│   ├── README.md                   # Project overview
│   ├── INDEX.md                    # Documentation navigator
│   ├── QUICK_START.md              # 5-minute quick start
│   ├── SETUP_GUIDE.md              # Detailed setup instructions
│   ├── DEPLOYMENT_CHECKLIST.md     # Deployment verification
│   ├── INTEGRATION_SUMMARY.md      # Integration overview
│   ├── CHANGELOG.md                # Version changes
│   └── PROJECT_STRUCTURE.md        # This file
│
├── 🛠️ Utilities & Tools
│   ├── generate_dropbox_token.py   # OAuth token generator
│   ├── requirements.txt            # Python dependencies
│   └── .gitignore                  # Git exclusions
│
└── ⚙️ Configuration Templates
    └── .streamlit/
        └── secrets.toml.template   # Secrets configuration template
```

---

## 📦 File Descriptions

### Core Application Files

#### app.py
```python
# Main entry point
# Creates tabs: Home, Register, Login, Clear
# Imports and organizes all modules
```
**Purpose:** Application launcher  
**Size:** ~10 lines  
**Dependencies:** All other UI modules

#### home.py
```python
# Welcome page with information
# Displays GIF and feature list
# Introduces the application
```
**Purpose:** Landing page  
**Size:** ~40 lines  
**Dependencies:** Streamlit

#### register.py
```python
# Student registration interface
# Captures/uploads photos
# Validates faces
# Saves to Dropbox
```
**Purpose:** New student registration  
**Size:** ~70 lines  
**Dependencies:** image, db, dropbox_utils

#### login.py
```python
# Student login via face recognition
# Compares with stored faces
# Displays student info
# Logs activity
```
**Purpose:** Student authentication  
**Size:** ~40 lines  
**Dependencies:** image, db, dropbox_utils

#### clear.py
```python
# Admin function to clear data
# Password protected
# Removes all Dropbox data
```
**Purpose:** Data management  
**Size:** ~25 lines  
**Dependencies:** dropbox_utils, encdec

#### UserDetail.py
```python
# Data model for student information
# Stores: name, dob, class
```
**Purpose:** Data structure  
**Size:** ~10 lines  
**Dependencies:** None

---

### Configuration & Integration

#### config.py
```python
# Manages configuration
# Loads Dropbox credentials
# Defines file paths
```
**Purpose:** Central configuration  
**Size:** ~25 lines  
**Dependencies:** Streamlit secrets

**Key Variables:**
- `DROPBOX_APP_KEY`
- `DROPBOX_APP_SECRET`
- `DROPBOX_REFRESH_TOKEN`
- `IMAGES_FOLDER`
- `USER_DATA_FILE`
- `LOG_FILE_PATH`

#### dropbox_utils.py
```python
# Dropbox integration functions
# Upload/download operations
# File management
# Activity logging
```
**Purpose:** Cloud storage operations  
**Size:** ~200 lines  
**Dependencies:** Dropbox SDK, pandas

**Key Functions:**
- `get_dropbox_client()`
- `upload_image_to_dropbox()`
- `download_image_from_dropbox()`
- `read_user_data_from_dropbox()`
- `save_user_data_to_dropbox()`
- `log_activity()`
- `clear_all_data()`

#### db.py
```python
# Database operations
# Uses Dropbox Excel files
# CRUD operations for users
```
**Purpose:** Data persistence  
**Size:** ~120 lines  
**Dependencies:** dropbox_utils, pandas

**Key Methods:**
- `insert_user_detail()`
- `get_user_detail()`
- `get_all_users()`
- `delete_user()`
- `update_user_detail()`

#### image.py
```python
# Face recognition logic
# Image upload/download
# Face comparison
# Validation
```
**Purpose:** Image & face processing  
**Size:** ~180 lines  
**Dependencies:** face_recognition, dropbox_utils, PIL

**Key Functions:**
- `save_image_to_dropbox()`
- `compare_face_with_dropbox()`
- `save_image_locally()` (legacy)
- `compare_faces_in_directory()` (legacy)

#### encdec.py
```python
# Password encryption/decryption
# Uses Fernet symmetric encryption
# Stores encrypted admin password
```
**Purpose:** Security utilities  
**Size:** ~15 lines  
**Dependencies:** cryptography

---

### Documentation Files

#### README.md
**Purpose:** Project introduction and overview  
**Contents:**
- Features
- Quick start
- Installation
- Usage guide
- Technologies used

#### INDEX.md
**Purpose:** Documentation navigator  
**Contents:**
- Document descriptions
- Use case mapping
- Quick reference
- Learning paths

#### QUICK_START.md
**Purpose:** Fast deployment guide  
**Contents:**
- 5-minute setup
- Essential steps only
- Quick troubleshooting

#### SETUP_GUIDE.md
**Purpose:** Comprehensive setup instructions  
**Contents:**
- Dropbox app creation
- Token generation
- Local setup
- Cloud deployment
- Troubleshooting

#### DEPLOYMENT_CHECKLIST.md
**Purpose:** Pre/post deployment verification  
**Contents:**
- Pre-deployment checklist
- Security verification
- Post-deployment testing

#### INTEGRATION_SUMMARY.md
**Purpose:** Overview of Dropbox integration  
**Contents:**
- What changed
- New features
- Migration guide

#### CHANGELOG.md
**Purpose:** Detailed version history  
**Contents:**
- All changes from v1 to v2
- Breaking changes
- Performance improvements

---

### Utilities & Tools

#### generate_dropbox_token.py
```python
# Interactive OAuth flow
# Generates refresh token
# Guides user through process
```
**Purpose:** Token generation helper  
**Size:** ~80 lines  
**Usage:** `python generate_dropbox_token.py`

#### requirements.txt
**Purpose:** Python package dependencies  
**Key Packages:**
- streamlit==1.31.1
- dropbox==12.0.2
- face-recognition==1.3.0
- pandas==2.2.1
- openpyxl==3.1.2

#### .gitignore
**Purpose:** Prevent committing sensitive files  
**Excludes:**
- .streamlit/secrets.toml
- *.pyc, __pycache__/
- db.sqlite
- known_user/, unknown_user/

---

## ☁️ Dropbox Folder Structure

When deployed, creates this structure in Dropbox:

```
/AI_NANBAN/
│
├── known_users/              # Student photos folder
│   ├── 1.jpg                # Student ID 1's photo
│   ├── 2.jpg                # Student ID 2's photo
│   ├── 3.jpg                # Student ID 3's photo
│   └── ...                  # More student photos
│
├── user_data.xlsx           # Student database
│   │
│   └── Columns:
│       ├── id              # Auto-incrementing ID
│       ├── name            # Student name
│       ├── dob             # Date of birth
│       └── class           # Class/grade
│
└── activity_log.xlsx        # Activity tracking
    │
    └── Columns:
        ├── Timestamp       # Date and time
        ├── Username        # Student name
        └── Role            # Action type
```

---

## 🔄 Data Flow

### Registration Flow
```
User (register.py)
    ↓
    [Capture/Upload Photo]
    ↓
Validate Face (image.py)
    ↓
Generate User ID (db.py)
    ↓
Upload Photo (dropbox_utils.py)
    ↓
Save User Data (dropbox_utils.py)
    ↓
Log Activity (dropbox_utils.py)
    ↓
    [Success Message]
```

### Login Flow
```
User (login.py)
    ↓
    [Capture Photo]
    ↓
Get All User IDs (dropbox_utils.py)
    ↓
For Each User:
    Download Photo (dropbox_utils.py)
    ↓
    Compare Faces (image.py)
    ↓
    [Match Found?]
    ↓
Get User Details (db.py)
    ↓
Log Activity (dropbox_utils.py)
    ↓
    [Display Welcome]
```

---

## 🔗 Module Dependencies

```
app.py
├── home.py
├── register.py
│   ├── image.py
│   │   └── dropbox_utils.py
│   │       └── config.py
│   └── db.py
│       └── dropbox_utils.py
├── login.py
│   ├── image.py
│   └── db.py
└── clear.py
    ├── dropbox_utils.py
    └── encdec.py
```

---

## 📊 File Size Reference

| File | Lines | Purpose |
|------|-------|---------|
| app.py | 10 | Entry point |
| home.py | 40 | UI |
| register.py | 70 | UI |
| login.py | 40 | UI |
| clear.py | 25 | UI |
| UserDetail.py | 10 | Model |
| config.py | 25 | Config |
| dropbox_utils.py | 200 | Integration |
| db.py | 120 | Data layer |
| image.py | 180 | Processing |
| encdec.py | 15 | Security |

**Total Code:** ~735 lines  
**Documentation:** ~4000 lines

---

## 🎯 Key Integration Points

### Dropbox Integration
- **config.py** → Credentials
- **dropbox_utils.py** → All Dropbox operations
- **db.py** → Uses dropbox_utils for storage
- **image.py** → Uses dropbox_utils for images

### Face Recognition
- **image.py** → Core face recognition
- **register.py** → Validation before save
- **login.py** → Face matching

### User Interface
- **app.py** → Tab organization
- **home.py** → Welcome screen
- **register.py** → Registration form
- **login.py** → Login camera
- **clear.py** → Admin panel

---

## 📝 Configuration Files

### .streamlit/secrets.toml (Create this)
```toml
DROPBOX_APP_KEY = "your_app_key"
DROPBOX_APP_SECRET = "your_app_secret"
DROPBOX_REFRESH_TOKEN = "your_refresh_token"
```
**⚠️ Never commit this file!**

### .streamlit/secrets.toml.template (Template)
```toml
# Template file - copy to secrets.toml
DROPBOX_APP_KEY = "your_app_key_here"
DROPBOX_APP_SECRET = "your_app_secret_here"
DROPBOX_REFRESH_TOKEN = "your_refresh_token_here"
```

---

## 🔐 Security Files

| File | Purpose | Commit? |
|------|---------|---------|
| .gitignore | Exclude sensitive files | ✅ Yes |
| secrets.toml | Store credentials | ❌ No |
| secrets.toml.template | Template | ✅ Yes |
| encdec.py | Password encryption | ✅ Yes |

---

## 📦 Deployment Structure

### Local Development
```
ai-nanban/
├── [All files above]
└── .streamlit/
    └── secrets.toml  ← Create locally
```

### GitHub Repository
```
ai-nanban/
├── [All files except secrets.toml]
└── .streamlit/
    └── secrets.toml.template  ← Only template
```

### Streamlit Cloud
```
Deployed from GitHub
    ↓
Secrets added via UI
    ↓
App runs with cloud secrets
```

---

## 🎯 Entry Points

### Main Application
```bash
streamlit run app.py
```

### Token Generation
```bash
python generate_dropbox_token.py
```

### Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## 📖 Documentation Flow

```
START HERE
    ↓
INDEX.md
    ↓
Choose based on need:
    ├── Quick deploy? → QUICK_START.md
    ├── Overview? → README.md
    ├── Detailed setup? → SETUP_GUIDE.md
    ├── Deployment? → DEPLOYMENT_CHECKLIST.md
    ├── What's new? → INTEGRATION_SUMMARY.md
    └── Technical details? → CHANGELOG.md
```

---

## ✅ Verification

**Project correctly set up when:**
- ✅ All files present
- ✅ secrets.toml configured (not committed)
- ✅ requirements.txt installed
- ✅ Dropbox app created
- ✅ Token generated
- ✅ App runs locally

---

**Last Updated:** 2024  
**Version:** 2.0 (Dropbox Integration)
