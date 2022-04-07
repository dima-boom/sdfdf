try:
	import vk_api, os, random
	from vk_api.longpoll import VkLongPoll, VkEventType
	from vk_api.utils import get_random_id
	print("Бот запущен!")

	def write_message(sender, message):
	    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id()})

	def uiui(text):
		return str(text.split())

	token = "0b19ba157b2a5c5820cd276334e99bcf6b717f358dd2c3aa8083414423588cf462a243bf3113b763e02ec"
	authorize = vk_api.VkApi(token=token)
	longpoll = VkLongPoll(authorize)
	admin = 574170405
	for event in longpoll.listen():
	    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		reseived_message = event.text.lower()
		sender = event.user_id
		if reseived_message[0:2] == 'вк' or reseived_message[0:2] == 'vk' or reseived_message[0:4] == 'в вк' or reseived_message[0:3] == '-вк' or reseived_message[0:3] == '-vk' and reseived_message[0:3] != 'vk.':
			write_message(sender, 'ВКонтакте: \n\n10₽ = 100 Просмотров.\n15₽ = 100 Лайков.\n25₽ = 100 Репостов. \n25₽ = 100 Подписчиков.\n50₽ = 100 Подписчиков (Живых). \n\nЕсли готовы сделать заказ напишите: \nКоличество и "Ссылку"\n\nАдминистратор примет ваш заказ в ближайшее время.')

		elif reseived_message[0:4] == 'здра' or reseived_message == 'привет' or reseived_message[0:6] == 'добрый' and len(reseived_message) > 10:
			write_message(sender, 'Что вас интересует? \n\nНакрутка.\nРассылка.\nЧат бот.')

		elif reseived_message[0:8] == 'рассылка' or reseived_message[0:7] == 'расылка' or 'заинтересованная аудитория' in reseived_message:
			write_message(sender, '👥 Рассылка:\n\nЭто хороший вариант для поиска заинтересованной аудитории.\nНаши боты будут искать такие же группы и оставлять там комментарии и посты с вашей рекламой, очень хороший способ для поиска заинтересованной аудитории, клиентов.'+
				'\n500₽ - 1000 Рекламных постов и комментариев в группах похожей тематики.')
			write_message(sender, 'Для рассылки придумайте рекламный текст, по желанию добавьте фотографию.')
		elif reseived_message[0:5] == 'insta' or reseived_message[0:5] == 'инста' or reseived_message[0:5] == 'инсту':
			write_message(sender, 'Инстаграм: \n10₽ = 100 Подписчиков.\n5₽ = 100 Лайков. \n\nЕсли готовы сделать заказ напишите: \nКоличество и "Ссылку"\n\nАдминистратор примет ваш заказ в ближайшее время.')
		elif 'боты' in str(reseived_message.split()) and 'или' in str(reseived_message.split()) or 'аудитория' in reseived_message or 'жив'[0:3] in str(reseived_message.split()) and 'или' in str(reseived_message.split()) or 'актив'[0:5] in reseived_message and '?' in reseived_message:
			write_message(sender, '50p за 100 Живых (Активных)')
		elif 'прайс' in str(reseived_message.split()) or 'цен'[0:3] in uiui(reseived_message) or reseived_message[0:8] == 'расценки' or reseived_message[0:10] == 'подписчики' or reseived_message[0:6] == 'накрут':
			write_message(sender, 'ВКонтакте: \n\n10₽ = 100 Просмотров.\n15₽ = 100 Лайков.\n25₽ = 100 Репостов. \n25₽ = 100 Подписчиков.\n50₽ = 100 Подписчиков (Живых). \n\nИнстаграм: \n10₽ = 100 Подписчиков.\n5₽ = 100 Лайков. \n\nЕсли готовы сделать заказ напишите: \nКоличество и "Ссылку"\n\nАдминистратор примет ваш заказ в ближайшее время.')
		elif 'дмитрий'[0:7] in uiui(reseived_message) and '?' in reseived_message or reseived_message[0:18] == 'дмитрий витальевич':
			write_message(sender, 'Да верно! \nМожете делать перевод.')
		elif 'пруф'[0:4] in uiui(reseived_message) or 'скрины' in uiui(reseived_message) or 'доказательства' in uiui(reseived_message) or 'доверять' in uiui(reseived_message) or 'доки' in uiui(reseived_message) or 'наёб' in uiui(reseived_message) or 'обман'[0:5] in uiui(reseived_message):
			write_message(sender, 'Под группой есть скрины покупок и отзывы клиентов, можете отзнакомиться.')
		elif 'спасиб'[0:6] in reseived_message or 'спс' in reseived_message or 'от души' in reseived_message or 'благ'[0:4] in reseived_message or 'блог'[0:4] in reseived_message:
			a = random.randint(1, 5)
			if a == 1:
			    write_message(sender, "Не за что 😉")
			if a == 2:
			    write_message(sender, "Рады помочь 😁")
			if a == 3:
			    write_message(sender, "Пожалуйста :)")
			if a == 4:
			    write_message(sender, 'Всегда пожалуйста ;)')
			if a == 5:
			    write_message(sender, 'Обращайтесь.)')
		elif 'qiwi'[0:4] in uiui(reseived_message) or 'киви'[0:4] in uiui(reseived_message) or reseived_message == '🥝':
			user = authorize.method("users.get", {"user_ids": event.user_id})  
			name = str(user[0]['first_name']) + ' ' + str(user[0]['last_name'])
			write_message(sender, f'Qiwi - 79283692011 \n\nКоментарий к платежу: \n{name}.')
		elif 'карт'[0:4] in uiui(reseived_message) or reseived_message[0:4] == 'сбер' or reseived_message[0:3] == 'сбп' or reseived_message == '💳':
			user = authorize.method("users.get", {"user_ids": event.user_id})  
			name = str(user[0]['first_name']) + ' ' + str(user[0]['last_name'])
			write_message(sender, f'Номер карты - 4279380644765168 \n\nСбп - 79064601130 \nЭто Сбербанк.\n\nКоментарий к платежу: \n{name}.')
except:
	os.system('python bot.py')
