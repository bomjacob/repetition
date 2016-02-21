init:
    define me = Character(name="[name]", who_color="#eeeeee", ctc="ctc_blink", ctc_position="fixed")
    define sensei = Character(name='Sensei', who_color="#ee3342", image="sensei", ctc="ctc_blink", ctc_position="fixed")
    define froggy = Character(name='Froggy', who_color="#D6FF95", image="froggy", ctc="ctc_blink", ctc_position="fixed")
    define magenta = Character(name='Magenta', who_color="#D747D0", image="magenta", ctc="ctc_blink", ctc_position="fixed")
    define cubey = Character(name='Cubey', who_color="#955273", image="cubey", ctc="ctc_blink", ctc_position="fixed")
    define narrator = Character(ctc="ctc_blink", ctc_position="fixed")
    define centered = Character(None, what_style="centered_text", window_style="centered_window", ctc="ctc_blink", ctc_position="fixed")
    define willo = Character(name="Will o' the Wisp", image="willo", who_color="#7EDEFF", ctc="ctc_blink", ctc_position="fixed")
    define unknown = Character(name="???", who_color="#EEEEEE", ctc="ctc_blink", ctc_position="fixed")
    define lilly = Character(name="Lilly", who_color="#9E1B08", image="lilly", ctc="ctc_blink", ctc_position="fixed")
    define squirrel = Character(name="Squirrel", who_color="#B89067", image="squirrel", ctc="ctc_blink", ctc_position="fixed")
    define partridge = Character(name="Partridge", who_color="#A43023", image="partridge", ctc="ctc_blink", ctc_position="fixed")
    define fox = Character(name="Fox", who_color="#F295CA", image="fox", ctc="ctc_blink", ctc_position="fixed")
    define ghost = Character(name="Ghost of Bad Film Making", who_color="#F3F6FB", image="ghost", ctc="ctc_blink", ctc_position="fixed")
    define sloth = Character(name="As of Yet Unnamed Sloth", who_color="#F0AE2E", image="sloth", ctc="ctc_blink", ctc_position="fixed")
    define raccoon = Character(name="Yen", who_color="#FFF", image="yen", ctc="ctc_blink", ctc_position="fixed")

    # Points for games/quizes and such
    default has_met_lilly = False
    default postermm_points = 0
    default postermm_done = {}

    default film_wrongpartridge = 0
    default film_partridge = 0
    default film_deadsquirrel = 0
    default film_squirrel = 0
    default film_wrongfox = 0
    default film_fox = 0

    default web_total = 0
    default code_asked = dict(doctype=False, enter=False, big=False, head=False, css=False)
    default code_correct = 0
    default code_asked_i = 0

    default comm_total = 0
    default comm_asked = dict(onemany=False, manynone=False, manyfew=False, oneeveryone=False, oneone=False, manymany=False, manyone=False, everyoneeveryone=False)
    default comm_correct = 0
    default comm_asked_i = 0


init python:
    import random
    import os
    
    def die(version=0):
        renpy.music.stop(fadeout=2)
        lengths = [4, 3, 3]
        for i in range(lengths[version]):
            renpy.show('overlay dead ' + str(version) + ' ' + str(i))
            renpy.sound.play('blood_drip')
            renpy.with_statement(trans=shake)
            renpy.pause((5-i) / 3)

    def random_file_line(afile):
        line = next(afile)
        for num, aline in enumerate(afile):
          if random.randrange(num + 2): continue
          line = aline
        return line

    def get_name(rnd_overwrite=False):
        #If windows then get system username
        if os.name == "nt" and not rnd_overwrite:
            return os.getenv("username").title()
        #If not windows, or windows messed up, just pick a random name
        if os.name != "nt" or name_placeholder is None or name_placeholder == "" or rnd_overwrite:
            with renpy.file("names.txt") as f:
                return random_file_line(f)[:-2]

# The game starts here.
label start:
    show expression mm_img:
        xalign 0.5 yalign 0.5
    $ name = _("DEFAULT NAME")

    jump tutorial_ask

label tutorial_ask:
    menu:
        "Would you like to play the tutorial? It is recommended, if you have never played a visual novel before."
    
        "Yes, a tutorial sounds good.":
            jump tutorial
    
        "No, I know what I'm doing.":
            "Okay then, let's jump right in."
            jump naming


