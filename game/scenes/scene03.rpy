label scene03:
    scene school bike
    "I looked up at the many tall buildings. This would be my final stop before the capital. For a moment I wondered why I was going to the capital in the first place. But then I remembered that my sensei once had said in a drunken haze, that it was where my parents grew up. So I wanted to see this capital for myself."
    "This city seemed a lot larger than the two previous I had visited."
    "As I walked up to a school bike parking place, I felt something tugging in my clothes from behind."
    unknown "Excuse me, sirmissperson?"
    show yen hi with dissolve
    "I turned around to see a small raccoon girl, tugging at my shirt. crouching down to be at eye-height with her, I tilted my head to the side."
    me "Well, hello there. What's your name?."
    show yen happy
    "She smiled at me."
    unknown "Hello! Uhh, my name is Yen. Would you mind, uhhmm, helping me with something?"
    menu:
        "Help her with something?"
        "Yes":
            jump __helpher
        "No":
            jump __busy

label __busy:
    me "I'm sorry, I'm quite busy."
    raccoon talking "Oh?... Does that make you a bad person?"
    "I raised an eyebrow. Something so simple didn't seem like enough to warrant calling me a bad person."
    me "I wouldn't say so, no."
    "The raccoon suddenly seemed quite gloomy."
    raccoon sad "I think you're a bad person... My parents have taught me what happens to bad people..."
    "Her mouth twisted into an evil grin."
    raccoon evil "BODYGUARD! Show this person what happens to meanies!"
    "A large shape approached from the shadows."
    me "Whoa, wait a minute, I didn't do anything!"
    "The shape simply grunted, as it pulled out a chainsaw."
    me "Please?..."
    "I was about to run away, when I suddenly found that I couldn't feel my feet anymore.{w}.......{w} In fact, I couldn't feel my entire body."
    "I looked down to find that my body had, in fact, been severed from my head. Or was it the other way around?"
    $ die(0)
    raccoon sad "Oh... I hope father won't be mad... I guess I'll just have to ask the next person that comes by... I trust you will clean up this mess?"
    "The large shape next to her simply grunted."
    jump you_dead

label __helpher:
    me "Sure. What do you need help with?"
    "I assumed that it wasn't going to be anything substantial. Maybe she lost a football in a tree or something. {w}She gave me a toothy smile and held up a tablet."
    raccoon talking "I need some help with my school assignment about web design! My parents care a lot about my grades, and they can get {i}very{/i} mad."
    "I raised an eyebrow. I really didn't want to spend my time on teaching a little girl web design, but if her parents were going to get mad... It couldn't be helped."
    me "I suppose I could help you a bit. Would you mind telling me a bit more about your project?"
    "She looked around, scanning the area for anyone that might be listening in."
    raccoon talking2 "We need to go somewhere, uhh... Private. Follow me!"
    "She grabbed my shirt again, dragging me along."
    scene school hallway with fade_scene
    "We went through a side-entrance to the school building, and up a flight of stairs, before we came to a brightly lit corridor. Several students were wandering around, talking to each other. {w}Some seemed to send me weary glances, probably because I didn't look like anyone belonging to this school"
    "A shadow drew my attention on the far end of the hallway. As soon as I looked at it, however, it disappeared."
    scene school roof with fade_scene
    show yen talking with dissolve
    "We soon got to the roof of the building. I immediately noticed that it was completely empty. But not only that; it was also completely open, with few places to hide. It also had benches to sit on."
    raccoon talking2 "Let's, uhhm, sit over here!"
    "I followed her to the nearest bench."
    raccoon talking "So, uhh, sirmissperson. Do you..."
    "As her voice turned to a whisper, I leaned in closer."
    raccoon "Do you... Believe in dragons?"
    "Before I could reply, she raised a hand to silence me."
    raccoon talking2 "No, let me speak first."
    "Seeing that I did not object, she continued."
    raccoon talking "Well... I wanted to make my website about how dragons exist, and, uhhmm, how we can be friends with them..."
    raccoon "You see, this other day, I met a dragon close to here and it was nice and wanted to be my friend... So I want to tell everybody about dragons and how everyone should be friends!"
    raccoon "Do you believe me, then?..."
    menu:
        "Do you believe in her story?"
        "Yes":
            jump __believe
        "No":
            jump __somethingclever

