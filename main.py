import telebot
from telebot import types

bot = telebot.TeleBot('6298761916:AAHAHBGmYJiAuE9szS9OgrSRNLk_3Cd5TMw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    theory = types.KeyboardButton('Теория')
    practice = types.KeyboardButton('Практика')
    markup.add(theory, practice)
    bot.send_message(message.chat.id, 'Чем займёмся сегодня?', reply_markup=markup)


@bot.message_handler()
def get_user_text(message):
    if message.text == "Теория":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        points = types.KeyboardButton('Замечательные точки треугольника')
        circles = types.KeyboardButton('Полезные факты про окружности')
        back = types.KeyboardButton('Вернуться в главное меню')
        markup1.add(points, circles, back)
        bot.send_message(message.chat.id, 'Выберите тему', reply_markup=markup1)

    if message.text == "Замечательные точки треугольника":
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        median = types.KeyboardButton('Центр тяжести')
        visoty = types.KeyboardButton('Ортоцентр')
        bissec = types.KeyboardButton('Инцентр')
        o9 = types.KeyboardButton('Центр окружности 9 точек')
        opis = types.KeyboardButton('Центр описанной окружности')
        eiler = types.KeyboardButton('Прямая Эйлера')
        back = types.KeyboardButton('Вернуться в главное меню')
        markup2.add(median, bissec, visoty, opis, o9, eiler, back)
        bot.send_message(message.chat.id, 'Выберите объект', reply_markup=markup2)

    if message.text == "Вернуться в главное меню":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        theory = types.KeyboardButton('Теория')
        practice = types.KeyboardButton('Практика')
        markup3.add(theory, practice)
        bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=markup3)

    if message.text == "Центр тяжести":
        photo1 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\Центр тяжести.png', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, 'Медианы треугольника пересекаются в одной точке, называемой центром тяжести треугольника и делятся в своей точке пересечения в отношении 2:1. При решении задач полезно удваивать медиану')

    if message.text == "Ортоцентр":
        photo2 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph2.png', 'rb')
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, 'Высоты у треугольника пересекаются в одной точке, называемой ортоцентром. Полезен факт, что четырёхугольники HBC1A1 и аналогичные - вписанные, так как сумма противоположных углов равна 180 градусам')

    if message.text == "Инцентр":
        photo3 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph3.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, 'Биссекртрисы пересекаются в центре вписанной окружности треугольника. Это легко осознать исходя из свойств биссектрисы: это ГМТ равноудалённых от сторон угла. Полезно использовать, что угол BIC равен сумме прямого угла и половины угла A')

    if message.text == "Центр описанной окружности":
        photo4 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph4.png', 'rb')
        bot.send_photo(message.chat.id, photo4)
        bot.send_message(message.chat.id,'У треугольника есть описанная окружность. Её центр можно найти, если пересечь серединные перпендикуляры к сторонам. Также углы, нарисованные на картинке имеют такие соотношения, как показано')

    if message.text == "Центр окружности 9 точек":
        photo5 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph5.png', 'rb')
        bot.send_photo(message.chat.id, photo5)
        bot.send_message(message.chat.id, 'Основания высот, середины сторон и середины отрезков, соединяющих вершины треугольника с ортоцентром лежат на одной окружности. Удивительно, что эта окружность 9 точек касается вписанной и вневписанных окружностей треугольника!')

    if message.text == "Прямая Эйлера":
        photo6 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph6.png', 'rb')
        bot.send_photo(message.chat.id, photo6)
        bot.send_message(message.chat.id, 'Удивительно, но факт. Центр описанной окружности треугольника, точка пересечения медиан, ортоцентр и центр окружности 9 точек лежат на одной прямой. Причем M лежит между O и H и делит их в отношении 1:2')

    if message.text == "Полезные факты про окружности":
        photo7 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph7.png', 'rb')
        bot.send_photo(message.chat.id, photo7)
        bot.send_message(message.chat.id, 'Поговорим о свойствах и признаках вписанных четырёхугольников. Углы, опирающиеся на одну дугу, равны. Сумма противоположных углов вписанного четырёхугольника равна 180 градусам. Верно и обратное: если у четырёхугольника сумма противопожных углов 180 или углы опирающиесся на одну "дугу" равны, то тогда четырёхугольник вписанный')
        photo8 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph8.png', 'rb')
        bot.send_photo(message.chat.id, photo8)
        bot.send_message(message.chat.id,'У точки есть так называемая степень относительно окружности. Для точки С степень относительно окружности равна произведению длин отрезков CE и CF(CF - какая-то прямая, пересекающая окружность). И для любой прямой это произведение фиксировано. Оно так же равно квадрату касательной, то есть квадрату CB или квадрату CA')

    if message.text == "Практика":
        bot.send_message(message.chat.id,'1) всерос 2022 9.2  Биссектрисы треугольника ABC пересекаются в точке I, внешние биссектрисы его углов B и C пересекаются в точке J. Окружность ωb с центром в точке Ob проходит через точку B и касается прямой CI в точке I. Окружность ωc с центром в точке Oc проходит через точку C и касается прямой BI в точке I. Отрезки ObOc и IJ пересекаются в точке K. Найдите отношение IK/KJ.')
        bot.send_message(message.chat.id,'2) всерос 2022 9.8  В треугольник ABC вписана окружность ω, касающаяся стороны BC в точке K. Окружность ω0 симметрична окружности ω относительно точки A. Точка A0 выбрана так, что отрезки BA0 и CA0 касаются ω0. Пусть M — середина стороны BC. Докажите, что прямая AM делит отрезок KA0 пополам')
        bot.send_message(message.chat.id,'3) всерос 2016 9.2  Дана равнобокая трапеция ABCD с основаниями BC и AD. Окружность ω проходит через вершины B и C и вторично пересекает сторону AB и диагональ BD в точках X и Y соответственно. Касательная, проведенная к окружности ω в точке C, пересекает луч AD в точке Z. Докажите, что точки X, Y и Z лежат на одной прямой.')
        bot.send_message(message.chat.id,'4) всерос 2016 9.7  Неравнобедренный треугольник ABC, в котором ∠ACB = 60◦,вписан в окружность Ω. На биссектрисе угла BAC выбрана точка A0, а на биссектрисе угла ABC — точка B0 так, что AB0 k BC и BA0 k AC. Прямая A0B0 пересекает Ω в точках D и E. Докажите, что треугольник CDE равнобедренный.')
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        s1 = types.KeyboardButton('Показать решение задачи 1')
        s2 = types.KeyboardButton('Показать решение задачи 2')
        s3 = types.KeyboardButton('Показать решение задачи 3')
        s4 = types.KeyboardButton('Показать решение задачи 4')
        back = types.KeyboardButton('Вернуться в главное меню')
        markup4.add(s1, s2, s3, s4, back)
        bot.send_message(message.chat.id, 'Удачи!', reply_markup=markup4)

    if message.text == "Показать решение задачи 1":
            photo9 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph9.png', 'rb')
            bot.send_photo(message.chat.id, photo9)

    if message.text == "Показать решение задачи 2":
            photo10 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph10.png', 'rb')
            bot.send_photo(message.chat.id, photo10)
    if message.text == "Показать решение задачи 3":
            photo11 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph11.png', 'rb')
            bot.send_photo(message.chat.id, photo11)

    if message.text == "Показать решение задачи 4":
            photo12 = open('D:\КОСТЯ\УЧЁБА 239\Картинки к геометрии\ph12.png', 'rb')
            bot.send_photo(message.chat.id, photo12)


bot.polling(none_stop=True, interval=0)
