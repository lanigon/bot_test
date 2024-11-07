from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.ext import filters

key = '7031960302:AAGZULaAsrqjOryNHDy0XvWxTSeJqEVyCQw'
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应start命令'''
    text = '你好~我是一个bot'
    
    await context.bot.send_message(chat_id=update.effective_chat.id,text=text)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="我不会这个哦~")


start_handler = CommandHandler('start', start)
#unknown_handler = MessageHandler(filters.COMMAND, unknown)

# 构建 bot
TOKEN= key
application = ApplicationBuilder().token(TOKEN).build()
# 注册 handler
application.add_handler(start_handler)
# run!
application.run_polling()