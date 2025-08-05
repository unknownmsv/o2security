# o2security/core.py
import os
from pathlib import Path
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

# مسیر ذخیره‌سازی کلید اصلی و داده‌ها
DATA_DIR = Path.home() / ".o2security"
KEY_FILE = DATA_DIR / "master.key"
PROJECTS_DIR = DATA_DIR / "projects"

def get_master_key() -> bytes:
    """
    کلید اصلی را از متغیر محیطی یا فایل محلی می‌خواند.
    اگر هیچکدام وجود نداشته باشد، یک کلید جدید ساخته و ذخیره می‌کند.
    """
    DATA_DIR.mkdir(exist_ok=True)
    
    key_b64 = os.environ.get("O2_SECURITY_KEY")
    if key_b64:
        return base64.urlsafe_b64decode(key_b64)
        
    if KEY_FILE.exists():
        return KEY_FILE.read_bytes()
    else:
        print("⚠️ کلید اصلی یافت نشد. یک کلید جدید در حال ساخت است...")
        print(f"🔑 مسیر ذخیره‌سازی کلید: {KEY_FILE}")
        print("🚨 این فایل را در جای امنی نگهداری کنید و از آن پشتیبان تهیه کنید!")
        new_key = os.urandom(32)  # 256-bit key
        KEY_FILE.write_bytes(new_key)
        return new_key

def encrypt(data: str, key: bytes) -> str:
    """یک رشته را با استفاده از AES-256-GCM رمزنگاری می‌کند."""
    iv = os.urandom(12)  # GCM recommends a 12-byte IV
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()
    
    ciphertext = encryptor.update(data.encode('utf-8')) + encryptor.finalize()
    # IV و tag را به همراه متن رمز شده ذخیره می‌کنیم
    return base64.urlsafe_b64encode(iv + encryptor.tag + ciphertext).decode('utf-8')

def decrypt(encrypted_data_b64: str, key: bytes) -> str:
    """یک رشته رمزنگاری شده با AES-256-GCM را رمزگشایی می‌کند."""
    try:
        encrypted_data = base64.urlsafe_b64decode(encrypted_data_b64)
        iv = encrypted_data[:12]
        tag = encrypted_data[12:28]
        ciphertext = encrypted_data[28:]
        
        decryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv, tag),
            backend=default_backend()
        ).decryptor()
        
        return (decryptor.update(ciphertext) + decryptor.finalize()).decode('utf-8')
    except Exception as e:
        print(f"خطا در رمزگشایی: {e}")
        return "DECRYPTION_ERROR"

# اطمینان از وجود پوشه‌ها هنگام ایمپورت شدن ماژول
PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
