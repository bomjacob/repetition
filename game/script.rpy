
init:
    define me = Character(name="Me", who_color="#eeeeee")
    define sensei = Character(name='Sensei', who_color="#ee3342", image="sensei")
    define froggy = Character(name='Froggy', who_color="#D6FF95", image="froggy")
    define magenta = Character(name='Magenta', who_color="#D747D0")

init python:
    def die(stages=[1,2,3,4]):
        for i in stages:
            renpy.show('overlay dead_' + str(i))
            if len(stages) != 1:
                renpy.pause((5-i) / 3)




# The game starts here.
label start:
    scene black

    jump scene01