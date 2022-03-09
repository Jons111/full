from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentTypes
from aiogram.types import ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup

from keyboards.default.menu import asosiy
from keyboards.default.tasdiqlash import tasdiq
from states.holatlar import Forma
from loader import dp, bot, db
from keyboards.default.mahallalar import tugmalar
from keyboards.default.tel import tel



@dp.message_handler(text='Murojat qilish')
async def bot_start(message: types.Message):

    await message.answer(text='📌 Iltimos, endi Ismni  kiriting: (Masalan: Islomjon )',reply_markup=ReplyKeyboardRemove())
    await Forma.Ism_qabul_qilish.set()

lugat = {}
@dp.message_handler(state=Forma.Ism_qabul_qilish)
async def bot_echo(message: types.Message):

    ism = message.text
    if not  ism.isdigit():
        lugat['ism']=ism
        await message.answer(text="📌 Yaxshi, endi  Familyani  kiriting: (Masalan: Olimov)")
        await Forma.Fam_qabul_qilish.set()
    else:
        await message.answer(text='Ism faqat harflardan tashkil topadi ')
        await Forma.Ism_qabul_qilish.set()


@dp.message_handler(state=Forma.Fam_qabul_qilish)
async def bot_echo(message: types.Message):

    fam = message.text
    if not  fam.isdigit():
        lugat['fam']=fam
        await message.answer(text="📌 Yaxshi,endi yoshingizni kiriting ")
        await Forma.Yosh_qabul_qilish.set()
    else:
        await message.answer(text='Yosh faqat raqamlardan tashkil  topadi ')
        await Forma.Fam_qabul_qilish.set()

@dp.message_handler(state=Forma.Yosh_qabul_qilish)
async def bot_echo(message: types.Message):

    yosh = message.text
    if  yosh.isdigit():
        lugat['yosh']=yosh
        await message.answer(text="📌 Yaxshi,yashash hududingizni tanlang ",reply_markup=tugmalar)
        await Forma.Shaxar_qabul_qilish.set()
    else:
        await message.answer(text='Yosh faqat raqamlardan tashkil topadi ')
        await Forma.Yosh_qabul_qilish.set()

@dp.message_handler(state=Forma.Shaxar_qabul_qilish)
async def bot_echo(message: types.Message):

    shax = message.text
    if not  shax.isdigit():
        lugat['shax']=shax
        await message.answer(text="📌 Zo'r, endi nomeringizni to'g'ri formatda kiriting: (+998YYXXXXXXX)",reply_markup=tel)
        await Forma.Tel_qabul_qilish.set()
    else:
        await message.answer(text='Shaxar faqat harflardan tashkil topadi ')
        await Forma.Shaxar_qabul_qilish.set()

@dp.message_handler(state=Forma.Tel_qabul_qilish,content_types=ContentTypes.CONTACT)
async def bot_echo(message: types.Message):

    tel = message.contact.phone_number
    print(tel)

    lugat['tel']=tel
    await message.answer(text="📌 Obod MFY yoshlar yetakchisi Islomjon Muhammadjonovga murojaatingizni yozib qoldiring!",reply_markup=ReplyKeyboardRemove())
    await Forma.Murojat_qabul_qilish.set()

@dp.message_handler(state=Forma.Tel_qabul_qilish)
async def bot_echo(message: types.Message):

    tel = message.text
    tel = tel.strip()
    davlat = tel[0:4]
    kod = tel[4:6]
    raqam = tel[6:]
    kodlar = [33,93,94,95,99,97,55,90,98,91,88,97,]
    if davlat !='+998':
        await message.answer(text='+998YYXXXXXXX formatda telefon raqamingizni kiriting')
    elif not int(kod) in kodlar:
        await message.answer(text=f'{kod} bunday kod mavjud emas')
    elif len(raqam)!=7:
        await message.answer(text=f'{raqam} da xatolik mavjud')

    elif davlat=='+998' and int(kod) in kodlar and len(raqam)==7:
        lugat['tel'] = tel
        await message.answer(text="📌 Obod MFY yoshlar yetakchisi Islomjon Muhammadjonovga murojaatingizni yozib qoldiring!", reply_markup=ReplyKeyboardRemove())
    await Forma.Murojat_qabul_qilish.set()






@dp.message_handler(state=Forma.Murojat_qabul_qilish)
async def bot_echo(message: types.Message):

   murojat = message.text
   lugat['text'] = murojat
   matn = ''

   user_id = message.from_user.id
   matn+=f"Ism : {lugat['ism']}\n" \
         f"fam : {lugat['fam']}\n" \
         f"yosh : {lugat['yosh']}\n" \
         f"Shaxar : {lugat['shax']}\n" \
         f"Tel : {lugat['tel']}\n" \
         f"\n                    " \
         f" \n Murojat : {lugat['text']}\n"
   await bot.send_message(chat_id=user_id,text=matn,reply_markup=tasdiq)
   await Forma.Tasdiqlash_qabul_qilish.set()

@dp.message_handler(state=Forma.Tasdiqlash_qabul_qilish,text='Tasdiqlash')
async def bot_echo(message: types.Message,state:FSMContext):
    Ism=lugat['ism']
    fam=lugat['fam']
    yosh=lugat['yosh']
    Shax=lugat['shax']
    Tel=lugat['tel']
    text = lugat['text']
    user_id = message.from_user.id
    username = message.from_user.username
    idd = db.count_users()
    id = idd[0]+1
    try:
        db.user_qoshish(id=id,username=username,ism=Ism,fam=fam,yosh=yosh,shaxar=Shax,matn=text,tel=Tel,tg_id=user_id)
    except Exception as xato:
        pass


    await bot.send_message (chat_id=user_id ,text="""
   📌 Xabaringiz uchun rahmat. Men 10 daqiqada siz bilan bog’lanaman. Ishingizga rivoj! Sizning yoshlar yetakchingiz.

        Islomjon Muhammadjonov
            (+998999948782)Meni tezlik bilan topish uchun quyida joylashuvimni yuboryabman👇
   """,reply_markup=ReplyKeyboardRemove())
    await bot.send_location(chat_id=user_id,latitude=40.170347,longitude=71.731552,reply_markup=asosiy)
    await state.finish()
    await bot.send_message(chat_id=1892438581,text=f"Ushbu foydalanuvchi : {message.from_user.username} \n quyidagi murojatni  yubordi\n {lugat['text']}",
                           reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                   [
                                             InlineKeyboardButton(text='Javob yuborish',callback_data=f'idd{user_id}')
                                   ],
                           ]))

@dp.message_handler(state=Forma.Tasdiqlash_qabul_qilish,text='Bekor qilish')
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text="Barcha malumotlar bekor qilindi")
    await state.finish()




