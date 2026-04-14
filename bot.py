import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

addresses = [
    "0xf466729D760e8AF856a6535C50a30847fdB1107B",
    "0x6471f7AAcA225dB0e560047FF075a9E02ECe0882",
    "0x8A806A0eC49c60246aD5427eDBA515E36a487067",
    "0xeE819B094943572D3C879946ADaA8e332F17b0A3",
    "0x9185c968cE57d83b604fDB9AEcbef6B794E5301c",
    "0xD3EdAB404cd7602c428F260708A727729782e53D",
    "0x8952cd1Bc903E6C26510Eda1c4248F927C5774f6"
]

used = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.message.from_user.id

    if uid in used:
        await update.message.reply_text("You already received an address ❗️")
        return

    if not addresses:
        await update.message.reply_text("No more addresses available ❌")
        return

    addr = addresses.pop(0)
    used.add(uid)

    await update.message.reply_text(addr)

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
