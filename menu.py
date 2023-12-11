from aiogram import Router,F
from aiogram.types import Message,CallbackQuery,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.startMenu import menu,majburiy_obuna
from loader import bot
from states.states import Form
from aiogram.fsm.context import FSMContext

menu_router: Router = Router()


@menu_router.message(F.text == "Sherik kerak")
async def menu(message: Message, state: FSMContext):
    await message.answer("""Sherik topish uchun ariza berish\n
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""",)
    await state.set_state(Form.ism_familiya)
    await message.answer("Ism, familiyangizni kiriting?",)


@menu_router.message(Form.ism_familiya)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(ism_familiya=message.text)
    await state.set_state(Form.texnolog)
    await message.answer("""📚 Texnologiya:\n

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan:\n

Java, C++, C#

""")
    


@menu_router.message(Form.texnolog)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(texnolog=message.text)
    await state.set_state(Form.aloqa)
    await message.answer("""📞 Aloqa:\n

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
""")




@menu_router.message(Form.aloqa)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await state.set_state(Form.hudud)
    await message.answer("""🌐 Hudud:\n 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
""")


@menu_router.message(Form.hudud)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await state.set_state(Form.Narx)
    await message.answer("""💰 Narxi:\n

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
""")

@menu_router.message(Form.Narx)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Narx=message.text)
    await state.set_state(Form.Kasb)
    await message.answer("""👨🏻‍💻 Kasbi:\n

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
""")


@menu_router.message(Form.Kasb)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Kasb=message.text)
    await state.set_state(Form.murojaat)
    await message.answer("""🕰 Murojaat qilish vaqti:\n 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
""")

@menu_router.message(Form.murojaat)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(murojaat=message.text)
    await state.set_state(Form.Maqsad)
    await message.answer("""🔎 Maqsad:\n

    Maqsadingizni qisqacha yozib bering.
    """)
    
@menu_router.message(Form.Maqsad)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Maqsad=message.text)
    
    
    
    
    
    user = await state.get_data()


    await message.answer(f"Sherik kerak:\n 🏅 Sherik: {user['ism_familiya']}\n 📚 Texnologiya: {user['texnolog']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Aloqa: {user['aloqa']}\n 🌐 Hudud: {user['hudud']}\n 💰 Narxi: {user['Narx']}\n 👨🏻‍💻 Kasbi: {user['Kasb']}\n 🕰 Murojaat qilish vaqti:{user['murojaat']}\n 🔎 Maqsad:{user['Maqsad']}\n #sherik")



    await message.answer(f"Qabul qilinsinmi?")

    menu = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Ha'),
                KeyboardButton(text="Yo'q")
            ],    
    ]
)



    @menu_router.message(F.text == "Ha")
    async def menu(message: Message):
        await message.answer("Qabul qilindi",reply_markup=menu)


    @menu_router.message(F.text == "Yo'q")
    async def menu(message: Message):
        await message.answer("Qabul qilinmadi",reply_markup=menu)









@menu_router.message(F.text == "Ish joyi kerak")
async def menu(message: Message, state: FSMContext):
    await message.answer("""Ish joyi topish uchun ariza berish\n

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""",)
    await state.set_state(Form.ism_familiya)
    await message.answer("Ism, familiyangizni kiriting?",)


@menu_router.message(Form.ism_familiya)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(ism_familiya=message.text)
    await state.set_state(Form.yosh)
    await message.answer("""🕑 Yosh: \n

Yoshingizni kiriting?
Masalan, 19

""")

@menu_router.message(Form.yosh)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(yosh=message.text)
    await state.set_state(Form.texnolog)
    await message.answer("""📚 Texnologiya:\n

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan:\n

Java, C++, C#

""")
    


@menu_router.message(Form.texnolog)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(texnolog=message.text)
    await state.set_state(Form.aloqa)
    await message.answer("""📞 Aloqa:\n

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
""")




@menu_router.message(Form.aloqa)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await state.set_state(Form.hudud)
    await message.answer("""🌐 Hudud:\n 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
""")


@menu_router.message(Form.hudud)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await state.set_state(Form.Narx)
    await message.answer("""💰 Narxi:\n

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
""")

@menu_router.message(Form.Narx)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Narx=message.text)
    await state.set_state(Form.Kasb)
    await message.answer("""👨🏻‍💻 Kasbi:\n

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
""")


@menu_router.message(Form.Kasb)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Kasb=message.text)
    await state.set_state(Form.murojaat)
    await message.answer("""🕰 Murojaat qilish vaqti:\n 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
""")

@menu_router.message(Form.murojaat)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(murojaat=message.text)
    await state.set_state(Form.Maqsad)
    await message.answer("""🔎 Maqsad:\n

    Maqsadingizni qisqacha yozib bering.
    """)
    
