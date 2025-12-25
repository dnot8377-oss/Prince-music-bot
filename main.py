from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive! 🎵"

def run_bot():
    # Tera poora bot code yahan (application.run_polling())
    app.run_polling()  # ya telegram_app.run_polling()

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
