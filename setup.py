# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="o2security",
    version="0.1.1", # افزایش نسخه
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple library for securely managing tokens and secrets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/o2security",
    
    # پیدا کردن تمام پکیج‌ها (شامل o2security و webapp)
    packages=find_packages(),
    
    # لحاظ کردن فایل‌های غیر پایتونی (مانند HTML)
    include_package_data=True,
    
    # تعریف دستور خط فرمان
    entry_points={
        'console_scripts': [
            'o2tokman = webapp.cli:main',
        ],
    },
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    
    # اضافه کردن Flask به نیازمندی‌های اصلی
    install_requires=[
        'cryptography',
        'python-dotenv',
        'Flask',
    ],
)