@menu_router.message(Form.Maqsad)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Maqsad=message.text)
    
    
    
    
    
    any = await state.get_data()


    await message.answer(f"Ish joyi kerak:\n 👨‍💼 Xodim: {any['ism_familiya']}\n 🕑 Yoshi:{any['yosh']}\n 📚 Texnologiya: {any['texnolog']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Aloqa: {any['aloqa']}\n 🌐 Hudud: {any['hudud']}\n 💰 Narxi: {any['Narx']}\n 👨🏻‍💻 Kasbi: {any['Kasb']}\n 🕰 Murojaat qilish vaqti:{any['murojaat']}\n 🔎 Maqsad:{any['Maqsad']}\n #xodim")
    
    
    
    await message.answer(f"Qabul qilinsinmi?")

    menu = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Ha'),
                KeyboardButton(text="Yo'q")
            ],    
    ]
)



    @menu_router.message(F.text == "Ha")
    async def menu(message: Message):
        await message.answer("Qabul qilindi",reply_markup=menu)


    @menu_router.message(F.text == "Yo'q")
    async def menu(message: Message):
        await message.answer("Qabul qilinmadi",reply_markup=menu)





@menu_router.message(F.text == "Xodim kerak")
async def menu(message: Message, state: FSMContext):
    await message.answer("""Xodim topish uchun ariza berish\n

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""",)
    await state.set_state(Form.idora)
    await message.answer("🎓 Idora nomi?",)


@menu_router.message(Form.idora)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(idora=message.text)
    await state.set_state(Form.texnolog)
    await message.answer("""📚 Texnologiya:\n

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan:\n

Java, C++, C#

""")


    


@menu_router.message(Form.texnolog)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(texnolog=message.text)
    await state.set_state(Form.aloqa)
    await message.answer("""📞 Aloqa:\n

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
""")




@menu_router.message(Form.aloqa)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await state.set_state(Form.hudud)
    await message.answer("""🌐 Hudud:\n 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
""")


@menu_router.message(Form.hudud)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await state.set_state(Form.owner)
    await message.answer("""✍️Mas'ul ism sharifi?
""")

@menu_router.message(Form.owner)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(owner=message.text)
    await state.set_state(Form.murojaat)
    await message.answer("""🕰 Murojaat qilish vaqti:\n 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
""")


@menu_router.message(Form.murojaat)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(murojaat=message.text)
    await state.set_state(Form.time)
    await message.answer("""🕰 Ish vaqtini ktime
""")

@menu_router.message(Form.time)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.set_state(Form.cost)
    await message.answer("""💰 Maoshni kiriting?
    """)


@menu_router.message(Form.cost)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(cost=message.text)
    await state.set_state(Form.addmean)
    await message.answer("""‼️ Qo`shimcha ma`lumotlar?
    """)
    
@menu_router.message(Form.addmean)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(addmean=message.text)
    
    
    
    
    
    some = await state.get_data()


    await message.answer(f"Xodim kerak:\n 🏢 Idora: {some['idora']}\n 📚 Texnologiya: {some['texnolog']}\n  🇺🇿 Telegram: @{message.from_user.username}\n  📞 Aloqa: {some['aloqa']}\n 🌐 Hudud: {some['hudud']}\n ✍️ Mas'ul: {some['owner']}\n 🕰 Murojaat vaqti: {some['murojaat']}\n 🕰 Ish vaqti: {some['time']}\n 💰 Maosh: {some['cost']}\n ‼️ Qo`shimcha: {some['addmean']}\n #ishJoyimenu")



    await message.answer(f"Qabul qilinsinmi?")

    menu = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Ha'),
                KeyboardButton(text="Yo'q")
            ],    
    ]
)



    @menu_router.message(F.text == "Ha")
    async def menu(message: Message):
        await message.answer("Qabul qilindi",reply_markup=menu)


    @menu_router.message(F.text == "Yo'q")
    async def menu(message: Message):
        await message.answer("Qabul qilinmadi",reply_markup=menu)




@menu_router.message(F.text == "Ustoz kerak")
async def menu(message: Message, state: FSMContext):
    await message.answer("""Ustoz topish uchun ariza berish\n

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""",)
    await state.set_state(Form.ism_familiya)
    await message.answer("Ism, familiyangizni kiriting?",)


@menu_router.message(Form.ism_familiya)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(ism_familiya=message.text)
    await state.set_state(Form.yosh)
    await message.answer("""🕑 Yosh: \n

Yoshingizni kiriting?
Masalan, 19

""")

@menu_router.message(Form.yosh)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(yosh=message.text)
    await state.set_state(Form.texnolog)
    await message.answer("""📚 Texnologiya:\n

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan:\n

Java, C++, C#

""")
    


@menu_router.message(Form.texnolog)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(texnolog=message.text)
    await state.set_state(Form.aloqa)
    await message.answer("""📞 Aloqa:\n

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
""")




@menu_router.message(Form.aloqa)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await state.set_state(Form.hudud)
    await message.answer("""🌐 Hudud:\n 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
""")


