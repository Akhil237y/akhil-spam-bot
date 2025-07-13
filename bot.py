from telethon import TelegramClient, events
import asyncio
import os

# Hardcoded API credentials
api_id = 21073191
api_hash = '272a189777e9c47af345a0dd52b1f0f9'

bot = TelegramClient("userbot_session", api_id, api_hash)

spam_text = "Default Spam Text"

# Create user log file if not exists
if not os.path.exists("users.txt"):
    with open("users.txt", "w") as f:
        f.write("UserID | Username\n")

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    sender = await event.get_sender()
    user_id = sender.id
    username = sender.username or "NoUsername"

    # Save user info
    with open("users.txt", "a") as f:
        f.write(f"{user_id} | {username}\n")

    await event.reply("Welcome, dear! 😊 Akhil's Spam Bot ❤️ is ready to do something crazy! ☠️\nType: Enter text <your message>")

@bot.on(events.NewMessage(pattern="^Enter text (.+)"))
async def set_text(event):
    global spam_text
    spam_text = event.pattern_match.group(1)
    await event.reply(f"✅ Spam message set to: `{spam_text}`")

@bot.on(events.NewMessage(pattern=r"\.raid (\d+)\s+@(\w+)"))
async def raid(event):
    count = int(event.pattern_match.group(1))
    target = "@" + event.pattern_match.group(2)
    await event.reply(f"🚀 Spamming {target} {count} times...")

    for _ in range(count):
        try:
            await bot.send_message(target, spam_text)
            await asyncio.sleep(0.4)
        except Exception as e:
            await event.reply(f"❌ Error: {e}")
            break

print("Bot Running...")
bot.start()
bot.run_until_disconnected()
