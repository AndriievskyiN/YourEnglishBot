from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

# SETTING UP DATABASES
conn = sqlite3.connect("users.sqlite")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Users (
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name TEXT,
    lastName TEXT,
    lang
)''')
conn.commit()


# PRE-BUILT INPUTS
hi_eng = ["hi", "hello", "what's up?", "what is up", "what's up", "what is up?", "hello there", "sup", "whassup", "wha sup", "hi there", "hey"]
hi_ukr = ["привіт", "хей", "добрий день"]
hi_ru = ["привет", "хей", "хай", "добрый день"]

# SETTING UP THE BOT
API_TOKEN = '5108593896:AAFrhYyfeqXLolGlyzOqNgxysSJwfg578-0'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# LANGUAGE BUTTONS
english = InlineKeyboardButton(text="🇺🇸English🇺🇸", callback_data="eng")
ukrainian = InlineKeyboardButton(text="🇺🇦Українська🇺🇦", callback_data="ukr")
ru = InlineKeyboardButton(text="русский", callback_data="ru")
langKeyboard = InlineKeyboardMarkup().add(english).add(ukrainian).add(ru)

# GET BACK BUTTON
gbeng = InlineKeyboardButton(text="⬅️Go Back", callback_data="gback")
gbukr = InlineKeyboardButton(text="⬅️Повернутися", callback_data="gback")
gbru = InlineKeyboardButton(text="⬅️Вернуться", callback_data="gback")


# START COMMAND
@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):

    try:
        cur.execute('''SELECT lang FROM Users WHERE id = ?''', (message.from_user.id,))
        global lang
        lang = cur.fetchone()[0]
    except:
        await message.answer(f"Hello {message.from_user.first_name}!\nI'm Your English Bro Bot \nWhat's up? \nFor starters /help")

    if lang == "eng":
        await message.answer(f"Hello {message.from_user.first_name}!\nI'm Your English Bro Bot \nWhat's up? \nFor starters type /help")
    elif lang == "ukr":
        await message.answer(f"Привіт {message.from_user.first_name}\nЯ твій English Bro Bot \Як ся маєш? \nДля початку введіть /help")
    elif lang == "ru":
        await message.answer(f"Привет {message.from_user.first_name}!\nЯ твой English Bro Bot \nКак дела? \nДля начала нажми /help")


    cur.execute('''INSERT OR IGNORE INTO Users (id,name, lastName)
        VALUES (?,?,?)''',(message.from_user.id, message.from_user.first_name, message.from_user.last_name))
    conn.commit()
# LANG COMMAND
@dp.message_handler(commands=["lang"])
async def lang(message: types.Message):
    await message.answer(responses("lang_command", message.from_user.id), reply_markup=langKeyboard)

# MANAGING LANGUAGES
@dp.callback_query_handler(text=["eng", "ukr", "ru"])
async def changeLang(call: types.CallbackQuery):
    if call.data == "eng":
        await call.message.delete()
        await call.message.answer("Agreed!")
    elif call.data == "ukr":
        await call.message.delete()
        await call.message.answer("Домовились!")
    elif call.data == "ru":
        await call.message.delete()
        await call.message.answer("Договорились!")

    cur.execute('''INSERT OR REPLACE INTO Users (id, name, lastName, lang)
        VALUES (?,?,?,?)''', (call.from_user.id,call.from_user.first_name, call.from_user.last_name, call.data))
    conn.commit()

# HELP COMMAND
@dp.message_handler(commands=["help"])
async def welcome(message: types.Message):
    await message.answer(responses("help_command", message.from_user.id))

# ABOUT COMMAND
@dp.message_handler(commands=["about"])
async def about(message: types.Message):
    await message.answer(responses("about_command",message.from_user.id))

# MANAGING REGULAR MESSAGES
@dp.message_handler()
async def messages(message: types.Message):
    await message.answer(responses(message.text, message.from_user.id))

def responses(command, id):
    cur.execute('''SELECT lang FROM Users WHERE id = ?''',(id,))
    lang = cur.fetchone()[0]
    print(lang)

    if str(command) == "help_command":
        if lang == "eng":
            return "This is the list of all commands: \n/start - Start the bot \n/about - Get to know the teacher better \n/lang - Select your language \n/contact - Contact the teacher \n/help - Get the list of all commands \n------------------- \nIf this is not something you're looking for, please contact the teacher directly: +380 95 177 5440"
        elif lang == "ukr":
            return "Це список усіх команд: \n/start - Запустити бота \n/about - Дізнатися більше про вчителя \n/lang - Виберіть свою мову \n/cotact - Зв'яжіться з викладачем \n/help - Отримайте список усіх команд \n------------------- \nЯкщо це не те, що ви шукаєте, зверніться безпосередньо до викладача: +380 95 177 5440"
        elif lang == "ru":
            return "Это список всех команд: \n/start - Запустить бота \n/about - Узнать больше про учителя \n/lang - Выбрать язык \n/cotact - Связаться с учителем \n/help - Получить список всех команд \n------------------- \nЕсли это не то, что вы ищете, свяжитесь напрямую с учителем: +380 95 177 5440"
        else:
            return "This is the list of all commands: \n/start - Start the bot \n/about - Get to know the teacher better \n/lang - Select your language \n/contact - Contact the teacher \n/help - Get the list of all commands \n------------------- \nIf this is not something you're looking for, please contact the teacher directly: +380 95 177 5440"

    if str(command) == "lang_command":
        return "Select your language"

    if str(command) == "about_command":
        if lang == "eng":
            return '''My name is Viacheslav aka Your English Bro 😎 

