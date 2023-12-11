from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.startMenu import menu,majburiy_obuna
from loader import bot
from states.states import Form
from aiogram.fsm.context import FSMContext

work_router: Router = Router()


@work_router.message(F.text == "Ish joyi kerak")
async def menu(message: Message, state: FSMContext):
    await message.answer("""Ish joyi topish uchun ariza berish\n

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""",)
    await state.set_state(Form.ism_familiya)
    await message.answer("Ism, familiyangizni kiriting?",)


@work_router.message(Form.ism_familiya)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(ism_familiya=message.text)
    await state.set_state(Form.yosh)
    await message.answer("""🕑 Yosh: \n

Yoshingizni kiriting?
Masalan, 19

""")

@work_router.message(Form.yosh)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(yosh=message.text)
    await state.set_state(Form.texnolog)
    await message.answer("""📚 Texnologiya:\n

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan:\n

Java, C++, C#

""")
    


@work_router.message(Form.texnolog)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(texnolog=message.text)
    await state.set_state(Form.aloqa)
    await message.answer("""📞 Aloqa:\n

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
""")




@work_router.message(Form.aloqa)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await state.set_state(Form.hudud)
    await message.answer("""🌐 Hudud:\n 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
""")


@work_router.message(Form.hudud)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await state.set_state(Form.Narx)
    await message.answer("""💰 Narxi:\n

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
""")

@work_router.message(Form.Narx)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Narx=message.text)
    await state.set_state(Form.Kasb)
    await message.answer("""👨🏻‍💻 Kasbi:\n

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
""")


@work_router.message(Form.Kasb)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Kasb=message.text)
    await state.set_state(Form.murojaat)
    await message.answer("""🕰 Murojaat qilish vaqti:\n 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
""")

@work_router.message(Form.murojaat)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(murojaat=message.text)
    await state.set_state(Form.Maqsad)
    await message.answer("""🔎 Maqsad:\n

    Maqsadingizni qisqacha yozib bering.
    """)
    
@work_router.message(Form.Maqsad)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(Maqsad=message.text)
    
    
    
    
    
    user = await state.get_data()


    await message.answer(f"Ish joyi kerak:\n 👨‍💼 Xodim: {user['ism_familiya']}\n 🕑 Yoshi:{user['yosh']}\n 📚 Texnologiya: {user['texnolog']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Aloqa: {user['aloqa']}\n 🌐 Hudud: {user['hudud']}\n 💰 Narxi: {user['Narx']}\n 👨🏻‍💻 Kasbi: {user['Kasb']}\n 🕰 Murojaat qilish vaqti:{user['murojaat']}\n 🔎 Maqsad:{user['Maqsad']}\n #xodim")

