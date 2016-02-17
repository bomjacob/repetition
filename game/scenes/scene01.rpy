# Code for scene 1, including the code for the poster minigame at the beginning of the game

label scene01:
    $ renpy.music.stop(fadeout=1)
    $ renpy.music.queue("sound/music/Serene-Separations-Soundtrack.ogg", loop=True, fadein=1)
    with Fade(0.5, 1.0, 0.5)

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

    "He really is an amazing person!{cps=1}...{/cps} Or should I say \“was\”.."

    hide book with dissolve
    centered "{size=+10}This is where my story begins.{/size}"
    
    "I opened my eyes slowly. Sunlight streamed in from the windows."

    scene sensei_room with dissolve

    "This was weird... Sensei would usually have woken me by now."
    "I looked around in confusion. The room was exactly like I had left it, when I had gone to bed.{w} But sensei was nowhere in sight."
    "I found the kettle that we usually use for boiling water.{w} It was completely cold."
    "I was about to walk away when I noticed a small slip of paper."

    me "Wait, is that..?"

    "I picked it up,{w}"
    show overlay sensei_letter at top with dissolve
    extend " reading over each word carefully."

    "As I read over the words, I could not help but despair.{w} The outside world sounded like a dangerous place, filled with mystery and horror. But then,{w} I thought back to my sensei's words.."

    hide overlay

    scene sensei_room_flashback
    with flash
    show sensei with dissolve
    sensei "With the power of communication/IT we can do {i}everything!{/i}"
    hide sensei with dissolve
    scene sensei_room
    with flash

    "With a look of determination in my eyes, I grabbed my bag and packed only the things of utmost necessity."

    scene mountains
    with door_trans
    $ renpy.sound.play("sound/fx/door_close.ogg")

    "As I closed the door behind me and looked at the mountains stretching out before me, I felt an ounce of regret."

    menu:
        "Go back and stay?"
    
        "No! Go on an adventure!":
            jump __adventure
    
        "Yeah... No place is better than home.":
            jump __back_home

label __back_home:
    "With a sigh of resignation, I turned back towards the house.\n"
    scene sensei_room
    with door_trans
    $ renpy.sound.play("sound/fx/door_close.ogg")
    extend "Walking back inside, I slammed the door behind me."
    me "I suppose... I couldn't do it after all."

    "I looked at the companion cube on the floor."

    me "But you still love me... Right?"
    show cubey cubey at left with dissolve:
        yoffset -50
        zoom 0.3
    cubey "I will love you forever! So now, don't go running off again... {w}Don't... {w}Be... {w}Naughty."
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
    $ die(0)
    "No one was close enough to hear my screams."
    jump you_dead

label __adventure:
    "With a sigh, I cast away my doubts, and looked towards the horizon.{w} The journey before me would be long and arduous, but I knew that I had no choice. It was my fate."

    scene cliffs with fade_scene
    
    $ renpy.pause(5)

    scene town town with fade_scene

    me "Oh, wow... It feels like I've been walking for days!"
    "I looked at the city rising up before me, my entire body aching from a long and tiring walk.{w} At least, that was what my body told me. My map told a different story."
    me "I should find a place to rest..."
    "I looked around at the houses gathered. Many of them had lights on behind the windows, though most of them had their curtains down. The streets were entirely empty, except for a few bottles lying about, and a stray cat every once in a while. A tumbleweed would not be misplaced."

    me "I wonder where all the people are?"

    scene mansion ext with fade_scene
    "Walking a bit further down the road, revealed a pompous-looking house with the sign “Mayor” above the entrance. {w}A confused-looking frog was standing by the entrance, looking at a piece of paper on the wall while mumbling to himself. {w}"

    show froggy hi with dissolve
    extend "The frog suddenly seemed to notice me, and waved me over."

    show froggy hi_talking with dissolve

    $ renpy.sound.play("sound/fx/First Call.ogg")

    froggy "Greetings!{w} Salutations!{w} Might I ask who you are, and what you are doing here?"

    me "Uh... Yeah... Hi. My name is [name]! I'm really just passing by, though I would like to know if you have any places to stay?"
    froggy "I am glad to make your acquaintance, [name]!"
    froggy talking "I am called Froggy! I am the mayor of this small town."
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
    froggy confused "That's a shame. I hope nothing bad happens to you on your journey, though."

    scene town walk

    "I turned my back towards the mayor, and started walking out of the town. Since it was a small town, the walk wasn't very far."

    $ renpy.music.stop(fadeout=1)
    $ renpy.music.queue("sound/music/Unity.ogg", loop=True, fadein=1)
    scene forest start
    with Fade(0.5, 1.0, 0.5)

    "At the edge of the city, a large forest stretched out before me. The thick crowns cast solid shadows on the ground, making it harder to see, but not impossible. A small forest path twisted its way between the trees."
    "I started walking along the forest path, enjoying the gentle breeze that whistled through the trees.{w} The path slowly grew more unclear, until it dwindled down into several smaller animal paths."

    scene forest dark
    "As I got further into the woods, I finally had to admit that I was lost. The large canopy had grown thicker, letting even less light come through the countless leaves. The wind that had earlier been nice and refreshing, suddenly felt harsh and prickly on my skin."
    "My ears suddenly picked up on a very low sound. Something that sounded almost like... A growl?..."
    "Looking around in confusion, I searched for the source of the sound. Surely it couldn't have been my imagination?"

    "As the leaves of a bush rustled to my right, I whipped my head in that direction. {nw}"

    show wolves normal at right with dissolve

    extend "Out of the bush appeared five large, black wolves, snarling menacingly, with their teeth bared, and their eyes fixed on me."
    me "E-... Easy now... I'm sure we can work this out, yes...?"
    "My plea was answered by a sharp bark from the foremost wolf, followed up by barks from the four others behind it. {w}I was about to turn around and make a run for it, when the wolves finally decided to jump at me."
    me "B-... Blood?... Is this... My blood?..."
    me "AAARRGGGHHHHH"
    $ die(1)
    "The woods were finally filled with silence."
    jump you_dead
    

