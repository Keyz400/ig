from instabot import Bot
import os
import time

# Instagram credentials
USERNAME = "AniMotion.57"
PASSWORD = "Vineet664"

# Folder containing videos
VIDEO_FOLDER = "video"

# Initialize and login to Instagram
bot = Bot()
bot.login(username=USERNAME, password=PASSWORD)

# Get a list of all videos in the folder
videos = [os.path.join(VIDEO_FOLDER, f) for f in os.listdir(VIDEO_FOLDER) if f.endswith(('.mp4', '.avi', '.mov'))]

# Sort videos alphabetically (optional)
videos.sort()

# Upload videos one by one
for idx, video in enumerate(videos):
    try:
        # Optional: Add captions dynamically
        caption = f"Uploading video {idx + 1}/{len(videos)}: {os.path.basename(video)}"
        
        # Upload the video
        print(f"Uploading: {video}")
        bot.upload_video(video, caption=caption)
        
        # Pause to avoid Instagram's anti-bot detection (adjust as needed)
        time.sleep(120)  # Wait 2 minutes between uploads
    except Exception as e:
        print(f"Failed to upload {video}. Error: {e}")

# Logout after uploading
bot.logout()
