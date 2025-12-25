# Prince-music-bot
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp

TOKEN = os.getenv("BOT_TOKEN")  # BotFather se mila token daal

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Send me YouTube link, main MP3 bhej dunga!")

async def download_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    msg = await update.message.reply_text("🔄 Downloading...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'song.mp3',
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Unknown')

        await update.message.reply_audio(audio=open('song.mp3', 'rb'), title=title)
        await msg.edit_text("✅ Done!")
        
        # Cleanup
        if os.path.exists('song.mp3'):
            os.remove('song.mp3')
            
    except Exception as e:
        await msg.edit_text("❌ Error! Valid YouTube link bhej.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_music))

app.run_polling()
