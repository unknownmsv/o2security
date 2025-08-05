# setup.py
from setuptools import setup, find_packages

# خواندن محتوای README.md برای توضیحات بلند
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="o2security",
    version="0.1.0",
    author="sina",  # نام خود را اینجا وارد کنید
    author_email="sina@unknownmsv.ir",  # ایمیل خود را اینجا وارد کنید
    description="A simple library for securely managing tokens and secrets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unknownmsv/o2security",  # آدرس گیت‌هاب پروژه
    packages=find_packages(exclude=["webapp", "webapp.*"]), # فقط پکیج o2security را شامل شود
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'cryptography',
        'python-dotenv',
    ],
)
