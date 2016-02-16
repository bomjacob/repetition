init:
    $ flash = Fade(.25, 0, .75, color="#fff")

    $ fade_scene = Fade(0.5, 1, 0.5)

    transform door_trans(new_widget, old_widget):
        delay 1.5
   
        contains:
            new_widget
        
        contains:
            old_widget
            pause 0.75
            alpha 0.0

        contains:
            "black"
            alpha 0.0
            ease 0.75 alpha 1.0
            pause 0.25
            xzoom 1.0
            easeout_circ 0.5 xzoom 0.0

    image ctc_blink:
        "ui/ctc.png"
        xpos 1230
        ypos 740
        block:
            easeout 0.75 alpha 0.0
            easein 0.75 alpha 1.0
            repeat

    image ctc_small:
        "ui/ctc.png"
        zoom 0.7

    image book sensei_and_me:
        "img/book/sensei/0.jpg"
        pause 0.4
        "img/book/sensei/1.jpg"
        pause 0.4
        repeat

    image book home:
        "img/book/home/0.jpg"
        pause 0.4
        "img/book/home/1.jpg"
        pause 0.4
        repeat

    image book flames:
        "img/book/flames/0.jpg"
        pause 0.4
        "img/book/flames/1.jpg"
        pause 0.4
        "img/book/flames/2.jpg"
        pause 0.4
        "img/book/flames/3.jpg"
        pause 0.4
        repeat

    image sensei_room_flashback = im.MatrixColor(
        "img/bg/sensei_room.jpg",
        im.matrix.saturation(0.1))

    image tutorial_ctc:
        pause 5.0
        Text("Left Click to continue.")

    image main_menu_image:
        choice:
            "forest start" with dissolve
        choice:
            "forest three" with dissolve
        choice:
            "mansion ext" with dissolve
        choice:
            "town square" with dissolve
        choice:
            "sensei_room" with dissolve
        pause 5.0
        repeat