label __postermm_start:
    $ postermm_points = 0
    $ __postermm_done = {}

    froggy neutral_talking "I am glad to hear it, [name]."
    "The mayor showed me inside his house, and we sat down in the living room."

    scene mansion livingroom with fade_scene
    show froggy neutral_talking with dissolve
    froggy "See, I have been working on a campaign to reduce the number of bottles and cans lying about. Sadly, the people in this village don't seem to care much about their mayor! Or the environment, for that matter."
    show froggy neutral
    me "So what do you want me to do?"
    froggy neutral_talking "Well, I was thinking of making a promotional poster, to raise awareness about the impending doom, that comes from littering bottles everywhere!"
    "I raised an eyebrow at the Mayor, but didn't feel the need to inquire further about the matter. He took the poster from the wall, and raised it in front of me."

    show overlay shitty_poster

    $ renpy.music.stop(fadeout=2)
    $ renpy.music.queue(["sound/music/ASOBEAT-BGM9-2.ogg", "sound/music/ASOBEAT-BGM9-10.ogg"], loop=True, fadein=1)

    froggy "So what do you think?"

    hide overlay

    menu:
        "How does the poster look?"
        "It looks amazing!":
            jump __postermm_amazing
        "It needs some work...":
            froggy talking "What would you say is wrong?"
            jump __postermm_wrong
        "It's fucking terrible!":
            jump __postermm_shit
        "Let me see the poster again please.":
            jump __postermm_show


label __postermm_amazing:
    me "It looks fantastic! That has to be the best promotional poster I've ever seen!"
    froggy neutral_talking "Really? You think so? I suppose I should print a couple of thousand posters then, and hang them about. Thanks for the help!"
    show froggy neutral
    me "No problem!"
    hide froggy with fade
    "As I waved to him and walked towards the edge of the village, I felt a bit of doubt. Had I chosen the right thing?"
    $ renpy.music.stop(fadeout=1)
    $ renpy.music.queue("sound/music/Not-As-It-Seems.ogg", loop=True, fadein=1)
    scene forest dark
    with Fade(0.5, 1.0, 0.5)

    "As I approached the forest, the air felt overwhelmingly humid. Small insects and lizards were scurrying around on the forest floor, as I took a weary step forwards.{w} It didn't feel directly hostile. The forest was simply so full of life that it itself felt alive."
    "The trees were swaying in the gentle wind that seemed to blow through the crowns, though barely a breeze could be felt on the forest floor. The rustling of leaves almost made it seem like the trees were having a conversation."
    "While I was following the forest path, looking up at the sky, I suddenly tripped."
    me "Aa-... Huh?"
    "I used my hands to soften the blow, as I looked behind me to see what I tripped over. {w}I couldn't see anything large enough to trip over."
    me "That's... Weird."
    "While mumbling to myself, I got up again and dusted off my palms and knees. {w}Were.. Those trees always so close?"
    "Suddenly, something gripped my ankle tightly. {w}Looking back in fright, I found a mossy root protruding from the ground, coiled around my ankle like a snake. {w}I tried kicking out with my leg to shake it off, but the root adamantly held its ground."
    "As I was distracted by the stubborn root, a second one shot out of the ground and fastened my right wrist. I raised my left hand to try and get it off of me, but the moment I was about to grab it, a third root shot out of the ground and entangled my left wrist too."
    "Fighting futilely against the roots, I could do nothing but look as large network of roots slowly entangled my entire body. An especially thick one lazily burst out of the ground next to me, wrapping itself around my stomach before going back into the earth. {w}It's grip slowly tightened as it dragged me downwards, forcing the air out of my lungs, as the earth slowly swallowed me whole."
    $ die(1)
    "Not even a trace was left."
    jump you_dead


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
    froggy murderous_talking "You... What? How dare you say that to me, the mighty mayor?!"
    show froggy_murderous
    "I quickly backed off, as a red aura started to envelop the mayor."
    froggy murderous_talking "We don't... Use swear words here... It's against the law!"
    show froggy murderous
    "As those deep red eyes caught mine, I found that I could no longer move a muscle. As I stood there, helpless, he walked towards me."
    froggy murderous_talking "Do you know what happens to lawbreakers in town, hmm?"
    show froggy murderous
    "The mayor was now close enough, that I could feel the stinging red aura, slowly peeling away my skin."
    show overlay red_haze with dissolve
    froggy murderous_talking"You may never utter a swearword again."
    $ die(1)
    froggy "Have you never heard of constructive criticism?"
    hide overlay
    jump you_dead    


