# webapp/app.py
import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash
from pathlib import Path
import sys

# افزودن مسیر ریشه پروژه به sys.path برای پیدا کردن ماژول o2security
sys.path.append(str(Path(__file__).parent.parent))
from o2security.core import encrypt, decrypt, get_master_key, PROJECTS_DIR

app = Flask(__name__)
app.secret_key = os.urandom(24)
MASTER_KEY = get_master_key()

def get_project_path(project_name: str) -> Path:
    """مسیر فایل JSON یک پروژه را برمی‌گرداند."""
    return PROJECTS_DIR / f"{project_name}.json"

def load_project_data(project_name: str) -> dict:
    """داده‌های یک پروژه را از فایل می‌خواند."""
    file_path = get_project_path(project_name)
    if file_path.exists():
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

def save_project_data(project_name: str, data: dict):
    """داده‌های یک پروژه را در فایل ذخیره می‌کند."""
    file_path = get_project_path(project_name)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        project_name = request.form.get('project_name')
        if project_name and not get_project_path(project_name).exists():
            save_project_data(project_name, {})
            flash(f'پروژه "{project_name}" با موفقیت ساخته شد!', 'success')
        else:
            flash('نام پروژه نامعتبر است یا پروژه از قبل وجود دارد.', 'danger')
        return redirect(url_for('index'))
    
    projects = [p.stem for p in PROJECTS_DIR.glob('*.json')]
    return render_template('index.html', projects=projects)

@app.route('/project/<project_name>', methods=['GET', 'POST'])
def project_view(project_name):
    if not get_project_path(project_name).exists():
        return redirect(url_for('index'))

    if request.method == 'POST':
        token_key = request.form.get('token_key')
        token_value = request.form.get('token_value')
        if token_key and token_value:
            encrypted_value = encrypt(token_value, MASTER_KEY)
            data = load_project_data(project_name)
            data[token_key] = encrypted_value
            save_project_data(project_name, data)
            flash(f'توکن "{token_key}" با موفقیت اضافه شد.', 'success')
        else:
            flash('نام و مقدار توکن نمی‌تواند خالی باشد.', 'danger')
        return redirect(url_for('project_view', project_name=project_name))

    project_data = load_project_data(project_name)
    return render_template('project.html', project_name=project_name, tokens=project_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
