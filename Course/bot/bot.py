import nltk
import random
import json
import telebot
import mysql.connector
import config_bot
import connect_SQL
from telebot import types
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split


with open("READABLE_BIG_BOT_CONFIG_2.json", 'r', encoding="UTF-8") as f:
    BOT_CONFIG = json.load(f)  # читаем json в переменную BOT_CONFIG


def cleaner(text):  # функция очистки текста
    cleaned_text = ''
    for ch in text.lower():
        if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz ':
            cleaned_text = cleaned_text + ch
    return cleaned_text


def match(text, example):  # гибкая функция сравнения текстов
    return nltk.edit_distance(text, example) / len(example) < 0.4 if len(example) > 0 else False


def get_intent(text):  # функция определения интента текста
    for intent_ in BOT_CONFIG['intents']:
        if 'examples' in BOT_CONFIG['intents'][intent_]:
            for example in BOT_CONFIG['intents'][intent_]['examples']:
                if match(cleaner(text), cleaner(example)):
                    return intent_


X = []
y = []

for intent in BOT_CONFIG['intents']:
    if 'examples' in BOT_CONFIG['intents'][intent]:
        X += BOT_CONFIG['intents'][intent]['examples']
        y += [intent for i in range(len(BOT_CONFIG['intents'][intent]['examples']))]

# Создаем обучающую выборку для ML-модели
vector = CountVectorizer(preprocessor=cleaner, ngram_range=(1, 3), stop_words=['а', 'и'])
# Создаем векторайзер – объект для превращения текста в вектора
vector.fit(X)
X_vector = vector.transform(X)
# Обучаем векторайзер на нашей выборке
X_train_vector, X_test_vector, y_train, y_test = train_test_split(X_vector, y, test_size=0.3)
# Разбиваем выборку на train и на test
sgd = SGDClassifier()  # Создаем модель
sgd.fit(X_vector, y)  # Тренируем модель
print(sgd.score(X_vector, y))  # Смотрим качество классификации


def get_intent_by_model(text):  # Функция определяющая интент текста с помощью ML-модели
    return sgd.predict(vector.transform([text]))[0]


def bot(text):  # функция бота
    received_intent = get_intent(text)  # 1. попытаться понять намерение сравнением по Левинштейну
    if received_intent is None:
        received_intent = get_intent_by_model(text)  # 2. попытаться понять намерение с помощью ML-модели
    return random.choice(BOT_CONFIG['intents'][received_intent]['responses']), received_intent


BOT = config_bot.BOT
dict_product = connect_SQL.select_all()
purchase = list()
number_phone = ""
category = ""


@BOT.message_handler(commands=["start"])
def start_help(message):
    BOT.send_message(message.from_user.id, "Вот информация о боте \U0001f43c:\n"
                                           "\U0001f4cc Бот предназначен для сбора онлайн заказов в нашем магазине\n"
                                           "\U0001f4cc Составить заказ легко, просто напишите что хотите"
                                           " и бот поможет вам составить заказ\n\n"
                                           "*Пример*  < Хочу телефон > ")


@BOT.message_handler(content_types=['text'])
def start(message):
    if bot(str(message.text))[1] == "hello":
        BOT.send_message(message.from_user.id, bot(str(message.text))[0])
        BOT.send_message(message.from_user.id, "Что хотите купить?")
        BOT.register_next_step_handler(message, dialog1)
    else:
        BOT.send_message(message.from_user.id, "Я не понял тебя")