label __postermm_heading:
    menu:
        "What's wrong with the heading?"
        "It's too big":
            froggy talking "Do you think so? I certainly have trouble seeing it as it is, at least without glasses. But I am sure that you're more qualified to say so than I."
            $ postermm_points -= 1
        "It's too small":
            froggy "Yes, I suppose it could be a bit larger. We really want the message to stand out, to attract more people!"
            $ postermm_points += 1
        "You should totally use WordArt! It's the professional choice!":
            froggy "What did you say? Well.. I suppose I do have word, but are you truly sure about this? It looks like something my grandson would do."
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_typography:
    menu:
        "What's wrong with the typography?"
        "The body text should be always without serifs.":
            froggy "Are you sure about that? I think it puts a bit of strain on the eyes, but I suppose you know best."
            $ postermm_points -= 1
        "You should use a fancy cursive font!":
            froggy "Wouldn't that be hard to read? People shouldn't have to strain their eyes to read the message."
            $ postermm_points -=1
        "You should use the same font for all of text.":
            froggy "Yes... I suppose I see what you mean by that. The text by the pricing is definitely a different font."
            $ postermm_points +=1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_colours:
    menu:
        "What's wrong with the colours?"
        "The colour of the body shouldn't match the background. It makes it difficult to distinguish.":
            froggy "Yes, I suppose you're right. It {i}is{/i} quite hard to read. I just really like green."
            $ postermm_points += 1
        "The white background is a tad bit boring. How about making it red?":
            froggy "Are you sure? Red seems quite stressing for the eyes, and a bit aggressive. We don't want to scare people away!"
            $ postermm_points -= 1
        "Black font colour is a bit boring. Try pink!":
            froggy "While it is a pretty colour and all, wouldn't that be difficult to see?.. Oh, well, I suppose you know best."
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_text:
    menu:
        "What's wrong with the text?"
        "It's full of grammatical errors and spelling errors!":
            froggy "Oh?.. Well, I wasn't quite sure how to spell a lot of these things, and I didn't bother to look the words up in a dictionary. {w}I'll have my secretary check through this."
            $ postermm_points += 1
        "The First Letter In Every Word Should Be Capitalized.":
            froggy "What, isn't that what they do in Germany or something?"
            $ postermm_points -= 1
        "This text is missing exclamation points!!1!":
            froggy "What now? Why did you add that number at the end of your sentence?"
            $ postermm_points -=1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_aida:
    me "Did you use the AIDA model to create this?"
    froggy confused "Ai-what now? Ai desu?"
    me "No, no, it's a communication model."

    menu:
        "So what is this so-called AIDA model?"
        "Action-Interest-Disire-Action":
            froggy "Action twice? That seems wrong"
            $ postermm_points -= 1
        "Attention-Ideas-Disinterest-Action":
            froggy "Why would I want someone to be disinterested?"
            $ postermm_points -= 1
        "Another-Invisible-Dragon-Attack":
            froggy "Dragon attack? Where?"
            $ postermm_points -= 1
        "Attention-Interest-Desire-Action":
            froggy "Now that you mention it, I do think I've heard of that somewhere before. I could probably ask my secretary to do something with that."
            $ postermm_points +=1
    jump __postermm_back

label __postermm_back:
    "Anything else wrong with this poster?"

    menu:
        "Yes":
            froggy "What else is wrong with it then?"
            jump __postermm_wrong
        "No, it's fine now":
            froggy "Let's take a look at it, then..."
            jump __postermm_done
        "Let me see the poster again please.":
            jump __postermm_show

label __postermm_done:    
    if postermm_points <= 2:
        jump __postermm_lose
    elif postermm_points > 2 and postermm_points <= 4:
        froggy neutral_talking "Well I guess it turned out alright. It is definitely better than it was before! {w}This campaign might not turn out to be be a total failure after all."
        jump __beforespeech
    elif postermm_points >= 5:
        froggy "This.. This is much better than I thought it could be! {w}This is sure to attract lots of people. Thank you very much!"
        jump __beforespeech
    
    return

