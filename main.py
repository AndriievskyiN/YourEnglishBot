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

# BOOK COMMAND BUTTONS
indeng = InlineKeyboardButton(text="🙋‍♂️Individual Class", callback_data="ind")
groupeng = InlineKeyboardButton(text="👨‍👩‍👧‍👦Group class", callback_data="group")
minigroupeng = InlineKeyboardButton(text="👬Mini Group class", callback_data="mini-group")
speakingeng = InlineKeyboardButton(text="🗣Speaking class", callback_data="speaking")
optionseng = InlineKeyboardMarkup().add(indeng).add(minigroupeng).add(groupeng).add(speakingeng).add(gbeng)

indukr = InlineKeyboardButton(text="🙋‍♂️Індивідуальний урок", callback_data="ind")
groupukr = InlineKeyboardButton(text="👨‍👩‍👧‍👦Груповий урок", callback_data="group")
minigroupukr = InlineKeyboardButton(text="👬Міні Груповий урок", callback_data="mini-group")
speakingukr = InlineKeyboardButton(text='"🗣Speaking" урок', callback_data="speaking")
optionsukr = InlineKeyboardMarkup().add(indukr).add(minigroupukr).add(groupukr).add(speakingukr).add(gbukr)

indru = InlineKeyboardButton(text="🙋‍♂️Индивидуальный урок", callback_data="ind")
groupru = InlineKeyboardButton(text="👨‍👩‍👧‍👦Групповой урок", callback_data="group")
minigroupru = InlineKeyboardButton(text="👬Мини Груповий урок", callback_data="mini-group")
speakingru = InlineKeyboardButton(text='"🗣Speaking" урок', callback_data="speaking")
optionsru = InlineKeyboardMarkup().add(indru).add(minigroupru).add(groupru).add(speakingru).add(gbru)

# INFO COMMAND BUTTONS
iindeng = InlineKeyboardButton(text="🙋‍♂️Individual Class", callback_data="iind")
igroupeng = InlineKeyboardButton(text="👨‍👩‍👧‍👦Group class", callback_data="igroup")
iminigroupeng = InlineKeyboardButton(text="👬Mini Group class", callback_data="imini-group")
ispeakingeng = InlineKeyboardButton(text="🗣Speaking class", callback_data="ispeaking")
ioptionseng = InlineKeyboardMarkup().add(iindeng).add(iminigroupeng).add(igroupeng).add(ispeakingeng).add(gbeng)

iindukr = InlineKeyboardButton(text="🙋‍♂️Індивідуальний урок", callback_data="iind")
igroupukr = InlineKeyboardButton(text="👨‍👩‍👧‍👦Груповий урок", callback_data="igroup")
iminigroupukr = InlineKeyboardButton(text="👬Міні Груповий урок", callback_data="imini-group")
ispeakingukr = InlineKeyboardButton(text='"🗣Speaking" урок', callback_data="ispeaking")
ioptionsukr = InlineKeyboardMarkup().add(iindukr).add(iminigroupukr).add(igroupukr).add(ispeakingukr).add(gbukr)

iindru = InlineKeyboardButton(text="🙋‍♂️Индивидуальный урок", callback_data="iind")
igroupru = InlineKeyboardButton(text="👨‍👩‍👧‍👦Групповой урок", callback_data="igroup")
iminigroupru = InlineKeyboardButton(text="👬Мини Груповий урок", callback_data="imini-group")
ispeakingru = InlineKeyboardButton(text='"🗣Speaking" урок', callback_data="ispeaking")
ioptionsru = InlineKeyboardMarkup().add(iindru).add(iminigroupru).add(igroupru).add(ispeakingru).add(gbru)