label __believe:
    me "... Yes, I believe you."
    "A wide smile spread across her face."
    raccoon happy "I knew I could get someone to help me!"
    raccoon taling "But... I have classes soon... Would you mind meeting me at the library in a couple of hours?"
    me "Alright."
    jump __dragons_exist

label __somethingclever:
    me "I'm sorry, but... Dragons? And friends? It seems a bit far-fetched."
    "Yen pouted."
    raccoon sad "I... Knew that you might doubt me...{w} Which is why I want to show you where I met the dragon!"
    "She looked expectantly at me."
    raccoon talking "So, uhh... Will you meet me there after school?... I have classes soon..."
    menu:
        "Meet her after school?"
        "Yes":
            jump __totallyinteresting
        "No":
            jump __sorrynope

label __sorrynope:
    me "I would... Rather not. I'm sorry, but I have other things to do."
    "Yen hung her head, seeming very disappointed. Tears started running down her cheeks."
    raccoon sad "N-... Nobody believes me..."
    "Crying, she ran towards the door to the rooftop terrace."
    hide yen with dissolve
    me "Wait a moment!"
    "I ran after her, following her down to the hallway we were previously on."
    scene school hallway
    "As I got down the stairs, I saw her run into the toilet."
    me "Please, wait!"
    "A sign saying \"Caution! - Floor slippery when wet\" was placed outside the toilets."
    "Just as I was about to run through the doorway, I felt my feet lose their grip on the floor."
    "As I got thrown through the air, my sense of time slowed to a crawl."
    "What was happening? Why was the world suddenly sideways?"
    "Something hard suddenly hit the back of my head. I felt my consciousness fade very quickly. What was happening again?..."
    $ die(2)
    "The wet floor was coloured red, as blood poured from my shattered skull."
    jump you_dead

label __totallyinteresting:
    me "... Alright, it sounds interesting."
    "I decided that it might be worth investigating, since I wasn't really in a hurry anyways."
    "Yen's face brightened."
    raccoon happy "Okay! Uhhmm... A bit further north, down the street, there's a library we could meet up at."
    "Just as I was about to reply, the school bell rung."
    raccoon talking "Oh, uhmm, I need to go now!"
    me "See you at the library!"
    hide yen with dissolve
    "As the little raccoon darted off, I started wondering how I would get off this roof."
    scene black
    centered "{size=+10}A couple of hours and some staircase-climbing later...{/size}"
    scene library with fade_scene
    "The small raccoon walked through the front doors, seeming unsure of herself. Then she saw me, and her face brightened up."
    show yen happy with dissolve
    raccoon "Oh, I was worried if you'd actually... You know... Come."
    me "Of course I would. Now, why don't we go to what you wanted to show me?"
    raccoon "Oh, of course! Follow me! It's just down by the beach."
    "I followed the little raccoon, unsure of what I'd find."
    centered "{size=+10}A short walk later...{/size}"
    "Yen had lead me down to a beach. Seagulls cawed, making the place very noisy."
    me "So is this where you-"
    raccoon "She isn't here! Where did she go?"
    me "Where did who go?"
    raccoon "The dragon! She was here last time I looked..."
    "Walking a bit further along the beach, we saw four large footprints in the sand, with something akin to claw marks, having bored deep into the ground. It would seem that whatever left these footprints had taken off."
    me "It's... Okay. I believe you."
    raccoon "Really?!"
    me "Yeah... Let's go back to the library and look at your assignment."
    raccoon "Yay!"
    "Yen smiled and ran off, forcing me to run after her."
    jump __dragons_exist

