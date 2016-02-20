# Based on http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=22481
label credits(frommenu=False):
    if not frommenu:
        if persistent.credits_seen is None:
            $ persistent.credits_seen = False
        $ hard = not persistent.credits_seen
    else:
        $ hard = False
    scene black
    with dissolve

    if not frommenu:
        show theend:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=hard)
        hide theend

    show cred
    $ renpy.pause(credits_speed, hard=hard)
    hide cred

    if not frommenu:
        show thanks:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(4, hard=hard)
        hide thanks

        $ persistent.credits_seen = True

    return

label credits_frommenu:
    call credits(True) from _call_credits_1

init python:
    cred_raw = (
        (_('Lead Developer'), ('Jacob Bom',)),
        (_('Lead Artist'), ('Olivia Hjorth',)),
        (_('Lead Handyman'), ('Nick Zhu',)),
        (_('Assets'), (
            (_('Background'), (
                _('mugenjohncel on lemmesoft.renai.us'),
                _('hellohello.dousetsu.com/free_material.html')
            )),
            (_('Sound and Music'), (
                _('Various SFX from www.freesound.org'),
                _('www.newgrounds.com/audio/listen/665861'),
                _('www.newgrounds.com/audio/listen/668009'),
                _('2 and 10 on BGM 9 by ASOBEAT'),
                _('Various BGM from pianosdauge.org/BGM/list.html'),
                _('\nImpending Boom, First Call, Unity, Not As It Seems, On the Cool Side, Carefree Investigations, Spy Glass, Twisted, Oppressive-Gloom, Kawai Katsune, The Forest and the Trees Arcadia, Water Prelude, Teller of the Tales, Take a Chance, To the Ends, Volatile Reaction and Looping String, Kevin MacLeod (incompetech.com)\nLicensed under Creative Commons: By Attribution 3.0 License\nhttp://creativecommons.org/licenses/by/3.0/')
            )),
            (_('Other'), (
                _('{size=-5}Letter:{/size}\nwww.flickr.com/photos/playingwithpsp/2546732435'),
            ))
        )),
        (_('Engine'), ("\n".join(str.split(renpy.version())),))
    )
    credits_s = _("{color=#fff}{size=80}Credits\n")
    for c in cred_raw:
        if c[0] == _("Assets"):
            credits_s += "\n{size=40}" + c[0]
            for subc in c[1]:
                credits_s += "\n{size=30}" + subc[0] + "\n{size=20}" + "\n".join(subc[1]) + "\n"
        else: 
            credits_s += "\n{size=40}" + c[0] + "\n{size=60}" + "\n".join(c[1]) + "\n"
    
init:
    $ credits_speed = 20
    image cred:
        Text(credits_s, text_align=0.5, xmaximum=740)
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        linear credits_speed ypos 0.0 yanchor 1.0
    image theend = Text(_("{color=#fff}{size=80}The end"), text_align=0.5)
    image thanks = Text(_("{color=#fff}{size=80}Thanks for Playing!"), text_align=0.5)
