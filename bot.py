try:
	import vk_api, os
	from vk_api.longpoll import VkLongPoll, VkEventType
	from vk_api.utils import get_random_id
	print("Бот запущен!")

	def write_message(sender, message):
	    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id()})

	def uiui(text):
		return str(text.split())

	token = "5a91868625113f0d46b39692bab0caa1003f3fb3530d2fce1e4329d6615f8211652731f5fd4d9e676eff1"
	authorize = vk_api.VkApi(token=token)
	longpoll = VkLongPoll(authorize)
	admin = 574170405
	for event in longpoll.listen():
	    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
	        reseived_message = event.text.lower()
	        sender = event.user_id
	        if reseived_message[0:2] == 'вк' or reseived_message[0:2] == 'vk' or reseived_message[0:4] == 'в вк' or reseived_message[0:3] == '-вк' or reseived_message[0:3] == '-vk':
	        	write_message(sender, 'ВКонтакте: \n\n6₽ = 100 Просмотров.\n10₽ = 100 Лайков.\n20₽ = 100 Репостов. \n20₽ = 100 Подписчиков.\n40₽ = 100 Подписчиков (Живых). \n\nЕсли готовы сделать заказ напишите: \nКоличество и "Ссылку"\n\nАдминистратор примет ваш заказ в ближайшее время.')
	        elif reseived_message[0:5] == 'insta' or reseived_message[0:5] == 'инста' or reseived_message[0:5] == 'инсту':
	        	write_message(sender, 'Инстаграм: \n10₽ = 100 Подписчиков.\n5₽ = 100 Лайков. \n\nЕсли готовы сделать заказ напишите: \nКоличество и "Ссылку"\n\nАдминистратор примет ваш заказ в ближайшее время.')
	        elif 'боты' in str(reseived_message.split()) and 'или' in str(reseived_message.split()) or 'аудитория' in reseived_message or 'жив'[0:3] in str(reseived_message.split()) and 'или' in str(reseived_message.split()) or 'актив'[0:5] and '?' in reseived_message:
	        	write_message(sender, '40p за 100 Живых (Активных)')
	        elif 'дмитрий' in str(reseived_message.split()) and '?' in str(reseived_message.split()):
	        	write_message(sender, 'Да верно!')
	        elif 'прайс' in str(reseived_message.split()) or 'цен'[0:3] in uiui(reseived_message) or reseived_message[0:8] == 'расценки' or reseived_message[0:10] == 'подписчики', or reseived_message == 'здравствуйте':
	        	write_message(sender, 'ВКонтакте: \n\n6₽ = 100 Просмотров.\n10₽ = 100 Лайков.\n20₽ = 100 Репостов. \n20₽ = 100 Подписчиков.\n40₽ = 100 Подписчиков (Живых). \n\nИнстаграм: \n10₽ = 100 Подписчиков.\n5₽ = 100 Лайков. \n\nЕсли готовы сделать заказ напишите: \nКоличество и "Ссылку"\n\nАдминистратор примет ваш заказ в ближайшее время.')

	        elif 'пруф'[0:4] in uiui(reseived_message) or 'скрины' in uiui(reseived_message) or 'доказательства' in uiui(reseived_message) or 'доверять' in uiui(reseived_message) or 'доки' in uiui(reseived_message):
	        	write_message(sender, 'Под группой есть скрины покупок и отзывы клиентов, можете отзнакомиться.')
	        elif 'qiwi'[0:4] in uiui(reseived_message) or 'киви'[0:4] in uiui(reseived_message):
	        	write_message(sender, 'Qiwi - 79283692011 \n\nПри возможности укажите ваш ник ВК.')
	        elif 'карт'[0:4] in uiui(reseived_message) or reseived_message[0:4] == 'сбер' or reseived_message[0:3] == 'сбп':
	        	write_message(sender, 'Номер карты - 4276600059773339 \nСбп - 79064601130\n\nПри возможности укажите ваш ник ВК.')
except:
	os.system('python bot.py')
