# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define n = Character('', color="#c8ffc8")
define I = Character('Илья', color="#c8ffc8")
define k = Character('Кашкин', color="#c8ffc8")
define c = Character('Местный житель', color="#c8ffc8")
define Door = Character('Голос из-за двери', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    play music "maintheme.mp3" volume 0.4
    scene bg tat

    

    show bg room
    I "Ну-с, попробуем"
    #*делает свои магические штуки, перемещается*
    scene bg bank
    n "(Евгений Кашкин был первым губернатором города)"
    k "Дамы и господа, уважаемые горожане и почтенные гости! "

    I "Где-то у меня был блокнот, это же такой материал!"

    k "Сегодня я с гордостью объявляю открытие нового губернского города - Перми...."

    I "Речь длилась около десяти минут, я старался ее дословно записать"

    k "На этой ноте я объявляю начало праздника в честь открытия города!"
    n "Ура!"
    I "Ух, вроде все успел записать"
    n "Илья поеживается"
    I "Мда, что-то я не подумал, сейчас же Октябрь!"
    I "А остаться хочется, интересно..."
    I "Пойду дальше, там должно найтись где погреться, там и людей поспрашиваю..."

    I "На набережной и правда оказались смоляные бочки для таких же замерзших как и я"

    c "Да-а-а, легковато ты оделся для такой погоды"
    I "И правда, не рассчитал, мне кстати интересно, что думают люди насчет открытия города, вот вы, например?"
    c "А ты кто такой, чтобы ходить, да расспрашивать?"
    I "Летописец я, хотя скорее его помощник"
    c "А-а-а, ну это дело хорошее, да"
    c "Ну, я, пожалуй, счастлив, праздник отличный, заняться есть чем"
    c "И сегодня он по-видимому заканчиваться не собирается...."
    
    I "Так я опросил еще несколько человек"
    I "А ближе к ночи повсюду зажглись фонари, их было великое множество, город засиял"
    I "А когда запустили фейерверки, тысячи ракет, осветилось еще и небо"

    I "Ладно, пора обратно, а то окончательно замерзну..."
    I "Тут я заметил знакомый силуэт, неужели это имя девушки, да ну, бред, может от недосыпа почудилось"

    #ГГ перемещается обратно и возвращается в комнату

    I "Я смотрю на исписанные страницы своего блокнота"
    I "моя курсовая будет действительно необычной"
    I "В ней будет отражено, в том числе, действительное отношение людей к событиям"
    I "Мне всегда было интересно именно это в истории."
    I "И что, такую возможность я буду использовать просто чтобы написать курсовую?"
    I "Это ведь великая сила, хотя повлиять на события я скорее всего не могу"
    I "в таком случае наблюдать и записывать - это, наверно, лучшее ее применение."
    I "Но на сегодня все, нужно поспать"
    I  "А то мерещится всякое"
    I "Но все-таки та девушка выглядела такой..."
    I "Настоящей...?"

    I "Продирая глаза я встаю. Здравствуй, новый день!"






    I "Итак, куда мне отправиться сегодня?"
    I "Возможно для более полной картины следует расспросить человека знающего?"
    I "Точно!"
    I "Историка, а лучше краеведа!"
    I "Так, кто там был здесь, в Перми?"
    I "М-м-м-м..."
    I "Может еще и с архитектурой связанное?"
    I "О, в  особняке Тупициных жил Шишонко"
    I "Краевед, описывал историю Перми, но дописать не успел"
    I "Может удастся выспросить, что-нибудь из ненаписанного..."
    I "Еще и фольклором занимался...."
    I "Х-м-м-м-м..."
    I "Решено! К Оперному!"

    I "Приезжает на место"
    I "Ну, вперед!"
    I "Перемещение"

    I "И вот я здесь!"
    I "Странно, вроде здание изначально задумывалось синим...."
    I "Так, где здесь вход"
    I "Спустя пару мгновений я обнаружил дверь и направился к ней"
    n "Тук-тук"

    Door "Кто там?"
    I "Черт, а что сказать я и не подумал."
    I "Я к Василию Никифоровичу, спросить насчет города."
    Door "Никого не ждем, катись отсюда"
    I "Но..."
    Door "Я сказал катись, а то за шкирку оттащу!"

    I "После такой угрозы я понял, что здесь мне ничего не светит и быстро отошел подальше"

    I "Что ж, обидно, ну хотя бы послоняюсь вокруг, как и хотел, архитектуру рассмотрю"
    I "Я шел по улице и оглядывался на здания вокруг меня"
    I "Никаких новостроек, никакой мерцающей рекламы, все относительно тихо и спокойно"
    I "Вокруг пробегает множество людей"
    I "Часть из них - чиновники, спешащие на службу, часть - курьеры, несущиеся с донесениями"
    I "Ну что ж, погуляли и хватит, нужно дальше путешествовать"
    I "Начинает творить колдунство"
    I "Тут я чувствую, что о мою ногу кто-то споткнулся"
    I "Черт!"
    G "ой!"
    I "Я подхватил какую-то даму."
    G "Ах, простите, я такая неловкая"
    I "Загляделась на что-то и, вот, уже у вас на рука…"
    I "Она начала пристально на меня глядеть, кажется, мы уже встречались…"
    I "Стоп…"
    I "Спасибо, что не дали мне упасть, до свидания!"
    I "Она начала поспешно удаляться"
    I "Я ее узнал, это же та девушка из библиотеки!"
    I "Постой!" 
    I "Погоди!"
#перемещенеие вреальность
    I "Все же не успел, хотя..."
    I "Точно!"
    I "Она же должна была переместится вместе со мной!"
    I "Оглядывается"
    I "Но почему-то ее здесь нет..."
    I "Что-то странное, пойду поразмыслю над этим у себя, в спокойной обстановке"


    return
