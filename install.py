# install.py
import subprocess
import sys

def install_package():
    """
    کتابخانه O₂Security را با استفاده از pip در محیط فعلی پایتون نصب می‌کند.
    """
    try:
        print("🚀 در حال نصب کتابخانه O₂Security...")
        
        # استفاده از sys.executable برای اطمینان از استفاده از مفسر پایتون صحیح
        # دستور 'pip install .' پکیج موجود در همین پوشه را نصب می‌کند
        command = [sys.executable, "-m", "pip", "install", "."]
        
        # اجرای دستور
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        print("\n--- خروجی نصب ---")
        print(result.stdout)
        print("------------------")
        
        print("\n✅ کتابخانه O₂Security با موفقیت نصب شد!")
        print("حالا می‌توانید با 'from o2security import tokman' از آن استفاده کنید.")

    except subprocess.CalledProcessError as e:
        print("\n❌ خطا در هنگام نصب:")
        print(e.stderr)
    except FileNotFoundError:
        print("\n❌ خطا: دستور 'pip' یافت نشد. لطفاً از نصب بودن پایتون و pip اطمینان حاصل کنید.")

if __name__ == "__main__":
    install_package()
