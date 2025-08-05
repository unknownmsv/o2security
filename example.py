import discord
from o2security.tokman import tokman
from discord.ext import commands

# Initial setup
PROJECT_NAME = "test"
TARGET_USER_ID = 1146057264969556018  # Target user ID

# Select project and get token
try:
    tokman.select_project(PROJECT_NAME)
    DISCORD_TOKEN = tokman.get("DISCORD_TOKEN")
    
    # Create bot instance
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')
        
        try:
            # Find target user
            user = await bot.fetch_user(TARGET_USER_ID)
            
            # Send message
            await user.send("hi")
            print(f"Message sent to {user.name}")
            
        except discord.NotFound:
            print("User not found!")
        except discord.Forbidden:
            print("Missing permissions to send message")
        except Exception as e:
            print(f"Unknown error: {e}")
        finally:
            await bot.close()

    # Run the bot
    bot.run(DISCORD_TOKEN)

except Exception as e:
    print(f"Error getting token: {e}")