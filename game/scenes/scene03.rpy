​
label scene03:
    scene school bike
    "I looked up at the many tall buildings. This would be my final stop before the capital. For a moment I wondered why I was going to the capital in the first place. But then I remembered that my sensei once had said in a drunken haze, that it was where my parents grew up. So I wanted to see this capital for myself."
    "This city seemed a lot larger than the two previous I had visited."
    "As I walked up to a school bike parking place, I felt something tugging in my clothes from behind."
    unknown "Excuse me, sirmissperson?"
    "I turned around to see a small raccoon girl, tugging at my shirt. crouching down to be at eyeheight with her, I tilted my head to the side."
    me "Well, hello there. What's your name?."
    "She smiled at me."
    unknown "Hello! Uhh, my name is NAME. Would you mind, uhhmm, helping me with something?"
    menu:
        "Help her with something?"
        "Yes":
            jump __helpher
        "No":
            jump __busy

label __busy:
    me "I'm sorry, I'm quite busy."
    raccoon "Oh?... Does that make you a bad person?"
    "I raised an eyebrow. Something so simple didn't seem like enough to warrant calling me a bad person."
    me "I wouldn't say so, no."
    "The raccoon suddenly seemed quite gloomy."
    raccoon "I think you're a bad person... My parents have taught me what happens to bad people..."
    "Her mouth twisted into an evil grin."
    raccoon "BODYGUARD! Show this person what happens to meanies!"
    "A large shape approached from the shadows."
    me "Whoa, wait a minute, I didn't do anything!"
    "The shape simply grunted, as it pulled out a chainsaw."
    me "Please?..."
    "I was about to run away, when I suddenly found that I couldn't feel my feet anymore.{w}.......{w} In fact, I couldn't feel my entire body."
    "I looked down to find that my body had, in fact, been severed from my head. Or was it the other way around?"
    $ die(0)
    raccoon "Oh... I hope father won't be mad... I guess I'll just have to ask the next person that comes by... I trust you will clean up this mess?"
    "The large shape next to her simply grunted."
    jump you_dead

label __helpher:
    me "Sure. What do you need help with?"
    "I assumed that it wasn't going to be anything substantial. Maybe she lost a football in a tree or something. {w}She gave me a toothy smile and held up a tablet."
    raccoon "I need some help with my school assignment about webdesign! My parents care a lot about my grades, and they can get {i}very{/i} mad."
    "I raised an eyebrow. I really didn't want to spend my time on teaching a little girl webdesign, but if her parents were going to get mad... It couldn't be helped."
    me "I suppose I could help you a bit. Would you mind telling me a bit more about your project?"
    "She looked around, scanning the area for anyone that might be listening in."
    raccoon "We need to go somewhere, uhh... Private. Follow me!"
    "She grabbed my shirt again, dragging me along."
    scene school hallway
    "We went through a side-entrance to the school building, and up a flight of stairs, before we came to a brightly lit corridor. Several students were wandering around, talking to eachother. {w}Some seemed to send me weary glances, probably because I didn't look like anyone belonging to this school"
    "A shadow drew my attention on the far end of the hallway. As soon as I looked at it, however, it dissapeared."
    scene school roof
    "We soon got to the roof of the building. I immediately noticed that it was completely empty. But not only that; it was also completely open, with few places to hide. It also had benches to sit on."
    raccoon "Let's, uhhm, sit over here!"
    "I followed her to the nearest bench."
    raccoon "So, uhh, sirmissperson. Do you..."
    "As her voice turned to a whisper, I leaned in closer."
    raccoon "Do you... Believe in dragons?"
    "Before I could reply, she raised a hand to silence me."
    raccoon "No, let me speak first."
    "Seeing that I did not object, she continued."
    raccoon "Well... I wanted to make my website about how dragons exist, and, uhhmm, how we can be friends with them..."
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
    "A wide smile spread accross her face."
    raccoon "I knew I could get someone to help me!"
    jump __dragons_exist

label __somethingclever:
    me "I'm sorry, but... Dragons? And friends? It seems a bit far-fetched."
    "NAME pouted."
    raccoon "I... Knew that you might doubt me...{w} Which is why I want to show you where I met the dragon!"
    "She looked expectantly at me."
    raccoon "So, uhh... Will you meet me there after school?... I have classes soon..."
    menu:
        "Meet her after school?"
        "Yes":
            jump __totallyinteresting
        "No":
            jump __sorrynope

label __sorrynope:
    me "I would... Rather not. I'm sorry, but I have other things to do."
    "NAME hung her head, seeming very disappointed. Tears started running down her cheeks."
    raccoon "N-... Nobody believes me..."
    "Crying, she ran towards the door to the rooftop terrace."
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
    "NAME's face brightened."
    raccoon "Okay! Uhhmm... A bit further north, down the street, there's a lirbrary we could meet up at."
    "Just as I was about to reply, the school bell rung."
    raccoon "Oh, uhmm, I need to go now!"
    me "See you at the library!"
    "As the little raccoon darted off, I started wondering how I would get off this roof."
    centered "{size=+10}A couple of hours and some staircase-climbing later...{/size}"
    scene library
    "The small raccoon walked through the front doors, seeming unsure of herself. Then she saw me, and her face brightened up."
    raccoon "Oh, I was worried if you'd actually... You know... Come."
    me "Of course I would. Now, why don't we go to what you wanted to show me?"
    raccoon "Oh, of course! Follow me! It's just down by the beach."
    "I followed the little raccoon, unsure of what I'd find."
    centered "{size=+10}A short walk later...{/size}"
    "NAME had lead me down to a beach. Seagulls cawed, making the place very noisy."
    me "So is this where you-"
    raccoon "She isn't here! Where did she go?"
    me "Where did who go?"
    raccoon "The dragon! She was here last time I looked..."
    "Walking a bit further along the beach, we saw four large footprints in the sand, with something akin to clawmarks, having bored deep into the ground. It would seem that whatever left these footprints had taken off."
    me "It's... Okay. I believe you."
    raccoon "Really?!"
    me "Yeah... Let's go back to the library and look at your assignment."
    raccoon "Yay!"
    "NAME smiled and ran off, forcing me to run after her."
    jump __dragons_exist

label __dragons_exist:
    "Stuff happens."