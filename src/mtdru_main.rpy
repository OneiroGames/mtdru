# Copyright (c) Oneiro Games. All Right Reserved.
# Licensed under the GPL License, Version 3.0.

init python:
    def mtdru_make_dark(path, intens=0.05):
        return im.MatrixColor(
                    path,
                    im.matrix.tint(intens, intens, intens))
init:
    $ mods ["mtdru"] = u"Да воссоединит нас рассвет"
    $ config.developer = True

    $ MTDRU_IMG_DIR = "mods/mtdru/assets/images/"
    $ MTDRU_SND_DIR = "mods/mtdru/assets/sounds/"

    $ mtdru_AlleyTint = 1.0

    image bg mtdru_hospital_ward_night = MTDRU_IMG_DIR + "bg/hospital_ward_night.jpg"

    image bg mtdru_hospital:
        contains:
            MTDRU_IMG_DIR + "bg/hospital.jpg"
            alpha 1.0
        contains:
            MTDRU_IMG_DIR + "bg/hospital.jpg"
            alpha 0.2 zoom 1.015
        contains:
            MTDRU_IMG_DIR + "bg/hospital.jpg"
            alpha 0.2 zoom 1.010
        contains:
            MTDRU_IMG_DIR + "bg/hospital.jpg"
            alpha 0.2 zoom 0.995
        contains:
            MTDRU_IMG_DIR + "bg/hospital.jpg"
            alpha 0.2 zoom 0.990

    image bg mtdru_storage_day = MTDRU_IMG_DIR + "bg/store_house_day.jpg"
    image bg mtdru_ext_clubs_rain = MTDRU_IMG_DIR + "bg/ext_clubs_rain_7dl.jpg"
    image bg mtdru_ext_house_of_un_night = MTDRU_IMG_DIR + "bg/ext_house_of_un_night_7dl.jpg"
    image bg mtdru_ext_square_rain_day = MTDRU_IMG_DIR + "bg/ext_square_rain_day_7dl.jpg"
    image bg mtdru_ext_bus_rain = MTDRU_IMG_DIR + "bg/ext_bus_rain.png"
    image bg mtdru_ext_camp_entrance_rain = MTDRU_IMG_DIR + "bg/ext_camp_entrance_rain.png"

    # sorry for this code tree
    image bg mtdru_rundown_alley_night = ConditionSwitch(
        "mtdru_AlleyTint == 0.5", im.MatrixColor(MTDRU_IMG_DIR + "bg/rundown_alley_night.jpg", im.matrix.tint(0.5, 0.5, 0.5)),
        "mtdru_AlleyTint == 0.6", im.MatrixColor(MTDRU_IMG_DIR + "bg/rundown_alley_night.jpg", im.matrix.tint(0.6, 0.6, 0.6)),
        "mtdru_AlleyTint == 0.7", im.MatrixColor(MTDRU_IMG_DIR + "bg/rundown_alley_night.jpg", im.matrix.tint(0.7, 0.7, 0.7)),
        "mtdru_AlleyTint == 0.8", im.MatrixColor(MTDRU_IMG_DIR + "bg/rundown_alley_night.jpg", im.matrix.tint(0.8, 0.8, 0.8)),    
        "mtdru_AlleyTint == 0.9", im.MatrixColor(MTDRU_IMG_DIR + "bg/rundown_alley_night.jpg", im.matrix.tint(0.9, 0.9, 0.9)),
        "True", im.MatrixColor(MTDRU_IMG_DIR + "bg/rundown_alley_night.jpg", im.matrix.tint(1.0, 1.0, 1.0))
    )

    image cg mtdru_day1_square_mt = MTDRU_IMG_DIR + "cg/day1_square_mt.jpg"
    image cg mtdru_day1_un_us_cat = MTDRU_IMG_DIR + "cg/day1_un_us_cat.jpg"
    image cg mtdru_day1_tie = MTDRU_IMG_DIR + "cg/day1_tie.png"

    image mg normal = MTDRU_IMG_DIR + "sprites/normal/mg/normal.png"
    
    image sn normal st close = MTDRU_IMG_DIR + "sprites/close/sn/normal.png"
    image sn embarrassed st close = MTDRU_IMG_DIR + "sprites/close/sn/embarrassed.png"
    image sn fears st close = MTDRU_IMG_DIR + "sprites/close/sn/fears.png"
    image sn offended st close = MTDRU_IMG_DIR + "sprites/close/sn/offended.png"
    image sn vulgar st close = MTDRU_IMG_DIR + "sprites/close/sn/vulgar.png"

    image sn normal pi close = MTDRU_IMG_DIR + "sprites/close/sn/pi/normal.png"
    image sn embarrassed pi close = MTDRU_IMG_DIR + "sprites/close/sn/pi/embarrassed.png"
    image sn fears pi close = MTDRU_IMG_DIR + "sprites/close/sn/pi/fears.png"
    image sn offended pi close = MTDRU_IMG_DIR + "sprites/close/sn/pi/offended.png"
    image sn vulgar pi close = MTDRU_IMG_DIR + "sprites/close/sn/pi/vulgar.png"

    image sn normal dress close = MTDRU_IMG_DIR + "sprites/close/sn/dress/normal.png"
    image sn embarrassed dress close = MTDRU_IMG_DIR + "sprites/close/sn/dress/embarrassed.png"
    image sn fears dress close = MTDRU_IMG_DIR + "sprites/close/sn/dress/fears.png"
    image sn offended dress close = MTDRU_IMG_DIR + "sprites/close/sn/dress/offended.png"
    image sn vulgar dress close = MTDRU_IMG_DIR + "sprites/close/sn/dress/vulgar.png"

    image sn normal pi far = MTDRU_IMG_DIR + "sprites/far/sn/sn_normal_pi.png"
    image sn laugh pi far = MTDRU_IMG_DIR + "sprites/far/sn/sn_laugh_pi.png"
    image sn dontlike pi far = MTDRU_IMG_DIR + "sprites/far/sn/sn_dontlike_pi.png"
    image sn grin pi far = MTDRU_IMG_DIR + "sprites/far/sn/sn_grin_pi.png"
    image sn scared pi far = MTDRU_IMG_DIR + "sprites/far/sn/sn_scared_pi.png"

    image sn normal dress far = MTDRU_IMG_DIR + "sprites/far/sn/sn_normal_dress.png"
    image sn laugh dress far = MTDRU_IMG_DIR + "sprites/far/sn/sn_laugh_dress.png"
    image sn dontlike dress far = MTDRU_IMG_DIR + "sprites/far/sn/sn_dontlike_dress.png"
    image sn grin dress far = MTDRU_IMG_DIR + "sprites/far/sn/sn_grin_dress.png"
    image sn scared dress far = MTDRU_IMG_DIR + "sprites/far/sn/sn_scared_dress.png"
    
    image sn normal darkdress far = mtdru_make_dark(MTDRU_IMG_DIR + "sprites/far/sn/sn_normal_dress.png", 0.1)
    image sn normal darkdress close = mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/dress/normal.png", 0.1)

    image sn normal darkst:
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/normal.png")
            alpha 1.0
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/normal.png")
            alpha 0.2 zoom 1.015
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/normal.png")
            alpha 0.2 zoom 1.010
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/normal.png", 0.1)
            alpha 0.2 zoom 0.995
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/normal.png", 0.1)
            alpha 0.2 zoom 0.990

    image sn normal darkdress close:
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/normal.png")
            alpha 1.0
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/normal.png")
            alpha 0.2 zoom 1.015
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/normal.png")
            alpha 0.2 zoom 1.010
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/normal.png", 0.1)
            alpha 0.2 zoom 0.995
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sn/normal.png", 0.1)
            alpha 0.2 zoom 0.990

    image sn normal darkdress far:
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/far/sn/sn_normal_dress.png")
            alpha 1.0
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/far/sn/sn_normal_dress.png")
            alpha 0.2 zoom 1.015
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/far/sn/sn_normal_dress.png")
            alpha 0.2 zoom 1.010
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/far/sn/sn_normal_dress.png", 0.1)
            alpha 0.2 zoom 0.995
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/far/sn/sn_normal_dress.png", 0.1)
            alpha 0.2 zoom 0.990

    image mg normal dark:
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/normal/mg/normal.png")
            alpha 1.0
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/normal/mg/normal.png")
            alpha 0.2 zoom 1.025
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/normal/mg/normal.png")
            alpha 0.22 zoom 1.010
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/normal/mg/normal.png", 0.1)
            alpha 0.18 zoom 0.99
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/normal/mg/normal.png", 0.1)
            alpha 0.23 zoom 0.98

    image sd smile darkpi:
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sd/sd_smile_pi.png")
            alpha 1.0
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sd/sd_smile_pi.png")
            alpha 0.2 zoom 1.025
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sd/sd_smile_pi.png")
            alpha 0.22 zoom 1.010
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sd/sd_smile_pi.png", 0.1)
            alpha 0.18 zoom 0.99
        contains:
            mtdru_make_dark(MTDRU_IMG_DIR + "sprites/close/sd/sd_smile_pi.png", 0.1)
            alpha 0.23 zoom 0.98

    image nt smile close = MTDRU_IMG_DIR + "sprites/close/nt/smile.png"

    define mtdru_kr = Character(u"Кирилл", who_color="#FFA700")
    define mtdru_sn = Character(u"Соня", who_color="#FFFA00")
    define mtdru_mg = Character(u"Михаил Гардеевич", who_color="#FFFFFF")
    define mtdru_shadow = Character(u"Тень", who_color="#FF0000")
    define mtdru_wm = Character(u"???", who_color="#454506")
label mtdru:
    window hide dissolve
    scene black with dissolve
    jump mtdru_prologue 