I’ve been teaching for more than 3 years. 
I am Business English teacher 👨‍🏫 in Ukrainian-American Concordia university. 
I’ve completed language courses in Reading, UK 🇬🇧, Exeter, UK 🇬🇧 and Toronto, Canada 🇨🇦 
I have BBA and MBA, so I know something about business as well as economics 💵 
I have worked as a farmer, a manager, a translator, a trainer, had my own company, but my real passion has always been teaching.

My big goal is to teach as many people as I can to make Ukraine an English speaking country'''
        elif lang == "ukr":
            return '''Мене звати В’ячеслав, він же «Ваш англійський брат» 😎

Викладаю більше 3 років.
Я викладач ділової англійської 👨‍🏫 в українсько-американському університеті Конкордія.
Я закінчив мовні курси в Редінгу, Великобританія 🇬🇧, Ексетер, Великобританія 🇬🇧 та Торонто, Канада 🇨🇦
У мене є BBA та MBA, тому я знаю дещо як про бізнес, так і про економіку 💵
Я працював фермером, менеджером, перекладачем, тренером, мав власну компанію, але моєю справжньою пристрастю завжди було навчання.

Моя велика мета – навчити якомога більше людей зробити Україну англомовною країною'''
        elif lang == "ru":
            return '''Меня зовут Вячеслав, он же Your English Bro 😎

Преподаю более 3-х лет.
Я преподаватель делового английского 👨‍🏫 в украинско-американском университете Конкордия.
Я прошла языковые курсы в Рединге, Великобритания 🇬🇧, Эксетере, Великобритания 🇷🇧 и Торонто, Канада 🇨🇦
У меня есть BBA и MBA, так что я знаю кое-что о бизнесе, а также экономике 💵
Я работал фермером, менеджером, переводчиком, тренером, имел собственную компанию, но моей настоящей страстью всегда было преподавание.

Моя большая цель — научить как можно больше людей сделать Украину англоязычной страной.'''
        else:
            return '''My name is Viacheslav aka Your English Bro 😎 

I’ve been teaching for more than 3 years. 
I am Business English teacher 👨‍🏫 in Ukrainian-American Concordia university. 
I’ve completed language courses in Reading, UK 🇬🇧, Exeter, UK 🇬🇧 and Toronto, Canada 🇨🇦 
I have BBA and MBA, so I know something about business as well as economics 💵 
I have worked as a farmer, a manager, a translator, a trainer, had my own company, but my real passion has always been teaching.

My big goal is to teach as many people as I can to make Ukraine an English speaking country'''

    if str(command).lower() in hi_eng:
        return "Hello there!"
    elif str(command).lower() in hi_ukr:
        return "Привіт!"
    elif str(command).lower() in hi_ru:
        return 'Привет!'
    else:
        if lang == "eng":
            return "I'm sorry... I don't understand what you mean :("
        elif lang == "ukr":
            return "Вибачте... я не розумію що ви маєте на увазі :("
        elif lang == "ru":
            return "Извините... я не понимаю, что вы имеете ввиду :("
        else:
            return "I'm sorry... I don't understand what you mean :("


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)