label __dragons_exist:
    scene library with fade_scene
    "In the library, we found an out-of-the-way table to sit by."
    if __lilly==1:
        "A small cough came from behind me."
        show lilly sad with dissolve
        "As I turned around, I was greeted by a familiar sight."
        me "Lilly! What are you doing here?"
        lilly "I was looking for... Groceries for the master."
        me "All the way out here?"
        lilly "The master was looking for some... Specific wares that are not easy to come by. I decided to look for good crime novels since I'm here anyways. It is the only way of keeping boredom at bay, that I have found to be pleasurable."
        me "Oh? Well, it is nice to see that you are doing well."
        lilly "Likewise, [name]. Now, if you would excuse me, I still have errands to run for the master."
        me "Thanks for coming by."
        lilly "It was my pleasure."
        hide lilly with dissolve
        "With this, the crane walked away, leaving us behind."
        show yen talking with dissolve
        raccoon "Who was that lady?"
        me "She's just a person I met earlier in my travels. But we shouldn't talk about that now. We have other things to do!"
        raccoon "Yeah!"
    else:
        show yen talking with dissolve
    me "So why don't you tell me a bit about your assignment?"
    "She found her tablet again, and showed me the current version of the website."
    raccoon talking2 "I was wondering a bit about the layout... It's about web design, after all... How do you make a good layout?"
    me "Well, a good layout should be..."
    menu:
        "How should the layout be?"
        "Simple, not too cluttered.":
            raccoon "That makes sense..."
        "Do as google. Almost nothing but empty space!":
            raccoon "But... Where will I put all of my content?"
        "Try to fit as much as possible in one page.":
            raccoon "Won't it be difficult then to find what I'm looking for?..."
    raccoon happy "Okay, I think I know what I should be doing now... So how do I make people notice my website? I want to spread the word!"
    me "Have you heard about \"SEO\"?"
    "Yen shook her head."
    raccoon talking "Nope. What is it?"
    menu:
        me "Well, \"SEO\" stands for..."
        "Search Engine Optimists":
            raccoon "Everyone loves an optimist!"
        "Search Engine Orbiting":
            raccoon "Isn't orbiting a space thing?"
        "Search Engine Optimization":
            $ web_total += 1
            raccoon "So what does that mean?"
            me "It means that you put some tags on your website that helps people find it."
        "Surviving Electronically Online":
            raccoon "Surviving is good."
        "Surviving Electronically On-time":
            raccoon "Surviving is good."
    raccoon "So... That actually works?"
    me "Yeah! I'm sure people will notice your website in no time."
    jump __code

label __code:
    raccoon sad "Okay... Then, uhhmm, I have this code that I wrote up that I wanted to get to work, but it didn't really work..."
    me "Could you show it to me?"
    jump __code_show
    me "Hmm... You're on the right track, but there are a few things you might want to fix..."
    
    while True:
        $ code_asked_i += 1
        menu:
            "What {i}three{/i} things need to be changed to make a functional website?"
            "It needs a <!DOCTYPE html>" if not code_asked['doctype']:
                $ code_asked['doctype'] = True
                me "This is to signify that we're using HTML5."
                $ code_correct += 1
            "It needs a enter (as in ENTER) after <body>" if not code_asked['enter']:
                $ code_asked['enter'] = True
                raccoon "I thought that stuff didn't matter?... It does look prettier, though..."
            "Big is not a html tag." if not code_asked['big']:
                $ code_asked['big'] = True
                $ code_correct += 1
                raccoon "It isn't? What if I want something big, then?"
                me "Well, then you use the \"h1\" tag, since it's a header."
            "Head should be before body." if not code_asked['head']:
                $ code_asked['head'] = True
                $ code_correct += 1
                raccoon "Oh, that's right, I think I remember that, now that you mention it..."
            "It needs CSS (styling) to work." if not code_asked['css']:
                $ code_asked['css'] = True
                raccoon "But... Doesn't that just make it prettier? Not that I don't want it pretty..."
            "Show it to me again please.":
                jump __code_show
        if code_asked['doctype'] and code_asked['big'] and code_asked['head']:
            $ web_total += (code_correct - code_asked_i)
            #So if you did everything correct then you get 0 points... if not you get subtracted up to 2 points... that's fair right?
            jump __colours

label __code_show:
    show overlay bad_html:
        xalign 0.5
        yalign 0.5
    raccoon talking2 "Sure!"
    hide overlay
    $ renpy.rollback(force=True, checkpoints=2)

