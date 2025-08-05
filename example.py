import discord
from o2security.tokman import tokman
from discord.ext import commands

# تنظیمات اولیه
PROJECT_NAME = "test"
TARGET_USER_ID = 1146057264969556018  # آیدی کاربر مورد نظر

# انتخاب پروژه و دریافت توکن
try:
    tokman.select_project(PROJECT_NAME)
    DISCORD_TOKEN = tokman.get("DISCORD_TOKEN")
    
    # ایجاد ربات
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'وارد شدیم به عنوان {bot.user}')
        
        try:
            # پیدا کردن کاربر هدف
            user = await bot.fetch_user(TARGET_USER_ID)
            
            # ارسال پیام
            await user.send("hi")
            print(f"پیام به {user.name} ارسال شد")
            
        except discord.NotFound:
            print("کاربر پیدا نشد!")
        except discord.Forbidden:
            print("اجازه ارسال پیام نداریم")
        except Exception as e:
            print(f"خطای ناشناخته: {e}")
        finally:
            await bot.close()

    # اجرای ربات
    bot.run(DISCORD_TOKEN)

except Exception as e:
    print(f"خطا در دریافت توکن: {e}")