label __postermm_lose:
    me "So?.. What do you think?"
    "Mayor Froggy tilted his head as he stared at the poster with something that might have been disgust."
    froggy confused "Well, uhh, I'd say the results are.. Debatable."
    show froggy neutral
    "I frowned slightly. Had I not done my best to make this campaign a success? Of course I knew the importance of helping the environment. {w}The mayor coughed lightly, bringing my attention back to him."
    froggy neutral_talking "I think we should call it a day, then. "
    "I nodded my head, looking at the front door.{w} Just as I was about to exit the room, however.."

    $ renpy.music.stop(fadeout=5)
    $ renpy.music.queue("sound/music/Volatile-Reaction.ogg", loop=True, fadein=5)

    "Mayor Froggy and I both turned immediately, as a shrill shriek abruptly came from behind us. {w}We both stood there for a while, looking for the source of the ear-piercing sound."
    "Another shriek echoed, turning both of our attention to the discarded poster. {w}It.. Didn't look like a poster anymore.{w} Instead, what used to be a terrible poster had turned into a terrifying paper monster, with sharp teeth and an even sharper voice."
    "I covered my ears as what appeared to be a mouth opened to shriek once again."
    me "What is that even?"
    froggy scared_talking "It would seem to be the poster. But hey, what's the worst it can do, give us p-paper cuts?"
    show froggy scared
    "The mayor attempted to make a joke, but his unsure voice made it sound more like a failed attempt at seeming brave. In reality, the frog was trembling in place. The poster seemed to glare at us - or at least, that was what it would have done, had it eyes."
    "Still, what's the worst a single poster can do?"
    "I instantly regretted that thought, as more prototype posters rose up behind the first one, the next more hideous than the previous, all having terrifying voices to match. They seemed to rip themselves apart, to form new, more spiky versions of themselves."
    "I ran towards the door in a final attempt at getting away, when I noticed that we had been surrounded. Several poster monsters stood in the way and hissed at me before I could even get close to the door."
    "All of them slowly moved closer in their own bizarre ways, as mayor Froggy and I moved closer together."
    froggy scared_talking "I suppose th-this.. Would be a fitting time for last words.."
    show froggy scared
    me "......"
    froggy scared_talking "No regrets?.. If only things had gone differently.."
    show froggy scared
    me "Who knows.. In another universe, we might be happy right now."
    "The mayor gulped and nodded, as the poster monsters had finally grown bored of waiting. Moving right next to us, they piled on top of each other, until we were covered in sharp paper spikes. I could feel the many paper cuts all over my body, stinging, slowly giving off blood as they were bleeding me dry."
    $ die(1)
    "What a mess. Someone would have to clean this up later."
    jump you_dead


label __postermm_show:
    show overlay shitty_poster

    froggy neutral talking "Here you go."

    hide overlay

    $ renpy.rollback(force=True, checkpoints=2)

label __beforespeech:
    froggy talking "Now that that has been sorted out.. Phew, that really was a day's work or two! You've really saved me, [name]."
    show froggy neutral
    me "No, no, it's okay. Like I said, my sensei taught me to always help those in need."
    froggy neutral_talking "Sounds like you have a very wise sensei!"
    show froggy neutral
    "I winced slightly at the mayor's words, though I didn't correct his assumption. It wasn't relevant for the mayor to know. {w}Barely noticing my hesitation, the mayor continued."
    froggy neutral_talking"Now we just need to print a couple of thousands of these! I can feel the success already!"
    "I raised an eyebrow at the mayor, that suddenly seemed very self-absorbed, as he ranted on."
    froggy "Come, my minion! Advance! You shall help me hang up the posters!"
    show froggy neutral
    me "But we don't even have the posters yet! We only just figured out what to change about them!"
    "The frog tilted his head, pondering for a while, before a light bulb suddenly went off in his head."
    froggy neutral_talking "Oh, but how could I forget? Hurry, to my secretary!"

    scene black
    with fade
    $ renpy.music.stop(fadeout=1)
    $ renpy.music.queue("sound/music/Teller-of-the-Tales.ogg", loop=True, fadein=1)
    centered "{size=+10}Two hours later...{/size}"
    scene mansion hallway
    with fade
    
    "I stood outside an office door a while later, looking out at the streets through an open window. There were still as few people on the streets as there had been when I arrived, but the sun was dangerously close to the horizon. If I didn't get out of the town soon, I would have to go through the thick woods on the north side of the town in almost complete darkness."
    "As the door creaked, I turned my head to see the mayor walk out of his secretary's office with a large stack of posters."
    froggy talking "Minion! Take half, and follow me!"
    hide froggy with dissolve
    "As he loaded half the stack of posters onto me, I watched him kick the door open and walk off. I wanted to facepalm, had I not been holding a large stack of posters. Also, when did he decide that I'm his minion?! You can't just decide that on your own!"
    me "Oh, well... Doesn't look like I have a say in the matter."
    "I hurried after the mayor, that didn't even look back to check whether I was following or not."

    scene town square
    with fade_scene

    "I finally caught up to the mayor, who was standing in the middle of an open plaza, looking expectantly at me. The street lights were still off, even though it was getting dark, but the remaining sunlight was bright enough that I could still properly see my surroundings."
    froggy hi_talking "Finally, you come. Now, let's hang up posters everywhere. I don't want anyone to miss them."
    show froggy hi
    "I nodded meekly at the mayor. He then pulled a tape dispenser from his pocket, somehow balancing the stack of posters on only one of his arms, and handed it to me."
    froggy neutral_talking "If you take the north part of city, I'll take the south part."
    show froggy neutral
    me "Alright. I'm not sure I can find my way around here, though..."
    froggy neutral_talking "I'm sure you'll manage! Let's meet up here again when we're done."
    show froggy neutral
    "I nodded at the mayor, and looked around the plaza."
    me "If the sun is over there, then that must mean... This is north."

    scene town streets evening
    with fade_scene

    "I chose a direction, and walked along the road, taping the posters to the street lamps every time I came across one."
    "As I walked along the many houses, I couldn't help but feel slightly creeped out by the emptiness of the streets, coupled with the diminishing sunlight."
    "The sound of a trash can falling over suddenly startled me, as I froze in place, looking for the perpetrator.{w}.....{w}\nFew moments later, a black cat ran across the streets. I breathed out in relief. For a moment, I had been afraid of something unfortunate happening to me. Deciding that I didn't want to spend longer than absolutely necessary in these empty streets, I finished hanging up posters as fast as possible.
    "

    scene black
    with fade
    centered "{size=+10}A thousand posters, and bit of running, later...{/size}"
    scene town square dark
    with fade
    show froggy neutral

    me "*pant* *pant*"
    "The mayor looked at me with a confused glance."
    froggy confused "You look like you ran from something. Are you feeling alright?"
    "I raised a hand, signaling for him to wait a moment, my chest heaving heavily. I really wasn't used to running."
    "A couple of minutes later, having finally regained my breath, I raised my head."
    me "Are we... Done now?"
    froggy talking "Indeed we are! Now, let us go back to my mansion and have a cup of tea, doesn't that sound nice?"
    show froggy not_talking
    "I looked down at my weary feet and sighed."
    me "I suppose sitting down for a moment would be nice..."
    froggy talking "Then it's decided! Hop along, now. No time for dallying."
    hide froggy with dissolve
    "I slumped my shoulders, and walked after the mayor, back to his mansion."
    scene mansion livingroom
    with fade_scene
    show froggy neutral
    "As we were sipping tea, the mayor suddenly spoke."
    froggy neutral_talking "So, [name], it has been a long day. Seeing as I have taken so much of your time, you would be welcome to stay a night in my mansion. And then you can also help me with the contest tomorrow. What do you say?"

    menu:
        "Stay with Mayor Froggy?"
        "Yes! I'd love to stay a night in your mansion!":
            jump __stay
        "No, I think I should be on my way.":
            if postermm_points >= 5:
                $ village_dead = True
                jump __almost_end
            else:
                jump __wolfsquad
                return