label __colours:
    raccoon talking "Oh... Uhh, okay... I don't know much about this stuff, so thanks."
    me "It's okay! Now then, have you thought about styling?"
    raccoon "Well, I have these colours that I wrote down when we had colour theory... I think I sort of get it, but maybe it would be a good idea to let you look through them..."
    menu:
        "Which of these colours is not a valid colour?" #Can you add some dialogue? And yeah two are wrong (so correct), but that doesn't matter
        "#FFF":
            raccoon "Oh... I thought that was allowed to be used here..."
        "#FFFFFF":
            raccoon "Oh... I thought that was allowed to be used here..."
        "hsl(255, 23, 4)":
            raccoon "I was a bit unsure about this one myself... But our teacher talked about it a lot..."
        "hsla(1, 45, 34, 2)":
            raccoon "I was a bit unsure about this one myself... But our teacher talked about it a lot..."
        "rgb(3, 5, 7)":
            raccoon "Was I thinking about cym then?... No, that's for printers, that can't have been right..."
        "rgba(6, 234, 56, 25)":
            raccoon "Was I thinking about cymb then?... No, that's for printers, that can't have been right..."
        "hsv(28, 186, 43)":
            $ web_total += 1
            raccoon "This was one of the ones I was unsure about, too... I just added it as a precaution."
        "hsva(89, 43, 23, 4)":
            $ web_total += 1
            raccoon "This was one of the ones I was unsure about, too... I just added it as a precaution."
    raccoon "So I should stick with these other ones instead? Okay..."
    me "The rest of them should work, yeah." # Maybe change this, due to the whole 2 out of 8 doesn't work, yet you only select 1 thing xD

    raccoon "So, uhhm, my last question is... I have this friend who draws really cool dragons, and I want to link to her website, but how do I link to stuff?"
    me "Well, I can see that you have worked with tags. To refer to another website, you just need to use the proper tag, which is..."
    menu:
        "How are links made in HTML?"
        "The l tag.":
            me "See, it stands for \"link\"! It's smart."
            raccoon "I don't remember it being {i}that{/i} straightforward."
        "The link tag.":
            raccoon "Aren't tags usually shorter?..."
        "The a tag.":
            $ web_total += 1
            raccoon "But how does that make sense?"
            me "Don't ask me, it just does."
        "The anchor tag.":
            raccoon "But I don't want to anchor anything..."
        "The p tag.":
            raccoon "I thought \"p\" was the classical symbol for \"parking space\"..."
        "The pointer tag.":
            raccoon "Pointer?... Aren't tags usually shorter?..."
    raccoon talking2 "Okay, that was all I needed I think. Thank you, sirmissperson!"
    me "It's okay, I'm happy to help. Oh, and I have a name."
    raccoon talking "What would that be?"
    me "[name]! Nice to make your acquaintance."
    raccoon happy "Uh-huh!"
    me "Well, let's find a place to publish it, then."
    raccoon talking2 "Can we go back to my school? I want to show it to my teacher."
    me "Sure."
    scene school hallway with fade_scene
    "While Yen was talking with her teacher, I looked at a bulletin board."
    "A poster with the title \"Dragons are real!\" was hanging there, probably from an earlier assignment. It looked a bit like a PSA."
    "The little raccoon hopped back towards me, apparently done with talking with her teacher."
    show raccoon talking with dissolve
    me "How long have you been running this campaign?"
    raccoon talking2 "Uhh... For a while, I suppose."
    me "So a lot of people here know about dragons?"
    raccoon talking "Uh-huh. Not a lot of people believe me, though..."
    #Split!

