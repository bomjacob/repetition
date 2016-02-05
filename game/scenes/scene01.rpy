# Code for scene 1, including the code for the poster minigame at the beginning of the game

label scene01:
    centered "{size=+10}Let me tell you a story.{/size}"
    centered "{size=+10}{cps=*0.25}Ah...{/cps} But where do I start?{/size}"
    centered "{size=+10}I suppose I should start with my name.{/size}"
    centered "{size=+10}I am [name] SURNAME.{/size}"

    show book sensei_and_me
    $ renpy.pause(5)
    "I have been living with my sensei for as long as I remember.{w} While he might not be family, he is the only person I have left."

    show book flames
    $ renpy.pause(5)
    "I barely remember my parents. They went away when I was little...{w} Sensei never wanted to tell me about them, other than that they were supposedly heroes.{w} I believe him."

    show book home
    $ renpy.pause(5)
    "And in their absence, he has cared for me in his mountaintop home. He has taught me everything I know.{w} While his house might seem out of the way at first, it is actually a technological heaven.{w} He specialises in a subject known as \“Communication and IT\”."

    "He really is an amazing person!{cps=1}...{/cps} Or should I say “was”.."

    hide book with dissolve
    centered "{size=+10}This is where my story begins.{/size}"
    
    "I opened my eyes slowly. Sunlight streamed in from the windows."

    scene sensei_room with dissolve
    show me with dissolve

    "This was weird... Sensei would usually have woken me by now."

    show sensei dead with dissolve

    sensei "I'm dead, danmit!" with shake

    me "Oh no!"

    me "Well... no time to dwell on the bad things. The mayor needs my help."

    scene town_square_with_people with fade

    show froggy hi with dissolve

    froggy "It's everyone's favourite mayor, Froggy!"

    froggy talking "Hello (name of main char), I need your help."

    menu:
        "Help Mayor Froggy?"
        "No":
            froggy "I really thought I could count on you for help."
            "Die by wolves :/"
            return
        "Yes":
            froggy "Thank you so much! I knew i could count on you."
            jump __postermm_start


label __postermm_start:
    $ postermm_points = 0
    $ __postermm_done = {}

    show overlay shitty_poster

    froggy "Here is a poster.{w}\nDo you see anything wrong with it?"

    hide overlay

    menu:
        "Anything wrong with the poster?"
        "The poster looks fine to me :)":
            jump __postermm_fine
        "Yeah, it's not quite right.":
            froggy talking "What would you say is wrong?"
            jump __postermm_wrong
        "It's absolute shit":
            jump __postermm_shit
        "Let me see the poster again please.":
            jump __postermm_show


label __postermm_fine:
    froggy "You will now die :/"

    return


label __postermm_wrong:
    menu:
        "(select a category)"
        "The heading" if (not 'heading' in __postermm_done):
            $ __postermm_done['heading'] = True
            jump __postermm_heading
        "The typography" if not 'typography' in __postermm_done:
            $ __postermm_done['typography'] = True
            jump __postermm_typography
        "The colours" if not 'colours' in __postermm_done:
            $ __postermm_done['colours'] = True
            jump __postermm_colours
        "The text in general" if not 'text' in __postermm_done:
            $ __postermm_done['text'] = True
            jump __postermm_text
        "AIDA" if not 'aida' in __postermm_done:
            $ __postermm_done['aida'] = True
            jump __postermm_aida
        "Nothing, if you fix those errors it's fine." if postermm_points != 0:
            jump __postermm_done
        "Let me see the poster again please.":
            jump __postermm_show


label __postermm_shit:
    froggy "You will now die :/"

    return


