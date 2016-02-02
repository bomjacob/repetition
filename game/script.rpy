
init:
    define me = Character(name="Me", who_color="#eeeeee")
    define sensei = Character(name='Sensei', who_color="#ee3342", image="sensei")
    define froggy = Character(name='Froggy', who_color="#D6FF95", image="froggy")


# The game starts here.
label start:
    scene black

    jump scene01