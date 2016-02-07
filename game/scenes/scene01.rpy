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
    "I looked around in confusion. The room was exactly like I had left it, when I had gone to bed.{w} But sensei was nowhere in sight."
    "I found the kettle that we usually use for boiling water.{w} It was completely cold."
    "I was about to walk away when I noticed a small slip of paper."

    me "Wait, is that..?"

    "I picked it up{nw}"
    show overlay sensei_letter at top with dissolve
    extend ", reading over each word carefully."

    "As I read over the words, I could not help but despair.{w} The outside world sounded like a dangerous place, filled with mystery and horror. But then,{w} I thought back to my sensei's words.."

    hide overlay

    "Flashback!"
    show sensei
    sensei "With the power of communication/IT we can do {i}everything!{/i}"
    hide sensei
    "End flashback"

    "With a look of determination in my eyes, I grabbed my bag and packed only the things of utmost necessity."

    scene mountains

    "As I opened the door and looked at the mountains stretching out before me, I felt an ounce of regret."

    menu:
        "Go back and stay?"
    
        "No! Go on an adventure!":
            jump __adventure
    
        "Yeah... No place is better than home.":
            jump __back_home

label __back_home:
    "With a sigh of resignation, I turned back towards the house.\n"
    scene sensei_room
    extend "Walking back inside, I slammed the door behind me."
    #$ renpy.sound.play("sound/fx/door_slam.ogg")
    me "I suppose... I couldn't do it after all."

    "I looked at the companion cube on the floor."

    me "But you still love me... Right?"
    show cubey cubey at left with dissolve:
        yoffset -50
        zoom 0.3
    cubey "I will love you forever! So now, don't go running off again... Don't... {w}Be... {w}Naughty."
    "I gave the companion cube worried glances, as I slowly backed away."
    show cubey cubey at left:
        yoffset -50
        zoom 0.3
        1.0
        linear 0.3 zoom 0.35
        1.0
        linear 0.3 zoom 0.40
        1.0
        linear 0.3 zoom 0.45
    "The cube seemed to move towards me, getting ever so slightly closer, every time I blinked."

    "The companion cube was getting awfully close now. A hollow noise resounded as my back hit the wall."
    cubey "Nowhere to go, nowhere to go, nowhere to go..."
    $ die(last_words="No one was close enough to hear my screams.")

label __adventure:
    "With a sigh, I slammed the door shut behind me, and looked towards the horizon.{w} The journey before me would be long and arduous, but I knew that I had no choice. It was my fate."

    scene black
    #scene 

    me "Oh, wow... It feels like I've been walking for days!"
    "I looked at the city rising up before me, my entire body aching from a long and tiring walk.{w} At least, that was what my body told me. My map told a different story."
    me "I should find a place to rest..."
    "I looked around at the houses gathered. Many of them had lights on behind the windows, though most of them had their curtains down. The streets were entirely empty, except for a few bottles lying about, and a stray cat every once in a while. A tumbleweed would not be misplaced."

    me "I wonder where all the people are?"
    "Walking a bit further down the road revealed a pompous-looking house with the sign “Mayor” above the entrance. {w}A confused-looking frog was standing by the entrance, looking at a piece of paper on the wall while mumbling to himself. {w}The frog suddenly seemed to notice me, and waved me over."

    show froggy hi with dissolve

    show froggy hi_talking with dissolve

    froggy "Greetings!{w} Salutations!{w} Might I ask who you are, and what you are doing here?"

    show me at right
    show froggy hi_talking at left with move

    me "Uh... Yeah... Hi. My name is [name]! I'm really just passing by, though I would like to know if you have any places to stay?"
    froggy "I am glad to make your acquaintance, [name]!"
    froggy talking "I am called Froggy! I am the mayor of this small town." #this one?
    froggy "Being a small town as this is, I can't say that we have any hotels or the likes. Sorry to disappoint you."
    me "No, it's okay. I suppose I should be on my way, then?"
    froggy "W-wait a second! Actually, there is something I could use a second opinion on. Would you mind staying for a bit, helping out a mayor in need?"

    menu:
        "Help Mayor Froggy?"
        "No":
            jump __no_help
        "Yes":
            jump __postermm_start

label __no_help:
    me "Actually, I'm... Rather busy at the moment! If you wouldn't mind, I need to be on my way."
    froggy confused "That's a shame. I hope nothing bad happens to you on your journey, though." #By displeased do you mean confused?
    "I turned my back towards the mayor, and started walking out of the small town. Since it was a small town, the walk wasn't very far."

    #scene ?
    "At the edge of the city, a large forest stretched out before me. The thick crowns cast solid shadows on the ground, making it harder to see, but not impossible. A small forest path twisted its way between the trees."
    "I started walking along the forest path, enjoying the gentle breeze that whistled through the trees.{w} The path slowly grew more unclear, until it dwindled down into several smaller animal paths."

    #scene ?
    "As I got further into the woods, I finally had to admit that I was lost. The large canopy had grown thicker, letting even less light come through the countless leaves. The wind that had earlier been nice and refreshing, suddenly felt harsh and prickly on my skin."
    "My ears suddenly picked up on a very low sound. Something that sounded almost like... A growl?..."
    "Looking around in confusion, I searched for the source of the sound. Surely it couldn't have been my imagination?"

    "As the leaves of a bush rustled to my right, I whipped my head in that direction. *show wolves* Out of the bush appeared five large, black wolves, snarling menacingly, with their teeth bared, and their eyes fixed on me."
    me "E-... Easy now... I'm sure we can work this out, yes...?"
    "My plea was answered by a sharp bark from the foremost wolf, followed up by barks from the four others behind it. I was about to turn around and make a run for it, when the wolves finally decided to jump at me."
    me "B-... Blood?... Is this... My blood?..."
    me "AAARRGGGHHHHH"
    $ die(last_words="The woods were finally filled with silence.")
    

label __postermm_start:
    $ postermm_points = 0
    $ __postermm_done = {}

    froggy "I am glad to hear it, [name]."
    froggy "See, I have been working on a campaign to reduce the number of bottles and cans lying about. Sadly, the people in this village don't seem to care much about their mayor! Or the environment, for that matter."
    me "So what do you want me to do?"
    froggy "Well, I was thinking of making a promotional poster, to raise awareness about the impending doom, that comes from littering bottles everywhere!"
    "I raised an eyebrow at the Mayor, but didn't feel the need to inquire further about the matter. He took the poster from the wall, and raised it in front of me."

    show overlay shitty_poster

    froggy "So what do you think?"

    hide overlay

    menu:
        "How does the poster look?"
        "It looks amazing!":
            jump __postermm_fine
        "It needs some work...":
            froggy talking "What would you say is wrong?"
            jump __postermm_wrong
        "It's fucking terrible!":
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
    froggy "The mayor's eye spasmed a bit, as he stared at me with malice."
    froggy murderous "You... What? How dare you say that to me, the mighty mayor?!"

    "I quickly backed off, as a red aura started to envelop the mayor."
    froggy "We don't... Use swear words here... It's against the law!"
    "As those deep red eyes caught mine, I found that I could no longer move a muscle. As I stood there, helpless, he walked towards me."
    froggy "Do you know what happens to lawbreakers in town, hmm?"
    "The mayor was now close enough, that I could feel the stinging red aura, slowly peeling away my skin."
    froggy "You may never utter a swearword again."
    $ die(last_words="Have you never heard of constructive criticism?", last_words_person=froggy)


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