import asyncio
import logging
import time
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
            await bot.send_message(message.from_user.id, '1. Основы предпринимательства 208'
                                                     '\n2. Русский язык 117'
                                                     '\n3. Литература 117'
                                                     '\n4. Разговоры о важном 312'
                                                     '\n5. Алгебра 313'
                                                     '\n6. Физическая культура 227'
                                                     '\n7. Обществознание 230')


@router.message(Command("sendall"))
async def send_lesson(msg: Message):
    if msg.chat.type == 'private':
        if msg.from_user.id == 793539079 or msg.from_user.id == 1213682706:
            text = msg.text[9:]
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], text)
                except:
                    db.set_active_user(user[0], 0)
            await bot.send_message(msg.from_user.id, 'Успешная рассылка')
        else:
            pass


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    db.create_db("database.db")
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

''' 
11.11.23
Разобраться почему не работает код, исправить эту фигню, скорее всего ячейка class в базе данных не инициальзируется и всё. надо исправить!

12.11.23
00:00-00:35 
-> Ошибка с классом не была исправлена, просто убрал эту часть пока что, альфа версия бота планируется только для 10 класса, так что надобность в классе пропадает.

9:30-10:00
-> Добавлена функция отключения и включения отправки сообщений пользователю. Изненен текст сообщений, теперь более подходяший. Нужно начать добавлять отправку расписания!
'''
