from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

les_kb = InlineKeyboardBuilder()
les_kb.add(InlineKeyboardButton(text='Расписание в понедельник', callback_data='mon'),
           InlineKeyboardButton(text='Расписание во вторник', callback_data='tue'),
           InlineKeyboardButton(text='Расписание в среду', callback_data='wed'),
           InlineKeyboardButton(text='Расписание в четверг', callback_data='thu'),
           InlineKeyboardButton(text='Расписание в пятницу', callback_data='fri'),
           InlineKeyboardButton(text='Включить рассылку уроков', callback_data='les_send'),
           )
les_kb.adjust(1)

admin_kb = InlineKeyboardBuilder()
admin_kb.add(InlineKeyboardButton(text='Изменение рассписания', callback_data='res'),
             InlineKeyboardButton(text='Просмотр списка пользователей бота', callback_data='check'),
             InlineKeyboardButton(text='Выйти', callback_data='quit')
             )
admin_kb.adjust(1)

re_kb = InlineKeyboardBuilder()
re_kb.add(InlineKeyboardButton(text='понедельник', callback_data='remon'),
          InlineKeyboardButton(text='вторник', callback_data='retue'),
          InlineKeyboardButton(text='среда', callback_data='rewed'),
          InlineKeyboardButton(text='четверг', callback_data='rethu'),
          InlineKeyboardButton(text='пятница', callback_data='refri'),
          )
re_kb.adjust(1)