label __stay:
    "The mayor nodded, seeming pleased with himself."
    froggy neutral_talking "Very well! We have a spare room or two. I will ask my secretary to prepare one of them."
    show froggy neutral
    "The mayor stood up from his chair, pushing it back in place."
    froggy neutral_talking "If you would excuse me for a moment."
    hide froggy with dissolve
    "I nodded at the mayor who was heading towards his secretary's office. The room quickly became oddly silent. For the lack of better things to do, I looked around, examining the room."
    "A large grandfather clock was standing on the far end of the room, ticking away in the otherways silent room. It was nearing 8 o'clock."
    "A few minutes slipped by, as I listened to the dull \"tick tock\" of the antique clock."
    "Several large vases with different patterns were standing on shelves on the far wall. A few family pictures of the mayor as a child were standing on the table."
    "Footsteps in the hallway were telling me that the mayor was on his way back."
    show froggy neutral with dissolve
    froggy talking "A room should be ready for you now. Follow me!"
    hide froggy with dissolve
    "I wordlessly followed the mayor as we walked up some winding stairs, and unto the second floor. Walking past several closed doors, he finally stopped."
    show froggy not_talking with dissolve
    froggy talking "This will be your room. If you need anything, my secretary is at the end of the hallway."
    show froggy not_talking
    me "Okay. Thank you for your hospitality."
    froggy talking "It is my pleasure."
    froggy "Oh, and... One last thing. Don't try to sneak around here."
    "The mayor's words seemed slightly eerie. Or maybe they seemed like a challenge."
    hide froggy with dissolve
    "The mayor went out the door, closing it behind him. As I heard his footsteps dissapear in the distance, I let out a breath I didn't know I had been holding."

    menu:
        "Go explore the mayor's mansion?"
        "Nah.":
            "I decided that it probably wouldn't be worth it. If I got caught, I could get into a lot of trouble; and I wasn't even sure I wanted to know what happened behind those closed doors. Something about the mayor seemed off, but I would be gone by the next day, so I decided not to worry about it."
            "Yawning, I decided to brush my teeth and go to bed."

        "Yes!":
            "I clenched my fist, looking at the door resolutely. Don't try to sneak around? I wondered what secrets the mayor could be hiding."
            "Approaching the door carefully, I turned the doorknob and pushed the door ajar, just enough to stick my head out. The lights in the hallway were still on."
            "Seeing as there was no one around, I opened the door a bit more, and sneaked my way across the hallway. Standing in front of the door across from mine, I tried to turn the doorknob. {w}The door was locked."
            "Walking along to the next door, I tried my luck here too. {w}This one was locked as well."
            "As I reached the third door, I noticed a peculiar smell. Almost like... Something rotten. I reached for the door when a sharp cough startled me."
            unknown "What do you think you're doing?"
            "I wearily turned my head towards the speaker."
            me "Uhm... I was just looking for the restroom."
            "A crane came into view."
            show lilly sad
            unknown "Oh, really? I suppose you wouldn't mind me showing you back to your room?"
            "I sighed dejectedly. I couldn't really refuse and still play innocent."
            "The crane opened the door to my room, and I reluctantly stepped inside."
            unknown "I believe I haven't introduced myself..."
            lilly "You may refer to me as Lilly. I excuse for the rules my master has imposed on you, but I must ask that you comply. These rules exist for a reason. Can I assume that you will refrain from such actions in the future?"
            "I wanted to ask her about the locked rooms and the weird smell, but something told me that it would be best not to."
            me "Okay. It won't happen again."
            "Lilly's face brightened."
            show lilly happy
            lilly "Oh, I am glad you understand."
            hide lilly with dissolve
            "The crane went out the door and closed it behind her, leaving me in the empty room. Deciding that it would be futile to attempt sneaking out again, I decided to go to sleep."

    scene black
    with fade
    centered "{size=+10}Next morning{/size}"
    scene mansion bedroom
    with fade

    "I opened my eyes to see sunlight streaming through the windows."
    me "Sensei?..."
    "Opening my eyes, I saw an unfamiliar ceiling."
    me "Oh... That's right... I'm at the mayor's place."
    "Feeling a bit dissapointed, I closed my eyes again, wishing myself back to just a few days ago. How certain the future had been back then. Now, nothing was certain."
    "Deciding to mull over this topic no longer, I got up from my bed and went downstairs."
    scene mansion livingroom with fade_scene
    show froggy neutral
    "The mayor was sitting in the living room, sipping a bit of tea. Noticing me, he raised a hand in greeting."
    froggy hi_talking "Greetings, [name]! Are you ready for my great speech today?"
    show froggy hi
    "I nodded, taking a seat next to the mayor. A second cup of tea had been prepared for me."
    me "So what do you expect me to do?"
    froggy neutral_talking "Not much, to be honest. You can just stand around, looking pretty."
    show froggy neutral
    me "That's it?"
    froggy neutral_talking "Pretty much! Ready to go then?"
    me "I suppose."
    hide froggy with dissolve
    "The frog nonchalantly strolled out the door, with me trotting a few metres behind him."

    if postermm_points >= 5:
        jump __too_sucessful
    else:
        jump __not_quite