label __postermm_heading:
    menu:
        "What's wrong with the heading?"
        "It's too big":
            froggy talking "Nah, it certainly shouldn't be smaller. Then people couldn't see it!"
            $ postermm_points -= 1
        "It's too small":
            froggy "Yes, it could be a bit bigger, I guess."
            $ postermm_points += 1
        "You should totally use WordArt! It's the professional choice!":
            froggy "Uhmm.. just no... no."
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_typography:
    menu:
        "What's wrong with the typography?"
        "The body text should be always without serifs.":
            froggy "Are you sure that's quite right?"
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_colours:
    menu:
        "What's wrong with the colours?"
        "The colour of the body really shouldn't match the background. It makes it very difficult to distinguish.":
            froggy "Yeah, i guess you're right. It {i}is{/i} quite hard to read."
            $ postermm_points += 1
        "The white background is a tad boring. How about making it red?":
            froggy "Uhmm.. are you sure...?"
            $ postermm_points -= 1
        "Black font colour is also boring, try pink!":
            froggy "Uhmm.. that would make it hard to see."
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_text:
    menu:
        "What's wrong with the text?"
        "It's full of grammatical and spelling errors.":
            froggy "Yeah, I didn't go to school. Whoops."
            $ postermm_points += 1
        "The First Letter In Every Word Should Be Capitalized.":
            froggy "Uhmm, that's not what they tought me in school."
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_aida:
    me "Did you use the AIDA model to create this?"
    froggy "Uhmm. No. What's that?"

    menu:
        "What is the AIDA model?"
        "Action-Interest-Disire-Action":
            froggy "Action twice? That seems wrong"
            $ postermm_points -= 1
        "Attention-Ideas-Disinterest-Action":
            froggy "Why would I want someone to be disinterested?!"
            $ postermm_points -= 1
    jump __postermm_back

label __postermm_back:
    "Anything else wrong with this poster?"

    menu:
        "Yes":
            froggy "What else is wrong with it then?"
            jump __postermm_wrong
        "No, it's fine now":
            froggy "Okay, if you say so"
            jump __postermm_done
        "Let me see the poster again please.":
            jump __postermm_show

label __postermm_done:
    "DEBUG: You scored [postermm_points] points :)"
    
    if postermm_points <= 2:
        froggy "I still don't like it very much."
        "You dead :/"
        return
    elif postermm_points > 2 and postermm_points <= 4:
        froggy "Well I guess it turned out allright."
        jump __speech
    elif postermm_points >= 5:
        froggy "It's perfect! Thank you so much!"
        jump __speech
    
    return

label __postermm_show:
    show overlay shitty_poster

    froggy "Here you go."

    hide overlay

    $ renpy.rollback(force=True, checkpoints=2)

label __speech:
    froggy "Bla bla bla. Recycling and whatnot."

    froggy "Would you like to stay with me in my mansion and help me with my campaign?"
    menu:
        "Stay with Mayor Froggy?"
        "Yes! I'd love to live in your mansion!":
            if postermm_points >= 5:
                jump __too_sucessful
            else:
                jump __not_quite
        "No! I would like to leave this village now.":
            if postermm_points >= 5:
                $ village_dead = True
                jump __end
            else:
                froggy "Have it your way then! Don't say I didn't give you a chance though."
                "You dead by the wolf squad of Mayor Froggy"
                return


label __too_sucessful:
    froggy "The campaign is going so incredibly well!"
    froggy "Perhaps even {i}too{/i} well"
    jump __dragon_eat

label __not_quite:
    froggy "The campaign is not going quite as well as I was hoping."
    froggy "Sure you fixed all the errors with that poster?"
    menu:
        "Did you fix {i}all{/i} the errors with the poster?"
        "Yes, of course I did.":
            froggy "That dragon sure seems to think otherwise!"
            jump __dragon_eat
        "I'm sorry... I might have made a few mistakes.":
            froggy "Yeah, I think you did."
            froggy "It's alright though, though you should probably leave my mansion."
            froggy "Like right now."
            froggy "Just leave already!"
            jump __end


label __dragon_eat:
    show magenta mad at right

    "Oh no! A dragon!"

    "You dead :/"

    return


label __end:
    #If village dead then hear dragon in distance

    "I left the village to continue my journey..."
    jump scene02