import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# আপনার বটের টোকেন এবং ইউজারনেম এখানে দিন
BOT_TOKEN = "7201062892:AAGewLnDhE6l7buTuXAIScVhI4d-XJZZ5Hs"  # আপনার আসল টোকেন এখানে দিন
BOT_USERNAME = "Easyearing99_bot"  # আপনার বটের ইউজারনেম দিন (শেষের @ ছাড়া)

# লগিং চালু করা হচ্ছে
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start কমান্ডের ফাংশন
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/start কমান্ড দিলে এই ফাংশনটি কাজ করবে"""
    user = update.effective_user
    
    # স্বাগতম বার্তা
    welcome_text = (
        "<b>Earn Real Cash with Our Bot!</b>\n\n"
        "Watch videos, complete simple tasks, and view ads to boost your income. "
        "Withdraw your earnings easily!\n\n"
        "Tap the buttons below to start."
    )

    # ইনলাইন বাটন তৈরি
    keyboard = [
        # বাটন ১: ওয়েব অ্যাপ খোলার জন্য
        [InlineKeyboardButton("📺 Watch to Earn", web_app=WebAppInfo(url="https://xmod.top/p/asyincome24-html"))],
        
        # বাটন ২: অফিসিয়াল চ্যানেলের লিংক
        [InlineKeyboardButton("✅ Official Channel", url="https://t.me/Easyearing99")],
        
        # বাটন ৩: বন্ধুদের ইনভাইট করার জন্য (callback_data ব্যবহার করে)
        [InlineKeyboardButton("🤝 Invited Friends", callback_data="invite_friends")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # বার্তাটি পাঠানো হচ্ছে
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='HTML' # Bold করার জন্য HTML পার্স মোড ব্যবহার করা হলো
    )

# বাটন ক্লিকের জন্য ফাংশন
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ইনলাইন বাটনে ক্লিক করলে এটি কাজ করবে"""
    query = update.callback_query
    await query.answer() # ব্যবহারকারীকে ফিডব্যাক দেয় যে ক্লিকটি গৃহীত হয়েছে

    # কোন বাটনে ক্লিক করা হয়েছে তা callback_data থেকে জানা যায়
    if query.data == 'invite_friends':
        user_id = query.from_user.id
        # রেফারেল লিংক তৈরি করা
        referral_link = f"https://t.me/{BOT_USERNAME}?start={user_id}"
        
        # রেফারেল বার্তা তৈরি
        invite_text = (
            "🎉 Invite your friends and earn more!\n\n"
            "Share your personal referral link with them:\n\n"
            f"<code>{referral_link}</code>"
        )
        
        # নতুন বার্তা হিসেবে রেফারেল লিংক পাঠানো হচ্ছে
        await query.message.reply_text(text=invite_text, parse_mode='HTML')


def main() -> None:
    """বটটি চালু করার প্রধান ফাংশন"""
    # Application তৈরি করা
    application = Application.builder().token(BOT_TOKEN).build()

    # কমান্ড হ্যান্ডলার যোগ করা
    application.add_handler(CommandHandler("start", start))
    
    # বাটন ক্লিকের জন্য Callback Query হ্যান্ডলার যোগ করা
    application.add_handler(CallbackQueryHandler(button_handler))

    # বটটি চালু করা
    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()