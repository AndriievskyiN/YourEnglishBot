from locale import DAY_2
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import psycopg2

# SETTING UP DATABASES
conn = psycopg2.connect(
    host = "ec2-23-20-224-166.compute-1.amazonaws.com",
    dbname = "d1jp2pb9ar87ii",
    user = "knovjuvpathzmp",
    password = "c42c064b4457b6c474c0fdf73b1b7f7011692fe10000a809f2ddb2965f5538d6",
    port = 5432
)
cur = conn.cursor()

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
    cur.execute('''SELECT lang FROM Users WHERE id = %s''', (message.from_user.id,))
    lang = cur.fetchone()

    if lang == "eng":
        await message.answer(f"Hello {message.from_user.first_name}!\nI'm Your English Bro Bot 🤖\nWhat's up? \nFor starters type /help")
    elif lang == "ukr":
        await message.answer(f"Привіт {message.from_user.first_name}!\nЯ твій English Bro Bot 🤖 \nЯк ся маєш? \nДля початку введи /help")
    elif lang == "ru":
        await message.answer(f"Привет {message.from_user.first_name}!\nЯ твой English Bro Bot 🤖\nКак дела? \nДля начала нажми /help")
    else:
        await message.answer(f"Hello {message.from_user.first_name}!\nI'm Your English Bro Bot 🤖\nWhat's up? \nFor starters /help")


    cur.execute('''INSERT INTO Users (id,firstName, lastName)
        VALUES (%s,%s,%s)
        ON CONFLICT (id) 
            DO NOTHING''',(message.from_user.id, message.from_user.first_name, message.from_user.last_name))
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

    cur.execute('''UPDATE Users 
                    SET lang = %s 
                        WHERE id = %s''', (call.data,call.from_user.id))
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

# TEST
@dp.message_handler(commands=["test"])
async def cancel(message: types.Message):
    if message.from_user.id == 579467950:
        cur.execute('''SELECT * FROM Users''')
        users = cur.fetchall()
        for i in users:
            await message.answer(i)
    else: 
        await message.answer(responses("", message.from_user.id))

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

# STUDENTS COMMAND FOR VYACHESLAV
@dp.message_handler(commands=["students"])
async def students(message: types.Message):
    if message.from_user.id == 579467950 or message.from_user.id == 467337605:
        await message.answer(replyVyacheslav("students_command",message.from_user.id), reply_markup=studentsKeyboard(message.from_user.id))
    else:
        await message.answer(responses(message.text, message.from_user.id))


# MANAGING STUDENTS BUTTONS
@dp.callback_query_handler(text=["all","mon","tue","wed","thu","fri","sat","sun","gb"])
async def manage_students(call: types.CallbackQuery):
    if call.data == "gb":
        await call.message.delete()
    else:
        count = 0
        await call.message.delete()
        for i in VyacheslavStudents(call.from_user.id, call.data):
            await call.message.answer(i)
            await call.message.answer("--------------------------------")
            count += 1
        await call.message.answer(replyVyacheslav("show_count", call.from_user.id,count))


# MANAGING REGULAR MESSAGES AND SPECIAL COMMANDS
@dp.message_handler()
async def messages(message: types.Message):
    # MANAGING COMMANDS FOR VYACHESLAV
    if message.text.startswith("@add"):
        if message.from_user.id == 467337605 or message.from_user.id == 579467950:
            global full
            full = message.text.split()
            global firstName
            firstName = full[1].lower()
            global lastName
            lastName = full[2].lower()
            day = full[3].lower()
            global hour
            hour = full[4]  
            global daydb
            daydb = str(translate("eng",day)).lower()

            # DUPLICATE VALIDATION
            cur.execute('''SELECT firstName, lastName FROM Schedule WHERE day = %s and time = %s''',(daydb, hour))
            class_ = cur.fetchone()
            if not class_ is None:
                await message.answer(replyVyacheslav("daytaken", message.from_user.id, class_[0],class_[1]))

            else:
                await message.answer(replyVyacheslav("vyacheslav_sure", message.from_user.id, message.text), reply_markup=yesnoKeyboard(message.from_user.id, "yesb", "nob"))

    elif message.text.startswith("@cancel"):
        if message.from_user.id == 467337605 or message.from_user.id == 579467950:
            global splitted
            splitted = message.text.split()

            firstName = splitted[1].lower()
            lastName = splitted[2].lower()
            day = splitted[3].lower()
            hour = splitted[4]

            daydb = str(translate("eng", day)).lower()
            await message.answer(replyVyacheslav("vyacheslav_sure", message.from_user.id, message.text), reply_markup=yesnoKeyboard(message.from_user.id, "yesd", "nod"))

    elif message.text.startswith("@group+"):
        if message.from_user.id == 467337605 or message.from_user.id == 579467950:
            global group_message
            group_message = str(message.text).lower().split()
            await message.answer(replyVyacheslav("group_sure", message.from_user.id, group_message), reply_markup=yesnoKeyboard(message.from_user.id, "yesg", "nog"))

    else:
        await message.answer(responses(message.text, message.from_user.id))

