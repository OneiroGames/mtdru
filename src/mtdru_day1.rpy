########################################################
###       Copyright (c) 2020-2022 ONEIRO GAMES       ###
###                 Version: 1.0.0                   ###
###             Description: MTDRU DAY 1             ###
########################################################

label mtdru_day1:
    $ new_chapter(1, u"ДВНР\nДень 1")
    python:
        renpy.music.set_volume(0, 2.5)
        renpy.sound.set_volume(0, 2.5)
    
    $ renpy.pause(0.5, hard = True)    
    show text "{size=+50}День 1{/size}" at truecenter
    with dissolve
    $ renpy.pause(1.2, hard = True)
    hide text
    with dissolve

    play ambience sfx_bus_interior_moving fadein 2.5 loop

    python:
        renpy.music.set_volume(1, 2.5)
        renpy.sound.set_volume(1, 2.5)

    scene bg int_bus_people_night with dissolve
    
    window show dspr

    "Я растерянно плюхнулся в кресло, которое было ближе всего ко мне."
    "Рядом была девушка с рыжими волосами. Она смотрела в окно, где дождь лил как из ведра. Быстро сменялись пейзажи: то сосновый лес, то березы, а порывы ветра заставляли их шататься."
    "Удивительно, как природа передает моё настроение, полный хаос и никакого спокойствия..."
    th "Как так вышло? Почему я.. Выходит, я и правда умер? Но… в том мире?!"
    th "Если верить голосу, то да…"
    th "Я ничего не помню из своей старой жизни, и это угнетает, а ещё эта тень… Кто это был и что он имел ввиду? Какой автобус и… причем здесь была Соня?!"
    th "Бедная Соня… В последние мгновения жизни она посмотрела на меня. Эти глаза, мне так жаль… Я их не забуду…"
    th "Я пообещал, что любым способом спасу её. Надеюсь, голос не соврал, то я и правда могу сделать это здесь."
    th "Этот ублюдок… Если он мне попадется ещё раз, я… я не знаю, что я с ним сделаю."
    "Мои кулаки непроизвольно сжались."

    show dv shocked pioneer close at center with dspr

    stop music fadeout 1.0
    play music music_list["i_want_to_play"] fadein 3.0

    dvp "Ты это чего?"
    mtdru_kr "А? Да так, забей…"

    show dv normal pioneer close at center with dspr

    dv "Ну ладно… Меня Алиса зовут, а тебя? И ты новенький тут? Я тебя раньше не видела."
    th "Что? Новенький? Она тоже из другого мира?!"
    th "Нет, должно быть, она из этого. Надо постараться подыграть. Неизвестно, куда я приеду. Прости меня… Соня."
    mtdru_kr "Да, я новенький, меня зовут Кирилл."
    dv "Хах, классное имечко. Так и запомним, Кириешка. Ахахахахах."
    mtdru_kr "Хах, смешно придумала, раз тебе так будет удобно, то называть можешь и Кириешкой."
    dv "Ты наверно ненормальный."
    "Она протяжно зевнула."
    dv "Так, до лагеря ещё далеко и я бы предпочла поспать вместо того, чтобы чесать языком с тобой. Алибидерчи."

    hide dv normal pioneer close with dspr

    th "Странная она…"

    show sl smile pioneer close at center with dspr

    sl "Не обращай внимания, в дороге она всегда такая. Я тут случайно подслушала вас. Кирилл - хорошее имя, а меня зовут Славяна, но для друзей просто Славя."
    mtdru_kr "Приятно познакомиться! Так мы едем в лагерь? Никогда в них не бывал…"

    show sl shy pioneer close at center with dspr

    sl "Хе-е-е-й! Не упрощай так! Это меня обижает. Мы едем не абы куда, а в пионерлагерь «Совёнок»!"

    show sl smile pioneer close at center with dspr

    sl "Это самое лучшее место, и тебе повезло, что твой первый пионерский опыт пройдет именно здесь!"
    sl "Добрые вожатые, прекрасная природа и, ой… я немного увлеклась, прости."
    mtdru_kr "Да нет, чего ты. Все твои слова, тебе дорог этот лагерь?"
    sl "Да."
    mtdru_kr "Наверное, это значит, что и я в нём не разочаруюсь. Как я понял, ты здесь не первый раз."
    mtdru_kr "Если тебе не трудно, то не могла бы ты провести мне экскурсию?"
    sl "Да, с радостью. Правда, весь лагерь я тебе показать не смогу – у меня есть дела, да и тебе нужно где-нибудь поселиться."
    sl "Проведу тебя по основным местам."
    sl "Ах да, точно. Мы приедем – и сразу будет линейка. Там и расскажут, где мы будем жить. Я проведу тебя до площади."
    mtdru_kr "Спасибо. А сейчас, если ты, конечно, не против, я последую примеру Алисы."
    sl "Ничего. Мы еще не скоро приедем."

    stop music fadeout 2.5
    hide sl smile pioneer close with dspr
    # (Окно автобуса)

    th "Что же меня ждёт здесь… Я теперь не попаду обратно? Я не знаю, о чём думать… Столько мыслей."
    th "Почему именно я? И… какой сейчас год? И куда я еду? Пионерлагерь… Я едва познакомился с Алисой… Ну как познакомился, хотя бы имя узнал."
    th "А Славя кажется очень доброй и простой, я могу сделать смелое предположение, что она живет в какой-нибудь деревушке."
    th "Спасибо ей, не думаю, что та же Алиса согласилась бы показать мне лагерь. Ладно, нужно поспать, это всё так выматывает…"    

    window hide dspr

    stop ambience fadeout 3.0

    scene black with dissolve
    $ renpy.pause(0.5, hard = True)
    $ prolog_time()
    scene bg mtdru_rundown_alley_night with dissolve

    play music music_list["door_to_nightmare"] fadein 4.0

    window show dspr

    th "Где я? Не понимаю, эти кирпичные стены выглядят довольно знакомо."
    th "Я однозначно здесь был, но не помню этого. Нужно постараться… Точно. Это было в детстве. Здесь меня первый раз избили."
    th "Я не помню уже за какие заслуги, но в чём я и правда уверен, что я просто не сопротивлялся… Стоп, там ребенок? Его кто-то тащит. ОН ЕГО УДАРИЛ!"
    mtdru_kr "ТЫ, УБЛЮДОК, УБРАЛ ОТ НЕГО СВОИ РУКИ, А НЕ ТО…"

    show sd smile darkpi with dspr

    mtdru_shadow "А не то что?! Вспомни. Ты тогда даже пошевелиться не мог от страха. Ты мог спасти её, но ты слишком труслив."
    mtdru_shadow "Намочил штанишки и сидел тихо. Ахахахаха… жалкое зрелище."
    mtdru_kr "Нет… всё было не так. Ты… ты…"
    mtdru_shadow "Все вокруг виноваты, что ты стал таким, что ты всё потерял, что ты попал сюда."

    $ mtdru_AlleyTint = 0.9
    "Всё пространство вокруг начало темнеть. Я оставался с ним один на один."
    $ mtdru_AlleyTint = 0.8
    mtdru_kr "Что ты имеешь ввиду?! С чего бы мне тебе верить?"
    $ mtdru_AlleyTint = 0.7
    mtdru_shadow "Можешь и не верить."
    $ mtdru_AlleyTint = 0.6
    mtdru_kr "Я поверю в это тогда, когда ты будешь умирать!"
    $ mtdru_AlleyTint = 0.5
    mtdru_shadow "Смешно…"

    stop music fadeout 3.0

    window hide dspr

    hide sd smile darkpi close with dspr

    scene black with dissolve

    $ AlleyTint = 1.0

    show text "{size=+50}5 часов спустя...{/size}" at truecenter
    with dissolve
    $ renpy.pause(1.0, hard = True)
    hide text
    with dissolve

    scene bg int_bus_people_night with dissolve
    show mt normal panama pioneer far at center with dspr

    play ambience sfx_bus_interior_moving loop fadein 4.0
    play music music_list["i_want_to_play"] fadein 4.0

    $ night_time()

    window show dspr

    mtp "Так, дети, быстро выходим. Я понимаю: вы все устали и хотите отдохнуть, но водитель не будет ждать."

    hide mt normal panama pioneer far with dspr
    show dv grin pioneer close at center with dspr

    dv "Слушай, я, конечно, польщена, что тебе так нравится мое плечо, но… НЕ МОГ БЫ ТЫ С НЕГО НАХРЕН СВАЛИТЬ?!"
    th "Ой, я, кажется, навалился на неё."
    mtdru_kr "Блин, извини... Это... Спасибо, что разбудила..."

    show dv normal pioneer close at center with dspr

    dv "Не, ну точно отбитый. Иди уже, ты мешаешь мне выйти."
    mtdru_kr "Да, окей."

    show dv shocked pioneer close at center with dspr

    dv "Окей?"
    mtdru_kr "Окей?"
    "Переспросил я с недоумением."
    th "Она, что не знает, что такое окей? Не может быть такого."
    dv "Ты иностранец?"
    mtdru_kr "Нет, я местный. А вы из каких краёв?"
    dv "Из родных. Если местный, то что это такое твоё окей? Никогда о таком слове не слышала."
    mtdru_kr "Ну, «окей» значит «хорошо» или же «я тебя понял»."
    dv "А почему ты не говоришь хор…"
    mtdru_kr "Нас уже вожатая заждалась, просто прими это как факт. Хорошо?"

    show dv smile pioneer close at center with dspr

    dv "Окей!"

    window hide dspr

    stop ambience fadeout 0.5
    stop music fadeout 0.5

    hide dv smile pioneer wtih dspr
    scene bg mtdru_ext_bus_rain with dissolve

    play ambience ambience_cold_wind_loop fadein 3.0
    play sound sfx_thunder_rumble loop fadein 3.0
    play music music_list["silhouette_in_sunset"] fadein 3.0

    window show dspr

    "Мы вместе вышли из автобуса. Воздух был очень свежим и бодрящим, но на небе не хватало солнца."
    "Серые тучи затянули всё небо. Казалось, что в любой момент они могли расплакаться и снова окутать землю своими холодными слезами."

    "Небольшие лужи после дождя ранним утром появились на плитке, и я случайно наступил в одну."

    show sl smile pioneer close at left with dspr
    show dv normal pioneer close at right with dspr

    "Меня и Алису сразу встретила Славя, как она и обещала."
    sl "Ну вот вы где, я вас заждалась. Пойдемте скорее, Ольга Дмитриевна скоро начнет свою речь."
    dv "Аааааааа, опять эта нудятина. Можно не идти?"

    show sl angry pioneer close at left with dspr

    "Славя грозно посмотрела на Алису." # убрал 'очень' тк не нужно

    show dv guilty pioneer close at right with dspr

    dv "Ладно, пошли..."

    window hide dspr

    scene bg mtdru_ext_camp_entrance_rain with dissolve
    $ renpy.pause(0.5, hard = True)
    scene bg mtdru_ext_clubs_rain with dissolve
    $ renpy.pause(0.5, hard = True)
    scene bg mtdru_ext_square_rain_day with dissolve

    show sl normal pioneer close at center with dspr

    window show dspr

    mtdru_kr "Спасибо. Славь, очень выручила."

    sl "Да не за что."

    show sl smile pioneer close at center with dspr

    "Она улыбнулась."

    stop music fadeout 5.0

    window hide dspr

    hide sl smile pioneer close with dspr
    show cg mtdru_day1_square_mt with dissolve
    # TODO
    
    window show dspr

    "Спустя пять минут ходьбы мы пришли на площадь. Наш отряд стоял почти в центре."

    mt "Здравствуйте, ребята! Вот и начался новый год, вот и началось новое лето, вот и началась наша первая смена."
    mt "Мне очень радостно, что в наш лагерь приехало столько ребят. И приехали не только те, кто уже был здесь, а еще и много новеньких."
    mt "Этот лагерь, это маленькое, совершенно новое приключение для вас и для нас."
    mt "Надеюсь, ваша первая смена вас не разочарует, а мы, вожатые, поможем вам сохранить о лагере теплые и хорошие воспоминания."
    mt "И, надеюсь, это лето запомнится вам навечно. Ура!"

    window hide dspr

    $ day_time()
    $ persistent.sprite_time = "day"

    stop ambience fadeout 0.5
    stop sound fadeout 0.5

    scene bg ext_square_day with dissolve

    play ambience ambience_ext_road_day fadein 3.0

    window show dspr

    "Все пионеры захлопали, кто-то даже присвистнул и приободряюще что-то выкрикнул с места."
    th "Да уж, эта женщина умеет вдохновлять. Надеюсь, и у меня все здесь сложится…"

    "Ольга Дмитриевна подошла к нашему отряду, начала знакомство и распределение по домикам."

    show mt smile panama pioneer at center with dspr
    # show dv normal pioneer far at right with dspr

    mt "Ещё раз привет. Скучали? Я снова буду вашей вожатой. Ура?"
    "Весь отряд прокричал «Ура!»"

    show mt normal panama pioneer at center with dspr

    mt "Так, у нас здесь есть пара новеньких. Знакомьтесь: это Кирилл, а вот это Соня."
    show sn normal dress close at left
    th "Она сказала Соня? Такие же голубые глаза, цвет волос…"

    show mt grin pioneer at center with dspr

    mt "Вы их сильно не обижайте!"
    "Она подмигнула и коротко улыбнулась."

    show mt normal panama pioneer at center with dspr

    mt "Покажите им лагерь, да вы всё и сами знаете."
    all "Да!"

    show mt smile panama pioneer at center with dspr

    mt "Ай какие умницы!"

    show mt normal panama pioneer at center with dspr

    mt "Так, теперь нужно вас поселить. Лена живёт вместе с Мику, Алиса с Ульянкой, только не сильно шалите, а то мне опять нагоняй даст начальство, Славяна с Женей…"
    mt "Шурик и Сергей, ваш домик недалеко от клубов. Кирилл и Соня, остались только вы. Мне придётся временно поселить вас вместе."

    stop music fadeout 0.5
    play music music_list["you_lost_me"] fadein 4.0

    mtdru_kr "Что?! Как это вместе?!"

    show mt normal pioneer at right with dspr
    show sn offended dress close at left with dspr

    mtdru_sn "Да, как так-то! Ольга Дмитриевна, это как бы…"
    mt "Знаю сама. Но по отдельности вас поселить не могу. Смена длится две недели."
    mt "Так что постарайтесь потерпеть друг друга, я уверена, что вы даже сможете найти общий язык. И еще через неделю приедут 2 пионера."
    mt "И если вы не приживетесь, то так уж и быть, расселю."
    
    hide mt grin pioneer with dspr
    show sn offended dress close at center with dspr
    
    stop music fadeout 0.5    
    play music music_list["timid_girl"] fadein 4.0

    mtdru_kr "Не самая лучшая перспектива, но ладно. Тут уже ничего не поделаешь. Слушай, может тебе помочь сумки донести?"
    mtdru_sn "Что? Хах. Нет."
    mtdru_kr "Но у тебя их так много, не уверен, что ты одна справишься."
    mtdru_sn "До этого справилась, вот и сейчас справлюсь."
    mtdru_kr "Может все же помочь?"
    mtdru_sn "Вот вместо того, чтобы языком чесать, сказал бы, где нас поселили."
    mtdru_kr "Ах да. Нас поселили в крайний домик у пляжа. Мне Ольга примерно рассказала маршрут, думаю, мы найдем дороге."
    mtdru_sn "Ну ты и дурак, думает он. Если мы будем блуждать по лагерю и так и не найдем жилье, весь остаток дня ты будешь таскать меня на спине. Давай, веди, Сусанин."

    stop ambience fadeout 0.5
    scene bg int_house_of_un_day with dissolve
    play ambience ambience_int_cabin_day fadein 3.0

    "Буквально через 10 минут мы уже были в домике и там стали располагаться." # разве не в домике?
    "Я занял кровать слева и спрятал все свои принадлежности, которые оказались в сумке. Интересно, откуда она взялась?"
    mtdru_kr "Хуууух. Вроде бы все, тебе помочь?"
    mtdru_sn "Сама как-нибудь."
    mtdru_kr "Сама да сама, ладно. Может, сходим лагерь разведаем?" 

    mtdru_sn "Хорошая идея, иди разведай. Мне еще нужно кое-что сделать. Думаю, я потом присоединюсь."
    mtdru_kr "Ну, как знаешь. Я ушел."

    stop ambience fadeout 0.5
    scene bg ext_house_of_un_day with dissolve
    play ambience ambience_ext_road_day fadein 5.0
    play sound sfx_open_door_1

    "На улице поддувал холодный ветерок, который иногда пробирал до мурашек."
    "Было еще довольно пасмурно, поэтому все выглядело серым и пустым без яркого солнца."
    
    scene bg ext_houses_day with dissolve

    "В лагере было тихо: наверное, все занимались делами в своих домиках. Эту тишину нарушал только шум деревьев, шум листвы и травы от ветра. Я, поглядывая под ноги, неторопливо шел."
    "Все дорожки были из плитки, которая даже не потрескалась. Она выглядела довольно новой, хотя между отдельным плитками иногда пробивалась трава."
    "Я добрался до домика, у которого росла пышная сирень. Из него вышли Славяна и Ольга Дмитриевна."

    window hide dspr

    scene bg ext_house_of_mt_day with dissolve
    show sl normal pioneer at right with dspr
    show mt normal pioneer at center with dspr

    window show dspr

    stop music fadeout 0.5

    sl "О, Кирилл! Ты уже тут, это хорошо."
    mt "Да, это очень даже хорошо."
    mt "Сейчас Славя тебя проводит в кладовую и выдаст комплект формы для тебя и твоей соседки. Выдаем по 2 комплекта." # 'Выдаем по 2 комплекта.' лучше убрать
    mt "А теперь, Славяна, ты за главную, мне нужно бежать к начальству."

    hide mt normal pioneer with dspr
    show sl normal pioneer at center with dspr

    sl "Хорошо, ну что, Кирилл, пошли?"
    mtdru_kr "Да, пошли."

    hide sl normal pioneer with dspr

    scene bg ext_houses_day with dissolve

    mtdru_kr "А почему Ольга тебе поручает такие задания? Ты же вроде отдыхающая."

    show sl normal pioneer at center with dspr

    sl "О, ты тоже заметил. На самом деле, мне просто нравится вот такая возня, да и вожатой полегче. Чувствую себя взрослой и ответственной."
    mtdru_kr "Ну если нравится. А ты сама откуда? Я, например, из Тулы, вернее, из Тульской области."
    sl "Ого, ну я подальше от тебя на пару сотен километров. Я из Украины. Но недавно переехали с родителями, но еще не знаю, надолго мы так."
    mtdru_kr "Понятно."

    hide sl normal pioneer with dspr

    "Весь остальной путь мы прошли в тишине. Оказалось, что склад был на другом конце лагеря. Славя достала форму для меня и Сони, погладила ее и отдала мне."

    scene bg mtdru_storage_day with dissolve
    
    mtdru_kr "Спасибо, но как-то даже неудобно."
    
    show sl normal pioneer close at center with dspr

    sl "Чего неудобно-то?"
    mtdru_kr "Ну вроде не маленький, мог и сам форму погладить."

    show sl smile pioneer close at center with dspr

    sl "Ага, знаю я вас, мальчишек."
    
    show sl normal pioneer close at center with dspr

    sl "Сейчас бы форма была вся мятая, а может и с дырками. А что тебе-то, тебе нормально, а Соне? Так, что бери форму и неси к себе."
    sl "Кстати, обед будет через полчаса – советую не опаздывать. После обеда Ольга Дмитриевна выдаст тебе обходной лист."
    mtdru_kr "Обходной? Зачем?"
    sl "Ну как же, каждый пионер должен быть чем-то занят. Ты сюда не развлекаться приехал, а развиваться, только в несколько расслабляющей атмосфере."
    mtdru_kr "Даже так… Надеюсь, с обходником не я один возиться буду."
    sl "Конечно не один, все новички будут. А те, кто уже здесь не первый раз, просто пойдут в клубы, в которых были до этого. Вряд ли за год у кого-то поменялись интересы."
    mtdru_kr "Понятно, еще раз спасибо. Я пойду обрадую Соню новым комплектом одежды, вы же, девочки, любите обновки? Я же прав?"
    sl "Да, ты прав."

    show sl smile pioneer close at center with dspr

    "Она хитро посмотрела на меня и улыбнулась."

    mtdru_kr "О чем ты подумала? Славя! Я не это имел ввиду."

    show sl laugh pioneer close at center with dspr

    sl "Иди уже, романтик."
    "Она громко засмеялась."

    hide sl laugh pioneer close with dspr

    th "Что я сказал, блин. Я же здесь не за этим. Надо просто быть повнимательнее."
    "От склада до моего домика было недалеко, я старался идти быстрее, как вдруг…"

    window hide dspr

    play sound ambience_lake_shore_day fadein 5.0
    play music music_list["i_want_to_play"] fadein 5.0

    scene bg ext_beach_day with dissolve
    show us smile pioneer far at center with dspr
    show un normal pioneer far at left with dspr

    window show dspr

    unp "Ульяна, если ты еще раз меня напугаешь, я все Ольге Дмитриевне расскажу!"
    us "Бе-бе-бе, ябеда-корябеда. {w}Оооооооо,{w} ЛЕНА!"
    un "Чего тебе? Если это снова жук, то тебе точно не поздоровится!"

    show us cry pioneer far at center with dspr

    us "Ну почему ты меня, Леночка, не любишь. Я к тебе со всей душой и сердцем. Ты обижаешь мои чувства."
    th "А эта Ульянка актриса та еще. Ого, она даже слезу пустила! Интересно, что будет дальше?"

    show un sad pioneer far at left with dspr

    un "Ох, Ульяночка. Прости, наверное, я переборщила. Просто ты всегда меня пугаешь. Давай мириться? Что ты там хотела показать?"
    
    show us smile pioneer far at center with dspr

    us "Давай! Так, только закрой глаза и вытяни губы."
    un "Вот так?"
    us "Ага."

    hide un sad pioneer far
    hide us smile pioneer far

    show cg mtdru_day1_un_us_cat with dissolve

    "В тот же момент Ульяна схватила мирно лежащего под кустами кота и поднесла к губам Лены."
    un "Ульяна!!!"
    us "Ахахахахаха, как тебе? Понравилось?{w} Отличная шутка, ты не обижайся только. Я ушла."

    scene bg ext_beach_day with dissolve
    
    show un normal pioneer far at center with dspr

    "Ульяна ушла в сторону столовой с довольной моськой, а Лена, кажется, была не очень-то довольна ее выходкой."

    stop music fadeout 5.0

    show un normal pioneer at center with dspr

    mtdru_kr "Привет, тебя же Лена зовут? Я тут случайно подсмотрел и… ну… это у вас так часто?"
    un "Ох эта Ульянка… Ой… п-привет… Ты новенький?"
    mtdru_kr "Да, меня Кирилл зовут, ну так?"
    un "Да, Ульянка часто подшучивает надо мной, иногда она перебарщивает… Я понимаю, что она маленькая, такие шалости — это нормально для нее, но от этого мне не становится менее обидно."
    mtdru_kr "Понимаю… Слушай, а я помочь с этим никак не смогу? Ну, допустим, поговорить с ней или что-то еще?"

    show un smile pioneer at center with dspr

    un "На самом деле это бесполезно, но спасибо."
    mtdru_kr "Ну я попытаюсь хоть что-нибудь сделать. Мне пора, рад знакомству!"
    un "И я."

    window hide

    stop ambience fadeout 0.5

    hide un smile pioneer with dspr
    scene bg ext_house_of_un_day with dissolve

    play ambience ambience_camp_center_day fadein 3.0

    window show dspr

    "До домика я добрался быстро – он был буквально в двух шагах. Странно, что Соня не слышала разговоры девочек, иначе она точно вышла бы."

    stop sound fadeout 0.5
    stop ambience fadeout 0.5

    window hide dspr

    play sound sfx_open_door_1
    scene bg int_house_of_un_day with dissolve
    show sn normal dress close at center with dspr
    play ambience ambience_int_cabin_day fadein 3.0
    play music music_list["eat_some_trouble"] fadein 5.0

    window show dspr

    mtdru_kr "Привет пионерам."
    mtdru_sn "Снова ты?"
    mtdru_kr "Не снова, а опять. Нам вместе жить, привыкай. А лучше смотри, что я тебе принес."
    "Я протянул ей ее форму."
    mtdru_sn "Спасибо, а где ты её?.."
    mtdru_kr "Где я ее достал? Ну, меня Славя проводила до склада, там и взял. Вот зря ты не пошла."
    mtdru_sn "Ну да, конечно."
    mtdru_kr "Так, давай переодеваться, скоро обед."
    "Я машинально начал переодеваться и уже снял брюки."

    show sn fears dress close at center with dspr

    mtdru_sn "Кхм! Кирилл!"
    mtdru_kr "Что?"
    mtdru_sn "У тебя случаем нет лишней хромосомы? Мог бы хотя бы попросить отвернуться!"
    mtdru_sn "Я, конечно, понимаю, мы соседи и т.п. но вот так… это наглость!"
    mtdru_sn "И что это за предложение, давай переодеваться?! Я не стану переодеваться вместе с тобой! Извращенец!"
    mtdru_kr "Я об этом не подумал, прости. Тогда отвернешься?"
    mtdru_kr "А когда тебе нужно будет переодеться, то я выйду из домика, хорошо?"
    mtdru_sn "Так бы сразу."

    stop ambience fadeout 0.5
    play sound sfx_open_door_1
    scene bg ext_house_of_un_day with dissolve
    play ambience ambience_ext_road_day fadein 5.0

    "Через минуту я уже был готов и уже вышел из домика."
    mtdru_kr "Сонь, скоро обед. Так что поторопись."
    mtdru_sn "Хорошо."

    stop music fadeout 5.0

    play sound sfx_dinner_horn_processed

    "Под звуки горна я почти собрался пойти на обед, но все же решил подождать Соню."

    show sn normal pi close at center with dspr

    mtdru_sn "О, как мило, ты решил меня подождать? Думаешь, из-за этого мое отношение к тебе изменится?"
    mtdru_kr "Мммм? Нет. Это всего лишь ради приличия, да и ты не знаешь, где находится столовая, так что, думаю, ответ сам всплыл."
    mtdru_sn "Хм, я тебе поверю, но не думай…"
    mtdru_kr "Почему ты галстук не завязала?"
    mtdru_sn "Я не… кхм… я не…"
    mtdru_kr "Ты не умеешь? А почему меня не попросила?"
    mtdru_sn "Не хочу оставаться в долгу, особенно у такого извращенца, как ты…"
    mtdru_kr "И еще кто-то не давно говорил про лишнюю хромосому. Ты не будешь мне должна, но галстук я тебе все равно завяжу."

    window hide dspr
    hide sn normal pi close with dspr

    hide sn normal pi close with dspr
    show cg mtdru_day1_tie with dissolve:
        zoom 1.0
        xalign 0.5

    window show dspr

    "Я приблизился к ней и начал завязывать галстук. Было немного непривычно: обычно я никому не завязывал, только себе."
    "Только после того, как я завязал галстук, я увидел покрасневшую Соню и понял, что наши лица были очень близко."

    window hide dspr

    scene bg ext_house_of_un_day with dissolve
    show sn fears pi close at center with dspr

    window show dspr

    mtdru_kr "Ну… эм… вот. Готово, ты это, обращайся."
    mtdru_sn "Да… хорошо. Давай пойдем уже?"
    mtdru_kr "Да, а то мы в первый же день опоздаем на важнейшее мероприятие."

    hide sn fears pi close with dspr

    scene bg ext_houses_day with dissolve
    show sn normal pi close at center with dspr

    "Пока мы шли к столовой, к нам присоединилась девочка. Она была очень бодрой и энергичной."

    show sn normal pi close at right with dspr
    show mi smile pioneer close at left with dspr

    mi "Привеееет, хух. Я Мику!"
    $ Character(u"Соня и Кирилл")("Привет.")
    mi "Вы тоже опаздываете? Я вот в музыкальном клубе засиделась."
    mi "Кстати, не хотите вступить? Даже если не умеете, я могу вас научить играть на любооооом инструменте. Или же клуб кинолюбителей? Я веду его вместе с клубом кибернетики. Вооот."
    mi "Что-то заговорилась, а как вас зовут?"
    mtdru_kr "Я Кирилл, а это Соня. Рады знакомству. Я подумаю по поводу клубов."
    mtdru_sn "Я тоже. Слушай, а что вы делаете в клубе киноискусства?"
    mi "Ох. Я рада, что заинтересовала, но я расскажу об этом попозже. И вот мы и пришли." # 'И вот мы и пришли.' поправь нормальна блять

    window hide dspr

    stop ambience fadeout 0.5
    hide sn normal pi close with dspr
    hide mi smile pioneer close with dspr
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 6.0

    window show dspr

    "За разговором дорога пролетела незаметно. Войдя в столовую, я увидел чистейшее помещение, наполненное не только пионерами, но и еще вкуснейшим запахом еды."
    "После того, как отстоял небольшую очередь, я взял свой обед и сел к окну за столик, где никого не было."
    th "Здесь неплохо кормят. Хах. Никогда так вкусно не ел, наверное… Амнезия – это ужасная штука, не пожелал бы даже врагу. Не знать кто ты… это страшно."
    th "Почему же меня отправили сюда? Как я здесь спасу и себя, и Соню? И почему Соня из этого мира так похожа на мою Соню? Так много вопросов и так мало ответов. Точнее… их вообще нет."
    th "Ну, если подумать, не так уж все плохо. По крайней мере, сегодняшний день пока идет вполне неплохо. Борщец вкусный, даже очень. Нужно отнести посуду и сходить к Ольге Дмитриевне."
    mtdru_kr "Спасибо, было очень вкусно."

    show nt smile close at center with dspr

    $ Character(u"Повариха")("Ну не льсти. Это моя работа. На улице, кажется, тебя Ольга ждет.")
    mtdru_kr "Тогда я пойду, до свидания."

    window hide dspr

    stop ambience fadeout 0.5
    hide nt smile close with dspr
    scene bg ext_dining_hall_away_day with dissolve
    show mt normal pioneer close at center with dspr

    window show dspr

    "Как только я вышел из столовой, меня сразу встретила Ольга Дмитриевна."

    play music music_list["two_glasses_of_melancholy"] fadein 3.0

    mt "Так, Кирилл, отлично. Вот, держи."
    "Она протянула мне какую-то бумажку."
    mtdru_kr "Что это?"
    mt "Это обходной лист. Тебе нужно сбегать и отметиться в клубах, а также у нашего врача. Сам сможешь?"

    show mt smile pioneer close at center with dspr

    mtdru_kr "Хм, думаю, это не так сложно… Я справлюсь."
    "Ольга сделала одобрительный жест, и я пошел в сторону клубов."

    stop music fadeout 5.0

    window hide dspr

    hide mt smile pioneer close with dspr
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 5.0

    window show dspr

    mtdru_kr "Так... и куда дальше?"
    "Я стоял посреди площади, от которой шли несколько дорог в разные стороны."
    "Недалеко на одной из лавочек сидела Лена и читала книгу. Я решил подойти к ней и попросить помощи."

    show un normal pioneer at center with dspr

    mtdru_kr "Ха, еще раз привет."
    "Лена посмотрела на меня большими, удивленными глазами."

    show un shy pioneer at center with dspr

    "Кажется, я ее смутил."
    un "Привет."
    mtdru_kr "Прости, если отвлекаю. Но не могла бы мне показать дорогу к клубам? У меня обходной, а я даже и не знаю куда идти."

    show un normal pioneer at center with dspr

    un "Я, наверное, смогу тебе показать, пошли."
    mtdru_kr "Спасибо, Ленчик!"

    scene bg ext_houses_day with dissolve

    "Эта фраза ее больше смутила. Мы шли по одной из дорожек: вокруг стояли пионерские домики в невысоких деревьях и цветах."
    "Под окнами одного из домиков росла пышная сирень, и я подумал, что в этом домике очень здорово, когда она цветет."
    "Иногда на территории, ближе к лесу, встречались сосны, поэтому дышалось здесь легко и спокойно. Шли мы в тишине, и я решил ее нарушить."
    mtdru_kr "Лен, тебе нравится книга, которую ты читаешь?"

    show un normal pioneer close at center with dspr

    un "Ага."
    mtdru_kr "А как она называется?"
    un "Унесенные ветром. Она мне очень-очень нравится. Но я читаю не только ее, а еще и море других книг… тебе интересно?"
    "Тихо спросила Лена."
    mtdru_kr "Мне? Я хоть и в литературе не слишком силен, но почитать тоже люблю. Можешь продолжать."
    "Мы шли, болтая о книгах. Мы перебрасывались с одной на другую, с жанра на жанр. Иногда наши мысли сходились, иногда - наоборот."
    "Я подумал, что мне могло быть интересно в клубе книголюбов, но пока не мог решить точно."
    "Неожиданно наш разговор прервала Соня."

    show un normal pioneer close at right with dspr
    show sn normal pi close at left with dspr

    mtdru_sn "Ох, еле вас догнала. Вы в клубы идете? Можно я с вами? А то я дороги не знаю..."
    "Она была вся красная, тяжело дышала и между каждым словом жадно вдыхала воздух. Сразу видно, что бег — это не ее конек."
    un "Да, конечно. Мы как раз уже подходим к клубу кибернетики."

    scene bg ext_clubs_day with dissolve

    "Мы подошли к вытянутому домику. Ступеньки были деревянные и слегка прогнившие. Я понял, что с началом смены здесь еще не успели убраться и привести клуб в надлежащий вид."

    window hide dspr

    stop ambience fadeout 0.5
    play sound sfx_open_door_1
    scene bg int_clubs_male_day with dissolve
    play ambience ambience_clubs_inside_day fadein 5.0

    window show dspr

    "За дверью нас встретила огромная куча пыли, которая вылетела на свободу. Сразу же после нее присоединились и члены этого клуба."
    
    play music music_list["went_fishing_caught_a_girl"] fadein 5.0

    show sh normal pioneer at center with dspr
    
    shp "Лена? Ребята? Что вы тут делаете?"

    show sh normal pioneer at right with dspr
    show el normal pioneer at left with dspr

    elp "Сань, где твои манеры? Приветствую в храме будущего, в храме современной кибернетики."
    el "Мое имя Сергей, но друзья зовут Электроником. А это мой товарищ по роду деятельности и очень хороший друг, Александр."
    sh "Привет. Извиняйте, что встретили не при параде, но как уж вышло."
    "Он протянул мне руку."
    mtdru_kr "Рад знакомству, я Кирилл."
    sh "Слыхали и даже видали… мммммм… вспомнил! На линейке виделись, но правда не познакомились, мы, кстати, в одном отряде. Так что видеться будем часто."
    mtdru_sn "Ну, а меня Соней звать. Мы чего пришли-то, нам бы обходной."
    el "Сейчас все организуем, а вы записаться не хотите?"
    "Я и Соня посмотрели друг на друга, посмеялись, наверное, и я и она представили, как бы это забавно выглядело, и сказали."
    $ Character(u"Соня и Кирилл")("Неее...")
    mtdru_kr "Это дело увлекательное, но…"
    mtdru_sn "Мы уже присмотрели себе клуб."
    mtdru_kr "Дааааа, наверное, только в один клуб можно записаться, но если вам понадобится помощь, то вы обращайтесь."
    sh "Ну, что ж, силком вас не затащим…"
    mtdru_kr "Ну мы пойдем дальше, хе-хе."
    $ Character(u"Соня и Лена")("Пока мальчики.")

    stop music fadeout 5.0

    window hide dspr

    stop ambience fadeout 0.5
    hide sh normal pioneer with dspr
    hide el normal pioneer with dspr
    play sound sfx_open_door_1
    scene bg ext_clubs_day with dissolve
    show un normal pioneer close at left with dspr
    show sn normal pi close at right with dspr
    play ambience ambience_camp_center_day fadein 5.0

    window show dspr

    un "Так, клуб кибернетики я вам показала. Тут недалеко, дальше по этой дорожке, будет муз кружок. Вы сами доберетесь?"
    mtdru_sn "Да, спасибо, Леночка. Слушай, а клуб кинолюбителей где?"
    mtdru_kr "Кстати да, в нем, я думаю, тоже нужно отметиться."
    un "Не беспокойтесь. Клуб кинолюбов в том же здании, что и муз кружок."
    mtdru_kr "Понятно, спасибо."
    un "Рада помочь."

    show un shy pioneer close at left with dspr

    "Она неловко улыбнулась и покраснела, быстро развернулась и ушла в сторону площади."

    hide un shy pioneer close with dspr
    show sn normal pi close at center with dspr

    mtdru_sn "Кирилл."
    mtdru_kr "Ммммм?"
    mtdru_sn "Подойди ближе, сейчас расскажу мысль."

    show sn normal pi close at center with dspr:
        zoom 1.15
    
    mtdru_kr "Чего? Зач… ай ладно. Что такое?"
    mtdru_sn "Мне кажется или Лена… кхм…"
    mtdru_kr "А? Что с ней?"
    mtdru_sn "Вот, все сходится." # Лена - вскрывашка
    mtdru_kr "Да что блин сходится?"

    show sn embarrassed pi close at center with dspr

    mtdru_sn "Лена в тебя впендехалась, а ты в нее!" # Соня еще не знает что ГГ ебал Лену :D
    "Прокричала она и рассмеялась."
    mtdru_kr "Что?! Глупости! Она, конечно, симпатичная, но…"

    show sn normal pi close at center with dspr

    mtdru_sn "Вот видишь, ты уже считаешь ее симпатичной, а за остальным и бежать не надо, со временем само придет."
    mtdru_kr "Глупости не говори. Странная ты. Пошли уже лучше к клубу."

    hide sn normal pi close with dspr
    scene bg ext_musclub_day with dissolve

    "Всю дорогу Соня доставала меня своей глупой мыслью и пыталась это обсудить."

    show sn normal pi close at center with dspr

    mtdru_sn "Ну согласись. Вы идеальная пара. Тихоня, а, как известно, в тихом омуте черти водятся, и озабоченный. Чем не пара."
    mtdru_kr "Да кто тут из нас озабоченный. Только об этом и твердишь."
    mtdru_sn "Ну одно же дело просто говорить, а другое делать."
    mtdru_kr "Так блин, это было с непривычки, и я уже извинился."
    mtdru_sn "Да-да. Болтай больше."
    mtdru_kr "Как же хорошо, что мы уже пришли. Ну, заходим?"

    window hide dspr

    stop ambience fadeout 0.5
    hide sn normal pi close with dspr
    play sound sfx_open_door_1
    scene bg int_musclub_day with dissolve
    show sn normal pi close at center with dspr
    play ambience ambience_music_club_day fadein 6.0

    window show dspr

    "Соня спокойно влетела в дверь и заорала на все помещение."
    mtdru_sn "ТЫСЯЧА ЧЕРТЕЙ, СУДАРИ И СУДАРЫНИ, ЧТО Я ЗДЕСЬ ВИЖУ… ой…" # СЛАВА УКРАИНЕ (И АЛЕНЕ)

    show sn normal pi close at left with dspr
    show mi sad pioneer close at right with dspr

    "В клубе была только одна Мику. Она со скучающим видом сидела на диванчике и задумчиво смотрела куда-то далеко."
    mtdru_kr "Ты, блин, в своем уме?! А если бы ты сорвала репетицию? Привет, Мику, мы тебе не помешали?"
    mi "Привет, ребята."
    "В ее словах не слышался энтузиазм, как во время похода в столовую. Мне показалось, что ей грустно, просто она не хочет этого показывать."
    mtdru_sn "Мику, что такое? Кто-то обидел?"
    mtdru_kr "Если что, мы можем помочь, только скажи!"
    mi "Спасибо ребята, но не стоит."
    mtdru_sn "Ну как это не стоит. Ты же наша подруга. Давай, рассказывай. На кого Кирилла натравить?"
    mtdru_kr "А? Ты чего?!"

    show mi laugh pioneer close at right with dspr
    pause 0.5
    show mi sad pioneer close at right with dspr

    mi "Ха-ха. Вы такие смешные. Не надо Кирилла ни на кого натравливать. Просто… я веду два клуба и ни в один из них никто не записался…"
    mi "А сюда приходили люди не только из нашего отряда, но и из других. Это… это просто очень обидно. Вроде и рада всем, и могу научить игре на разных инструментах, да и вообще."
    "Едва заметная слеза покатилась по ее щеке, но Мику тут же ее смахнула."
    mtdru_kr "Стоп, стоп, стоп. Плакать тебе-то кто разрешал? Ну же, успокаивайся. Я и Соня хотели вступить в кружок кинолюбителей. Правда ведь?!"
    mtdru_sn "Да, Микунь. Вытирай слезы и запиши нас. А мы в свою очередь подумаем, как завлечь сюда еще больше людей."
    mi "Но зачем вам это? Если из жалости ко мне, то не надо…"
    mtdru_kr "Нет. Мы делаем это потому, что хотим этого. Так что вставай и заканчивай плакать. Вздохни полной грудью и направляйся к своему будущему." # вздохни полной грудью и осознай что все пошло по пизде
    mtdru_sn "Микусь, видала, какую речь тебе выдал Кирилл? Успокаивайся потихоньку, ты не одна!"
    mi "Спасибо вам. Тогда, наверное, мне нужно что-то придумать, что может привлечь побольше людей? Может, музыкальный конкурс?"
    mtdru_sn "Вряд ли. Не знаю, как остальные, но вот я не умею играть ни на одном инструменте. Может какая-нибудь сценка?"
    mi "Сценка? Но ведь мы этим не занимаемся…"
    mtdru_kr "Что вы голову ломаете. Микусь, какие клубы ты держишь?"
    mi "Музыкальный и кино…"

    show mi smile pioneer close at right with dspr

    mi "ТОЧНО! Кирилл, ты гений!"

    hide mi smile pioneer close with dspr
    hide sn normal pi close with dspr

    "Мику запрыгнула на стул и громко прокричала."

    show mi smile pioneer close at center with dspr

    mi "Да будет кино!"
    mtdru_kr "Я думаю, нужно как-то проинформировать других ребят?"

    show mi smile pioneer close at right with dspr
    show sn normal pi close at left with dspr

    mtdru_sn "Не слишком уж торопитесь? Первый день все-таки."
    mtdru_kr "Да, ты права. Завтра можно будет начать, если Ольга не запряжет."

    show mi laugh pioneer close at right with dspr
    show sn embarrassed pi close at left with dspr
    pause 0.4
    show mi normal pioneer close at right with dspr
    show sn normal pi close at left with dspr    

    "Мы все вместе посмеялись. Девочки заметно повеселели, и атмосфера стала приятной."
    mtdru_kr "А сейчас мы тебя покинем: нам нужно еще в библиотеку забежать и в медпункт."
    mi "Давайте, ребята, на ужине увидимся."
    $ Character(u"Соня и Кирилл")("Пока!")

    window hide dspr

    stop ambience fadeout 0.5
    play sound sfx_open_door_1
    scene bg ext_musclub_day with dissolve
    show sn normal pi close at center with dspr
    play ambience ambience_camp_center_day fadein 5.0

    window show dspr

    mtdru_sn "Кирилл, а у меня тут такой вопрос…"
    mtdru_kr "Да?"
    mtdru_sn "Куда мы сейчас идем? Я бы забежала в медпункт по-быстрому, а потом уже и в библиотеку."
    mtdru_kr "Я бы, наверное, сначала в библиотеку сходил бы. Может разделимся? В крайнем случае если потеряемся – встретимся у Генды."
    mtdru_sn "Ты, наверное, мои мысли читаешь, бывай."

    hide sn normal pi close with dspr

    "В тот же момент Соня убежала."
    th "Да уж… Моя компания настолько ей противна? Да и о чем я. Не об этом надо думать. Надеюсь, хоть что-нибудь об этом месте найду в библиотеке."
    mtdru_kr "Красиво же здесь и дышать легко, ляпота."

    stop music fadeout 0.5

    show dv normal pioneer2 at center with dspr

    play music music_list["sweet_darkness"] fadein 3.0

    dv "То значит говоришь непонятные иностранные слова, а теперь ты решил и старорусские использовать? Ты точно чудак."
    mtdru_kr "Алиса, привет. С самой линейки не виделись. Куда идешь?"
    dv "Не твоего ума дело куда я иду."

    show dv grin pioneer2 at center with dspr

    dv "Или ты хочешь проводить даму как истинный джентльмен?"
    "Она хитро посмотрела на меня."
    mtdru_kr "Ну, если ваш путь лежит через библиотеку, то так уж и быть, провожу."
    dv "Не знала, что ты ботаник. А с виду нормальный парень. Как жаль, а то почти влюбилась в тебя."

    show dv laugh pioneer2 at center with dspr

    "Она звонко засмеялась и подмигнула."

    show dv normal pioneer2 at center with dspr

    mtdru_kr "Что? Бредятину не неси, я хоть и люблю почитать, но уж точно не учебники по ботанике."
    dv "Ну да, ну да, конечно. Тогда скажи мне, зачем ты идешь в первый же день в библиотеку? Ахахахах, можешь не отвечать, ботаник."
    mtdru_kr "Ну вообще-то у меня обходной. Может я и не очень хочу туда идти, но все равно должен."

    show dv grin pioneer2 at center with dspr

    dv "Ой. Ладно, ты выиграл."
    mtdru_kr "Мы во что-то играли?"

    show dv normal pioneer2 at center with dspr

    dv "Да ну тебя. Мне в другую сторону, пока."

    hide dv normal pioneer2 with dspr

    mtdru_kr "Постой."

    show dv normal pioneer2 at center with dspr

    dv "Чего тебе?"
    mtdru_kr "Где библиотека?"
    dv "За Гендой поворот на право. Надеюсь, ты не такой глупый, как я думаю, и не заблудишься."
    mtdru_kr "Сделаю все возможное и невозможное."
    "После этого я стал по стойке смирно и отдал честь."
    dv "Вольно."

    hide dv normal pioneer2 with dspr

    "В тот же момент она развернулась и ушла."

    stop music fadeout 5.0

    th "Боже, что за цирк я здесь устраиваю. Мне 25, мне 25. Все, собрался."
    th "Днем нужно играть роль пай мальчика, а ночью - искать ответы. Еще нужно найти карту местности, иначе я так и буду здесь теряться."
    th "Соня… Я найду его и тебя, я тебя смогу защитить."
    th "Все это закончится, все снова будет хорошо."

    scene bg ext_library_day with dissolve

    mtdru_kr "А вот и библиотека. Красивое здание."

    play sound sfx_knock_door2

    "Я постучался."
    mtdru_kr "Извините, можно войти?"
    "Ответа не последовало."
    mtdru_kr "Извините? Мне нужно подписать обходной, здесь кто-нибудь есть?"
    mzp "Да заходи ты уже."

    window hide dspr

    stop ambience fadeout 0.5
    play sound sfx_open_door_1
    scene bg int_library_day with dissolve
    show mz normal glasses pioneer close at center with dspr
    play ambience ambience_library_day fadein 5.0

    window show dspr

    mtdru_kr "Привет, а где тут библиотекарша?"

    show mz angry glasses pioneer close at center with dspr

    mzp "Ты тупой?! Я и есть библиотекарша. Чего тебе?"
    mtdru_kr "Да вот."
    "Я протянул ей обходной."

    show mz normal glasses pioneer close at center with dspr

    mzp "А, понятно, ты же новенький. Что же сразу не сказал. Давай уж накалякаю тебе здесь. Вот, держи."
    mtdru_kr "Спасибо. Слушай, а как тебя зовут?"
    mz "Меня не зовут, если хочу - сама прихожу. А мое имя – Женя." # Уважаемая мадмуазель, вас зовут швабра, а не Женя (шутка, Женяфаги не бейте пж)
    mtdru_kr "Рад знакомству. Слушай, пока не ушел, у тебя здесь есть карта лагеря? А то я немного плохо ориентируюсь."
    mz "Да, конечно, подожди здесь."
    mtdru_kr "Еще раз спасибо."

    hide mz normal glasses pioneer close with dspr
    pause 0.4
    show mz normal glasses pioneer close at center with dspr

    "Через минуту Женя принесла большущую карту, сложенную в несколько раз. Я был весьма удивлен."
    mtdru_kr "Это, эммм?"
    mz "Лучше не смогла найти. Сейчас мы на тебя ее оформим, ты до какого ее берешь? До конца смены?"
    mtdru_kr "Да, наверное. Если не будет нужна, могу и раньше занести."
    mz "Так, готово. А теперь, если ты доволен, можешь уйти?"
    mtdru_kr "Пока."

    window hide dspr

    stop ambience fadeout 0.5
    hide mz normal glasses pioneer close with dspr
    play sound sfx_open_door_1
    scene bg ext_library_day with dissolve
    play ambience ambience_camp_center_day fadein 5.0

    window show dspr

    th "Все вокруг такие добрые и милые, а Женя такая токсичная. Видимо, вселенский баланс и правда существует, и Женя отдувается за всех. Ну, лагерь, чем ты меня еще удивишь?"

    show sn fears pi close at center with dspr

    play music music_list["you_lost_me"] fadein 5.0

    "В этот момент к библиотеке подошла Соня."
    mtdru_kr "О, Соня! Нашла медпункт?"
    mtdru_sn "…"
    mtdru_kr "Соня?"

    show sn fears pi close at center with dspr:
        zoom 1.15
        xalign 0.5
    
    "Она продолжала молчать. Я подошел к ней и взял ее за плечи."
    mtdru_kr "Соня, что случилось? Я твой сосед, можешь мне рассказать."
    mtdru_sn "Она…"
    mtdru_kr "Кто?"
    mtdru_sn "Она… Виола, она…"
    mtdru_kr "Что за Виола? Что она сделала?"
    mtdru_sn "Она жуткая извращенка… Кирилл, я не знаю, как я выжила после нее."

    hide sn fears pi close
    show sn normal pi close at center with dspr

    stop music fadeout 0.5
    play music music_list["i_want_to_play"] fadein 3.0

    mtdru_kr "И все? Ты меня напугала знатно. Я думал, что то серьезное случилось, а ты."
    mtdru_sn "Ты не знаешь, о чем ты говоришь…"
    mtdru_kr "Так или иначе, пойду и узнаю."
    # mtdru_sn "Вот и помер дед Кирилл…"

    hide sn normal pi close with dspr

    th "Что случилось? Почему она так драматизирует? Может, пытается запугать?"
    th "Вполне логично. Скорее всего она хочет, чтобы я показал себя в дурном свете перед этим божьим одуванчиком Виолой."
    th "Хах, хороший план, Соня, но меня не проведешь."

    scene bg ext_square_day with dissolve

    "С этими мыслями и приподнятым настроением я направился в медпункт. Дорога была не дальняя, даже новичок не заблудится."
    "Отдельное внимание я обратил на погоду. Утром был ужасный дождь, но сейчас… даже и лужицы не было видно."
    th "Странное место… Но свежий запах после дождя никуда не делся, что меня это немного подбадривало."

    stop music fadeout 5.0

    scene bg ext_aidpost_day with dissolve

    "Тем временем я уже подошел к домику с «крестом»."

    play sound sfx_knock_door2
    pause 0.4

    mtdru_kr "Можно войти?"
    csp "Входи, пион{b}Э{/b}р…"
    
    stop ambience fadeout 0.5
    play sound sfx_open_door_1
    scene bg int_aidpost_day with dissolve
    play ambience ambience_medstation_inside_day fadein 5.0

    mtdru_kr "Тут такое дело, я новенький и мне тут…"

    show cs normal close at center with dspr

    cs "Чщ, чщ, чщ. Не спеши ты так. Соня мне уже сказала, что ты придёшь."
    "Она посмотрела на меня взглядом хищника."
    mtdru_kr "Так вы знаете, что мне нужны подписи на…"
    cs "Вы, молодые, все время куда-то торопитесь,{w} спешите…"

    show cs shy close at center with dspr

    "Она закрыла глаза и, кажется, покраснела."

    show cs smile close at center with dspr

    cs "Раздевайся и ложись на кушетку. Сейчас мы проведем полный осмотр."
    "Она натянула свои перчатки и улыбнулась."
    mtdru_kr "Постойте, зачем мне это? Я здоров, мне нужна лишь подпись…"
    cs "Может все-таки ты передумаешь?"

    show cs smile close at center with dspr:
        zoom 1.25
        xalign 0.45
    
    "В этот момент она нагнулась так, что с кушетки были видны все прелести ее… медформы."
    "Я тяжело сглотнул."
    mtdru_kr "Нет, я не знаю, что у вас за осмотры такие, но мне нужна лишь подпись. Надеюсь, я смогу ее получить?"
    cs "Мда, скучное поколение растет, ну ничего не поделаешь, перевоспитаем…"

    play sound sfx_open_door_strong
    hide cs smile close
    show cs normal close at right with dspr
    show mt angry pioneer close at left with dspr

    "В этот момент влетела в помещение Ольга Дмитриевна, за ней стояла Соня."
    mt "Виола, поставь этому пионеру подпись, а потом мне нужно будет с тобой кое-что обсудить!"
    th "Боже, спаси и сохрани эту святую женщину!"

    window hide dspr

    stop ambience fadeout 0.5
    hide cs normal close with dspr
    hide mt angry pioneer close with dspr
    play sound sfx_open_door_1
    scene bg ext_aidpost_day with dissolve
    play ambience ambience_camp_center_day fadein 5.0

    window show dspr

    "Я пулей вылетел из медпункта и в шоке сел на ступеньку. Рядом села Соня."

    show sn normal pi close at center with dspr

    mtdru_sn "Мог бы и спасибо сказать…"
    mtdru_kr "Да, прости, спасибо. Не думаю, что она сделала что-нибудь из того, что мы представили, но все же… это все было неожиданно... Прости… Я хотел бы побыть один."
    mtdru_kr "Если не трудно, заберешь мой обходник?"

    show sn embarrassed pi close at center with dspr

    mtdru_sn "Да, конечно. Ну, ты это, не расстраивайся, будут у тебя еще шуры муры."
    "Она засмеялась и ударила меня по плечу."

    show sn normal pi close at center with dspr

    mtdru_kr "Что? Расстраиваться? Шуры муры? Ты меня точно не за того принимаешь. Я пойду."

    hide sn normal pi close with dspr

    scene bg ext_houses_day with dissolve

    th "Что здесь вообще происходит? Как это вообще понять? Зачем этот голос отправил меня сюда… Спасение…"    
    th "Что он имел ввиду? Я здесь не нахожу ничего, что может меня спасти. Нужно попробовать поискать ответы. Я ничего совершенно не понимаю."

    stop ambience fadeout 0.5
    scene bg ext_path2_day with dissolve
    play ambience ambience_forest_day fadein 5.0

    "В глубоких раздумьях я даже не заметил, как оказался на тропинке, ведущей в лес."
    mtdru_kr "Отлично, как раз прогуляюсь."
    "Как только я сделал шаг в лес, атмосфера как будто поменялась: пионерская суета осталась за спиной, а вся мирская тишина, наоборот, лишь заманивала в глубь леса."
    "Тишина и покой. Красота. Это место и вправду замечательное. Птицы… птицы здесь поют красиво, зазывая ближе к себе в чащу."
    "Казалось, что вокруг больше нет ни лагеря, ни домиков, ни обходных, ни одного человека. Вокруг не было ничего, кроме высоких сосен, уходящих в небо, свежего воздуха после дождя и мягкой травы."

    play sound sfx_bodyfall_1

    mtdru_kr "АГХ, ЧЕРТ!"
    
    scene black with dissolve

    "Совсем неожиданно Кирилла как будто ударило током и повалило на землю. В глазах медленно темнело, а когда стемнело окончательно, начали всплывать различные силуэты."
    
    play music music_list["door_to_nightmare"] fadein 5.0

    window hide dspr

    stop ambience fadeout 0.5
    
    $ persistent.sprite_time = "night"
    $ night_time()

    scene ext_path2_night with dissolve
    show sn normal darkdress far at center with dspr

    window show dspr
    
    th "Что это? Где я? Лес? Он похож на тот, где я был сейчас. Девушка… Я вижу девушку, может спросить у нее, где я? Да, пожалуй, стоит."
    
    show sn normal darkdress close at center with dspr

    mtdru_kr "Девушка! Девушка, простите, а вы…?"
    "Девушка никак не реагировала на зов Кирилла."
    th "Что? Почему она меня не слышит? Она остановилась? Стоп, ее лицо. Она же… СОНЯ?!"
    th "Но как, стоп. Этого не может быть! Она похожа на Соню, которая была в моей реальности, но не может же она быть настоящей…"
    "Девушка села на землю, облокотившись на дерево, стоящее позади нее. Она достала тетрадку и начала что-то писать, напевая до боли мне знакомую мелодию."
    th "Я вспомнил… Эта мелодия… Это моя Соня! Я вспомнил, как она напевала ее, когда пыталась заснуть. Боже мой, значит, я здесь не просто так."
    th "Соня жива? Мы как будто находимся в стеклянных звуконепроницаемых ящиках. Нужно как-то привлечь ее внимание."
    "Около получаса я делал различные вещи, чтобы ее привлечь, но все безуспешно."
    th "Как же это все работает… я же вижу ее, слышу, но почему она нет?"
    
    hide sn normal darkdress close at center with dspr
    
    mtdru_wm "Конечно не слышит, с чего бы это?"
    mtdru_kr "КТО ЗДЕСЬ?!"

    # (спрайта не будет, чувак вьетнамец)

    mtdru_wm "Неважно. Слушай, ты, наверное, и не догадаешься, что это лишь твое воспоминание."
    mtdru_kr "Воспоминание? Но я здесь никогда не был."
    mtdru_wm "Физически не был, но ментально…"
    mtdru_kr "Что? Похоже, я начал сходит с ума здесь…"
    mtdru_wm "Не перебивай! Вспомни: она же рассказывала тебе об этом месте?"
    mtdru_kr "Да, точно… Откуда ты это знаешь?"
    mtdru_wm "Ты задаешь не те вопросы, Кирилл."
    mtdru_kr "Хм, если это и мое воспоминание, то каким образом я помню его так детально? И к тому же, если я был здесь лишь ментально, то этот мир - плод моего воображения?"
    mtdru_wm "Нет, ты ошибаешься."
    mtdru_kr "Тогда как ты все это объяснишь?"
    mtdru_wm "У тебя выработались определенные навыки за время твоей работы в газете, поэтому с ее слов ты так хорошо представил это место."
    mtdru_wm "Не могу сказать, что это правда, что это место вообще существует, но пусть будет так…"
    mtdru_kr "Стоп, я работал в газете? Я совсем этого не помню. Ты же все обо мне знаешь… РАССКАЖИ!"
    mtdru_wm "Я знаю о тебе столько, сколько того хочет он…"
    mtdru_kr "Кто он?! Скажи!"
    mtdru_wm "Ты его сам увидишь, он же сказал тебе что, где и когда."
    mtdru_kr "Значит ты от него… зачем он это делает?"
    mtdru_wm "Это ты узнаешь у него, твое время истекло."
    "В этот момент она щелкнула пальцами, мир вокруг перестал быть серым, налился красками и звуками."

    stop music fadeout 5.0

    window hide dspr

    scene ext_path2_night with flash
    play ambience ambience_forest_night fadein 6.0

    window show dspr

    mtdru_kr "Гхм… голова…"

    show mt surprise pioneer close at center with dspr

    mt "Боже, ты очнулся!"

    show mt surprise pioneer close at right with dspr
    show cs normal at left with dspr

    cs "А ты сомневалась? Нашатырь и не таких из могилы вытаскивал."

    show cs smile at left with dspr

    "Она звонко засмеялась, как будто ничего не случилось."

    show cs normal at left with dspr
    show mt angry pioneer close at right with dspr

    mt "Виола!"
    cs "Всего лишь шутка."

    show mt normal pioneer close at right with dspr

    mt "Ты как? Все в порядке?"
    mtdru_kr "Ну, все кости на месте, жить можно, но мне бы не помешало утихомирить боль в голове…"
    mt "Виола, сходи с пионером. И без всяких там шуточек!"
    cs "Да-да…" # Сахаров: Да-да
    mt "Кирилл…"
    mtdru_kr "Извините, что доставил хлопот."
    mt "Просто больше так не пропадай. И скажи спасибо Соне, она заметила твою пропажу."
    mtdru_kr "Обязательно. Тогда я пойду в медпункт."
    cs "Оля, погрей чайник, хорошо?"
    mt "Иди уже."

    hide mt normal pioneer close with dspr
    hide cs normal at center with dspr

    th "Не знаю, какие между ними взаимоотношения, но они явно подруги."
    th "Хоть Ольга и проявила строгость к ней во время обеда, но это скорее из-за должности и в целом из-за ситуации."
    th "Интересно, давно ли они знакомы? Как они оказались здесь вместе?"

    show cs normal close at center with dspr

    cs "О чем задумался?"
    mtdru_kr "А? Да так, прохладно что-то."
    cs "Да, здесь так, разве не красота?"
    mtdru_kr "Да, но, если бы не было комаров, было бы намного лучше."
    cs "Ха-ха-ха, да уж."

    window hide dspr

    stop ambience fadeout 0.5
    hide cs normal close with dspr
    scene bg ext_square_night with dissolve
    show cs normal close at center with dspr
    play ambience ambience_camp_center_night fadein 5.0

    window show dspr

    mtdru_kr "Чего вы?"
    "Я насторожился, ожидая какой-нибудь неудобной ситуации как в прошлый раз. Кажется, от этой женщины можно ожидать что угодно в любой момент времени."
    cs "Попросить спрей не мог?"
    mtdru_kr "Ну знаете, наше знакомство вышло несколько сумбурным."

    show cs smile close at center with dspr

    cs "Да, люблю пошутить над молодыми пионерами. Ты бы видел их лица, умора просто."
    "Она заметно повеселела."
    mtdru_kr "Да уж, ха-ха-ха. Но вы же так отпугиваете людей от медпункта, разве это не плохо?"

    show cs normal close at center with dspr

    cs "Это очень даже хорошо, меньше работы как с пионерами, так и с бумагами." # Гайд как не работать, но получать за это деньги
    cs "Можно сказать, я запугала вас сразу, чтобы бы вы были аккуратнее, потому что знаете, что если что-то случится, то придется снова идти в медпункт к ужасной Виоле. И всем проще."
    mtdru_kr "Хитро вы, хах."

    hide cs normal close with dspr

    "Дальнейшую дорогу мы шли полностью в тишине. Вокруг кипела жизнь, нет, не пионеры, местная живность."
    "Сверчки, кузнечики, комары. Все вместе они создавали прекрасную мелодию, мелодию ночи, которую в городе и не услышать."
    "Ночь одарила меня не только красивой песней, но и своей свежестью, которая не давала уснуть, но в то же время очень сильно выматывала."
    "Облака разошлись, поэтому, если замедлить шаг, можно было разглядеть звезды на небе. Я раньше любил их рассматривать и искать созвездия."
    th "Ну и ну. Кажется, будто бы впервые чувствую себя настолько хорошо. Хм, я помню этот поворот, значит мы близко к медпункту."

    scene bg ext_aidpost_night with dissolve

    "Через минуту я и Виола были у дверей медпункта. Она достала ключи и открыла дверь."

    show cs normal close at center with dspr

    cs "Постой здесь, сейчас я принесу тебе таблетку."
    mtdru_kr "Спасибо."

    window hide dspr

    hide cs normal close with dspr
    pause 0.5
    show cs normal close with dspr

    window show dspr

    "Виола зашла в домик и через минуту вышла с таблеткой и стаканом воды."
    cs "Хорошенько запей, а потом иди спать."
    mtdru_kr "Хорошо."

    hide cs normal close with dspr

    "Выпив таблетку и отдав стакан Виоле, я направился обратно в свой домик. На улице было уже совсем темно. Хорошо, что тут есть фонари, возле которых всегда кружатся мотыльки."

    scene bg ext_square_night with dissolve

    th "Что же их привлекает в этом свете? Может быть, этот яркий свет? Не думаю, тогда бы они и днем везде летали бы. Может, тепло от лампы?"
    th "Тоже глупости. Может, в этом и есть их смысл существования? Искать свет в кромешной тьме? Глупо звучит, но по-другому я и думать не могу."
    th "Удивительные создания эти мотыльки, люди похожи на них, а иногда и наоборот, являются полной противоположностью."
    th "Кто-то тянется к прекрасному и не ищет славы, а кто-то делает все, что угодно ради капельки внимания. Глупо как-то…"

    scene bg mtdru_ext_house_of_un_night with dissolve

    "Вскоре я уже подходил к своему домику и оказался удивлен: кто-то сидел на порожках и, кажется, спал."

    # (да тут рил нужно еще цг) ХИХИ ХАХА
    # пидарас
    # кто?

    mtdru_kr "Глупышка… Зачем же ты так."

    stop ambience fadeout 0.5
    play sound sfx_open_door_1
    scene bg int_house_of_un_night with dissolve
    play ambience ambience_int_cabin_night fadein 5.0

    "Соня ответила лишь тихим посапыванием. Я аккуратно взял ее на руки, вошел в наш домик и положил ее на кровать."
    mtdru_kr "Спи сладко и не делай глупости…"
    "Я накрыл ее одеялом, и она свернулась калачиком."
    mtdru_kr "Да, это точно ты, я помню… Но вот помнишь ли ты."
    th "Поздно уже, пора бы на боковую. Интересно это все: лагерь, пионеры, Соня… Что за чудак хотел убить меня с Соней? И кто спас нас?"
    th "Нужно со всем разобраться, но сил уже нет, глаза сами закрываются."
    mtdru_kr "Спокойной ночи, Совёнок."

    window hide dissolve
    stop ambience fadeout 4.0
    scene black with Dissolve(4.0)
    return