label __wolfsquad:
    froggy neutral_talking "Really? What a shame. I would have liked to have you stay for another day. But if you insist... I suppose I have to let you go."
    "I nodded, and went out the front door. The street lights were on, making it easier to navigate. It wouldn't be that easy once I got to the forest though. But I had stayed in one place long enough, and it was time to move on."

    $ renpy.music.stop(fadeout=1)
    $ renpy.music.queue("sound/music/Unity.ogg", loop=True, fadein=1)
    scene forest dark
    with fade_scene

    "The chilly forest didn't seem directly hostile. The low moonlight was just enough for me to see where I was going."
    "The light liked to play tricks on my imagination. Sometimes I had to stop and stare at a thing to make sure it wasn't a dangerous monster out to eat me."
    "The rustling leaves and chilly wind didn't help my imagination, as the forest that was actually quite peaceful quickly turned into a hellish swamp out to imprison me and kill me. The trees seemed to grow thorns, and I thought I could see yellow eyes between the bushes, observing me intently."
    "A deep growl interrupted my thoughts, as I froze in place."
    me "Was that my imagination?..."
    "One of the bushes seemed to glow a faint red colour. I rubbed my eyes, still not sure whether this was all something I had imagined."
    "A glowing red shape crept out of the bushes, snarling at me menacingly."
    me "I don't think this is my imagination anymore..."
    show wolves mad at right with dissolve
    "The shape resembled that of a wolf, but it was coated in a malicious, red aura. It wore a collar with the nametag \"fluffy\" on it. A couple of wolves bearing the same red aura followed behind it, all of them glaring at me."
    me "Oh no! It's the mayor's wolf squad! It looks like he really didn't like me leaving..."
    "The foremost wolf barked at me, staring me in the eyes. I gulped, as I stepped slowly backwards. Rationally, I knew that it was impossible to get away from the mayor's wolf squad. Instinctally, however, there was nothing I'd rather do than run."
    "So I ran."
    "I turned my back to the wolves, and ran as fast as I could. {w}I could hear their shallow panting as they chased after me, only a few steps behind."
    "As I turned my head to see how far behind me they were, my foot was caught under a root."
    "My panicked breathing intensified as I crawled away, too much in a hurry to even think about standing up. The wolves had slowed down to walking tempo. They knew that it was game over for me. I knew it too."
    me "Please!.."
    "I knew it was useless, but I couldn't help but beg. The wolves finally decided that they had grown tired of me, though, and pounced. Teeth tore into skin. Claws ripped at flesh."
    $ die(0)
    "My sorry remains were never found."
    jump you_dead

label __too_sucessful:
    #Is this correct?
    jump __dragon_eat