# ASKING IF EVERYTHING IS CORRECT
@dp.callback_query_handler(text=["yesb", "nob", "yesd", "nod", "yesg", "nog"])
async def uSure(call: types.CallbackQuery):
    if call.data == "yesb":
        cur.execute('''INSERT INTO Schedule (firstName, lastName, day, time)
            VALUES (%s,%s,%s,%s)''',(firstName, lastName, daydb, hour))
        conn.commit()
        await call.message.delete()
        await call.message.answer(replyVyacheslav("vyacheslav_add", call.from_user.id, full))

    elif call.data == "nob":
        await call.message.delete()
        await call.message.answer(replyVyacheslav("nob", call.from_user.id))

    elif call.data == "yesd":
        await call.message.delete()

        cur.execute('''SELECT * FROM Schedule WHERE firstName = %s and lastName = %s and day = %s and time = %s''',(firstName, lastName, daydb, hour))
        class_ = cur.fetchone()
        if class_ is None:
            await call.message.answer(replyVyacheslav("doesn't_exist", call.from_user.id)) 
            
        else:
            cur.execute('''DELETE
                            FROM
                                Schedule
                            WHERE firstName = %s and lastName = %s and day = %s and time = %s''', (firstName, lastName, daydb, hour))
            conn.commit()
    
            cur.execute("SELECT lang FROM Users WHERE id = %s",(call.from_user.id,))
            lang = cur.fetchone()[0]
            await call.message.answer(replyVyacheslav("cancel_success", call.from_user.id, (firstName.capitalize(), lastName.capitalize(), translate(lang,daydb), hour)))

    elif call.data == "nod":
        await call.message.delete()
        await call.message.answer(replyVyacheslav("nod", call.from_user.id))

    elif call.data == "yesg":
        if len(group_message) == 6:
            cur.execute('''INSERT INTO Groups (group_type, day1, hour1, day2, hour2)
                            VALUES (%s,%s, %s, %s,%s)''',(group_message[1],group_message[2],group_message[3], group_message[4],group_message[5]))
        elif len(group_message) == 8:
            cur.execute('''INSERT INTO Groups (group_type, day1, hour1, day2, hour2, day3, hour3)
                            VALUES (%s,%s, %s, %s,%s,%s,%s)''',(group_message[1],group_message[2],group_message[3], group_message[4],group_message[5], group_message[6],group_message[7]))
        
        conn.commit()
        await call.message.delete()
        await call.message.answer(replyVyacheslav("yesg", call.from_user.id,group_message[1]))

    elif call.data == "nog":
        await call.message.delete()
        await call.message.answer(replyVyacheslav("nog", call.from_user.id))

