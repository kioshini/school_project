from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from kb.keyb import les_kb, admin_kb, re_kb
from db import Database

send_router = Router()
db = Database('database.db')


@send_router.message(Command('start'))
async def start(message: Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}! \nВ этом боте ты можешь узнать рассписание и подключить рассылку,'
        f' чтобы всегда знать какой у тебя следуюющий урок!', reply_markup=les_kb.as_markup())
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)


@send_router.callback_query(F.data == 'mon')
async def monday(callback_query: CallbackQuery):
    await callback_query.message.answer('1. Основы предпринесательства - 208 кабинет (Кокорина Д.Д)'
                                        '\n2. Русский язык - 117 кабинет (Милькова Т.Н.)'
                                        '\n3. Литература - 117 кабинет (Милькова Т.Н.)'
                                        '\n4. Разговоры о важном - 312 кабинет (Горева Я.В.)'
                                        '\n5. Алгебра - 313 кабинет (Сивов И.А.)'
                                        '\n6. Физ.культура - 229/227 кабинет (Войцехвоская / Малков Ф.А.)'
                                        '\n7. Обществознание - 230 кабинет (Казаков Г.В.)')


@send_router.callback_query(F.data == 'tue')
async def monday(callback_query: CallbackQuery):
    await callback_query.message.answer('1. [Коледж-класс] Основы философии - 312 кабинет (Горева Я.В)'
                                        '\n2. История - 230 кабинет (Казаков Г.В.)'
                                        '\n3. История - 230 кабинет (Казаков Г.В.)'
                                        '\n4. География - 208 кабинет (Абрамовская Я.В.)'
                                        '\n5. Литература - 117 кабинет (Милькова Т.Н.)'
                                        '\n6. Иностранный язык - 202 кабинет (Сагадиева Ю.С.)'
                                        '\n7. [Углубленный уровень] Информатика - 306 кабинет /'
                                        '\n* [Коледж-класс] Иностранный язык - 202 кабинет (Сагадиева Ю.С.)'
                                        '\n8. [Коледж-класс] Иностранный язык - 202 кабинет (Сагадиева Ю.С.)')


@send_router.callback_query(F.data == 'wed')
async def monday(callback_query: CallbackQuery):
    await callback_query.message.answer('1. Искусство публичных выступлений - 208 кабинет (Абрамовская Я.В.)'
                                        '\n2. Геометрия - 314 кабинет (Саблина Н.А.)'
                                        '\n3. Литература - 117 кабинет (Милькова Т.Н.)'
                                        '\n4. Химия - 208 кабинет (Кузякин А.Д.)'
                                        '\n5. Физика - 308{314} кабинет (Лобанова Л.В.)'
                                        '\n6. Обществознание - 230 кабинет (Казаков Г.В.)'
                                        '\n7. История - 230 кабинет (Казаков Г.В.)'
                                        '\n8. Дискусионный киноклуб - 230 кабинет (Казаков Г.В.)')


@send_router.callback_query(F.data == 'thu')
async def monday(callback_query: CallbackQuery):
    await callback_query.message.answer('1. Статистика - 313 кабинет (Сивов И.А.)'
                                        '\n2. Алгебра - 313 кабинет (Сивов И.А.)'
                                        '\n3. Основы безопасности жизнедеятельности - 105 кабинет (Лесунова Т.П.)'
                                        '\n4. Иностранный язык - 202 кабинет (Сагадиева Ю.С.)'
                                        '\n5. Биология - 206 кабинет (Жест Н.И.)'
                                        '\n6. География - 208 кабинет (Абрамовская Я.В.)'
                                        '\n7. Физ.культура - 229/227 кабинет (Войцехвоская / Малков Ф.А.)'
                                        '\n8. ((*)_Окно_(*))'
                                        '\n9. [Коледж-класс] Иностранный язык - 202 кабинет (Сагадиева Ю.С.)')


@send_router.callback_query(F.data == 'fri')
async def monday(callback_query: CallbackQuery):
    await callback_query.message.answer('1. [Углубленный уровень] Информатика - 306 кабинет (Шевелева М.П.)'
                                        '\n* [Углубленный уровень] Физика - 308 кабинет (Лобанова Л.В.)'
                                        '\n* [Углубленный уровень] Обществознание - 230 кабинет (Казаков Г.В.)'
                                        '\n2. Физика - 308 кабинет (Лобанова Л.В.)'
                                        '\n3. Геометрия - 314 кабинет (Саблина Н.А.)'
                                        '\n4. Алгебра - 313 кабинет (Сивов И.А.)'
                                        '\n5. Русский язык - 117 кабинет (Милькова Т.Н.)'
                                        '\n6. Литература - 117 кабинет (Милькова Т.Н.)'
                                        '\n7. Информатика - 306 кабинет (Шевелева М.П.)')


@send_router.callback_query(F.data == 'res')
async def change_les(call_query: CallbackQuery):
    await call_query.message.answer('Выбери день недели:', reply_markup=re_kb)


@send_router.callback_query(F.data == 'remon')
async def remonday(call_query: CallbackQuery):
    await call_query.message.answer(text='a')


@send_router.message(Command('change'))
async def change(message: Message):
    text = message.text.split(' ')
    if len(text) == 1:
        await message.answer('Эта команда нужна для изменения рассписания. \nОбразец:\n'
                             '/change <день недели цифрой>(от 1 до 5) <номер урока цифрой>(от 1 до 9)] <урок который надо поставить>')
    if len(text) == 2:
        await message.answer('Проверь, ты где-то ошибся')
    elif len(text) > 3:
        if text[1] == '1':
            print("Понедельник")
            if text[2] == '1':
                with open('lessons.py', 'r') as f:
                    lines = f.readlines()
                    index = 0
                    for line in lines:
                        if line[0 - 5] == 'mon_1':
                            lines[index] = text[3]
                        else:
                            index += 1
                    with open('lessons.py', 'w') as file:
                        file.writelines(lines)

            elif text[2] == '2':
                print('второй урок')
            elif text[2] == '3':
                print('третий урок')
            elif text[2] == '4':
                print('четвертый урок')
            elif text[2] == '5':
                print('пятый урок')
            elif text[2] == '6':
                print('шестой урок')
            elif text[2] == '7':
                print('седьмой урок')
            elif text[2] == '8':
                print('восьмой урок')
            elif text[2] == '9':
                print('девятый урок')
            else:
                if text[2]:
                    print('такого урока по счету в рассписании нет(пиши номер урока цифрой)')


@send_router.message(Command('admin'))
async def admin_menu(message: Message):
    if message.from_user.id == 793539079:
        await message.answer(text='Админ меню:', reply_markup=admin_kb.as_markup())

# добавить функционал админ менюшки(редактирование рассписания, просмотр всех пользователей бота, закрытие админ-меню)
# макет для понедельника готов
