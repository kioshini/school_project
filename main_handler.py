import json

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from db import Database
from kb.keyb import les_kb, admin_kb

send_router = Router()
db = Database('database.db')
with open('lesons.json', 'r', encoding='utf-8') as file:
    list_of = json.loads(file.read())

with open('default.json', 'r', encoding='utf-8') as dflt:
    save = json.loads(dflt.read())


@send_router.message(Command('start'))
async def start(message: Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}! \nВ этом боте ты можешь узнать рассписание'
        f' чтобы всегда знать какой у тебя следуюющий урок!', reply_markup=les_kb.as_markup())


@send_router.callback_query(F.data == 'mon')
async def monday(callback_query: CallbackQuery):
    day = list_of["10"]["monday"]
    lessons = '\n'.join([f'{value}' for key, value in day.items()])
    await callback_query.message.answer(lessons)


@send_router.callback_query(F.data == 'tue')
async def monday(callback_query: CallbackQuery):
    day = list_of["10"]["tuesday"]
    lessons = '\n'.join([f'{value}' for key, value in day.items()])
    await callback_query.message.answer(lessons)


@send_router.callback_query(F.data == 'wed')
async def monday(callback_query: CallbackQuery):
    day = list_of["10"]["wednesday"]
    lessons = '\n'.join([f'{value}' for key, value in day.items()])
    await callback_query.message.answer(lessons)


@send_router.callback_query(F.data == 'thu')
async def monday(callback_query: CallbackQuery):
    day = list_of["10"]["thursday"]
    lessons = '\n'.join([f'{value}' for key, value in day.items()])
    await callback_query.message.answer(lessons)


@send_router.callback_query(F.data == 'fri')
async def monday(callback_query: CallbackQuery):
    day = list_of["10"]["friday"]
    lessons = '\n'.join([f'{value}' for key, value in day.items()])
    await callback_query.message.answer(lessons)


@send_router.callback_query(F.data == 'les_send')
async def les_send(callback_query: CallbackQuery):
    if not db.user_exists(callback_query.message.from_user.id):
        db.add_user(callback_query.message.from_user.id)
        await callback_query.message.answer('Ты успешно подключил получение следующего урока! ')
    else:
        await callback_query.message.answer('[Ты уже подключил получение следующего урока]')


@send_router.message(Command('change'))
async def change(message: Message):
    if message.from_user.id == 793539079:
        index = 1
        text = message.text.split(' ')
        if len(text) == 1:
            await message.answer('Эта команда нужна для изменения рассписания. \nОбразец:\n'
                                 '/change <день недели цифрой>(от 1 до 5) <номер урока цифрой>(от 1 до 9)] <урок который надо поставить>')
        elif len(text) == 2:
            if text[1] == 'default':
                for i, k in save.items():
                    list_of["10"]['monday'] = k['monday']
                    list_of["10"]['tuesday'] = k['tuesday']
                    list_of["10"]['wednesday'] = k['wednesday']
                    list_of["10"]['thursday'] = k['thursday']
                    list_of["10"]['friday'] = k['friday']

        elif len(text) > 3:
            try:
                if int(text[1]) and int(text[2]):
                    if text[1] == '1':
                        day = list_of["10"]['monday']
                    elif text[1] == '2':
                        day = list_of["10"]['tuesday']
                    elif text[1] == '3':
                        day = list_of["10"]['wednesday']
                    elif text[1] == '4':
                        day = list_of["10"]['thursday']
                    elif text[1] == '5':
                        day = list_of["10"]['friday']
                    for i in range(9):
                        if text[2] == str(index):
                            vstr = " ".join(text[3:])
                            # noinspection PyUnboundLocalVariable
                            day[f'{index}'] = f"{index}. {vstr}"
                        else:
                            index += 1
                    with open('lesons.json', 'w', encoding='utf-8') as f:
                        json.dump(list_of, f, indent=4, ensure_ascii=False)
                    await message.answer('[Расписание изменено успешно!]')
            except:
                await message.answer('[Проверь, ты где-то ошибся!]')


@send_router.message(Command('admin'))
async def admin_menu(message: Message):
    if message.from_user.id == 793539079:
        await message.answer(text='Админ меню:', reply_markup=admin_kb.as_markup())

# добавить функционал админ менюшки(редактирование рассписания, просмотр всех пользователей бота, закрытие админ-меню)
# макет для понедельника готов
