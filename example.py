# example.py
# مثالی از نحوه استفاده از کتابخانه در یک پروژه دیگر
from o2security.tokman import tokman
import os

# نام پروژه‌ای که در داشبورد ساخته‌اید
PROJECT_NAME = "discord-bot" 

try:
    # ۱. انتخاب پروژه
    tokman.select_project(PROJECT_NAME)

    # ۲. دریافت توکن‌ها
    discord_token = tokman.get("DISCORD_TOKEN")
    database_url = tokman.get("DATABASE_URL")

    print("\n--- توکن‌های دریافت شده ---")
    print(f"توکن دیسکورد: ...{discord_token[-6:]}") # نمایش چند کاراکتر آخر برای امنیت
    print(f"آدرس دیتابیس: {database_url}")
    print("--------------------------\n")

    # حالا می‌توانید از این توکن‌ها در کد خود استفاده کنید
    # مثلا برای یک ربات دیسکارد:
    # import discord
    # client = discord.Client()
    # client.run(discord_token)

except (FileNotFoundError, KeyError, Exception) as e:
    print(f"\n❌ خطا: {e}")
    print("لطفاً مطمئن شوید که پروژه را در داشبورد ساخته و توکن‌ها را اضافه کرده‌اید.")