label __not_quite:
    scene town square people
    "A small crowd was gathered in the town square. Fewer than I would have liked, but still better than none. In fact, I should have been surprised that any turned up at all, since we only just hung up posters the day before. The mayor cleared his throat, and started his speech."
    froggy talking "Greetings! I am glad to see you, dedicated citizens, that care about our environment."
    hide froggy with dissolve
    "The mayor received little to no response from the crowd."
    froggy talking with dissolve "First of all, I am sorry to announce that the contest will be postponed. This is due to the late announcement. Second of all..."
    "The mayor continued talking, as I blocked him out. Listening to his one-sided speech quickly became dull. I quickly dozed off under the shade of a tree, as I waited for the mayor to finish his speech."

    scene black
    with fade
    centered "{size=+10}One hour later...{/size}"
    scene town square dark
    with fade
    show froggy with dissolve

    froggy talking "... And that, my dear citizens, was all I had to say. Are there any questions?"
    hide froggy
    "No one replied."
    froggy talking "Very well. This speech is over; thank you all for attending."
    show froggy neutral
    "I walked up to the mayor, who was in the process of packing together his cue cards."
    me "Was that it, then?"
    froggy neutral_talking "Indeed it was! I thank you for your help. While there weren't that many people that showed up, there were definitely more than there would have been, had you not helped me."
    show froggy neutral
    me "No problem!.. But I think I should be on my way now. What is the quickest way to the capital?"
    "The mayor seemed to ponder for a moment."
    froggy neutral_talking "Well, the fastest way would be to the north. There are wolves in the forest, but they only come out at night, so you should be fine."
    me "Okay. Good luck with your campaign!"
    "I waved goodbye to the mayor, and to the small town."

    scene town walk with fade_scene
    $ renpy.pause(5)
    scene forest start with fade_scene

    "As I approached the forest, I was surprised by how calm and tranquil it seemed. Sunlight streamed through the leaves, and birds were tweeting. Finding my way through the bright forest wasn't difficult at all."

    scene meadows with fade_scene

    "As the woods thinned out, I was greeted by the sight of a bright meadows. Across the meadows was a clear path. This would take me to the capital eventually, though I might pass by a couple of cities first."
    "As I walked along, I thought about how glad I was to be alive. The outside world was definitely a dangerous place, filled with horrors... But on a sunny day like this, being alive wasn't so bad after all."
    "But I still had a long way to go."

    jump __end


label __dragon_eat:
    scene town square people
    with fade_scene
    "A large crowd had gathered at the square. Smalltalk filled the air, as people were conversing with eachother."
    "I was very surprised by the number of people that showed up, considering that we had only just hung up the posters the day before."
    "Everyone suddenly grew silent, as the mayor walked up the stairs, looking over everyone."
    show froggy hi with dissolve
    froggy hi_talking "Greetings, my citizens! First, a little announcement. I realise that this contest was issued very late, so we will hold it next Tuesday instead. Second of.."

    $ renpy.music.stop(fadeout=1)
    $ renpy.music.queue("sound/music/Oppressive-Gloom.ogg", loop=True, fadein=1)

    "The mayor continued talking, as I blocked him out. Listening to his one-sided speech quickly became dull."
    "I looked up at the gentle clouds and clear skies. The horizon to the south was lined with much darker clouds."
    "Something sounding like a roar could be heard in the distance. Or maybe it was thunder. No one seemed to notice it."
    with shake
    "A second roar followed the first one, this one much closer. A few of the villagers sent concerned glances at the black clouds, hushed whispers slowly rising from the crowd. The mayor, who had finally noticed that his peers seemed distracted, paused to look at the black clouds to the south."
    with shake
    "A dark shape large enough to block out the sun approached. Some people started screaming, running away from the town square. Others were frozen in place, either by fear or wonder."
    "The distinct smell of smoke filled everyone's nostrils, as some buildings in the south part of town burst into flames."
    show magenta annoyed_shadow at right with dissolve
    show froggy hi_talking at left with move:
        xzoom -1.0
    unknown "MWAAAHAHAHAH!"
    "An evil cackle startled everyone, as the shape landed on the ground with an earth-shattering thump,"
    with shake
    extend " blocking the sun so that we could only see a shadow."
    unknown "PUNY MORTALS! I shall enjoy TEARING YOU APART!"
    "The large shape folded together the two bat-like wings that were blocking the sun, finally revealing its shape."
    froggy "D-d-dra-dragon!"
    "The large dragon seemed to smirk amusedly. Apparently it relished in the horror and misery of others."
    show magenta annoyed at right with dissolve
    show froggy scared at left with move
    magenta mad "I AM MAGENTA! FEAR MY NAME!"
    show magenta glee
    "The dragon cackled, releasing a bout of flame from its jaws, setting fire to the large building by the town square."
    froggy scared talking "P-please! Spare u-"
    hide froggy with dissolve
    show magenta glee with dissolve
    "The mayor didn't get to say anymore, as Magenta's jaws closed around his small form. She shook her head a few times, burying her teeth deeper into the limp mayor, before she carelessly threw him away, his discarded body ragdolling to the floor."
    "The few people that had not fled yet, started running around the square like ants. Magenta stomped on the few unlucky ones that came too close, ending their lives in a second."
    magenta annoyed_talking "I GROW BORED OF YOU. Now DIE like the MIDGETS you are!"
    show magenta mad
    "Magenta took a deep breath before covering the entire square in molten flames. They had somehow miraculously avoided me. I considered getting up and running away. Then Magenta stared me down, her furious eyes filled with glee."
    magenta annoyed_talking "YOU! {w}"
    show magenta talking
    extend "I have been searching for you."
    show magenta neutral
    "Her voice changed from bottomless rage to coy smugness in an instant. She suddenly seemed like a completely different person. Her evil grin was more than slightly unnerving."
    magenta talking "And here I thought it would be more difficult to find you. What a stroke of luck!\nI would consider this... Cleaning up."
    me "Do I... Know you?"
    "Magenta let out an evil cackle."
    magenta glee "That matters not, puny mortal. What matters is that I know you. And now you... Are at my mercy."
    "Magenta raised a clawed hand, effortlessly picking me up from the ground. My attempts in getting out of her grasp only resulted in her tightening her grip. She then raised her other hand, now resting on her hind legs, and placed her thumb and forefinger on each side of my head."
    magenta annoyed_talking "Goodnight. Ant."
    show magenta annoyed
    "The enourmous pressure on my head was overwhelming, as it felt like my eyes would pop out. She slowly pressed harder. I didn't even realise that I was screaming."
    $ die(0)
    "Magenta licked the remaining blood of her fingers, as she threw my headless body to the side."
    magenta annoyed_talking "I had expected more excitement from chasing this one. Oh, well. Time to find some other place to wreak havoc."
    show magenta neutral
    "Magenta spread her wings and took off, leaving behind the charred village."
    jump you_dead

