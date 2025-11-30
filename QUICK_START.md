# ⚡ QUICK START GUIDE - 5 Minutes to Deploy

## 🎯 Goal
Get your AI NANBAN app running on Streamlit Cloud with Dropbox in ~5 minutes.

---

## ⏱️ Step 1: Get Dropbox Credentials (2 minutes)

### A. Create Dropbox App
1. Go to https://www.dropbox.com/developers/apps
2. Click **"Create app"**
3. Choose:
   - API: **Scoped access**
   - Access: **Full Dropbox**
   - Name: **AI-NANBAN**
4. Click **"Create app"**

### B. Set Permissions
1. Go to **Permissions** tab
2. Enable these checkboxes:
   - ✅ files.metadata.write
   - ✅ files.metadata.read
   - ✅ files.content.write
   - ✅ files.content.read
3. Click **"Submit"**

### C. Get App Key & Secret
1. Go to **Settings** tab
2. Copy **App key**
3. Copy **App secret**

---

## ⏱️ Step 2: Generate Token (1 minute)

Run the token generator:
```bash
python generate_dropbox_token.py
```

Follow the prompts:
1. Paste your App Key
2. Paste your App Secret
3. Open the URL shown
4. Click "Allow"
5. Copy the authorization code
6. Paste it back in terminal
7. **Save the Refresh Token shown!**

---

## ⏱️ Step 3: Test Locally (1 minute)

### A. Install
```bash
pip install -r requirements.txt
```

### B. Create Secrets File
Create `.streamlit/secrets.toml`:
```toml
DROPBOX_APP_KEY = "paste_your_app_key"
DROPBOX_APP_SECRET = "paste_your_app_secret"
DROPBOX_REFRESH_TOKEN = "paste_your_refresh_token"
```

### C. Run
```bash
streamlit run app.py
```

### D. Quick Test
1. Go to "Register Student" tab
2. Upload a photo
3. Fill details and submit
4. Check your Dropbox → /AI_NANBAN/ folder should appear!

---

## ⏱️ Step 4: Deploy to Cloud (1 minute)

### A. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

**⚠️ Important:** The `.gitignore` file prevents secrets.toml from being uploaded!

### B. Deploy on Streamlit
1. Go to https://share.streamlit.io/
2. Click **"New app"**
3. Connect your GitHub repo
4. Select **app.py**
5. Click **"Deploy"**

### C. Add Secrets
1. In your app, click **"Settings"** (⚙️)
2. Go to **"Secrets"**
3. Paste:
```toml
DROPBOX_APP_KEY = "your_app_key"
DROPBOX_APP_SECRET = "your_app_secret"
DROPBOX_REFRESH_TOKEN = "your_refresh_token"
```
4. Click **"Save"**
5. Click **"Reboot app"**

---

## ✅ You're Done!

Your app is now live! Share the URL with your students.

---

## 🎮 Quick Test Checklist

After deployment:
- [ ] Open your app URL
- [ ] Register a test student
- [ ] Login with the same student
- [ ] Check Dropbox for files
- [ ] Verify activity log created

---

## 📱 Share With Students

Your app URL: `https://share.streamlit.io/YOUR_USERNAME/YOUR_REPO/main/app.py`

Students can:
1. **Register** - Upload photo once
2. **Login** - Use camera anytime to login

---

## 🆘 If Something Goes Wrong

### "Cannot connect to Dropbox"
→ Double-check secrets are pasted correctly (no extra spaces!)

### "No module named 'dropbox'"
→ Run: `pip install -r requirements.txt`

### "App crashes"
→ Check Streamlit Cloud logs for detailed error

### "Face not detected"
→ Use a clear, well-lit, front-facing photo

---

## 📚 Need More Help?

- **Full Setup:** See SETUP_GUIDE.md
- **Deployment Details:** See DEPLOYMENT_CHECKLIST.md
- **Overview:** See README.md
- **Summary:** See INTEGRATION_SUMMARY.md

---

## 🎉 Success Indicators

You know it's working when:
- ✅ App loads without errors
- ✅ Can register a student
- ✅ Files appear in Dropbox
- ✅ Can login with face recognition
- ✅ Activity log is created

---

## 🔐 Security Reminder

**Never commit `.streamlit/secrets.toml` to GitHub!**

The .gitignore file prevents this, but always double-check before pushing.

---

## 💡 Pro Tips

1. **Test Registration First**
   - Upload 2-3 test students
   - Try login with each
   - Verify face matching works

2. **Monitor Dropbox**
   - Check /AI_NANBAN/ folder
   - Verify images are uploading
   - Review activity_log.xlsx

3. **Share Responsibly**
   - Change admin password
   - Review privacy requirements
   - Monitor usage logs

---

**Time to deploy:** ~5 minutes ⏱️  
**Difficulty:** Easy ⭐  
**Support:** Full documentation included 📚

**Ready? Start at Step 1! 🚀**
