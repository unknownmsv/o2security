# o2security/tokman.py
import json
from .core import decrypt, get_master_key, PROJECTS_DIR

class TokenManager:
    def __init__(self):
        self._master_key = get_master_key()
        self._current_project_data = None
        self._current_project_name = None

    def select_project(self, project_name: str):
        """یک پروژه را برای خواندن توکن‌ها انتخاب می‌کند."""
        project_file = PROJECTS_DIR / f"{project_name}.json"
        if not project_file.exists():
            raise FileNotFoundError(f"پروژه '{project_name}' یافت نشد. آیا آن را در داشبورد ساخته‌اید؟")
        
        with open(project_file, 'r') as f:
            self._current_project_data = json.load(f)
        self._current_project_name = project_name
        print(f"✅ پروژه '{project_name}' با موفقیت انتخاب شد.")

    def get(self, token_name: str) -> str:
        """یک توکن را از پروژه انتخاب شده، رمزگشایی کرده و برمی‌گرداند."""
        if self._current_project_data is None:
            raise Exception("هیچ پروژه‌ای انتخاب نشده است. ابتدا از متد `select_project` استفاده کنید.")
        
        encrypted_value = self._current_project_data.get(token_name)
        if encrypted_value is None:
            raise KeyError(f"توکن '{token_name}' در پروژه '{self._current_project_name}' یافت نشد.")
            
        return decrypt(encrypted_value, self._master_key)

# ساخت یک نمونه از کلاس برای استفاده آسان در سطح ماژول
tokman = TokenManager()
