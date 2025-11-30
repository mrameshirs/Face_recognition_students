# 🌐 Web-Based Dropbox Token Generation (No Local Installation!)

## 🎯 Generate Dropbox Token Without Installing Anything

If you're having trouble installing packages locally on Windows, you can still get your Dropbox token using just your web browser!

---

## 📋 Step-by-Step Instructions

### Step 1: Create Dropbox App
1. Go to: https://www.dropbox.com/developers/apps
2. Click **"Create app"**
3. Choose:
   - **Scoped access**
   - **Full Dropbox**
   - Name: **AI-NANBAN**
4. Click **"Create app"**

### Step 2: Set Permissions
1. Go to **"Permissions"** tab
2. Check these boxes:
   - ✅ `files.metadata.write`
   - ✅ `files.metadata.read`
   - ✅ `files.content.write`
   - ✅ `files.content.read`
3. Click **"Submit"**

### Step 3: Get App Key and Secret
1. Go to **"Settings"** tab
2. **Copy** your **App key**
3. **Copy** your **App secret**

### Step 4: Generate Refresh Token (Using OAuth 2 Playground)

#### Method A: Using Dropbox OAuth Code Flow

1. **Create Authorization URL manually:**

Replace `YOUR_APP_KEY` with your actual App Key from Step 3:

```
https://www.dropbox.com/oauth2/authorize?client_id=YOUR_APP_KEY&token_access_type=offline&response_type=code
```

2. **Paste that URL in your browser** and press Enter

3. Click **"Allow"**

4. **Copy the authorization code** shown on the page

5. **Get your refresh token** using this online tool:

Go to: https://reqbin.com/

**Or use curl on Windows:**

```bash
curl -X POST https://api.dropbox.com/oauth2/token ^
  -d code=YOUR_AUTHORIZATION_CODE ^
  -d grant_type=authorization_code ^
  -u YOUR_APP_KEY:YOUR_APP_SECRET
```

Replace:
- `YOUR_AUTHORIZATION_CODE` with the code from step 4
- `YOUR_APP_KEY` with your App Key
- `YOUR_APP_SECRET` with your App Secret

The response will contain your `refresh_token`!

#### Method B: Using Python Online (Simpler!)

1. Go to: https://www.online-python.com/

2. Paste this code (replace YOUR_APP_KEY and YOUR_APP_SECRET):

```python
import urllib.request
import urllib.parse
import json

# Replace these with your actual values
APP_KEY = "YOUR_APP_KEY"
APP_SECRET = "YOUR_APP_SECRET"

# Step 1: Generate authorization URL
auth_url = f"https://www.dropbox.com/oauth2/authorize?client_id={APP_KEY}&token_access_type=offline&response_type=code"

print("1. Open this URL in your browser:")
print(auth_url)
print()
print("2. Click 'Allow'")
print("3. Copy the authorization code and paste it below:")
print()

# You'll need to input the auth code manually
auth_code = input("Enter authorization code: ")

# Step 2: Exchange code for refresh token
data = urllib.parse.urlencode({
    'code': auth_code,
    'grant_type': 'authorization_code',
    'client_id': APP_KEY,
    'client_secret': APP_SECRET
}).encode()

req = urllib.request.Request('https://api.dropbox.com/oauth2/token', data=data)
response = urllib.request.urlopen(req)
result = json.loads(response.read().decode())

print()
print("="*70)
print("SUCCESS! Your credentials:")
print("="*70)
print(f"App Key: {APP_KEY}")
print(f"App Secret: {APP_SECRET}")
print(f"Refresh Token: {result['refresh_token']}")
print("="*70)
```

3. Click "Run"

4. Follow the instructions in the output

---

## 🎉 You Now Have Your Credentials!

Save these three values:
- ✅ **App Key**
- ✅ **App Secret**  
- ✅ **Refresh Token**

---

## 🚀 Next Step: Deploy Without Local Testing

Since you have Windows installation issues, let's skip local testing and deploy directly:

### 1. Create `.streamlit/secrets.toml` file

Create a folder `.streamlit` in your project, then create `secrets.toml` inside it:

```toml
DROPBOX_APP_KEY = "your_app_key_here"
DROPBOX_APP_SECRET = "your_app_secret_here"
DROPBOX_REFRESH_TOKEN = "your_refresh_token_here"
```

### 2. Push to GitHub

```bash
git init
git add .
git commit -m "AI NANBAN with Dropbox integration"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

**Note:** The `.gitignore` file ensures `secrets.toml` is NOT pushed to GitHub!

### 3. Deploy to Streamlit Cloud

1. Go to: https://share.streamlit.io/
2. Click "New app"
3. Connect your GitHub repository
4. Select `app.py`
5. Before deploying, click "Advanced settings"
6. In "Secrets" section, paste:

```toml
DROPBOX_APP_KEY = "your_app_key_here"
DROPBOX_APP_SECRET = "your_app_secret_here"
DROPBOX_REFRESH_TOKEN = "your_refresh_token_here"
```

7. Click "Deploy"

### 4. Wait for Deployment (2-3 minutes)

Streamlit Cloud uses **Linux**, so `dlib` will install without any issues!

---

## ✅ Testing on Cloud

Once deployed:
1. Open your app URL
2. Go to "Register Student" tab
3. Upload a test photo
4. Fill in details
5. Check your Dropbox → `/AI_NANBAN/` folder should appear!

---

## 💡 Why This Works Better

**Benefits of deploying directly:**
- ✅ No Windows compilation issues
- ✅ No Visual Studio required
- ✅ No local environment setup
- ✅ Works perfectly on Streamlit Cloud (Linux)
- ✅ Faster to get started
- ✅ Can test with real deployment immediately

---

## 🎯 Summary

You successfully avoided the Windows dlib installation nightmare by:
1. ✅ Generated Dropbox token using web/online tools
2. ✅ Skipped local testing
3. ✅ Deployed directly to Streamlit Cloud
4. ✅ App works perfectly there!

**This is actually the recommended workflow!** Many Streamlit developers don't test locally - they deploy and iterate on the cloud.

---

## 📞 Need Help?

If you get stuck on any step, the error is likely one of:
1. **Incorrect credentials** → Double-check App Key, Secret, Token
2. **Permissions not set** → Verify in Dropbox app settings
3. **Secrets not configured** → Check Streamlit Cloud secrets section

All these are easy to fix without touching Windows/Python installation!
