from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ilmiy_suhbatlar_menu = {"Жонли суҳбатлар": "jonli", "Сурхондарё сафари": "surhon", "Тошкент вилояти": "toshvil",
                        "Тошкент шаҳри (1-тўплам)": "tosh1", "Тошкент шаҳри (2-тўплам)": "tosh2",
                        "Ҳаж ва курбонлик": "hajqurbonlik", "1-тўплам": "birt", "2-тўплам": "ikkit", "3-тўплам": "ucht"
                        }

ilmiy_suhbatlar_list = ["1-5 сyҳбатлар", "6-10 сyҳбатлар", "11-15 сyҳбатлар", "16-20 сyҳбатлар", "21-25 сyҳбатлар",
                        "26-30 сyҳбатлар", "31-35 сyҳбатлар", "36-40 сyҳбатлар", "41-45 сyҳбатлар", "46-52 сyҳбатлар"]

ilmiy_suhbatlar_audios = {'1-5 сyҳбатлар': [720, 721, 722, 723, 724], '6-10 сyҳбатлар': [725, 726, 727, 728, 729],
                          '11-15 сyҳбатлар': [730, 731, 732, 733, 734], '16-20 сyҳбатлар': [735, 736, 737, 738, 739],
                          '21-25 сyҳбатлар': [740, 741, 742, 743, 744], '26-30 сyҳбатлар': [745, 746, 747, 748, 749],
                          '31-35 сyҳбатлар': [750, 751, 752, 753, 754], '36-40 сyҳбатлар': [755, 756, 757, 758, 759],
                          '41-45 сyҳбатлар': [760, 761, 762, 763, 764],
                          '46-52 сyҳбатлар': [765, 766, 767, 768, 769, 770, 771]
                          }
ilmiy_suhbatlar_videos = {'1-5 сyҳбатлар': [772, 773, 774, 775, 776], '6-10 сyҳбатлар': [777, 778, 779, 780, 781],
                          '11-15 сyҳбатлар': [782, 783, 784, 785, 786], '16-20 сyҳбатлар': [787, 788, 789, 790, 791],
                          '21-25 сyҳбатлар': [792, 793, 794, 795, 796], '26-30 сyҳбатлар': [797, 798, 799, 800, 801],
                          '31-35 сyҳбатлар': [802, 803, 804, 805, 806], '36-40 сyҳбатлар': [807, 808, 809, 810, 811],
                          '41-45 сyҳбатлар': [812, 813, 814, 815, 816],
                          '46-52 сyҳбатлар': [817, 818, 819, 820, 821, 822, 823]
                          }


async def ilmiy_suhbatlar_buttons():
    key = ReplyKeyboardMarkup(row_width=2,
                              resize_keyboard=True,
                              one_time_keyboard=True)
    key.add("⏮ Олдинги")
    key.insert("🏡 Бош саҳифа")
    key.add("1-5 сyҳбатлар")
    for n in ilmiy_suhbatlar_list:
        if n == "1-5 сyҳбатлар":
            pass
        else:
            key.insert(n)
    return key


async def ilmiy_suhbatlar_home_page():
    key = ReplyKeyboardMarkup(row_width=2,
                              resize_keyboard=True,
                              one_time_keyboard=True)
    key.add("🏡 Бош саҳифа"),
    key.add("Жонли суҳбатлар")

    for n in ilmiy_suhbatlar_menu.keys():
        if n == "Жонли суҳбатлар":
            pass
        else:
            key.insert(n)
    return key


audio_video_page = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏮ Олдинги"),
            KeyboardButton(text="🏡 Бош саҳифа"),
        ],
        [
            KeyboardButton(text="🎧 Ayдиo"),
            KeyboardButton(text="🎬 Видео"),

        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
