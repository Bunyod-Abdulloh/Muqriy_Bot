from aiogram.types import ReplyKeyboardMarkup

adm_adm = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

adm_adm.row("Sending messages", "Cancel sending messages")
adm_adm.row("Count_all_users", "Count_blocked_users")
adm_adm.add("Sql buttons", "🏡 Бош саҳифа")

admin_sql_buttons = ReplyKeyboardMarkup(resize_keyboard=True,
                                        one_time_keyboard=True)
admin_sql_buttons.add("Delete blocked users")
admin_sql_buttons.row("🔙 Ortga", "🏡 Бош саҳифа")
