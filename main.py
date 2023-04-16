import telebot
from telebot import types
from transformers import FSMTForConditionalGeneration, FSMTTokenizer

bot = telebot.TeleBot('6284659931:AAGW4k18XPA9HlYwUobf8h2yeCClwSasVcI')

global answers
answers = []
answers.append('no command')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Воспользоваться переводчиком')
        btn2 = types.KeyboardButton('Продолжить фразу')
        btn3 = types.KeyboardButton('Сгенерировать текст')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Нужно выбрать действие', reply_markup=markup) #ответ бота


    elif message.text == "Воспользоваться переводчиком":

        '''mname = "facebook/wmt19-ru-en"
        tokenizer = FSMTTokenizer.from_pretrained(mname)
        model = FSMTForConditionalGeneration.from_pretrained(mname)

        input = message.text
        input_ids = tokenizer.encode(input, return_tensors="pt")
        outputs = model.generate(input_ids)
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(decoded)  # Machine learning is great, isn't it?'''
        answers.append('translate')

        bot.send_message(message.from_user.id, 'Введите текст на русском',  parse_mode='Markdown')

    elif message.text == 'Продолжить фразу':
        bot.send_message(message.from_user.id, 'Извините, функция пока недоступна :(', parse_mode='Markdown')
        answers.append('phrase')

    elif message.text == 'Сгенерировать текст':
        bot.send_message(message.from_user.id, 'Извините, функция пока недоступна :(', parse_mode='Markdown')
        answers.append('generate')
    else:


        if answers[len(answers)-1] == "translate":
            mname = "facebook/wmt19-ru-en"
            tokenizer = FSMTTokenizer.from_pretrained(mname)
            model = FSMTForConditionalGeneration.from_pretrained(mname)

            input = message.text
            input_ids = tokenizer.encode(input, return_tensors="pt")
            outputs = model.generate(input_ids)
            decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(decoded)  # Machine learning is great, isn't it?

            bot.send_message(message.from_user.id, decoded, parse_mode='Markdown')



bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть