"""
Helper script to generate Dropbox refresh token for OAuth 2.0
Run this script once to get your refresh token, then save it in secrets.toml
"""

import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

def generate_refresh_token():
    print("=" * 70)
    print("DROPBOX REFRESH TOKEN GENERATOR")
    print("=" * 70)
    print()
    
    # Get credentials from user
    print("First, you need your Dropbox App credentials:")
    print("1. Go to: https://www.dropbox.com/developers/apps")
    print("2. Create a new app or select an existing one")
    print("3. Get your App Key and App Secret from the Settings tab")
    print()
    
    app_key = input("Enter your Dropbox App Key: ").strip()
    app_secret = input("Enter your Dropbox App Secret: ").strip()
    
    if not app_key or not app_secret:
        print("\n❌ Error: App Key and App Secret are required!")
        return
    
    print("\n" + "=" * 70)
    print("GENERATING AUTHORIZATION URL...")
    print("=" * 70)
    
    try:
        # Create OAuth flow with offline access for refresh token
        auth_flow = DropboxOAuth2FlowNoRedirect(
            app_key, 
            app_secret,
            token_access_type='offline'  # This is important for refresh token
        )
        
        authorize_url = auth_flow.start()
        
        print("\n📋 STEPS TO AUTHORIZE:")
        print("1. Open this URL in your browser:")
        print(f"\n   {authorize_url}\n")
        print("2. Click 'Allow' (you might need to log in to Dropbox first)")
        print("3. Copy the authorization code shown on the page")
        print()
        
        auth_code = input("Enter the authorization code here: ").strip()
        
        if not auth_code:
            print("\n❌ Error: Authorization code is required!")
            return
        
        print("\n⏳ Generating refresh token...")
        
        # Complete the OAuth flow
        oauth_result = auth_flow.finish(auth_code)
        
        print("\n" + "=" * 70)
        print("✅ SUCCESS! YOUR CREDENTIALS:")
        print("=" * 70)
        print(f"\nApp Key:        {app_key}")
        print(f"App Secret:     {app_secret}")
        print(f"Refresh Token:  {oauth_result.refresh_token}")
        print("\n" + "=" * 70)
        print("NEXT STEPS:")
        print("=" * 70)
        print("\n1. Copy these credentials to your .streamlit/secrets.toml file:")
        print("\n   DROPBOX_APP_KEY = \"" + app_key + "\"")
        print("   DROPBOX_APP_SECRET = \"" + app_secret + "\"")
        print("   DROPBOX_REFRESH_TOKEN = \"" + oauth_result.refresh_token + "\"")
        print("\n2. For Streamlit Cloud, add these to your app's secrets settings")
        print("\n⚠️  IMPORTANT: Keep these credentials secure and never commit them to Git!")
        print("=" * 70)
        
    except Exception as e:
        print(f'\n❌ Error: {e}')
        print("\nTroubleshooting:")
        print("- Make sure your App Key and App Secret are correct")
        print("- Ensure you copied the full authorization code")
        print("- Check that your Dropbox app has the correct permissions set")

if __name__ == "__main__":
    try:
        generate_refresh_token()
    except KeyboardInterrupt:
        print("\n\n❌ Process cancelled by user")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