def dialog1(message):
    global purchase
    global category
    req_2_lvl = ""
    category = ""
    for sign in cleaner(message.text):
        req_2_lvl += sign
    req_2_lvl = req_2_lvl.split(" ")

    req = cleaner(message.text)
    for key, val in dict_product.items():
        for i_val in range(len(val)):
            if len(purchase) == 4:
                break
            description = val[i_val][3].split("; ")
            for i in description:
                if match(cleaner(i), req):
                    purchase = [
                        key,
                        val[i_val][0],
                        val[i_val][1],
                        val[i_val][2]
                    ]
                    BOT.send_message(message.from_user.id, f"Вы хотите {val[i_val][0]}?")
                    BOT.register_next_step_handler(message, dialog_purchase)
                    break

            if len(purchase) == 4:
                break

            for j in req_2_lvl:
                if category == "":
                    if match(cleaner(key), cleaner(j)):
                        category = key
                        BOT.send_message(message.from_user.id, f"Вы хотите {category}?")
                        BOT.register_next_step_handler(message, choice_item)
                        break

    if len(purchase) == 0 and category == "":
        BOT.send_message(message.from_user.id, f"Я вас не понял, давайте попробуем снова.\n"
                                               f"Что хотите купить?")
        BOT.register_next_step_handler(message, dialog1)


def choice_item(message):
    global category
    if message.text.casefold() == "да":
        message_for_choice_item = f"Доступные позиции по категории {category}\n"
        for key, val in dict_product.items():
            for elem_val in val:
                if key == category:
                    message_for_choice_item += f" * {elem_val[0]} - {elem_val[2]}руб\n"
        BOT.send_message(message.from_user.id, f"{message_for_choice_item}")
        BOT.send_message(message.from_user.id, f"Что выберите?")
        BOT.register_next_step_handler(message, dialog1)

    else:
        BOT.send_message(message.from_user.id, f"Я вас понял, давайте попробуем снова.\n"
                                               f"Что хотите купить?")
        BOT.register_next_step_handler(message, dialog1)


def dialog_purchase(message):
    global purchase
    if message.text.casefold() == "да":
        if int(purchase[2]) > 0:
            mess = "Есть в наличие"
            BOT.send_message(message.from_user.id, f"Ваш заказ:\n\n"
                                                   f"\tКатегория: {purchase[0]}\n"
                                                   f"\tНазвание товара: {purchase[1]}\n"
                                                   f"\tНаличие: {mess}\n"
                                                   f"\tЦена: {purchase[3]} руб\n\n")
            BOT.register_next_step_handler(message, num_phone)
            BOT.send_message(message.from_user.id, f"Последний шаг\n"
                                                   f"Введите номер телефона, благодаря которому мы сможем с вами "
                                                   f"связаться\n"
                                                   f"Формат +7... !\n")
        else:
            BOT.send_message(message.from_user.id, f"Извините, но товара нет в наличие\n"
                                                   f"Начнем с начала")
            purchase = []
            BOT.register_next_step_handler(message, dialog1)
    else:
        BOT.send_message(message.from_user.id, f"Хорошо, вернемся в начало\n"
                                               f"Что хотите купить?")
        purchase = []
        BOT.register_next_step_handler(message, dialog1)


def num_phone(message):
    if message.text[0] == "+" and message.text[1] == "7" and len(message.text) == 12:
        global number_phone
        number_phone = message.text
        BOT.send_message(message.from_user.id, f"Отлично!\n"
                                               f"Оформляем заказ?")
        BOT.register_next_step_handler(message, dialog_final)
    else:
        BOT.send_message(message.from_user.id, f"Не правильный формат!\n"
                                               f"Введите снова")
        BOT.register_next_step_handler(message, num_phone)


def dialog_final(message):
    if message.text.casefold() == "да":
        global purchase
        global number_phone
        connect_SQL.edit_poz_in_data(str(purchase[0]), str(purchase[1]),
                                     str(int(purchase[2])-1), str(purchase[3]))
        connect_SQL.add_in_order_data(str(purchase[0]), str(purchase[1]), "1", str(purchase[3]), number_phone)
        BOT.send_message(message.from_user.id, f"Отлично\n"
                                               f"Заказ зарезервирован и скоро с вами свяжутся\n")
    else:
        BOT.send_message(message.from_user.id, f"Хорошо\n"
                                               f"Начнем с начала")
        purchase = []
        BOT.register_next_step_handler(message, dialog1)


BOT.polling()
