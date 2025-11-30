# 🚀 DEPLOYMENT CHECKLIST

## ✅ Pre-Deployment

### 1. Dropbox Setup
- [ ] Create Dropbox app at https://www.dropbox.com/developers/apps
- [ ] Set app permissions (files.metadata.write, files.metadata.read, files.content.write, files.content.read)
- [ ] Note App Key and App Secret
- [ ] Run `python generate_dropbox_token.py` to get refresh token
- [ ] Test credentials locally first

### 2. Local Testing
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Create `.streamlit/secrets.toml` with Dropbox credentials
- [ ] Run locally: `streamlit run app.py`
- [ ] Test registration (upload a photo)
- [ ] Test login (verify face recognition works)
- [ ] Check Dropbox folder structure created correctly
- [ ] Verify data appears in Dropbox

### 3. GitHub Repository
- [ ] Create new GitHub repository
- [ ] Add `.gitignore` file (already created)
- [ ] Commit all files EXCEPT `.streamlit/secrets.toml`
- [ ] Push to GitHub
- [ ] Verify secrets.toml is NOT in repository

## ☁️ Streamlit Cloud Deployment

### 1. Deploy App
- [ ] Go to https://share.streamlit.io/
- [ ] Click "New app"
- [ ] Connect GitHub repository
- [ ] Select repository, branch, and `app.py`
- [ ] Click "Deploy"

### 2. Configure Secrets
- [ ] In app dashboard, click "Settings"
- [ ] Navigate to "Secrets" section
- [ ] Paste secrets in TOML format:
```toml
DROPBOX_APP_KEY = "your_app_key"
DROPBOX_APP_SECRET = "your_app_secret"
DROPBOX_REFRESH_TOKEN = "your_refresh_token"
```
- [ ] Click "Save"
- [ ] Reboot app

### 3. Post-Deployment Testing
- [ ] Wait for app to finish deploying
- [ ] Open deployed app URL
- [ ] Test registration feature
- [ ] Test login feature
- [ ] Verify Dropbox integration works
- [ ] Check activity logs are being created
- [ ] Test from multiple devices

## 🔒 Security Checklist

### Before Going Live
- [ ] Secrets.toml not in Git repository
- [ ] Strong admin password configured
- [ ] Dropbox 2FA enabled
- [ ] App permissions minimized
- [ ] Privacy policy created (if needed)
- [ ] Data retention policy defined
- [ ] Backup strategy in place

## 📋 Credentials Template

Save this information securely (use a password manager):

```
=== DROPBOX CREDENTIALS ===
App Name: _________________
App Key: _________________
App Secret: _________________
Refresh Token: _________________

=== STREAMLIT ===
App URL: _________________
GitHub Repo: _________________

=== ADMIN ===
Admin Password: _________________ (Change default!)

=== NOTES ===
Deployment Date: _________________
Contact Email: _________________
```

## 🎯 Quick Commands Reference

```bash
# Local development
pip install -r requirements.txt
streamlit run app.py

# Generate token
python generate_dropbox_token.py

# Git commands
git add .
git commit -m "Initial commit"
git push origin main
```

## 📞 Support Resources

- Dropbox Developers: https://www.dropbox.com/developers
- Streamlit Docs: https://docs.streamlit.io
- Face Recognition: https://github.com/ageitgey/face_recognition
- Setup Guide: See SETUP_GUIDE.md

## ⚠️ Common Deployment Issues

**Issue**: "Module not found"
**Fix**: Check requirements.txt includes all dependencies

**Issue**: "Dropbox authentication failed"
**Fix**: Verify secrets are correctly configured in Streamlit Cloud

**Issue**: "App crashes on startup"
**Fix**: Check logs in Streamlit Cloud dashboard for detailed error

**Issue**: "Face recognition not working"
**Fix**: Ensure dlib and face-recognition installed correctly

---

**Ready to deploy?** Follow the checklist from top to bottom! ✅