# START COMMAND
@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    cur.execute('''SELECT lang FROM Users WHERE id = ?''', (message.from_user.id,))
    lang = cur.fetchone()

    if lang == "eng":
        await message.answer(f"Hello {message.from_user.first_name}!\nI'm Your English Bro Bot 🤖\nWhat's up? \nFor starters type /help")
    elif lang == "ukr":
        await message.answer(f"Привіт {message.from_user.first_name}!\nЯ твій English Bro Bot 🤖 \nЯк ся маєш? \nДля початку введи /help")
    elif lang == "ru":
        await message.answer(f"Привет {message.from_user.first_name}!\nЯ твой English Bro Bot 🤖\nКак дела? \nДля начала нажми /help")
    else:
        await message.answer(f"Hello {message.from_user.first_name}!\nI'm Your English Bro Bot 🤖\nWhat's up? \nFor starters /help")


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

# CONTACT COMMAND
@dp.message_handler(commands=["contact"])
async def contact(message: types.Message):
    await message.answer(responses("contact_command", message.from_user.id))

# BOOK COMMAND
@dp.message_handler(commands=["book"])
async def book(message: types.Message):
    await message.answer(responses("book_command", message.from_user.id),reply_markup=optionsKeyboard(message.from_user.id))

# MANAGING BOOK OPTIONS
@dp.callback_query_handler(text=["gback","ind","group","mini-group","speaking"])
async def manage_options(call: types.CallbackQuery):
    if call.data == "gback":
        await call.message.delete()
    elif call.data == "ind":
        await call.message.delete()
        await call.message.answer(responses("ind_classes", call.from_user.id))
    elif call.data == "group":
        await call.message.delete()
        await call.message.answer(responses("group_classes", call.from_user.id))
    elif call.data == "mini-group":
        await call.message.delete()
        await call.message.answer(responses("mini-group_classes",call.from_user.id))
    elif call.data == "speaking":
        await call.message.delete()
        await call.message.answer(responses("speaking_classes", call.from_user.id))

# CANCEL COMMAND
@dp.message_handler(commands=["cancel"])
async def cancel(message: types.Message):
    await message.answer(responses("cancel_command", message.from_user.id))

# ABOUT CLASS INFO
@dp.message_handler(commands=["info"])
async def lessoninfo(message: types.Message):
    await message.answer(responses("lessoninfo_command", message.from_user.id), reply_markup=optionsInfo(message.from_user.id))

# MANAGING CLASS INFO BUTTONS
@dp.callback_query_handler(text=["gback","iind","igroup","imini-group","ispeaking"])
async def manage_classinfo(call: types.CallbackQuery):
    if call.data == "gback":
        await call.message.delete()
    elif call.data == "iind":
        await call.message.delete()
        await call.message.answer(responses("indinfo", call.from_user.id))
    elif call.data == "igroup":
        await call.message.delete()
        await call.message.answer(responses("groupinfo", call.from_user.id))
    elif call.data == "imini-group":
        await call.message.delete()
        await call.message.answer(responses("mini-groupinfo", call.from_user.id))
    elif call.data == "ispeaking":
        await call.message.delete()
        await call.message.answer(responses("speakinginfo", call.from_user.id))

# MANAGING REGULAR MESSAGES
@dp.message_handler()
async def messages(message: types.Message):
    await message.answer(responses(message.text, message.from_user.id))

