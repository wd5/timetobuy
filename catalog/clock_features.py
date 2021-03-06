    # -*- coding: utf-8 -*-

# Пол
GENGER_CHOICES = (
    (0, 'Мужской'),
    (1, 'Женский'),
    (2, 'Унисекс'),
)

# Механизм
MECHANISM_CHOICES = (
    (0, 'Кварцевые'),
    (1, 'Механические'),
    (2, 'Электронные'),
)

# Корпус
BODY_CHOICES = (
    (0, 'Нет данных'),
    (1, 'Вольфрамовый сплав'),
    (2, 'Горный хрусталь'),
    (3, 'Алюминий'),
    (4, 'Золото'),
    (5, 'Карбон'),
    (6, 'Керамика'),
    (7, 'Латунь'),
    (8, 'Медь'),
    (9, 'Нерж. cталь'),
    (10, 'Нерж. cталь + золото'),
    (11, 'Нерж. cталь + керамика'),
    (12, 'Нерж. cталь + пластик'),
    (13, 'Палладий'),
    (14, 'Пластик'),
    (15, 'Платина'),
    (16, 'Серебро'),
    (17, 'Титан'),
    (18, 'Цинково-алюминиевый сплав'),
)

# Браслет
BRACELET_CHOICES = (
    (0, 'Отсутствует'),
    (1, 'Золото'),
    (2, 'Каучук'),
    (3, 'Керамика'),
    (4, 'Кожа'),
    (5, 'Нерж. cталь'),
    (6, 'Нерж. cталь + золото'),
    (7, 'Нерж. cталь + керамика'),
    (8, 'Нерж. cталь + кожа'),
    (9, 'Нерж. cталь + пластик'),
    (10, 'Жемчуг'),
    (11, 'Пластик'),
    (12, 'Силикон'),
    (13, 'Текстиль'),
    (14, 'Титан'),
    (15, 'Платина'),
    (16, 'Серебро'),
    (17, 'Цинково-алюминиевый сплав'),
)

# Длина браслета
BRACELET_LENGTH_CHOICES = (
    (0, 'Нет данных'),
    (1, '17 см'),
    (2, '18 см'),
    (3, '19 см'),
    (4, '20 см'),
    (5, '21 см'),
    (6, '22 см'),
    (7, '23 см'),
    (8, '16 см'),
    (9, '15 см'),

)

# Стекло
WINDOW_CHOICES = (
    (0, 'Минеральное'),
    (1, 'Минеральное/сапфировое'),
    (2, 'Пластиковое'),
    (3, 'Сапфировое'),
)

# Водозащита
WATERPROOF_CHOICES = (
    (0, 'WR'),
    (1, 'WR20 (2 атм)'),
    (2, 'WR30 (3 атм)'),
    (3, 'WR50 (5 атм)'),
    (4, 'WR60 (6 атм)'),
    (5, 'WR100 (10 атм)'),
    (6, 'WR150 (15 атм)'),
    (7, 'WR200 (20 атм)'),
    (8, 'WR300 (30 атм)'),
    (9, 'WR330 (33 атм)'),
    (10, 'WR500 (50 атм)'),
    (11, 'WR600 (60 атм)'),
    (12, 'WR1000 (100 атм)'),
    (13, 'WR3000 (300 атм)'),
    (14, 'Нет'),
)

# Гарантия
GUARANTEE_CHOICES = (
    (0, '1 год'),
    (1, '2 года'),
    (2, '3 года'),
    (3, '4 года'),
    (4, '5 лет'),
    (5, '6 лет'),
    (6, '7 лет'),
    (7, '8 лет'),
    (8, '9 лет'),
    (9, '10 лет'),
    (10, 'Пожизненно'),
)

# Цвет ремня/браслета
COLOR_CHOICES = (
    (0, 'Нет данных'),
    (1, 'Бежевый'),
    (2, 'Белый'),
    (3, 'Желтый'),
    (4, 'Зеленый'),
    (5, 'Золотой'),
    (6, 'Комбинированный'),
    (7, 'Коричневый'),
    (8, 'Красный'),
    (9, 'Металлический'),
    (10, 'Оранжевый'),
    (11, 'Разноцветный'),
    (12, 'Серый'),
    (13, 'Синий'),
    (14, 'Стальной'),
    (15, 'Фиолетовый'),
    (16, 'Черный'),
)

# Индикация времени
TIME_INDICATION_CHOICES = (
    (0, 'Аналоговый (стрелки)'),
    (1, 'Аналоговый + цифровой'),
    (2, 'Цифровой (электронный)'),
    (3, 'Twelv'),
)

# Покрытие корпуса
COATED_HOUSING_CHOICES = (
    (0, 'Без покрытия'),
    (1, 'Позолота'),
    (2, 'Темное покрытие'),
    (3, 'Частичное покрытие'),
    (4, 'IPG'),
    (5, 'PVD'),
)

