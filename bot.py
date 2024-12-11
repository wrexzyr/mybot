from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Замените на ваш токен
TOKEN = '7738199778:AAFnT5v2BVHol7GUmz7N9DGSwvsFye4ijL0'

# Список ID пользователей, которым будут отправляться предложения
USER_IDS = [7639766026, 1162774908]  # Замените на реальные ID пользователей

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Отправьте ваше предложение, и я передам его владельцу.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    user_message = update.message.text

    # Отправляем сообщение каждому указанному пользователю
    for recipient_id in USER_IDS:
        try:
            await context.bot.send_message(chat_id=recipient_id, 
                                            text=f'Предложение от пользователя: {user_message}')
        except Exception as e:
            print(f"Не удалось отправить сообщение владельцу {recipient_id}: {e}")

    await update.message.reply_text('Ваше предложение отправлено владельцу! Спасибо!')

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
