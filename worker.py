from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.startMenu import menu,majburiy_obuna
from loader import bot
from states.states import Form
from aiogram.fsm.context import FSMContext

worker_router: Router = Router()


@worker_router.message(F.text == "Xodim kerak")
async def menu(message: Message, state: FSMContext):
    await message.answer("""Xodim topish uchun ariza berish\n

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""",)
    await state.set_state(Form.idora)
    await message.answer("🎓 Idora nomi?",)


@worker_router.message(Form.idora)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(idora=message.text)
    await state.set_state(Form.texnolog)
    await message.answer("""📚 Texnologiya:\n

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan:\n

Java, C++, C#

""")


    


@worker_router.message(Form.texnolog)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(texnolog=message.text)
    await state.set_state(Form.aloqa)
    await message.answer("""📞 Aloqa:\n

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
""")




@worker_router.message(Form.aloqa)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await state.set_state(Form.hudud)
    await message.answer("""🌐 Hudud:\n 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
""")


@worker_router.message(Form.hudud)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await state.set_state(Form.owner)
    await message.answer("""✍️Mas'ul ism sharifi?
""")

@worker_router.message(Form.owner)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(owner=message.text)
    await state.set_state(Form.murojaat)
    await message.answer("""🕰 Murojaat qilish vaqti:\n 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
""")


@worker_router.message(Form.murojaat)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(murojaat=message.text)
    await state.set_state(Form.time)
    await message.answer("""🕰 Ish vaqtini ktime
""")

@worker_router.message(Form.time)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.set_state(Form.cost)
    await message.answer("""💰 Maoshni kiriting?
    """)


@worker_router.message(Form.cost)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(cost=message.text)
    await state.set_state(Form.addmean)
    await message.answer("""‼️ Qo`shimcha ma`lumotlar?
    """)
    
@worker_router.message(Form.addmean)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(addmean=message.text)
    
    
    
    
    
    user = await state.get_data()


    await message.answer(f"Xodim kerak:\n 🏢 Idora: {user['idora']}\n 📚 Texnologiya: {user['texnolog']}\n  🇺🇿 Telegram: @{message.from_user.username}\n  📞 Aloqa: {user['aloqa']}\n 🌐 Hudud: {user['hudud']}\n ✍️ Mas'ul: {user['owner']}\n 🕰 Murojaat vaqti: {user['murojaat']}\n 🕰 Ish vaqti: {user['time']}\n 💰 Maosh: {user['cost']}\n ‼️ Qo`shimcha: {user['addmean']}\n #ishJoyi " )

