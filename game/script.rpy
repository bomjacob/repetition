
init:
    define me = Character(name="Me", who_color="#eeeeee")
    define sensei = Character(name='Sensei', who_color="#ee3342", image="sensei")
    define froggy = Character(name='Froggy', who_color="#D6FF95", image="froggy")


# The game starts here.
label start:
    scene black

    "*door to house opens*"

    scene sensei_room with dissolve

    show sensei dead with dissolve

    sensei "I'm dead, danmit!"

    me "Oh no!"

    me "Well... no time to dwell on the bad things. The mayor needs my help."

    scene town_square_with_people with fade

    show froggy hi with dissolve

    froggy "It's everyone's favourite mayor, Froggy!"

    show overlay flames with dissolve

    "Flames!"

    show overlay shitty_poster with dissolve

    "Shitty Poster"

    hide overlay

    "Okay, choice test"

    jump postermm_start

    return


label postermm_start:
    $ postermm_points = 0
    $ postermm_done = {}

    show overlay shitty_poster

    "Here is a poster.{w}Do you see anything wrong with it?"

    hide overlay

    menu:
        "{fast}Do you see anything wrong with it?"
        "The poster looks fine to me :)":
            jump postermm_fine
        "Yeah, it's not quite right.":
            "What would you say is wrong?"
            jump postermm_wrong
        "It's absolute shit":
            jump postermm_shit
        "Let me see the poster again please.":
            jump postermm_show

label postermm_fine:
    "You will now die :/"

    return

label postermm_wrong:
    menu:
        "(select a category)"
        "The heading" if (not 'heading' in postermm_done):
            $ postermm_done['heading'] = True
            jump postermm_heading
        "The typography" if not 'typography' in postermm_done:
            $ postermm_done['typography'] = True
            jump postermm_typography
        "The colours" if not 'colours' in postermm_done:
            $ postermm_done['colours'] = True
            jump postermm_colours
        "The text in general" if not 'text' in postermm_done:
            $ postermm_done['text'] = True
            jump postermm_text
        "AIDA" if not 'aida' in postermm_done:
            $ postermm_done['aida'] = True
            jump postermm_aida
        "Nothing, it looks fine now.":
            jump postermm_done
        "Let me see the poster again please.":
            jump postermm_show

label postermm_shit:
    "You will now die :/"

    return

label postermm_heading:
    menu:
        "What's wrong with the heading?"
        "It's too big":
            "Nah, it certainly shouldn't be smaller. Then people couldn't see it!"
            $ postermm_points -= 1
        "It's too small":
            "Yes, it could be a bit bigger, I guess."
            $ postermm_points += 1
        "You should totally use WordArt! It's the professional choice!":
            "Uhmm.. just no... no."
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump postermm_show
    jump postermm_back


label postermm_typography:
    menu:
        "What's wrong with the typography?"
        "The body text should be always without serifs.":
            "Are you sure that's quite right?"
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump postermm_show
    jump postermm_back



label postermm_colours:
    menu:
        "What's wrong with the colours?"
        "The colour of the body really shouldn't match the background. It makes it very difficult to distinguish.":
            "Yeah, i guess you're right. It {i}is{/i} quite hard to read."
            $ postermm_points += 1
        "The white background is a tad boring. How about making it red?":
            "Uhmm.. are you sure...?"
            $ postermm_points -= 1
        "Black font colour is also boring, try pink!":
            "Uhmm.. that would make it hard to see."
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump postermm_show
    jump postermm_back


label postermm_text:
    menu:
        "What's wrong with the text?"
        "It's full of grammatical and spelling errors.":
            "Yeah, I didn't go to school. Whoops."
            $ postermm_points += 1
        "The First Letter In Every Word Should Be Capitalized.":
            "Uhmm, that's not what they tought me in school."
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump postermm_show
    jump postermm_back


label postermm_aida:


label postermm_back:
    "Anything else wrong with this poster?"

    menu:
        "Yes":
            "What else is wrong with it then?"
            jump postermm_wrong
        "No, it's fine now":
            "Okay, if you say so"
            jump postermm_done
        "Let me see the poster again please.":
            jump postermm_show

label postermm_done:
    "You scored [postermm_points] points :)"
    
    return

label postermm_show:
    show overlay shitty_poster

    "Here you go."

    hide overlay

    $ renpy.rollback(force=True, checkpoints=2)

