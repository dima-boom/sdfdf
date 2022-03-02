try:
	import vk_api, os, random
	from vk_api.longpoll import VkLongPoll, VkEventType
	from vk_api.utils import get_random_id
	print("Бот запущен!")

	def write_message(sender, message):
	    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id()})

	def uiui(text):
		return str(text.split())

	token = "432ccbea79c1c0dbeb3db0c5673e880746478cf1e0db3bd7a77b4f585b79cd2fda41fb13460d01aabd983"
	authorize = vk_api.VkApi(token=token)
	longpoll = VkLongPoll(authorize)
	admin = 574170405
	for event in longpoll.listen():
	    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
	        reseived_message = event.text.lower()
	        sender = event.user_id
	        if reseived_message[0:2] == 'вк' or reseived_message[0:2] == 'vk' or reseived_message[0:4] == 'в вк' or reseived_message[0:3] == '-вк' or reseived_message[0:3] == '-vk':
	        	write_message(sender, 'ВКонтакте: \n\n10₽ = 100 Просмотров.\n15₽ = 100 Лайков.\n25₽ = 100 Репостов. \n25₽ = 100 Подписчиков.\n50₽ = 100 Подписчиков (Живых). \n\nЕсли готовы сделать заказ напишите: \nКоличество и "Ссылку"\n\nАдминистратор примет ваш заказ в ближайшее время.')
	        elif reseived_message[0:5] == 'insta' or reseived_message[0:5] == 'инста' or reseived_message[0:5] == 'инсту':
	        	write_message(sender, 'Инстаграм: \n10₽ = 100 Подписчиков.\n5₽ = 100 Лайков. \n\nЕсли готовы сделать заказ напишите: \nКоличество и "Ссылку"\n\nАдминистратор примет ваш заказ в ближайшее время.')
	        elif 'боты' in str(reseived_message.split()) and 'или' in str(reseived_message.split()) or 'аудитория' in reseived_message or 'жив'[0:3] in str(reseived_message.split()) and 'или' in str(reseived_message.split()) or 'актив'[0:5] in reseived_message and '?' in reseived_message:
	        	write_message(sender, '40p за 100 Живых (Активных)')
	        elif 'прайс' in str(reseived_message.split()) or 'цен'[0:3] in uiui(reseived_message) or reseived_message[0:8] == 'расценки' or reseived_message[0:10] == 'подписчики' or reseived_message == 'здравствуйте':
	        	write_message(sender, 'ВКонтакте: \n\n10₽ = 100 Просмотров.\n15₽ = 100 Лайков.\n25₽ = 100 Репостов. \n25₽ = 100 Подписчиков.\n50₽ = 100 Подписчиков (Живых). \n\nИнстаграм: \n10₽ = 100 Подписчиков.\n5₽ = 100 Лайков. \n\nЕсли готовы сделать заказ напишите: \nКоличество и "Ссылку"\n\nАдминистратор примет ваш заказ в ближайшее время.')
	        elif 'дмитрий'[0:7] in uiui(reseived_message) and '?' in reseived_message or reseived_message[0:18] == 'дмитрий витальевич':
	        	write_message(sender, 'Да верно! \nМожете делать перовод.')
	        elif 'пруф'[0:4] in uiui(reseived_message) or 'скрины' in uiui(reseived_message) or 'доказательства' in uiui(reseived_message) or 'доверять' in uiui(reseived_message) or 'доки' in uiui(reseived_message) or 'наёб' in uiui(reseived_message) or 'обман'[0:5] in uiui(reseived_message):
	        	write_message(sender, 'Под группой есть скрины покупок и отзывы клиентов, можете отзнакомиться.')
	        elif 'спасиб'[0:6] in reseived_message or 'спс' in reseived_message or 'от души' in reseived_message:
	        	write_message(sender, 'Всегда пожалуйста ;)')
	        elif 'qiwi'[0:4] in uiui(reseived_message) or 'киви'[0:4] in uiui(reseived_message):
	        	user = authorize.method("users.get", {"user_ids": event.user_id})  
	        	name = str(user[0]['first_name']) + ' ' + str(user[0]['last_name'])
	        	write_message(sender, f'Qiwi - 79283692011 \n\nКоментарий к платежу: \n{name}.')
	        elif 'карт'[0:4] in uiui(reseived_message) or reseived_message[0:4] == 'сбер' or reseived_message[0:3] == 'сбп':
	        	user = authorize.method("users.get", {"user_ids": event.user_id})  
	        	name = str(user[0]['first_name']) + ' ' + str(user[0]['last_name'])
	        	write_message(sender, f'Номер карты - 4276600059773339 \n\nСбп - 79064601130 \nЭто Сбербанк.\n\nКоментарий к платежу: \n{name}.')
except:
	os.system('python bot.py')
