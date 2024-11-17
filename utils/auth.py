import os
import pickle
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
import streamlit as st
def authenticate_user(client_secret_file, scopes):
    """Authenticate the user with Google OAuth."""
    credentials = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = Flow.from_client_secrets_file(client_secret_file, scopes=scopes)
            flow.redirect_uri = "urn:ietf:wg:oauth:2.0:oob"

            auth_url, _ = flow.authorization_url(prompt="consent")
            st.info(f"[Click here to authorize]({auth_url})")

            auth_code = st.text_input("Enter the authorization code here:")
            if auth_code:
                flow.fetch_token(code=auth_code)
                credentials = flow.credentials

                with open("token.pickle", "wb") as token:
                    pickle.dump(credentials, token)

    return credentials