@menu_router.message(Form.hudud)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await state.set_state(Form.Narx)
    await message.answer("""💰 Narxi:\n

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
""")

@menu_router.message(Form.Narx)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Narx=message.text)
    await state.set_state(Form.Kasb)
    await message.answer("""👨🏻‍💻 Kasbi:\n

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
""")


@menu_router.message(Form.Kasb)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Kasb=message.text)
    await state.set_state(Form.murojaat)
    await message.answer("""🕰 Murojaat qilish vaqti:\n 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
""")

@menu_router.message(Form.murojaat)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(murojaat=message.text)
    await state.set_state(Form.Maqsad)
    await message.answer("""🔎 Maqsad:\n

    Maqsadingizni qisqacha yozib bering.
    """)
    
@menu_router.message(Form.Maqsad)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Maqsad=message.text)
    
    
    
    
    
    thing = await state.get_data()


    await message.answer(f"Ustoz kerak:\n 🎓 Shogird: {thing['ism_familiya']}\n 🕑 Yoshi:{thing['yosh']}\n 📚 Texnologiya: {thing['texnolog']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Aloqa: {thing['aloqa']}\n 🌐 Hudud: {thing['hudud']}\n 💰 Narxi: {thing['Narx']}\n 👨🏻‍💻 Kasbi: {thing['Kasb']}\n 🕰 Murojaat qilish vaqti:{thing['murojaat']}\n 🔎 Maqsad:{thing['Maqsad']}\n #shemenu")


    await message.answer(f"Qabul qilinsinmi?")

    menu = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Ha'),
                KeyboardButton(text="Yo'q")
            ],    
    ]
)



    @menu_router.message(F.text == "Ha")
    async def menu(message: Message):
        await message.answer("Qabul qilindi",reply_markup=menu)


    @menu_router.message(F.text == "Yo'q")
    async def menu(message: Message):
        await message.answer("Qabul qilinmadi",reply_markup=menu)







@menu_router.message(F.text == "Shogird kerak")
async def menu(message: Message, state: FSMContext):
    await message.answer("""Shogird topish uchun ariza berish\n

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""",)
    await state.set_state(Form.ism_familiya)
    await message.answer("Ism, familiyangizni kiriting?",)


@menu_router.message(Form.ism_familiya)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(ism_familiya=message.text)
    await state.set_state(Form.yosh)
    await message.answer("""🕑 Yosh: \n

Yoshingizni kiriting?
Masalan, 19

""")

@menu_router.message(Form.yosh)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(yosh=message.text)
    await state.set_state(Form.texnolog)
    await message.answer("""📚 Texnologiya:\n

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan:\n

Java, C++, C#

""")
    


@menu_router.message(Form.texnolog)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(texnolog=message.text)
    await state.set_state(Form.aloqa)
    await message.answer("""📞 Aloqa:\n

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
""")




@menu_router.message(Form.aloqa)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await state.set_state(Form.hudud)
    await message.answer("""🌐 Hudud:\n 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
""")


@menu_router.message(Form.hudud)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await state.set_state(Form.Narx)
    await message.answer("""💰 Narxi:\n

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
""")

@menu_router.message(Form.Narx)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Narx=message.text)
    await state.set_state(Form.Kasb)
    await message.answer("""👨🏻‍💻 Kasbi:\n

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
""")


@menu_router.message(Form.Kasb)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Kasb=message.text)
    await state.set_state(Form.murojaat)
    await message.answer("""🕰 Murojaat qilish vaqti:\n 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
""")

@menu_router.message(Form.murojaat)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(murojaat=message.text)
    await state.set_state(Form.Maqsad)
    await message.answer("""🔎 Maqsad:\n

    Maqsadingizni qisqacha yozib bering.
    """)
    
@menu_router.message(Form.Maqsad)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Maqsad=message.text)
    
    
    
    
    
    mem = await state.get_data()


    await message.answer(f"Ustoz kerak:\n 🎓 Shogird: {mem['ism_familiya']}\n 🕑 Yoshi:{mem['yosh']}\n 📚 Texnologiya: {mem['texnolog']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Aloqa: {mem['aloqa']}\n 🌐 Hudud: {mem['hudud']}\n 💰 Narxi: {mem['Narx']}\n 👨🏻‍💻 Kasbi: {mem['Kasb']}\n 🕰 Murojaat qilish vaqti:{mem['murojaat']}\n 🔎 Maqsad:{mem['Maqsad']}\n #sherik")


    await message.answer(f"Qabul qilinsinmi?")

    menu = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Ha'),
                KeyboardButton(text="Yo'q")
            ],    
    ]
)



    @menu_router.message(F.text == "Ha")
    async def menu(message: Message):
        await message.answer("Qabul qilindi",reply_markup=menu)


    @menu_router.message(F.text == "Yo'q")
    async def menu(message: Message):
        await message.answer("Qabul qilinmadi",reply_markup=menu)