def responses(command, id):
    cur.execute('''SELECT lang FROM Users WHERE id = %s''',(id,))
    lang = cur.fetchone()[0]

    if str(command) == "help_command":
        if lang == "eng":
            return "This is the list of all commands: \n/start - Start the bot \n/about - Get to know the teacher better \n/lang - Select your language \n/contact - Contact the teacher \n/info - Understand what lesson fits you the best\n/book - Book a class \n/cancel Cancel a class \n/help - Get the list of all commands \n------------------------------------------------------------- \nIf this is not something you're looking for, please contact the teacher directly: \n/contact"
        elif lang == "ukr":
            return "Це список усіх команд: \n/start - Запустити бота \n/about - Дізнатися більше про вчителя \n/lang - Вибери свою мову \n/contact - Зв'яжись з вчителем \n/info - Зрозумій, який урок тобі найбільше підходить\n/book - Забронювати урок \n/cancel - Скасувати урок \n/help - Отримай список усіх команд \n------------------------------------------------------------- \nЯкщо це не те, що ти шукаєш, звернись безпосередньо до вчителя: \n/contact"
        elif lang == "ru":
            return "Это список всех команд: \n/start - Запустить бота \n/about - Узнать больше про учителя \n/lang - Выбрать язык \n/contact - Связаться с учителем \n/info - Пойми, какой урок подходит тебе лучше всего\n/book - Забронировать урок \n/cancel - Отменить урок \n/help - Получить список всех команд \n-------------------------------------------------------------- \nЕсли это не то, что ты ищешь, свяжись напрямую с учителем: \n/contact"
        else:
            return "This is the list of all commands: \n/start - Start the bot \n/about - Get to know the teacher better \n/lang - Select your language \n/contact - Contact the teacher \n/info - Understand what lesson fits you the best\n/book - Book a class \n/cancel Cancel a class \n/help - Get the list of all commands \n------------------------------------------------------------- \nIf this is not something you're looking for, please contact the teacher directly: \n/contact"

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

    elif str(command) == "no_group_classes":
        if lang == "eng":
            return "There is currently no group classes available :( Try a different type of lesson \n/book"
        elif lang == "ukr":
            return "Наразі немає доступних групових занять :( Спробуй інший тип уроку \n/book"
        elif lang == "ru":
            return "В настоящее время нет доступных групповых занятий :( Попробуй другой тип урока \n/book"
        else:
            return "There is currently no group classes available :( Try a different type of lesson \n/book"

    elif str(command) == "mini-group_classes":
        if lang == "eng":
            return "If you want to attend a mini-group class, please contact the teacher directly via Telegram, phone call, or Instagram \n/contact"
        elif lang == "ukr":
            return "Якщо ти хочеш відвідати заняття в міні-групі, зв’яжись з вчителем безпосередньо через Telegram, телефонний дзвінок або Instagram \n/contact"
        elif lang == "ru":
            return "Если ты хочешь посетить занятие в мини-группе, свяжись с учителем напрямую в Telegram, по телефону или в Instagram \n/contact"
        else:
            return "If you want to attend a mini-group class, please contact the teacher directly via Telegram, phone call, or Instagram \n/contact"

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
            return '''🙋‍♂️Individual lesson is a perfect option for a person who wants to prepare for passing exams like: TOEFL, IELTS, ЗНО or ДПА \n \nDuration: 55 minutes \nSchedule is created based on clients preference \n/book'''
        elif lang == "ukr":
            return '''🙋‍♂️Індивідуальне заняття - ідеальний варіант для людини, яка хоче підготуватися до здачі іспитів, таких як: TOEFL, IELTS, ЗНО або ДПА \n \nТривалість: 55 хвилин \nРозклад створюється на основі уподобань клієнта \n/book'''
        elif lang == "ru":
            return '''🙋‍♂️Индивидуальное занятие - идеальный вариант для человека, который хочет подготовиться к сдаче таких экзаменов, как: TOEFL, IELTS, ЗНО или ДПА \n \nПродолжительность: 55 минут \nРасписание составляется исходя из предпочтений клиента \n/book'''
        else:
            return '''🙋‍♂️Individual lesson is a perfect option for a person who wants to prepare for passing exams like: TOEFL, IELTS, ЗНО or ДПА \n \nDuration: 55 minutes \nSchedule is created based on clients preference \n/book'''

    elif str(command) == "groupinfo":
        if lang == "eng":
            return '''👨‍👩‍👧‍👦Group lessons is a perfect option for a person who wants to ,(along with other people), improve: \n\n✅grammar \n📖reading \n👂listening skills. \nEveryone in the group is of a similar age and level. \n \nDuration: 55 or 115 minutes \n5-8 people in the group \n/book'''
        elif lang == "ukr":
            return '''👨‍👩‍👧‍👦Групові заняття – ідеальний варіант для людини, яка хоче разом з іншими людьми покращити \n\n✅граматику \n📖навички читання \n👂аудіювання. \nУсі в групі однакового віку та рівня. \n \nТривалість: 55 або 115 хвилин \n5-8 осіб у групі \n/book'''
        elif lang == "ru":
            return '''👨‍👩‍👧‍👦Групповые занятия — идеальный вариант для человека, который хочет, вместе с другими людьми, улучшить \n\n✅грамматику \n📖навыки чтения \n👂аудирования. \nВсе в группе одного возраста и уровня. \n \nПродолжительность: 55 или 115 минут \n5-8 человек в группе \n/book'''
        else:
            return '''👨‍👩‍👧‍👦Group lessons is a perfect option for a person who wants to,(along with other people), improve: \n\n✅grammar \n📖reading \n👂listening skills. \nEveryone in the group is of a similar age and level. \n \nDuration: 55 or 115 minutes \n5-8 people in the group \n/book'''

    elif str(command) == "mini-groupinfo":
        if lang == "eng":
            return '''👬Mini-group lesson is a perfect option for a person who wants to, (along with a small group of people), improve: \n\n🗣speaking \n✅grammar \n📖reading \n👂listening skills. \nAll students are of a similar age and level. \n \nDuration: 55 or 115 minutes \n2-4 people in the group \n/book'''
        elif lang == "ukr":
            return '''👬Заняття в міні-групі – ідеальний варіант для людини, яка хоче разом з невеликою групою людей покращити \n\n🗣навички говоріння \n✅граматики \n📖читання \n👂аудіювання. \nУсі учні однакового віку та рівня. \n \nТривалість: 55 або 115 хвилин \n2-4 людини в групі \n/book'''
        elif lang == "ru":
            return '''👬Занятие в мини-группе — идеальный вариант для человека, который хочет, вместе с небольшой группой, улучшить: \n\n🗣навыки говорения \n✅грамматики \n📖чтения \n👂аудирования. \nВсе ученики одного возраста и уровня. \n \nПродолжительность: 55 или 115 минут \n2-4 человека в группе \n/book'''
        else:
            return '''👬Mini-group lesson is a perfect option for a person who wants to, (along with a small group of people), improve \n\n🗣speaking \n✅grammar \n📖reading \n👂listening skills. \nAll students are of a similar age and level. \n \nDuration: 55 or 115 minutes \n2-4 people in the group \n/book'''
    
    elif str(command) == "speakinginfo":
        if lang == "eng":
            return '''🗣Speaking club is a perfect type of lesson where you can improve your speaking skills. \n\nFor now the speaking classes are completely free \n/book'''
        elif lang == "ukr":
            return '''🗣Speaking club – ідеальний тип уроку, де ви можете покращити свої мовленнєві навички. \n\nНаразі Speaking уроки абсолютно безкоштовні \n/book'''
        elif lang == "ru":
            return '''🗣Разговорный клуб — это идеальный вариант урока, на котором вы можете улучшить свои разговорные навыки. \n\nНа данный момент Speaking уроки совершенно бесплатны \n/book'''
        else:
            return '''🗣Speaking club is a perfect type of lesson where you can improve your speaking skills. \n\nFor now the speaking classes are completely free \n/book'''

    elif str(command) == "about_command":
        if lang == "eng":
            return '''My name is Viacheslav aka Your English Bro 😎 

I’ve been teaching for more than 3 years now. 
I am a Business English teacher 👨‍🏫 in Ukrainian-American Concordia university. 
I’ve completed language courses in \n\nReading, UK 🇬🇧 \nExeter, UK 🇬🇧 \nToronto, Canada 🇨🇦

I have BBA and MBA, so I know something about business as well as economics 💵 
I have worked as a farmer, a manager, a translator, a trainer, had my own company, but my real passion has always been teaching.

My big goal is to teach as many people as I can to make Ukraine an English speaking country'''
        elif lang == "ukr":
            return '''Мене звати В’ячеслав, так само відомий як Your English Bro 😎

Викладаю більше 3 років.
Я викладач ділової англійської 👨‍🏫 в українсько-американському університеті Конкордія.
Я закінчив мовні курси в: \n\nРедінгу, Великобританія 🇬🇧 \nЕксетер, Великобританія 🇬🇧 \nТоронто, Канада 🇨🇦

У мене є BBA та MBA, тому я знаю дещо як про бізнес, так і про економіку 💵
Я працював фермером, менеджером, перекладачем, тренером, мав власну компанію, але моєю справжньою пристрастю завжди було навчання.

Моя велика мета – навчити якомога більше людей, щоб Україна була англомовною країною'''
        elif lang == "ru":
            return '''Меня зовут Вячеслав, так же известный как Your English Bro 😎

Преподаю более 3-х лет.
Я преподаватель делового английского 👨‍🏫 в украинско-американском университете Конкордия.
Я прошел языковые курсы в: \n\nРединге, Великобритания 🇬🇧 \nЭксетере, Великобритания 🇬🇧 \nТоронто, Канада 🇨🇦

У меня есть BBA и MBA, так что я знаю кое-что о бизнесе, а также экономике 💵
Я работал фермером, менеджером, переводчиком, тренером, имел собственную компанию, но моей настоящей страстью всегда было преподавание.

Моя большая цель — научить как можно больше людей, что бы Украина была англоязычной страной.'''
        else:
            return '''My name is Viacheslav aka Your English Bro 😎 

I’ve been teaching for more than 3 years now. 
I am a Business English teacher 👨‍🏫 in Ukrainian-American Concordia university. 
I’ve completed language courses in: \n\nReading, UK 🇬🇧 \nExeter, UK 🇬🇧 \nToronto, Canada 🇨🇦

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
    cur.execute('''SELECT lang FROM Users WHERE id = %s''', (id,))
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
    cur.execute('''SELECT lang FROM Users WHERE id = %s''', (id,))
    lang = cur.fetchone()[0]

    if lang == "eng":
        return optionseng
    elif lang == "ukr":
        return optionsukr
    elif lang == "ru":
        return optionsru
    else:
        return optionseng

def replyVyacheslav(*args):
    cur.execute('''SELECT lang FROM Users WHERE id = %s''', (args[1],))
    lang = cur.fetchone()[0]

    if args[0] == "vyacheslav_add":
        cur.execute('''SELECT day, time FROM Schedule WHERE firstName = %s and lastName = %s''',(str(args[2][1]).lower(),str(args[2][2]).lower()))
        global day
        day, hour = cur.fetchall()[-1]
        if lang == "eng":
            return f"{str(args[2][1]).capitalize()} {str(args[2][2]).capitalize()} is successfully added on {str(day).capitalize()} {args[2][4]}"
        elif lang == "ukr":
            if day == "monday":
                day = "Понеділок"
            elif day == "tuesday":
                day = "Вівторок"
            elif day == "wednesday":
                day = "Середу"
            elif day == "thursday":
                day = "Четвер"
            elif day == "friday":
                day = "П'ятницю"
            elif day == "saturday":
                day = "Суботу"
            elif day == "sunday":
                day = "Неділю"
            return f"{str(args[2][1]).capitalize()} {str(args[2][2]).capitalize()} успішно доданий на {day} {args[2][4]}"
    
        elif lang == "ru":
            if day == "monday":
                day = "Понедельник"
            elif day == "tuesday":
                day = "Вторник"
            elif day == "wednesday":
                day = "Среду"
            elif day == "thursday":
                day = "Четверг"
            elif day == "friday":
                day = "Пятницу"
            elif day == "saturday":
                day = "Субботу"
            elif day == "sunday":
                day = "Воскресенье"
            return f"{str(args[2][1]).capitalize()} {str(args[2][2]).capitalize()} удачно добавленый на {str(day).capitalize()} {args[2][4]}"
        else:
            return f"{str(args[2][1]).capitalize()} {str(args[2][2]).capitalize()} is successfully added on {str(args[2][3]).capitalize()} {args[2][4]}"

    elif args[0] == "vyacheslav_sure":
        message = str(args[2]).split()
        firstName = str(message[1]).capitalize()
        lastName = str(message[2]).capitalize()
        dday = str(message[3]).lower()
        hour = message[4]

        if lang == "eng":
            theday = translate("eng", dday)
            return f"Is everything correct? \n{firstName} {lastName} {theday} {hour}"
        elif lang == "ukr":
            theday = translate("ukr", dday)
            return f"Все правильно? \n{firstName} {lastName} {theday} {hour}"
        elif lang == "ru":
            theday = translate("ru", dday)
            return f"Всё правильно? \n{firstName} {lastName} {theday} {hour}"
        else: 
            theday = translate("eng", dday)
            return f"Is everything correct? \n{firstName} {lastName} {theday} {hour}"

    elif args[0] == "group_sure":
        group_type = args[2][1]
        if group_type == "el":
            if lang == "eng":
                group_type = "Elementary"
            elif lang == "ukr":
                group_type = "Початковий"
            elif lang == "ru":
                group_type = "Начальный"
            else:
                group_type = "Elementary"

        elif group_type == "int":
            if lang == "eng":
                group_type = "Intermediate"
            elif lang == "ukr":
                group_type = "Середній"
            elif lang == "ru":
                group_type = "Средний"
            else:
                group_type = "Intermediate"
        
        if len(args[2]) == 6:
            day1 = translate(lang, args[2][2])
            hour1 = translate(lang, args[2][3])

            day2 = translate(lang, args[2][4])
            hour2 = translate(lang, args[2][5])

        elif len(args[2]) == 8:
            day1 = translate(lang, args[2][2])
            hour1 = translate(lang, args[2][3])

            day2 = translate(lang, args[2][4])
            hour2 = translate(lang, args[2][5])

            day3 = translate(lang, args[2][6])
            hour3 = translate(lang, args[2][7])
        
        if lang == "eng":
            if len(args[2]) == 6:
                return f"Is everything correct? \nLevel: {group_type} \n1st class {day1} {hour1} \n2nd class {day2} {hour2} \n"
            elif len(args[2]) == 8:
                return f"Is everything correct? \nLevel: {group_type} \n1st class {day1} {hour1} \n2nd class {day2} {hour2} \n3rd class {day3} {hour3} \n"
        elif lang == "ukr":
            if len(args[2]) == 6:
                return f"Все правильно? \nРівень: {group_type} \n1й урок {day1} {hour1} \n2й урок {day2} {hour2} \n"
            elif len(args[2]) == 8:
                return f"Все правильно? \nРівень: {group_type} \n1й урок {day1} {hour1} \n2й урок {day2} {hour2} \n3й урок {day3} {hour3} \n"
        elif lang == "ru":
            if len(args[2]) == 6:
                return f"Всё правильно? \nУровень: {group_type} \n1й урок {day1} {hour1} \n2й урок {day2} {hour2} \n"
            elif len(args[2]) == 8:
                return f"Всё правильно? \nУровень: {group_type} \n1й урок {day1} {hour1} \n2й урок {day2} {hour2} \n3й урок {day3} {hour3} \n"
        else:
            if len(args[2]) == 6:
                return f"Is everything correct? \nLevel: {group_type} \n1st class {day1} {hour1} \n2nd class {day2} {hour2} \n"
            elif len(args[2]) == 8:
                return f"Is everything correct? \nLevel: {group_type} \n1st class {day1} {hour1} \n2nd class {day2} {hour2} \n3rd class {day3} {hour3} \n"

    # REPLYING WHEN NOT SURE (WHEN ADDING A CLASS)
    elif args[0] == "nob":
        if lang == "eng":
            return "Okay, this class was not added... If you want to change something and add a class again, please type the same command, and make sure everything is correct😁"
        elif lang == "ukr":
            return "Гаразд, цей урок не додано... Якщо ви хочете щось змінити та знову додати урок, введіть ту саму команду та переконайтеся, що все правильно😁"
        elif lang == "ru":
            return "Хорошо, этот урок не был добавлен... Если вы хотите что-то изменить и снова добавить урок, введите ту же команду, и убедитесь, что все правильно😁"
        else:
            return "Okay, this class was not added... If you want to change something and add a class again, please type the same command, and make sure everything is correct😁"

    elif args[0] == "show_count":
        if lang == "eng":
            return f"Total number of classes: {args[2]}"
        elif lang == "ukr":
            return f"Всього уроків: {args[2]}"
        elif lang == "ru":
            return f"Всего уроков: {args[2]}"
        else:
            return f"Total number of classes: {args[2]}"

    elif args[0] == "students_command":
        if lang == "eng":
            return "Select what day you want to view"
        elif lang == "ukr":
            return "Виберіть день, який ви хочете переглянути"
        elif lang == "ru":
            return "Выберите, какой день вы хотите просмотреть"
        else:
            return "Select what day you want to view"

    elif args[0] == "doesn't_exist":
        if lang == "eng":
            return "Hmm... It seems to me that this class does NOT exist. Check your spelling and try again"
        elif lang == "ukr":
            return "Хм... Мені здається, що цього класу НЕ існує. Перевірте правопис і спробуйте ще раз"
        elif lang == "ru":
            return "Хм... Мне кажется, что этого класса НЕ существует. Проверьте правильность написания и повторите попытку"
        else:
            return "Hmm... It seems to me that this class does NOT exist. Check your spelling and try again"

    elif args[0] == "cancel_success":
        if lang == "eng":
            return f"{args[2][0]} {args[2][1]} on {args[2][2]} {args[2][3]} has been successfully removed"
        elif lang == "ukr":
            return f"{args[2][0]} {args[2][1]} {args[2][2]} {args[2][3]}... Успішно скасовано"
        elif lang == "ru":
            return f"{args[2][0]} {args[2][1]} {args[2][2]} {args[2][3]}... Удачно отменено"
        else:
            return f"{args[2][0]} {args[2][1]} on {args[2][2]} {args[2][3]} has been successfully removed"
    
    elif args[0] == "nod":
        if lang == "eng":
            return "Okay, this class was not removed... If you do want to cancel a class, please do the process again"
        elif lang == "ukr":
            return "Гаразд, цей урок не було видалено... Якщо ви все ж таки хочете скасувати урок, виконайте процес ще раз"
        elif lang == "ru":
            return "Хорошо, этот урок не был удален... Если вы все таки хотите отменить урок, повторите процес ещё раз"
        else:
            return "Okay, this class was not removed... If you do want to cancel a class, please do the process again"

    elif args[0] == "yesg":
        if lang == "eng":
            if args[2] == "int":
                group_type = "Intermediate"
            elif args[2] == "el":
                group_type = "Elementary"
            return f"Great! The {group_type} group was added successfully!"
        elif lang == "ukr":
            if args[2] == "int":
                group_type = "Середня"
            elif args[2] == "el":
                group_type = "Початкова"
            return f"Чудово! {group_type} група додана успішно!"
        elif lang == "ru":
            if args[2] == "int":
                group_type = "Средняя"
            elif args[2] == "el":
                group_type = "Начальная"
            return f"Отлично! {group_type} группа добавлена удачно!"          

    elif args[0] == "nog":
        if lang == "eng":
            return "Okay, this group was not added... If you do want to add a group, please repeat the process again"
        elif lang == "ukr":
            return "Гаразд, ця група не була додана... Якщо ви все ж таки хочете додати групу, виконайте процес ще раз"
        elif lang == "ru":
            return "Хорошо, эта группа не была добавлена... Если вы все таки хотите добавать группу, повторите процес ещё раз"
        else:
            return "Okay, this group was not added... If you do want to add a group, please repeat the process again"
    
    # THIS CLASS ALREADY EXISTS MESSAGE
    elif args[0] == "daytaken":
        if lang == "eng":
            return f"It seems to me that {str(args[2]).capitalize()} {str(args[3]).capitalize()} has a class at this time...Try to add a different time"
        elif lang == "ukr":
            return f"Мені здається, що {str(args[2]).capitalize()} {str(args[3]).capitalize()} має урок у цей час... Спробуйте додати інший час"
        elif lang == "ru":
            return f"Мне кажется, что {str(args[2]).capitalize()} {str(args[3]).capitalize()} имеет урок в это время... Попробуйте добавить другое время"
        else:
            return f"It seems to me that {str(args[2]).capitalize()} {str(args[3])} has a class at this time...Try to add a different time"

def VyacheslavStudents(id,option):
    students = []
    cur.execute("SELECT lang FROM Users WHERE id = %s",(id,))
    lang = cur.fetchone()[0]
    
    if option == "all":
        cur.execute("SELECT * FROM Schedule")
        classes = cur.fetchall()
    elif option == "mon":
        cur.execute("SELECT * FROM Schedule WHERE day = 'monday'")
        classes = cur.fetchall()
    elif option == "tue":
        cur.execute("SELECT * FROM Schedule WHERE day = 'tuesday'")
        classes = cur.fetchall()
    elif option == "wed":
        cur.execute("SELECT * FROM Schedule WHERE day = 'wednesday'")
        classes = cur.fetchall()
    elif option == "thu":
        cur.execute("SELECT * FROM Schedule WHERE day = 'thursday'")
        classes = cur.fetchall()
    elif option == "fri":
        cur.execute("SELECT * FROM Schedule WHERE day = 'friday'")
        classes = cur.fetchall()
    elif option == "sat":
        cur.execute("SELECT * FROM Schedule WHERE day = 'saturday'")
        classes = cur.fetchall()
    elif option == "sun":
        cur.execute("SELECT * FROM Schedule WHERE day = 'sunday'")
        classes = cur.fetchall()  

    for i in classes:
        if lang == "eng":
            day = str(i[3]).capitalize()
        elif lang == "ukr":
            day = translate("ukr", i[3])
        elif lang == "ru":
            day = translate("ru", i[3])
        else:
            day = str(i[3]).capitalize()

        students.append(f"{str(i[1]).capitalize()} {str(i[2]).capitalize()} {day} {i[4]}")
    return students

def yesnoKeyboard(id, cbdatayes, cbdatano):
    cur.execute("SELECT lang FROM Users WHERE id = %s", (id,))
    lang = cur.fetchone()[0]

    if lang == "eng":
        yesb = InlineKeyboardButton(text="Yes", callback_data=cbdatayes)
        nob = InlineKeyboardButton(text="No", callback_data=cbdatano)
    elif lang == "ukr":
        yesb = InlineKeyboardButton(text="Так", callback_data=cbdatayes)
        nob = InlineKeyboardButton(text="Ні", callback_data=cbdatano)
    elif lang == "ru":
        yesb = InlineKeyboardButton(text="Да", callback_data=cbdatayes)
        nob = InlineKeyboardButton(text="Нет", callback_data=cbdatano)
    
    return InlineKeyboardMarkup().add(yesb).add(nob)

def translate(lang, day):
    if lang == "ukr":
        if str(day) == "monday":
            day = "Понеділок"
        elif str(day) == "tuesday":
            day = "Вівторок"
        elif str(day) == "wednesday":
            day = "Середа"
        elif str(day) == "thursday":
            day = "Четвер"
        elif str(day) == "friday":
            day = "П'ятниця"
        elif str(day) == "saturday":
            day = "Субота"
        elif str(day) == "sunday":
            day = "Неділя"
        elif str(day) == "понедельник":
            day = "Понеділок"
        elif str(day) == "вторник":
            day = "Вівторок"
        elif str(day) == "среда":
            day = "Середа"
        elif str(day) == "четверг":
            day = "Четвер"
        elif str(day) == "пятница":
            day = "П'ятниця"
        elif str(day) == "суббота":
            day = "Субота"
        elif str(day) == "воскресенье":
            day = "Неділя"

    elif lang == "ru":
        if str(day) == "monday":
            day = "Понедельник"
        elif str(day) == "tuesday":
            day = "Вторник"
        elif str(day) == "wednesday":
            day = "Среда"
        elif str(day) == "thursday":
            day = "Четверг"
        elif str(day) == "friday":
            day = "Пятница"
        elif str(day) == "saturday":
            day = "Суббота"
        elif str(day) == "sunday":
            day = "Воскресенье"
        elif str(day) == "понеділок":
            day = "Понедельник"
        elif str(day) == "вівторок":
            day = "Вторник"
        elif str(day) == "середа":
            day = "Среда"
        elif str(day) == "четвер":
            day = "Четверг"
        elif str(day) == "п'ятниця":
            day = "Пятница"
        elif str(day) == "субота":
            day = "Суббота"
        elif str(day) == "неділя":
            day = "Воскресенье"
    
    elif lang == "eng":
        if str(day) == "понедельник":
            day = "Monday"
        elif str(day) == "вторник":
            day = "Tuesday"
        elif str(day) == "среда":
            day = "Wednesday"
        elif str(day) == "четверг":
            day = "Thursday"
        elif str(day) == "пятница":
            day = "Friday"
        elif str(day) == "cуббота":
            day = "Saturday"
        elif str(day) == "Воскресенье":
            day = "Sunday"
        elif str(day) == "понеділок":
            day = "Monday"
        elif str(day) == "вівторок":
            day = "Tuesday"
        elif str(day) == "середа":
            day = "Wednesday"
        elif str(day) == "четвер":
            day = "Thursday"
        elif str(day) == "п'ятниця":
            day = "Friday"
        elif str(day) == "субота":
            day = "Saturday"
        elif str(day) == "неділя":
            day = "Sunday"

    return day.capitalize()


def studentsKeyboard(id):
    all = InlineKeyboardButton(text=str(textOptions(id, "all")), callback_data="all")
    monday = InlineKeyboardButton(text=str(textOptions(id, "mon")), callback_data="mon")
    tuesday = InlineKeyboardButton(text=str(textOptions(id, "tue")), callback_data="tue")
    wednesday = InlineKeyboardButton(text=str(textOptions(id, "wed")), callback_data="wed")
    thursday = InlineKeyboardButton(text=str(textOptions(id, "thu")), callback_data="thu")
    friday = InlineKeyboardButton(text=str(textOptions(id, "fri")), callback_data="fri")
    saturday = InlineKeyboardButton(text=str(textOptions(id, "sat")), callback_data="sat")
    sunday = InlineKeyboardButton(text=str(textOptions(id, "sun")), callback_data="sun")
    gb = InlineKeyboardButton(text=str(textOptions(id, "gb")), callback_data="gb")

    daysKeyboard = InlineKeyboardMarkup().add(all).add(monday, tuesday).add(wednesday, thursday).add(friday, saturday).add(sunday).add(gb)
    return daysKeyboard

def textOptions(id,day):
    cur.execute('''SELECT lang FROM Users WHERE id = %s''', (id,))
    lang = cur.fetchone()[0]

    if lang == "eng":
        if day == "all":
            return "All"
        elif day == "mon":
            return "Monday"
        elif day == "tue":
            return "Tuesday"
        elif day == "wed":
            return "Wednesday"
        elif day == "thu":
            return "Thursday"
        elif day == "fri":
            return "Friday"
        elif day == "sat":
            return "Saturday"
        elif day == "sun":
            return "Sunday"
        elif day == "gb":
            return "⬅️Go back"
    
    elif lang == "ukr":
        if day == "all":
            return "Всі"
        elif day == "mon":
            return "Понеділок"
        elif day == "tue":
            return "Вівторок"
        elif day == "wed":
            return "Середа"
        elif day == "thu":
            return "Четвер"
        elif day == "fri":
            return "П'ятниця"
        elif day == "sat":
            return "Субота"
        elif day == "sun":
            return "Неділя"
        elif day == "gb":
            return "⬅️Повернутися"
        
    elif lang == "ru":
        if day == "all":
            return "Все"
        elif day == "mon":
            return "Понедельник"
        elif day == "tue":
            return "Вторник"
        elif day == "wed":
            return "Среда"
        elif day == "thu":
            return "Четверг"
        elif day == "fri":
            return "Пятница"
        elif day == "sat":
            return "Суббота"
        elif day == "sun":
            return "Воскресенье"
        elif day == "gb":
            return "⬅️Вернуться"

    else:
        if day == "all":
            return "All"
        elif day == "mon":
            return "Monday"
        elif day == "tue":
            return "Tuesday"
        elif day == "wed":
            return "Wednesday"
        elif day == "thu":
            return "Thursday"
        elif day == "fri":
            return "Friday"
        elif day == "sat":
            return "Saturday"
        elif day == "sun":
            return "Sunday"
        elif day == "gb":
            return "⬅️Go back"


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)