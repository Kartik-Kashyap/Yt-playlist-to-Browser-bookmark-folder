import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def authenticate():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            flow.run_local_server(port=8080)
            creds = flow.credentials
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def fetch_playlists(channel_id):
    creds = authenticate()
    youtube = build('youtube', 'v3', credentials=creds)

    playlist_names = []
    next_page_token = None

    while True:
        request = youtube.playlists().list(
            part="snippet",
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        playlists = response['items']
        playlist_names.extend([playlist['snippet']['title'] for playlist in playlists])

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    with open('playlist_names.txt', 'w', encoding='utf-8') as f:
        for name in playlist_names:
            f.write(name + '\n')

    print("Playlist names have been saved to playlist_names.txt")

if __name__ == '__main__':
    # Use your channel ID directly here
    channel_id = 'UCXgLqblLn6IvyOgPXs9GKWQ'
    fetch_playlists(channel_id)
