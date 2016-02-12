init:
    define me = Character(name="[name]", who_color="#eeeeee", ctc="ctc_blink", ctc_position="fixed")
    define sensei = Character(name='Sensei', who_color="#ee3342", image="sensei", ctc="ctc_blink", ctc_position="fixed")
    define froggy = Character(name='Froggy', who_color="#D6FF95", image="froggy", ctc="ctc_blink", ctc_position="fixed")
    define magenta = Character(name='Magenta', who_color="#D747D0", ctc="ctc_blink", ctc_position="fixed")
    define cubey = Character(name='Cubey', who_color="#955273", image="cubey", ctc="ctc_blink", ctc_position="fixed")
    define narrator = Character(ctc="ctc_blink", ctc_position="fixed")

init python:
    import random
    
    def die(version=0):
        renpy.music.stop(fadeout=2)
        lengths = [4, 3]
        for i in range(lengths[version]):
            renpy.show('overlay dead ' + str(version) + ' ' + str(i))
            renpy.sound.play('sound/fx/blood_drip.ogg')
            renpy.with_statement(trans=shake)
            renpy.pause((5-i) / 3)

    def random_file_line(afile):
        line = next(afile)
        for num, aline in enumerate(afile):
          if random.randrange(num + 2): continue
          line = aline
        return line

# The game starts here.
label start:
    scene black

    menu:
        "What would you like to do?"
        "Start game":
            jump naming
        "Die":
            $ die(0)

label naming:
    $ name = "DEFAULT NAME"
    python:
        namenotok = True
        while namenotok:
            with renpy.file("names.txt") as f:
                name = renpy.input(prompt="{size=+10}Before we begin.\nWould you mind telling us your name?", default=random_file_line(f)[:-2])

                if len(name) > 20:
                    renpy.say(None, "Are you sure? That name seems very long.")
                    continue
                elif len(name) < 2:
                    renpy.say(None, "Are you sure? That name seems unusually short.")
                    continue
                renpy.say(None, "Your name is [name]?", interact=False)
                if renpy.display_menu([("Yes", True), ("No", False)]) == True:
                    namenotok = False
                    continue
                else:
                    continue
        
    menu:
        "Would you like to play the tutorial. It's quite quick I assure you."
    
        "Yeah (recommended if you've never played virtual novels before)":
            jump tutorial
    
        "No, I know what I'm doing.":
            "Okay then, let's jump right in."
            jump scene01

label tutorial:
    "Hello welcome to this Virtual Novel. What is a virtual novel you ask?"
    "Well, acording to wikipedia:\nA visual novel is an interactive game, featuring mostly static graphics, most often using anime-style art or occasionally live-action stills (and sometimes video footage). As the name might suggest, they resemble mixed-media novels.\nRead more: {a=https://en.wikipedia.org/wiki/Visual_novel}en.wikipedia.org/wiki/Visual_novel{/a}"

    "The controls are as follows:\nLEFT CLICK to advance dialogues (this only applies if {image=ctc_small} is shown in the corner of the window, otherwise a LEFT CLICK will cause more text to appear.{w}\nLEFT CLICK is also used to select different options when you're presented with a choice."
    "RIGHT CLICK or ESC is used to open the menu.\nFrom the menu you can save/load the game, and also quit it.\nIt is also here you can access the prefrenses, where you can enter fullscreen, change volume levels and much more."
    "Since this game uses an engine called Ren'Py it has a special mechanic named {i}rollback{/i}.\nRollback allows you to (upon pressing either PGUP or scrolling your scrollwheel) to go back in time! Try it now!"
    "Click {a=show_help}here{/a} to open a webbrowser to display additional controls and help. This can be accessed anytime by going to the menu and clicking \"Help\"."

    menu:
        "Think you're ready now?"
    
        "No! Show me the tutorial again!":
            jump tutorial

        "Yeah, I'm totally ready!":
            jump scene01

label you_dead:
    scene black
    with fade
    centered "{size=+10}Things didn't go quite as well as you had planed.\nYou can now choose to either rollback using PGUP\n or click anywhere to return to the main menu.{/size}"
    return

label show_help:
    $ _help()