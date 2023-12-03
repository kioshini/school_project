import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import time
from aiogram import Bot, Dispatcher

import config
from handlers.main_handler import send_router

from db import Database
import lessons

db = Database("database.db")

lt = ['7:30:10',
      '8:40:01',
      '9:25:30',
      '10:25:30',
      '11:25:30',
      '12:25:30',
      '13:25:30',
      '14:20:30',  # Начало второй смены
      '15:10:30',
      '16:10:30',
      '17:10:30',
      '18:00:30',
      '18:50:30']  # Lesson time

mt = [
    '7:30:10',
    '8:35:10',
    '9:20:10',
    '10:10:10',
    '11:05:10',
    '12:00:10',
    '12:55:10',
    '13:40:10',
    '14:35:10',
    '15:20:10',
    '16:15:10',
    '17:10:10',
    '17:55:10']


async def daw(bot: Bot):
    if datetime.now().weekday() == 0:
        current_time = datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        if current_time == mt[0]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        await bot.send_message(user[0], lessons.mon_1)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == mt[1]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.mon_2)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == mt[2]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.mon_3)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == mt[3]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        await bot.send_message(user[0], lessons.mon_4)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == mt[4]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.mon_5)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == mt[5]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.mon_6)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == mt[6]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.mon_7)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == mt[7]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.mon_8)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == mt[8]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.mon_9)
                except:
                    db.set_active_user(user[0], 0)
    elif datetime.now().weekday() == 1:
        current_time = datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        if current_time == lt[0]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        await bot.send_message(user[0], lessons.tue_1)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[1]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.tue_2)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[2]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.tue_3)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[3]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        await bot.send_message(user[0], lessons.tue_4)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[4]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.tue_5)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[5]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.tue_6)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[6]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.tue_7)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[7]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.tue_8)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[8]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.tue_9)
                except:
                    db.set_active_user(user[0], 0)
    elif datetime.now().weekday() == 2:
        current_time = datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        if current_time == lt[0]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        await bot.send_message(user[0], lessons.wed_1)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[1]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.wed_2)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[2]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.wed_3)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[3]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        await bot.send_message(user[0], lessons.wed_4)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[4]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.wed_5)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[5]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.wed_6)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[6]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.wed_7)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[7]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.wed_8)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[8]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.wed_9)
                except:
                    db.set_active_user(user[0], 0)
    elif datetime.now().weekday() == 3:
        current_time = datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        if current_time == lt[0]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        await bot.send_message(user[0], lessons.thu_1)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[1]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.thu_2)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[2]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.thu_3)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[3]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        await bot.send_message(user[0], lessons.thu_4)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[4]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.thu_5)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[5]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.thu_6)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[6]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.thu_7)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[7]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.thu_8)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[8]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.thu_9)
                except:
                    db.set_active_user(user[0], 0)
    elif datetime.now().weekday() == 4:
        current_time = datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        if current_time == lt[0]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        await bot.send_message(user[0], lessons.fri_1)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[1]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.fri_2)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[2]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.fri_3)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[3]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        await bot.send_message(user[0], lessons.fri_4)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[4]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.fri_5)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[5]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.fri_6)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[6]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    if user[1] == 1:
                        print(f'пользователь: {user[0]}, его активность: {user[1]}')
                        await bot.send_message(user[0], lessons.fri_7)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[7]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], lessons.fri_8)
                except:
                    db.set_active_user(user[0], 0)
        elif current_time == lt[8]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], lessons.fri_9)
                except:
                    db.set_active_user(user[0], 0)


async def main():
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher()
    dp.include_router(send_router)
    bot = Bot(token=config.bot_api)
    scheduler = AsyncIOScheduler(timezone='Asia/Yekaterinburg')
    scheduler.add_job(daw, trigger='interval', seconds=60, args=(bot,), next_run_time=datetime.now())
    try:
        scheduler.start()
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    try:
        db.create_db('database.db')
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