label __almost_end:
    "The mayor sighed, but nodded at me."
    froggy "Very well. If that is what you wish, I shan't hold you back. I would have wished that you stayed, but I suppose that is too much to ask after all you've done for me. I wish you a merry journey though! And don't get lost in the woods."

    show froggy neutral at right
    with dissolve

    me "Do you have any advice for me, when going through the woods?"
    froggy neutral_talking "Advice? I've got lots! First of all, avoid the forest entrance to the north by northeast. The trees there are a bit suspicious.{w} You should also stay away from the northern entrance, as wolves like to roam around there. {w}I would suggest going to the entrance to the west of town, and following the path north from there."
    show froggy neutral
    me "Thank you for the advice! I'll keep that in mind."
    show froggy hi
    "I waved goodbye to the mayor as I exited through the front door."

    scene town streets night
    with fade_scene

    scene forest start night
    with fade_scene

    "The forest seemed relatively quiet. A few fireflies fluttered around, giving off a small amount of light. It wasn't enough to see properly, but it made it easier to see where the trees were. Pale moonlight shone through the leaves, vaguely illuminating the forest path."

    scene forest three
    with fade_scene

    "Getting deeper into the forest, it suddenly seemed brighter. Almost... Like there was something magical about it. The path spread out and faded out, leaving me next to a forest lake."
    "Small lights were flickering around the edges of the treeline, but it was no longer fireflies. {w}A large, blue light flickered towards me from between the trees, and towards me. Its presence seemed calming."
    
    show willo willo at right
    with dissolve

    unknown "It... is rare that we see strangers like you in these woods... You do not belong here... We shall show you the way you seek..."
    me "Who are you?"
    unknown "We... Are..."
    willo "Often referred to as being the Will o' the Wisp... Others prefer to call us... Fairies..."
    me "Fairies?!"
    "The glowing light seemed to disregard me, hovering silently in front of me."
    willo "We... Are many...\nYou... Are not us...\nSpeak... And we shall lead you to your destination..."
    "The many lights spread around the forest seemed to draw closer."
    me "I would like to go to the north of the forest. I heard that the capital is that way."
    "The Will o' the Wisp didn't reply, though it seemed to convey some sort of silent understanding. {w}Suddenly, all of the lights disappeared."
    me "Wh-where did you go?"
    "As if replying to my question, a light blinked into existence a short way away. I walked towards the light. Just before I reached it, the light disappeared, replaced by a new one even farther away."
    "This continued until the edge of the forest was in sight. As the last light disappeared, I knew that the Will o' the Wisp had lead me as far as they could."
    "Silently thanking the strange beings, I decided that this was a good place to rest for a while. And thus, I drifted into an eventless sleep."

    scene meadows
    with fade

    "Yawning loudly, I rubbed my eyes open and looked around. I hadn't slep amazingly, but I was also unharmed, which could be seen as a miracle. I looked up at the lazy clouds. Packing together my stuff, I got up and walked along the path. This would take me to the capital eventually, though I might pass by a couple of cities first."
    "As I walked along, I thought about how glad I was to be alive. The outside world was definitely a dangerous place, filled with horrors... But on a sunny day like this, being alive wasn't so bad after all."
    "As I walked towards my future, a deep roar could be heard in the distance."

    jump __end

label __end:
    #If village dead then hear dragon in distance
    # The music "Take a chance could maybe work here? or maybe the travelling scene earlier?"
    #these notes are basically pointless now :P
    scene black with fade_scene
    centered "{size=+10}End of chapter 1.{/size}"
    jump scene02