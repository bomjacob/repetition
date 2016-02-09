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
    python:
        with renpy.file("names.txt") as f:
            namenotok = True
            while namenotok:
                name = renpy.input(prompt="Before we begin.\nWould you mind telling us your name?", default=random_file_line(f)[:-2])

                if len(name) > 30:
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

    me "Hi"
    jump scene01