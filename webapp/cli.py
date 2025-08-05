# webapp/cli.py
import sys
from pathlib import Path

# افزودن مسیر ریشه پروژه به sys.path تا ماژول o2security پیدا شود
# این کار برای زمانی که اسکریپت به صورت مستقیم اجرا می‌شود ضروری است
sys.path.append(str(Path(__file__).resolve().parent.parent))

# حالا می‌توانیم اپلیکیشن را ایمپورت کنیم
from webapp.app import app

def main():
    """تابع اصلی برای اجرای سرور از طریق خط فرمان."""
    print("🚀 سرور O₂Security در حال اجراست...")
    print("🌐 برای دسترسی به داشبورد به آدرس http://127.0.0.1:5001 مراجعه کنید.")
    try:
        # اجرای سرور Flask
        app.run(host='0.0.0.0', port=5001)
    except KeyboardInterrupt:
        print("\n👋 سرور متوقف شد.")

if __name__ == '__main__':
    main()
