from bot_keyboard import *
import telebot

bot = telebot.TeleBot('TOKEN')

value = ''
old_value = ''

@bot.message_handler(commands=['start'])
def get_message(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def main(query):
    global value, old_value 
    data = query.data

    if data == 'no':
        pass
    elif data == 'c':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'error'
    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
            old_value = value
    
    if value == 'error': value = ''


bot.polling(none_stop=False, interval=0)

if __name__ == "__main__":
    main()