# Форма корпуса
CASE_FORM_CHOICES = (
    (0, 'Бочкообразная'),
    (1, 'Квадрат'),
    (2, 'Круг'),
    (3, 'Нестандартная'),
    (4, 'Овал'),
    (5, 'Прямоугольник'),
    (6, 'Ромб'),
    (7, 'Сердце'),
    (8, 'Трапеция'),
)

# Покрытие браслета
COATING_BRACELET_CHOICES = (
    (0, 'Без покрытия'),
    (1, 'Позолота'),
    (2, 'Темное покрытие'),
    (3, 'Частичное покрытие'),
)

# Цвет циферблата
DIAL_COLOR_CHOICES = (
    (0, 'Нет данных'),
    (1, 'Бежевый'),
    (2, 'Белый'),
    (3, 'Желтый'),
    (4, 'Зеленый'),
    (5, 'Золотой'),
    (6, 'Комбинированный'),
    (7, 'Коричневый'),
    (8, 'Красный'),
    (9, 'Металлический'),
    (10, 'Оранжевый'),
    (11, 'Разноцветный'),
    (12, 'Серый'),
    (13, 'Синий'),
    (14, 'Стальной'),
    (15, 'Фиолетовый'),
    (16, 'Черный'),
)

# Календарь
CALENDAR_CHOICES = (
    (0, 'Есть'),
    (1, 'Нет'),
    (2, 'Нет данных'),
)

# Хронограф
CHRONOGRAPH_CHOICES = (
    (0, 'Есть'),
    (1, 'Нет'),
    (2, 'Нет данных'),
)

# Тип застежки
TYPE_OF_LOCK_CHOICES = (
    (0, 'Ремешок'),
    (1, 'Браслет'),
)

# Питание
BATTERY_CHOICES = (
    (0, 'От батарейки'),
    (1, 'От солнечной батареи'),
    (2, 'От тепла руки'),
    (3, 'Пружинный механизм'),
    (4, 'Kinetic'),
)

# GPS
GPS_CHOICES = (
    (0, 'Есть'),
    (1, 'Нет'),
    (2, 'Нет данных'),
)

# Цифры
DIGIT_CHOICES = (
    (0, 'Арабские'),
    (1, 'Арабские+римские'),
    (2, 'Римские'),
    (3, 'Отсутствуют'),
)

# Формат
FORMAT_TIME_CHOICES = (
    (0, '12 часов'),
    (1, '12/24 часа'),
    (2, '24 часа'),
)

# Секундная стрелка
SECOND_ARROW_CHOICES = (
    (0, 'Отсутствует'),
    (1, 'Смещенная'),
    (2, 'Центральная'),
)

# Скелетон
SCELETON_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Противоударные
BOOM_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Автоподзавод
AUTO_BATTERY_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Антибликовое покрытие стекла
ANTI_REFLECTIVE_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Камень-вставка
STONE_CHOICES = (
    (0, 'Агат'),
    (1, 'Аметист'),
    (2, 'Бирюза'),
    (3, 'Бриллиант'),
    (4, 'Гранат'),
    (5, 'Жемчуг'),
    (6, 'Кристаллы swarovski'),
    (7, 'Оникс'),
    (8, 'Рубин'),
    (9, 'Сапфир'),
    (10, 'Топаз'),
    (11, 'Фианит'),
    (12, 'Хрусталь'),
    (13, 'Циркон'),
    (13, 'Отсутствует'),
)

# Точность хода
CLOCK_ACCURACY_CHOICES = (
    (0, '7 с/мес'),
    (1, '10 с/мес'),
    (2, '15 с/мес'),
    (3, '18 с/мес'),
    (4, '20 с/мес'),
    (5, '25 с/мес'),
    (6, '30 с/мес'),
    (7, '5 с/мес'),
    (8, '3 с/мес'),
    (9, '1 с/мес'),
)

# Будильник
ALARM_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Пульсометр
PULSE_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Подсветка дисплея
FLASH_LIGHT_DISPLAY_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Подсветка стрелок
FLASH_LIGHT_ARROW_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Второй часовой пояс
SECOND_TIME_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Записная книжка
NOTE_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Секундомер
SECOND_TIMER_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Компас
COMPASS_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Таймер обратного отсчета
TIMER_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Термометр
THERMOMETER_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Высотомер 
ALTIMETER_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Высотомер 
ALTIMETER_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Встроенная память
MEMORY_CHOICES = (
    (0, 'Да'),
    (1, 'Нет'),
)

# Вес часов
WEIGHT_CHOICES = (
    (0, 'Легкие'),
    (1, 'Средние'),
    (2, 'Тяжелые'),
)

# Размер часов
SIZE_CHOICES = (
    (0, 'Маленькие'),
    (1, 'Средние'),
    (2, 'Крупные'),
)