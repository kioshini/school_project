import asyncio
import json
import time
from datetime import datetime

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import config
from db import Database
from handlers.main_handler import send_router

dp = Dispatcher()
SAVE_DIR = r"C:\Users\romak\PycharmProjects\pythonProject4"
db = Database("database.db")
boot = Bot(token=config.bot_api)
lt = ['7:30',
      '8:40',
      '9:25',
      '10:25',
      '11:25',
      '12:25',
      '13:25',
      '14:20',  # Начало второй смены
      '15:10',
      '16:10',
      '17:10',
      '18:00',
      '18:50']  # Lesson time

mt = [
    '7:30',
    '8:35',
    '9:20',
    '10:10',
    '11:05',
    '12:00',
    '12:55',
    '13:40',
    '14:35',
    '15:20',
    '16:15',
    '17:10',
    '17:55']


with open('default.json', 'r', encoding='utf-8') as default:
    save = json.loads(default.read())


async def daw(bot: Bot):
    with open('lesons.json', 'r', encoding='utf-8') as file:
        list_of_lessons = json.loads(file.read())
    if datetime.now().weekday() == 0:
        day = list_of_lessons["10"]["monday"]
        current_time = datetime.now().strftime("%H:%M")
        time.sleep(1)

        if current_time == mt[0]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["1"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == mt[1]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["2"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == mt[2]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["3"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == mt[3]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["4"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == mt[4]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["5"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == mt[5]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["6"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == mt[6]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["7"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == mt[7]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["8"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == mt[8]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["9"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
    elif datetime.now().weekday() == 1:
        day = list_of_lessons["10"]["tuesday"]
        current_time = datetime.now().strftime("%H:%M")
        time.sleep(1)
        if current_time == lt[0]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["1"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[1]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["2"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[2]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["3"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[3]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["4"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[4]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["5"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[5]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["6"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[6]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["7"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[7]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["8"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[8]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["9"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
    elif datetime.now().weekday() == 2:
        day = list_of_lessons["10"]["wednesday"]
        current_time = datetime.now().strftime("%H:%M")
        time.sleep(1)
        if current_time == lt[0]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["1"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[1]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["2"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[2]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["3"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[3]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["4"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[4]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["5"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[5]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["6"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[6]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["7"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[7]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["8"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[8]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["9"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
    elif datetime.now().weekday() == 3:
        day = list_of_lessons["10"]["thursday"]
        current_time = datetime.now().strftime("%H:%M")
        time.sleep(1)
        if current_time == lt[0]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["1"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[1]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["2"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[2]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["3"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[3]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["4"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[4]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["5"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[5]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["6"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[6]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["7"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[7]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["8"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[8]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["9"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
    elif datetime.now().weekday() == 4:
        day = list_of_lessons["10"]["friday"]
        current_time = datetime.now().strftime("%H:%M")
        time.sleep(1)
        if current_time == lt[0]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["1"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[1]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["2"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[2]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["3"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[3]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["4"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[4]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["5"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[5]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["6"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[6]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["7"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[7]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["8"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
        elif current_time == lt[8]:
            print('pass')
            users = db.get_users()
            for user in users:
                try:
                    print(f'пользователь: {user[0]}, его активность: {user[1]}')
                    await bot.send_message(user[0], day["9"])
                except:
                    print(f'пользователь: {user[0]}, до него не доходит, тормоз крч.')
    elif datetime.now().weekday() == 4:
        current_time = datetime.now().strftime("%H:%M")
        time.sleep(1)
        if current_time == '00:05':
            for v, k in save.items():
                list_of_lessons["10"]['monday'] = k['monday']
                list_of_lessons["10"]['tuesday'] = k['tuesday']
                list_of_lessons["10"]['wednesday'] = k['wednesday']
                list_of_lessons["10"]['thursday'] = k['thursday']
                list_of_lessons["10"]['friday'] = k['friday']


async def main():
    dp.include_router(send_router)
    scheduler = AsyncIOScheduler(timezone='Asia/Yekaterinburg')
    scheduler.add_job(daw, trigger='interval', seconds=60, args=(boot,), next_run_time=datetime.now())
    try:
        scheduler.start()
        await boot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(boot)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    try:
        db.create_db('database.db')
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
