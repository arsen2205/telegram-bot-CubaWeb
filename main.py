import telebot
from flask import Flask, request

TOKEN = "7769430876:AAEYNrldkEY5REQ3XZj5VFMxDb0aHpy6pyI"
WEBHOOK_URL = "https://telegram-bot-cubaweb.onrender.com/{TOKEN}"  # Reemplaza con tu URL en Render

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    if update:
        bot.process_new_updates([telebot.types.Update.de_json(update)])
    return "OK", 200

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = (
        "🌟 ¡Bienvenido a CubaWeb! 🌟\n\n"
        "¿Tienes un negocio y necesitas una página web profesional que te ayude a crecer? 🚀\n\n"
        "En CubaWeb, creamos soluciones digitales para que te destaques de la competencia. 😍\n\n"
        "🎯 ¡Es momento de transformar tu presencia en línea! 🖥\n\n"
        "🔹 Solicita nuestro servicio con un clic.\n"
        "🔹 Descubre por qué tener una web te cambiará la vida.**\n"
        "⬇️ ¡Elige una opción abajo! ⬇️"
    )

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('✨ Solicitar servicio ✨', callback_data='solicitar_servicio'))
    markup.add(telebot.types.InlineKeyboardButton('💡 ¿Por qué tener una web?', callback_data='ventajas_web'))
    
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'solicitar_servicio')
def handle_service_request(call):
    bot.send_message(call.message.chat.id, "🎉 ¡Gracias por tu interés! Un administrador se pondrá en contacto contigo pronto. 🚀")
    
    user_info = (
        f"🔔 Nuevo cliente potencial: 🔔\n"
        f"📛 Nombre: {call.from_user.first_name} {call.from_user.last_name}\n"
        f"🧑‍💻 Username: @{call.from_user.username}\n"
        f"💬 ID: {call.from_user.id}"
    )

    bot.send_message("818966535", user_info)

@bot.callback_query_handler(func=lambda call: call.data == 'ventajas_web')
def handle_advantages(call):
    advantages_message = (
        "💡 ¿Por qué tener una página web? 💡\n\n"
        "🔹 Atraes más clientes: Una web trabaja por ti 24/7. 📈\n"
        "🔹 Genera confianza: Una presencia profesional online aumenta la credibilidad. ✅\n"
        "🔹 Mayor alcance: Tu negocio llega a clientes fuera de tu zona. 🌍\n"
        "🔹 Más ventas: Puedes vender productos o servicios en línea. 💰\n"
        "🔹 Publicidad efectiva: Integración con redes sociales y Google para más visibilidad. 🚀\n\n"
        "📩 **¡No pierdas más oportunidades! Solicita tu web hoy mismo."
    )
    
    bot.send_message(call.message.chat.id, advantages_message)

if __name__ == "__main__":
    print("Setting webhook...")
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)  
    app.run(host="0.0.0.0", port=10000)
