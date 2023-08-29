from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from loader import dp

from keyboards.default.start_dk import main_keyboard

haj_dict = {1:{'v':'BAACAgIAAxkBAAEHR6pizPDZTkItGjGp0ZbpiPP1eH2nUAACtRgAAgjeaEpiX-PDWq-iUSkE','c':'«Ҳаж-2022» мавсуми доирасида сўнги зиёратчилар гуруҳи Саудия Арабистонига жўнаб кетдилар\n\n<a href=\'https://youtu.be/nBL3h8ATsyg\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/c/Portalislomuz\'>Youtube</a>'},2: {'v': 'BAACAgIAAxkBAAEGwkhivyEC-g_2zBb3ygvV9wYXmYXxnAACTBsAApxW-EkSAW4ocUR9EikE','c': 'Ҳаж қилишнинг ҳукмлари, фазилатлари ва муҳим тавсиялар\n\n<a href=\'https://youtu.be/1mBJO9LmgXE\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/c/Portalislomuz\'>Youtube</a>'},3:{'v':'BAACAgIAAxkBAAEHR6xizPEZXopAqKzxPXEizCdQ9sPJGwACthgAAgjeaEpBGylMEiullCkE','c':'Эҳромда кийим кийиш\n\n<a href=\'https://youtu.be/WIRjIINBqak\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/c/Portalislomuz\'>Youtube</a>'},4:{'v':'BAACAgIAAxkBAAEHR65izPFa8NGrezf9M9EITyXNqjRilQACuBgAAgjeaErn2VtiT-wauykE','c':'Эҳромда хушбўйлик ва бошқа масалалар\n\n<a href=\'https://youtu.be/bfBHpdq7R5w\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/c/Portalislomuz\'>Youtube</a>'},5:{'v':'BAACAgIAAxkBAAEHR6hizPBNrGT0LwYoamgU2aVVr55iaQACtBgAAgjeaEoglCA_WODjPCkE','c':'Ушбу тоғ бизни ва биз ҳам уни яхши кўрамиз\n\n<a href=\'https://youtu.be/c-x-CM1GyNs\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/c/Portalislomuz\'>Youtube</a>'},6:{'v':'BAACAgIAAxkBAAEHR7xizPK9hwW2d3X73dc7oVU2SVfS1gACvBgAAgjeaErzGBmy87dKyikE','c':'Қирон ҳажга оид тавсиялар\n\n<a href=\'https://youtu.be/c8jAKM1peUc\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/c/Portalislomuz\'>Youtube</a>'},7:{'v':'BAACAgIAAxkBAAEHR7pizPKmOTXyJeW7FgsGRzZwjVVGWQACuxgAAgjeaErvrE6BsIvb1SkE','c':'Ҳасанхон Яҳё Абдулмажид Каъбаи муаззама олдида Қорақалпоқ қардошларимизни бирдамликка чақирди\n\n<a href=\'https://youtu.be/Fh2mJzOFP_k\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/c/Portalislomuz\'>Youtube</a>'},8:{'v':'BAACAgIAAxkBAAEHR7hizPII2cyPw0ZMIPqg0TV0U-aMhAACuhgAAgjeaEpUX8ifH23wmSkE','c':'Эҳсон Шеножак жаноблари халқимизни Қурбон ҳайити байрами билан табриклади!\n\n<a href=\'https://youtu.be/r3MjimJzkUA\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/c/Portalislomuz\'>Youtube</a>'},9:{'v':'BAACAgIAAxkBAAEHR75izPMJiohrU7TchshJb6RE4bFNiQACvRgAAgjeaErMdYfNAf2B9ikE','c':'Қурбон ҳайитингиз муборак бўлсин!\n\n<a href=\'https://youtu.be/NYCByQmQqiE\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/c/Portalislomuz\'>Youtube</a>'}}

@dp.message_handler(text="🕋 Ҳаж - 2022")
async def hajvid(msg: types.Message):
	for qulf, kalit in haj_dict.items():
		await msg.answer_video(video=kalit['v'], caption=kalit['c'], reply_markup=main_keyboard)