label __toowrong:
    "A loud \"thump\" could be heard, almost as if something had landed on the roof."
    raccoon talking2 "We should go investigate!"
    me "I'm really not sure that's a wise id-..."
    "Yen grabbed my shirt and dragged me along, leaving me little room for objection."
    scene school roof with fade_scene
    "As soon as we rushed out the door, we were greeted by two bright eyes, staring at us intently."
    show magenta talking at right
    unknown "Greetings. WORMS. I had thought that getting this far would be FAR more difficult. But once again, the mortal races PROVE THEIR INCOMPETENCE."
    show magenta neutral
    show raccoon talking at left, flip with dissolve
    raccoon "Y-you don't need to yell!"
    show magenta glee
    unknown "MWAHAHAHAHAH!"
    "The dragon let out a terrifying cackle."
    show magenta talking
    unknown "You think that YOU, a little MIDGET can command me around, the mighty MAGENTA?"
    magenta annoyed_talking "DIE, mortal!"
    show magenta annoyed
    hide raccoon with dissolve
    "The dragon, who had dubbed herself \"Magenta\", lowered her clawed hand, piercing the chest of Yen with a sharp claw.{w} The raccoon gurgled, desperately trying to breathe, but instead she found blood spilling out from her mouth."
    "She looked to me with a desperate look in her eyes, trying to say something... But no intelligible sounds escaped her mouth."
    me "Y-you... You monster! What did she do to-"
    magenta annoyed_talking "SILENCE, mortal! You lesser races have NO RIGHT to speak to me! I do AS I PLEASE."
    show magenta annoyed
    "I backed away towards the rooftop door. Magenta grinned evilly at me."
    magenta glee "Going somewhere?"
    "She looked at me gleefully, seemingly enjoying the moment."
    magenta talking "I think not."
    "She raised a hand and placed it right in front of the door."
    "I started at the mocking face that was getting closer... Her jaws opened around me... And then her jaws closed."
    $ die(0)
    magenta annoyed_talking "Well, that was easy..."
    show magenta annoyed
    "Magenta looked around at the city, several armored cars encroaching on her position."
    magenta annoyed_talking "I should probably get out of here."
    "With that said, Magenta spread her large bat-like wings and took off, leaving behind the bodies of Yen and [name]."
    jump you_dead

label __semicorrect:
    "A loud alarm suddenly rung through the city."
    me "Wha-what is that?"
    raccoon talking2 "It's the alarm! Something big is coming... Could it be?"
    me "Could it be what?"
    raccoon "Dragon!"
    "A loud roar soon followed."
    raccoon "Come on, let's go to the roof!"
    "I was about to protest that being outside with a dragon approaching probably wasn't a good idea, but I couldn't help but be intrigued myself."
    scene school roof with fade_scene
    show raccoon talking2 with dissolve
    raccoon "It... It's coming this way. It's coming closer!"
    "Indeed, the looming shape of the reptile was swiftly approaching us."
    raccoon talking "It seems like they couldn't keep it back at the walls... Why is it here, I wonder?"
    me "It probably doesn't have good intentions."
    raccoon sad "B-but... We can be friends!"
    me "Look at its eyes. Does that look like a friendly dragon to you?"
    "As we talked, the dragon kept getting closer. It seemed like it was heading directly for us."
    centered "{size=+10}End of Chapter 3.{/size}"
    centered "{size=+10}... To be continued...{/size}"
    #jump scene04

label __allcorrect:
    "A loud alarm suddenly rung through the city."
    me "Wha-what is that?"
    raccoon talking2 "It's the alarm! Something big is coming... Could it be?"
    me "Could it be what?"
    raccoon "Dragon!"
    "A loud roar soon followed."
    raccoon "Come on, let's go to the roof!"
    "I was about to protest that being outside with a dragon approaching probably wasn't a good idea, but I couldn't help but be intrigued myself."
    scene school roof with fade_scene
    show raccoon talking2 with dissolve
    raccoon "Look, out there at the town walls!"
    "Indeed, a large shape had placed itself on the walls, spewing fire at the building. Several firetrucks were already at the sites, spraying water at the fires, which lead to huge columns of smoke rising up from the buildings.{w} The raccoon seemed devastated."
    raccoon sad "B-but... Why can't we just be friends? Why can't everyone just get along?"
    me "Does that dragon seem like it has good intentions?!"
    raccoon "I-... I'm sure it has its reasons..."
    "As even more smoke spread in the distance, i shook my head."
    me "I don't think so."
    "The dragon seemed determined to burn this whole place to the ground."
    centered "{size=+10}End of Chapter 3.{/size}"
    centered "{size=+10}... To be continued...{/size}"
    #jump scene04