label naming:
    $ save_name = _("What's your name?")
    python:
        name_placeholder = get_name()
        while True:
            name = renpy.input(prompt=_("{size=+10}Before we begin.\nWould you mind telling us your name?\nLeave it blank to choose a random one."), default=name_placeholder, length=20)

            if name == "":
                name_placeholder = get_name(rnd_overwrite=True)
                continue

            if len(name) > 20:
                narrator(_("Are you sure? That name seems very long."))
                continue
            elif len(name) < 2:
                narrator(_("Are you sure? That name seems unusually short."))
                continue

            narrator(_("Your name is [name]?"), interact=False)
            if menu([(_("Yes"), True), (_("No"), False)]) == True:
                break
            else:
                if name == name_placeholder:
                    name_placeholder = get_name(rnd_overwrite=True)
                else:
                    name_placeholder = name
                continue

    jump scene01

label tutorial:
    $ save_name = _("Tutorial")
    "Hello! Welcome to this Virtual Novel. What is a virtual novel, you may ask?\n{image=tutorial_ctc}"
    "Well, according to Wikipedia:\nA visual novel is an interactive game, featuring mostly static graphics, most often using anime-style art or occasionally live-action stills (and sometimes video footage). As the name might suggest, they resemble mixed-media novels.\nRead more: {a=https://en.wikipedia.org/wiki/Visual_novel}en.wikipedia.org/wiki/Visual_novel{/a}\n{image=tutorial_ctc}"

    "Controls are quite simple. LEFT CLICK is used to advance dialogues. If, when all text is displayed, {image=ctc_small} is shown, it will advance to next page and remove all current text. If not, more text will appear on the screen, once you click again. If you're ever in doubt which button to press, it is probably LEFT CLICK."
    "LEFT CLICK is also used to select options in menus.{w} Try it now!{nw}"
    menu:
        "LEFT CLICK is also used to select options in menus. Try it now!{fast}\nDo you understand everything so far?"

        "Yeah!":
            jump tutorial_part_2
        "Nope! I'm totally lost!":
            "Sorry to hear that. Hopefully it will help to hear it once again."
            jump tutorial

label tutorial_part_2:
    "Then let's promptly continue."
    "Press RIGHT CLICK or ESC anytime while in-game, to access the game-menu. From here you can save (the default), load, quit, or open the help document."
    if renpy.in_rollback():
        jump tutorial_part_3
    "In the game-menu you will also find the game's preferences. From there you can switch between fullscreen and windowed mode, change volume levels, change text speed and much much more."
    if renpy.in_rollback():
        jump tutorial_part_3
    "This game uses a powerful engine known as Ren'Py. Ren'Py comes with a special mechanic called \"{i}rollback{/i}\" which allows to player to go \"back in time\" in terms of the game. PGUP or mousewheel up will go back in time, while PGDN or mousewheel down will go forward, if you've already gone backwards. Try it now!"
    $ __i = 0
    while True:
        if renpy.in_rollback():
            jump tutorial_part_3
        "Please try using rollback at least once. It's sure to come in handy."
        $ __i += 1
        if __i > 10:
            if renpy.in_rollback():
                jump tutorial_part_3
            "I really didn't want it to come to this..."
            if renpy.in_rollback():
                jump tutorial_part_3
            menu:
                "Rollback... (using PGUP or mousewheel up) or die!"
                "Okay! I'll rollback!":
                    if renpy.in_rollback():
                        jump tutorial_part_3
                    "You better..."
                    if renpy.in_rollback():
                        jump tutorial_part_3
                    "Do it, or you'll die!"
                    $ die(2)
                    "Don't say I didn't warn you!"
                    return
                "Never! I'd rather die, than rollback.":
                    "Very well..."
                    $ die(1)
                    return

label tutorial_part_3:
    "Well done! Normally that would have taken you back to the previous dialogue block, but for now let's continue with the tutorial."
    "If you want to go back further than a simple rollback, then saving is the way to go. The game will also auto-save before every single choice. Auto-saves can be accessed by clicking \"Auto\" in the save/load screen."
    "If at any time you need any help with controls or an explanation of the different preferences you can access additional help anytime by going into the game-menu (RIGHT CLICK OR ESC, remember?) and choosing \"Help\". You can also click {a=show_help}here{/a}."

    menu:
        "That's the end of the tutorial. Do you think you're ready for the game now?"
    
        "No! Show me the tutorial again!":
            jump tutorial

        "Yeah, I'm totally ready!":
            jump naming

label you_dead:
    scene black
    with fade
    centered "{size=+10}Things didn't go quite as well as you had wanted...\nBut you can always rollback and change your fate using PGUP\n... or click anywhere to return to the main menu.{/size}"
    return

label show_help:
    $ _help()