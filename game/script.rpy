init:
    define me = Character(name="[name]", who_color="#eeeeee")
    define sensei = Character(name='Sensei', who_color="#ee3342", image="sensei")
    define froggy = Character(name='Froggy', who_color="#D6FF95", image="froggy")
    define magenta = Character(name='Magenta', who_color="#D747D0")

init python:
    import random
    
    def die(stages=[1,2,3,4]):
        for i in stages:
            renpy.show('overlay dead_' + str(i))
            renpy.music.play('sound/fx/blood_drip.ogg', channel='sound')
            renpy.with_statement(trans=shake)
            if len(stages) != 1:
                renpy.pause((5-i) / 3)

        renpy.jump('credits')

# The game starts here.
label start:
    scene black

    $ die()

    python:
        def random_file_line(afile):
            line = next(afile)
            for num, aline in enumerate(afile):
              if random.randrange(num + 2): continue
              line = aline
            return line

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