def responses(command, id):
    cur.execute('''SELECT lang FROM Users WHERE id = ?''',(id,))
    lang = cur.fetchone()[0]

    if str(command) == "help_command":
        if lang == "eng":
            return "This is the list of all commands: \n/start - Start the bot \n/about - Get to know the teacher better \n/lang - Select your language \n/contact - Contact the teacher \n/book - Book a class \n/cancel Cancel a class \n/help - Get the list of all commands \n------------------------------------------------------------- \nIf this is not something you're looking for, please contact the teacher directly: \n/contact"
        elif lang == "ukr":
            return "Це список усіх команд: \n/start - Запустити бота \n/about - Дізнатися більше про вчителя \n/lang - Вибери свою мову \n/contact - Зв'яжись з вчителем \n/book - Забронювати урок \n/cancel - Скасувати урок \n/help - Отримай список усіх команд \n------------------------------------------------------------- \nЯкщо це не те, що ти шукаєш, звернись безпосередньо до вчителя: \n/contact"
        elif lang == "ru":
            return "Это список всех команд: \n/start - Запустить бота \n/about - Узнать больше про учителя \n/lang - Выбрать язык \n/contact - Связаться с учителем \n/book - Забронировать урок \n/cancel - Отменить урок \n/help - Получить список всех команд \n-------------------------------------------------------------- \nЕсли это не то, что ты ищешь, свяжись напрямую с учителем: \n/contact"
        else:
            return "This is the list of all commands: \n/start - Start the bot \n/about - Get to know the teacher better \n/lang - Select your language \n/contact - Contact the teacher \n/book - Book a class \n/cancel Cancel a class \n/help - Get the list of all commands \n------------------------------------------------------------- \nIf this is not something you're looking for, please contact the teacher directly: \n/contact"

    elif str(command) == "lang_command":
        if lang == "eng":
            return "Select your language"
        elif lang == "ukr":
            return "Вибери свою мову"
        elif lang == "ru":
            return "Выбери свой язык"
        else:
            return "Select your language"


    elif str(command) == "contact_command":
        if lang == "eng":
            return "📷Instagram: \nhttps://instagram.com/your_english_bro?igshid=YmMyMTA2M2Y= \n------------------------------------------------------------- \n📞Phone number: +380951775440"
        elif lang == "ukr":
            return "📷Instagram: \nhttps://instagram.com/your_english_bro?igshid=YmMyMTA2M2Y= \n------------------------------------------------------------- \n📞Номер телефону: +380951775440"
        elif lang == "ru":
            return "📷Instagram: \nhttps://instagram.com/your_english_bro?igshid=YmMyMTA2M2Y= \n------------------------------------------------------------- \n📞Номер телефона: +380951775440"
        else:
            return "📷Instagram: \nhttps://instagram.com/your_english_bro?igshid=YmMyMTA2M2Y= \n------------------------------------------------------------- \n📞Phone number: +380951775440"

    elif str(command) == "cancel_command":
        if lang == "eng":
            return "If you want to cancel a class, please contact the teacher directly: \n+380951775440"
        elif lang == "ukr":
            return "Якщо ты хочеш скасувати урок, звернись безпосередньо до вчителя: \n+380951775440"
        elif lang == "ru":
            return "Если ты хочешь отменить занятие, свяжись с учителем напрямую: \n+380951775440"
        else:
            return "If you want to cancel a class, please contact the teacher directly: \n+380951775440"


    elif str(command) == "book_command":
        if lang == "eng":
            return "These are the options you can choose from"
        elif lang == "ukr":
            return "Це варіанти, які ти можеш вибрати"
        elif lang == "ru":
            return "Это варианты, которые ты можешь выбрать"
        else:
            return "These are the options you can choose from"

    elif str(command) == "ind_classes":
        if lang == "eng":
            return "To book an individual class, please contact the teacher directly via Telegram, phone call, or Instagram \n/contact"
        elif lang == "ukr":
            return "Щоб забронювати індивідуальний урок, зв’яжись з вчителем безпосередньо через Telegram, телефонний дзвінок або Instagram \n/contact"
        elif lang == "ru":
            return "Чтобы записаться на индивидуальный урок, свяжись с учителем напрямую в Telegram, по телефону или в Instagram \n/contact"
        else: 
            return "To book an individual class, please contact the teacher directly via Telegram, phone call, or Instagram \n/contact"

    elif str(command) == "group_classes":
        if lang == "eng":
            return "I'm sorry... This command doesn't work for now :("
        elif lang == "ukr":
            return "Вибачте... Ця команда зараз не працює :("
        elif lang == "ru":
            return "Извините... Эта команда пока не работает :("
        else: 
            return "I'm sorry... This command doesn't work for now :("

    elif str(command) == "mini-group_classes":
        if lang == "eng":
            return "If you want to attend a mini-group class, please contact the teacher directly via Telegram, phone call, or Instagram \n/contact"
        elif lang == "ukr":
            return "Якщо ти хочеш відвідати заняття в міні-групі, зв’яжись з вчителем безпосередньо через Telegram, телефонний дзвінок або Instagram \n/contact"
        elif lang == "ru":
            return "Если ты хочешь посетить занятие в мини-группе, свяжись с учителем напрямую в Telegram, по телефону или в Instagram \n/contact"
        else:
            return "If you want to attend a mini-group class, please contact the teacher directly via Telegram, phone call, or Instagram \n/contact v"

    elif str(command) == "speaking_classes":
        if lang == "eng":
            return "If you want to attend a speaking class, join this group for further information: \nhttps://t.me/your_english_bro"
        elif lang == "ukr":
            return "Якщо ти хочеш відвідати speaking урок, зоходь до цієї групи, щоб отримати додаткову інформацію: \nhttps://t.me/your_english_bro"
        elif lang == "ru":
            return "Если ты хочешь посетить speaking урок, заходи в эту группу для дополнительной информации: \nhttps://t.me/your_english_bro"
        else: 
            return "If you want to attend a speaking class, join this group for further information: \nhttps://t.me/your_english_bro"

    elif str(command) == "lessoninfo_command":
        if lang == "eng":
            return "Select a lesson you want to know more about"
        elif lang == "ukr":
            return "Обери урок, про який хочеш дізнатися більше"
        elif lang == "ru":
            return "Выбери урок, о котором хочешь узнать больше"
        else:
            return "Select a lesson you want to know more about"

    elif str(command) == "indinfo":
        if lang == "eng":
            return '''Individual lesson is a perfect option for a person who wants to prepare for passing exams like TOEFL, IELTS, ЗНО or ДПА \n \nDuration: 55 minutes \nSchedule is created based on clients preference'''
        elif lang == "ukr":
            return '''Індивідуальне заняття - ідеальний варіант для людини, яка хоче підготуватися до здачі іспитів, таких як TOEFL, IELTS, ЗНО або ДПА \n \nТривалість: 55 хвилин \nРозклад створюється на основі уподобань клієнта'''
        elif lang == "ru":
            return '''Индивидуальное занятие - идеальный вариант для человека, который хочет подготовиться к сдаче таких экзаменов, как TOEFL, IELTS, ЗНО или ДПА \n \nПродолжительность: 55 минут \nРасписание составляется исходя из предпочтений клиента'''
        else:
            return '''Individual lesson is a perfect option for a person who wants to prepare for passing exams like TOEFL, IELTS, ЗНО or ДПА \n \nDuration: 55 minutes \nSchedule is created based on clients preference'''

    elif str(command) == "groupinfo":
        if lang == "eng":
            return '''Group lessons is a perfect option for a person who wants to improve grammar, reading and listening skills along with other people. All people in the groups are of a similar age and level. \n \nDuration: 55 or 115 minutes \n5-8 people in the group'''
        elif lang == "ukr":
            return '''Групові заняття – ідеальний варіант для людини, яка хоче разом з іншими людьми покращити граматику, навички читання та аудіювання. Усі люди в групах однакового віку та рівня. \n \nТривалість: 55 або 115 хвилин \n5-8 осіб у групі'''
        elif lang == "ru":
            return '''Group lessons is a perfect option for a person who wants to improve grammar, reading and listening skills along with other people. All people in the groups are of a similar age and level. \n \nDuration: 55 or 115 minutes \n5-8 people in the group'''
        else:
            return '''Group lessons is a perfect option for a person who wants to improve grammar, reading and listening skills along with other people. All people in the groups are of a similar age and level. \n \nDuration: 55 or 115 minutes \n5-8 people in the group'''

    elif str(command) == "mini-groupinfo":
        if lang == "eng":
            return '''Mini-group lesson is a perfect option for a person who wants to improve speaking, grammar, reading and listening skills along with a small group of people. All students are similar age and level. \n \nDuration: 55 or 115 minutes \n2-4 people in the group'''
        elif lang == "ukr":
            return '''Заняття в міні-групі – ідеальний варіант для людини, яка хоче разом з невеликою групою людейи покращити навички говоріння, граматики, читання та аудіювання. Усі учні однакового віку та рівня. \n \nТривалість: 55 або 115 хвилин \n2-4 людини в групі'''
        elif lang == "ru":
            return '''Занятие в мини-группе — идеальный вариант для человека, который хочет улучшить навыки говорения, грамматики, чтения и аудирования вместе с небольшой группой. Все ученики одного возраста и уровня. \n \nПродолжительность: 55 или 115 минут \n2-4 человека в группе'''
        else:
            return '''Mini-group lesson is a perfect option for a person who wants to improve speaking, grammar, reading and listening skills along with a small group of people. All students are similar age and level. \n \nDuration: 55 or 115 minutes \n2-4 people in the group'''
    
    elif str(command) == "speakinginfo":
        if lang == "eng":
            return '''Speaking club is a perfect type of the lesson where you can improve your speaking skills. \nFor now the speaking classes are completely free'''
        elif lang == "ukr":
            return '''Speaking club – ідеальний тип уроку, де ви можете покращити свої мовленнєві навички. \nНаразі Speaking урокы абсолютно безкоштовні'''
        elif lang == "ru":
            return '''Разговорный клуб — это идеальный вариант урока, на котором вы можете улучшить свои разговорные навыки. \nНа данный момент Speaking уроки совершенно бесплатны.'''
        else:
            return '''Speaking club is a perfect type of the lesson where you can improve your speaking skills. \nFor now the speaking classes are completely free'''
    
    elif str(command) == "about_command":
        if lang == "eng":
            return '''My name is Viacheslav aka Your English Bro 😎 

I’ve been teaching for more than 3 years. 
I am Business English teacher 👨‍🏫 in Ukrainian-American Concordia university. 
I’ve completed language courses in Reading, UK 🇬🇧, Exeter, UK 🇬🇧 and Toronto, Canada 🇨🇦 
I have BBA and MBA, so I know something about business as well as economics 💵 
I have worked as a farmer, a manager, a translator, a trainer, had my own company, but my real passion has always been teaching.

My big goal is to teach as many people as I can to make Ukraine an English speaking country'''
        elif lang == "ukr":
            return '''Мене звати В’ячеслав, так само відомий як Your English Bro 😎

Викладаю більше 3 років.
Я викладач ділової англійської 👨‍🏫 в українсько-американському університеті Конкордія.
Я закінчив мовні курси в Редінгу, Великобританія 🇬🇧, Ексетер, Великобританія 🇬🇧 та Торонто, Канада 🇨🇦
У мене є BBA та MBA, тому я знаю дещо як про бізнес, так і про економіку 💵
Я працював фермером, менеджером, перекладачем, тренером, мав власну компанію, але моєю справжньою пристрастю завжди було навчання.

Моя велика мета – навчити якомога більше людей зробити Україну англомовною країною'''
        elif lang == "ru":
            return '''Меня зовут Вячеслав, так же известный как Your English Bro 😎

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
    else:
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


def optionsInfo(id):
    cur.execute('''SELECT lang FROM Users WHERE id = ?''', (id,))
    lang = cur.fetchone()[0]

    if lang == "eng":
        return ioptionseng
    elif lang == "ukr":
        return ioptionsukr
    elif lang == "ru":
        return ioptionsru
    else:
        return ioptionseng


def optionsKeyboard(id):
    cur.execute('''SELECT lang FROM Users WHERE id = ?''', (id,))
    lang = cur.fetchone()[0]

    if lang == "eng":
        return optionseng
    elif lang == "ukr":
        return optionsukr
    elif lang == "ru":
        return optionsru
    else:
        return optionseng

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)