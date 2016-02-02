init python:
    if persistent.disclaimer_seen is None:
        persistent.disclaimer_seen = False

label splashscreen: #TODO: REMOVE no
    scene black
    $ renpy.pause(0.5, hard=True)

    image disclaimer:
        Text("""\n{color=#fff}{size=80}Disclaimer{/size}\n\n{size=25}This game is shit. Like really... This is a shitty school project. Why would you even download this?!?{/size}{/color}""", text_align=0.5, xmaximum=740)
    image ctc:
        linear 0.75 alpha 1.0
        Text("""{color=#fff}{size=20}Press any key to continue{/size}{/color}\n""", text_align=0.5, xmaximum=740)
        linear 0.75 alpha 0.25
        repeat

    show disclaimer at top with dissolve
    if not persistent.disclaimer_seen:
        $ renpy.pause(5.0, hard=True)
        show ctc at center with dissolve
        $ renpy.pause()
    else:
        show ctc at center with dissolve
        $ renpy.pause(3)
    hide disclaimer
    hide ctc
    with dissolve
    $ persistent.disclaimer_seen = True

    show text "{color=#fff}{size=+40}Neko Productions {/size}{image=ui/neko.png}\n{size=+10}presents...{/size}{/color}" at truecenter with dissolve
    $ renpy.pause(2, hard=False)

    hide text with dissolve
    $ renpy.pause(0.5, hard=False)

    return