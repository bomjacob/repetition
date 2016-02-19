init python:
    import random
    mm_imgs = ["forest start", "forest three", "mansion ext", "town square", "sensei_room", "mansion hallway", "meadows evening", "town2 playground"]
    mm_img = mm_imgs[random.randrange(len(mm_imgs))]

    def mm_img_next():
        mm_index = mm_imgs.index(mm_img)
        rnd = mm_index
        while rnd == mm_index:
            rnd = random.randrange(len(mm_imgs))
        mm_index = rnd
        return mm_imgs[mm_index]

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
        Text(_("Left Click to continue."))

    image ghosti:
        on show:
            "img/characters/ghost/0.png"
            pause 0.2
            "img/characters/ghost/1.png"
            pause 0.2
            "img/characters/ghost/3.png"
            pause 0.2
            "img/characters/ghost/4.png"
            pause 0.2
        "img/characters/ghost/full.png"

    transform flip:
        xzoom -1.0
    transform unflip:
        xzoom 1.0

    transform floating:
        ease 2 yoffset 20
        ease 2 yoffset -20
        repeat

