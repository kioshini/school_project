import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

import config
from db import Database

bot = Bot(token=config.API)
router = Router()
db = Database("database.db")


@router.message(Command("start"))
async def start_handler(message: Message):
    await bot.send_message(message.from_user.id,
                           'Привет, в этом боте ты можешь посмотреть рассписание на сегодняшний день! Чтобы это сделать пропиши команду /lessons'
                           '\nЕсли хочешь получать уведомления какой у тебя следущий урок, пиши /sub !!!')


@router.message(Command('sub'))
async def sub_main(message: Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    await message.answer("Отлично, t.me/Dissipation_bot <- Сюда приходят уведомления о следущем уроке! "
                         "\nПереходи по ссылке чтобы начать получать уведомления! (больше ничего делать не нужно)   ")


@router.message(Command("off"))
async def off_send(message: Message):
    if message.chat.type == 'private':
        db.set_active_user(message.from_user.id, 0)
        await bot.send_message(message.from_user.id, 'Вы успешно откллючили получение рассписания')


@router.message(Command("on"))
async def off_send(message: Message):
    if message.chat.type == 'private':
        db.set_active_user(message.from_user.id, 1)
        await bot.send_message(message.from_user.id, 'Вы успешно включили получение рассписания')


@router.message(Command("lessons"))
async def send_lesson(message: Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Расписание на сегодня:')
        if datetime.today().weekday() == 0:
            await bot.send_message(message.from_user.id, '1. Основы предпринесательства - 208 кабинет (Кокорина Д.Д)'
                                                         '\n2. Русский язык - 117 кабинет (Милькова Т.Н.)'
                                                         '\n3. Литература - 117 кабинет (Милькова Т.Н.)'
                                                         '\n4. Разговоры о важном - 312 кабинет (Горева Я.В.)'
                                                         '\n5. Алгебра - 313 кабинет (Сивов И.А.)'
                                                         '\n6. Физ.культура - 229/227 кабинет (Войцехвоская / Малков Ф.А.)'
                                                         '\n7. Обществознание - 230 кабинет (Казаков Г.В.)')

        elif datetime.today().weekday() == 1:
            await bot.send_message(message.from_user.id, '1. [Коледж-класс] Основы философии - 312 кабинет (Горева Я.В)'
                                                         '\n2. История - 230 кабинет (Казаков Г.В.)'
                                                         '\n3. История - 230 кабинет (Казаков Г.В.)'
                                                         '\n4. География - 208 кабинет (Абрамовская Я.В.)'
                                                         '\n5. Литература - 117 кабинет (Милькова Т.Н.)'
                                                         '\n6. Иностранный язык - 202 кабинет (Сагадиева Ю.С.)'
                                                         '\n7. [Углубленный уровень] Информатика - 306 кабинет /'
                                                         '\n [Коледж-класс] Иностранный язык - 202 кабинет (Сагадиева Ю.С.)'
                                                         '\n8. [Коледж-класс] Иностранный язык - 202 кабинет (Сагадиева Ю.С.)')

        elif datetime.today().weekday() == 2:
            await bot.send_message(message.from_user.id, '1. Искусство публичных выступлений - 208 кабинет (Абрамовская Я.В.)'
                                                         '\n2. Геометрия - 314 кабинет (Саблина Н.А.)'
                                                         '\n3. Литература - 117 кабинет (Милькова Т.Н.)'
                                                         '\n4. Химия - 208 кабинет (Кузякин А.Д.)'
                                                         '\n5. Физика - 308{314} кабинет (Лобанова Л.В.)'
                                                         '\n6. Обществознание - 230 кабинет (Казаков Г.В.)'
                                                         '\n7. История - 230 кабинет (Казаков Г.В.)'
                                                         '\n8. Дискусионный киноклуб - 230 кабинет (Казаков Г.В.)')

        elif datetime.today().weekday() == 3:
            await bot.send_message(message.from_user.id, '1. Статистика - 313 кабинет (Сивов И.А.)'
                                                         '\n2. Алгебра - 313 кабинет (Сивов И.А.)'
                                                         '\n3. Основы безопасности жизнедеятельности - 105 кабинет (Лесунова Т.П.)'
                                                         '\n4. Иностранный язык - 202 кабинет (Сагадиева Ю.С.)'
                                                         '\n5. Биология - 206 кабинет (Жест Н.И.)'
                                                         '\n6. География - 208 кабинет (Абрамовская Я.В.)'
                                                         '\n7. Физ.культура - 229/227 кабинет (Войцехвоская / Малков Ф.А.)'
                                                         '\n8. ((*)_Окно_(*))'
                                                         '\n9. [Коледж-класс] Иностранный язык - 202 кабинет (Сагадиева Ю.С.)')

        elif datetime.today().weekday() == 4:
            await bot.send_message(message.from_user.id, '1. [Углубленный уровень] Информатика - 306 кабинет (Шевелева М.П.)'
                                                         '\n* [Углубленный уровень] Физика - 308 кабинет (Лобанова Л.В.)'
                                                         '\n* [Углубленный уровень] Обществознание - 230 кабинет (Казаков Г.В.)'
                                                         '\n2. Физика - 308 кабинет (Лобанова Л.В.)'
                                                         '\n3. Геометрия - 314 кабинет (Саблина Н.А.)'
                                                         '\n4. Алгебра - 313 кабинет (Сивов И.А.)'
                                                         '\n5. Русский язык - 117 кабинет (Милькова Т.Н.)'
                                                         '\n6. Литература - 117 кабинет (Милькова Т.Н.)'
                                                         '\n7. Информатика - 306 кабинет (Шевелева М.П.)')


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    db.create_db("database.db")
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
