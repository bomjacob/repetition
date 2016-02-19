label scene02:
    play music "sound/music/Twisted.ogg"
    scene dusty_road
    with fade_scene
    "I walked along a dusty asphalt road."
    "..."
    "Was that a car I could hear in the distance?"
    "I looked around to orient myself. True enough, a red car was about to drive by. I raised a thumb, in the hopes that the driver was kind enough to pick up a stray soul." #Can you say true enough? Isn't it sure enough?
    "The car didn't seem to slow down at all. {w}I had almost lost hope."
    "Then the driver stopped."
    "The driver was a sloth, wearing a sheriff’s badge. He looked expectantly at me."
    sloth "So? Are you going to hop in, or what?"
    "Barely believing my luck, I nodded voicelessly, and opened the door to get in. Starting the car again, the sloth began speaking to me."

    menu:
        sloth "What’s a person like you doing around these parts then?"
        "I’m just passing by":
            sloth "Oh? Well, in that case, we’re nearing the city where I live, Pollyhoot city. If you would like, I could tell you about some points of interest?"
            me "Sure! I might as well, since I have nothing better to do."
            "The sloth turned his eyes towards the road as he thought.{w} Suddenly, a metaphorical lightbulb went off in his head."
            sloth "I know! We currently have a filmcrew in town. People talk a lot about it, since it’s rare that we get something like that in town, despite its name’s semblance to that other city."
            me "A filmcrew? That sounds interesting. I’d love to have a look at it, if you wouldn’t mind telling me where it is."
            sloth "I’m going that way anyways, so I can drive you there if you want a lift?"
            me "That would be awesome. Thanks!"
            "The rest of the ride happened in silence."

            scene town2 red_houses
            with fade_scene

            "About twenty minutes later, we arrived at a set of red wooden houses."
            sloth "This is where they film! Go to the second hut on the right, and they should be in there."
            me "Thank you for the ride, sir sloth."
            sloth "Please, call me NAME."
            me "Okay, NAME. I hope I can repay the favour sometime."
            sloth "Don’t worry about it! Though if you do get time, I’m at the police station."
            "I exited the car and waved goodbye to the sloth sheriff."

            "Walking towards the red houses, I felt something like a chill. It was very brief, but noticeable. But the memory of it even being there in the first place soon escaped my mind."
            jump __cafe

        "I’m actually a secret agent from the government; don’t tell anyone.":
            sloth "Oh? Are you now? Would you forgive me if I said that I don’t believe you?"
            "I crossed my arms and huffed. "
            me "I find that rude."
            "The sloth stared me in the eyes, an air of seriousness about him,"
            sloth "Lying about being a secret agent isn’t exactly light stuff. You shouldn’t go around te-.."
            "The sloth was suddenly cut off as the front of his car smashed into a tree. His head had been thrown violently into the steering wheel, blood running from his forehead and down through his fur. The windshield was shattered into many pieces."
            "A few moments later, I discovered that I, myself, was not doing too well. Feeling slightly dizzy, I raised a hand to my head. {w}Bringing it down again, I saw that my hand was covered in blood."
            "I would have panicked, had I not suddenly felt so very tired."
            "Just... A moment of rest... Was all I needed..."
            $ die(2)
            "Public Safety Announcement: Pay attention when you drive! Avoid car accidents!{w}\nOh, and you should probably not tell others that you’re a secret agent either."
            jump you_dead

label __cafe:
    scene town2 cafe
    with fade_scene
    show fox talking_normal at center with dissolve
    show partridge neutral at right with dissolve
    show squirrel neutral at left, flip with dissolve
    "As I opened the saloon-like doors, I was greeted by a place furnished like a restaurant. A partridge, a fox and a squirrel (and possibly more) seemed to be arguing about something."
    partridge no "No, it should definitely be cut like this! That adds the most suspense!"
    fox neutral_sceptic "No, this it should be cut like this instead. This shows me from the best angle!"
    squirrel no "My professional opinion states that it should be cut like this, for the best dramatic effect!"
    "As the saloon-like doors closed behind me, three pairs of eyes stared intently at me."
    partridge hi "You there! What do you think? Crossclipping, zooming or an over-shoulder view of our heroine?"
    "The fox scoffed."
    fox talking_sceptic "Why do I work with such simpleminded people? Clearly zooming on my face here would be the best option! It’s what the people want!"
    "The partridge crossed its wings."
    partridge no "A camera movement like that wouldn’t progress the story in any way! We should cut it just as he runs out the door.."
    "The squirrel shook its head, sighing resignedly."

    menu:
        squirrel "So? What do you think?"
        "Cut! It adds suspense.":
            partridge neutral "Hah! See, this person agrees with me! I kne-.."
        "Zoom! It’s what the people want.":
            fox talking_normal "See, this person is smart. This person knows what is the right thing to-.."
        "Over-shoulder! It’s dramatic.":
            squirrel happy "That’s what I thought too. See, people? This is definitely the right cho-.."


    "The lights suddenly flickered off, as the front doors flew open, a gust of wind circling around the room before dying out.{w} A few seconds later, the lights flickered back on."
    fox neutral_sceptic "I thought you hired proper electricians for this job!"
    partridge sad "I-.. I did, I swear! I’m not sure what that-.."
    squirrel no "Silent everyone! It would seem something is coming."
    "As if waiting for this to happen, a mysterious voice resounded through the wooden walls and fake furniture."
    unknown "Fire? Yes, yes! Fire. You have done me injustice. You have done the world a horrible injustice!"
    ghost "I am the Ghost of Bad Filmmaking here to tell you that you are doing the world a terrible, unjustified injustice! The world weeps!"
    "The fox’s eyes widened, though she seemed to keep her calm, denying the existence of this bodyless voice for the moment. The squirrel kept moving his head around, searching for the voice of the perpetrator. The partridge seemed to have the most calm out of all of them, even daring to speak."
    partridge no "Who is this? Show yourself!"
    hide partridge with dissolve
    hide fox with dissolve
    hide squirrel with dissolve
    show ghost appear
    "A ghostly laugh went through the walls, seeming to come from all directions. A small light flickered in mid-air. {w}The light flickered again, growing a bit larger. It seemed to rotate around itself, swallowing itself, growing larger and larger until it formed a ghastly shape."
    show ghost full
    ghost "I have seen your sin! This terrible crime of a movie! I am in disgust!"
    "The ghost seemed to cry out of a strange mix between rage and sadness, the luminescent tears disappearing without a trace as soon as they touched the ground below."
    ghost fire "I give you this warning! If you do not fix your terrible excuse for a film, this crime against humanity, you will be punished! Nothing less than death will suffice! Now, flee! Tremble in terror and repent! I am a merciful evil!"
    "The ghost snapped what looked like its fingers, making a small spark appear. The small spark jumped around, hopping from the ghostly shape to the floor, and around the furniture. Everywhere it touched, burst into flames."

    scene town2 burning_cafe
    with dissolve
    show ghost fire

    "I, who was standing at the entrance, quickly realised what was happening."
    me "Hurry up, guys! If you stay like this, you'll get charred to ash!"
    "This seemed to snap the three out of their trance, as they ran for the front door. Just as we got to the doorway, the entire inside of the fake restaurent burst into flames. The ghost-like form cackled."
    ghost "You may have escaped your doom this time. But as long as your sin remains, do not expect to avoid the fiery demise that awaits you! The world will have justice from terrible filmmakers like you!"

    scene town2 red_houses
    with fade_scene
    show fox neutral_sceptic at center with dissolve
    show partridge very_sad at right with dissolve
    show squirrel hmm at left, flip with dissolve
    "We ran outside, leaving behind the burning props. The fox seemed offended that she had to run anywhere. The partridge looked back at the burning building in despair."
    me "Does anyone have a phone? We should probably call the firefighters.."
    "The squirrel took a mobile phone out of his pocket, pressing a few buttons before holding it to his ear."
    squirrel no "Yes, hello? We have a fire out here, you might want to send some people."
    "I turned my attention towards the fox and the partridge."
    me "I don't think we're safe yet. Do you know of anywhere we can talk? I get the feeling you guys have some things we need to talk about."
    "The partridge was finally able to draw his eyes away from the burning building, and looked at me."
    partridge sad "We should probably go somewhere else."
    "We waited a few more moments before the fire department arrived, before going to a nearby playground."

    scene town2 playground
    with fade_scene
    show partridge sad at right
    partridge "We can sit here."
    "I nodded at him, and we all took place around the playground."
    me "So... In a desperate attempt to save your hides, why don't we start at the beggining? That would be pre-production..."
    "Upon hearing this, the fox immediately seemed disinterested. It would seem she didn't have much to do with the pre-production."
    show squirrel hmm at left, flip with dissolve
    squirrel no "We have planned this project meticulously!"
    me "Yeah? So what did your pre-production consist of?"
    hide squirrel with dissolve


    $ __wrongpartridge = 0
    $ __partridge = 0
    #Preparation for killing people. Yay!

    # I'm not sure if I'm doing this right, but hey, I'm trying
    #I'm not sure this is what you want for this part :/ Like do you wanna go to the "go on" part even if you answer wait? It's kinda hard to decode without /any/ tabs/leading spaces in your text.
    menu:
        partridge "Well, we started out with finding our cast..."
        "Wait!":
            me "You started with /casting/?"
            partridge "Yes? Is there anything wrong with that?"
            me "Yes! Everything is wrong with that!"
            jump __pre
        "Go oon...":
            menu:
                partridge "Then we went on with making a storyboard..."
                "Wait!":
                    me "You made a storyboard before you made the actual story??"
                    partridge "Well, we wanted a visual representation..."
                    me "No, no, no. That's completely wrong."
                    jump __pre
                "Go oooon...":
                    menu:
                        partridge "After that, we found the music we wanted to use."
                        "Wait!":
                            me "So let me get this right.. You haven't even found a genre yet, and you already found music for it?"
                            partridge "Genre is unimportant! We could always decide that after finding some awesome music!"
                            me "That's not how filmmaking works!"
                            jump __pre
                        "Go oooooon...":
                            partridge "Lastly, we made our synopsis to recap all things we had planned."
                            menu:
                                "Wait!":
                                    me "You made your synopsis last?! You're supposed to make that first!"
                                    partridge "You are? But.. But.."
                                    me "Yes! It's completely wrong!"
                                    jump __pre
                                "That sounds completely fine.":
                                    me "I'm not sure why the ghost is hunting you down, then. This is a stellar example of how to do pre-production!"
                                    $ __wrongpartridge += 1
                                    jump __storyboard


label __pre:
    partridge no "Well, how would /you/ do it then?"

    menu:
        "How would you do it?"
        "Brainstorm, Synopsis, Manuscirpt, Storyboard":
            partridge "I suppose that makes sense..."
            jump __storyboard
        "Storyboard, Manuscript, Synopsis, Brainstorm":
            jump __bad_pre
        "Synopsis, Manuscript, Storyboard, Brainstorm":
            jump __bad_pre
        "Synopsis, Synopsis, Synopsis, Synopsis!":
            jump __bad_pre
        "Storyboard, Brainstorm, Synopsis, Manuscript":
            jump __bad_pre
        "Brainstorm, Synopsis, Brainstorm, Synopsis, Manuscirpt, Storyboard":
            jump __bad_pre

label __bad_pre:
    $ __deadpartridge += 1
    partridge "Well, it is certainly not what we did..."
    jump __storyboard

label __storyboard:
    me "And now that we're on the subject of pre-production, why don't we talk about your storyboard?"
    partridge neutral "I would've shown it to you, but our storyboard was too large to carry around."
    me "It sounds like you're planned your story very well, then?"
    partridge sad "We have? I was just talking about the large sign we have, saying \"Story\". What are you talking about?"
    me "Sign? What exactly do you think a storyboard it?"
    partridge neutral "Exactly what it sounds like! A board that says \"story\"!"

    #It's funny and all, but doesn't the perosn say above that they wanted a visual representation of their story so they created a storyboard?
    #Oh, crap, forgot about that part.

    "I covered my face with my palm, sighing."
    menu:
        me "No, that's not a storyboard at all! A storyboard is..."
        "Where you plan out the story using pictures":
            partridge neutral "I... Suppose I have learned something today. I thank you, stranger."
            jump __good_storyboard
        "Where you plan out the story using only text":
            jump __bad_storyboard
        "A special type of black-board, especially made for story-writing":
            jump __bad_storyboard
        "A story with boards":
            jump __bad_storyboard
        "A board with stories":
            jump __bad_storyboard

label __bad_storyboard:
    $ __wrongpartridge += 1
    partridge sad "Hmm.. You do seem knowledgeable on the subject. I think."
    jump __good_storyboard

label __good_storyboard:
    "We were suddenly interrupted by an evil cackle. A ghotly voice came from behind us."
    show ghost appear at left
    ghost "There you are..."
    scene town2 frosty_playground
    with dissolve
    show ghost happy at left
    show partridge sad at right
    "A chill ran down my spine, as the air suddenly seemed colder. The playground suddenly started freezing from one end to the other."
    ghost "Flee, flee, flee in horror!"
    "We all got up and ran."
    me "Squirrel! Call the icefighters!"
    hide partridge with dissolve
    show squirrel no at right with dissolve
    squirrel "Icefighters? What universe do you live in?!"
    hide squirrel with dissolve
    me "Less talking, more running!"
    if __wrongpartridge > 0:
        jump __rippartridge
    else:
        jump __perspective

label __rippartridge:
    "As we ran, I noticed that only the fox and squirrel were next to me."
    me "Partridge? Anyone know where the partridge went?"
    "I slowed down, and looked back at the playground. {w}"
    show partridge sad at right with dissolve
    "There stood the partridge, having not moved out of his spot."
    me "What are you doing? We need to get away from that ghost!"
    ghost "Mwaahahah... He is mine. He knows his sin, and he cannot flee."
    show partridge very_sad
    "The partidge shook in fear, as the icy cold drew closer."
    ghost "Yeesss... I feel that this is a fitting end for you... Frozen, frozen in place!"
    "We watched in horror as the ice slowly spread from te grass, up the partridge's leg, slowly crawling across his body and trapping him in ice."
    hide partridge with dissolve
    show fox neutral_sceptic at right with dissolve
    fox "Come on you two, no time for staring. Unless you want to end up like him."
    hide fox with dissolve
    "Those simple words of \"encouragement\" were enough to get us moving. The ghost cackled evilly as we ran, but made no move to follow us."
    $ __partridge = 1
    jump __perspective

label __perspective:
    scene town2 palms
    with fade_scene

    $ __deadsquirrel = 0
    $ __squirrel = 0
    #moved this here for rollback purposes
    "When we finally stopped running, we were by the ocean. Large palm trees were standing by the sidewalks, giving us a bit of shade from the harsh sun."
    show squirrel hmm with dissolve
    "After regaining my breath, I I looked at the squirrel."
    me "So... Let's continue where we left off."
    "I looked at the squirrel, who seemed to avoid my gaze."
    me "Let's talk about camera. What did you do when recording?"
    squirrel happy "Well, we used many cinematic effects to make it into a more interesting watching experience-..."
    "I raised a hand to silence him."
    me "Who's being chased by the Ghost of Bad Filmmaking? You. So let's skip the lying part."
    show squirrel mad
    "The squirrel seemed annoyed."
    me "Tell me a bit about the scenes you have."
    squirrel no "Well, we have this one scene where this one person tries to look intimidating."
    me "And what perspective did you use?"
    squirrel talking "We used the, uhh, apple perspective!"

    menu:
        "No, no, that's not right at all.":
            me "I'm pretty sure that the \"apple perspective\" doesn't exist."
            "The squirrel seemed pretty nervous."
            squirrel no "Well, uuh.. How would you do it, then?"
        "That sounds correct.":
            me "Let's move on to the next thing, then."
            $ __deadsquirrel += 1
            jump __camera

    menu:
        "To make someone look intimidating, I would use.."
        "Worm's-eye view":
            squirrel "O-of course I knew that."
            me "In that case, let's move on!"
            jump __good_perspective
        "Low angle":
            jump __bad_perspective
        "Eye-level":
            jump __bad_perspective
        "High angle":
            jump __bad_perspective
        "Bird's-eye view":
            jump __bad_perspective

label __bad_perspective:
    $ deadsquirrel += 1
    squirrel no "W-well, I liked my suggestion just as much!"
    me "Do I look like I care? No. Let's move on!"
    jump __good_perspective

label __good_perspective:
    jump __camera

label __camera:
    me "What kind of camera movements did you use?"
    squirrel no "We used, uhmm, tanning at one point."
    me "I've never heard of a camera movement called \"tanning\"."
    squirrel hmm "......"
    "I crossed my arms."
    me "What do you actually know about camera movement?"
    squirrel no "Lots! What do {i}you{/i} know?"

    menu:
        "The three basic camera movements are called..."
        "Panning, tilting and moving":
            squirrel ".. Alright, I admit you might know a thing or two."
            jump __good_camera
        "Tilting, angling and booming":
            jump __bad_camera
        "Moving, angling and zooming":
            jump __bad_camera
        "Tilting, panning and zooming":
            jump __bad_camera
        "Panning, focusing and moving":
            jump __bad_camera

label __bad_camera:
    squirrel "Not a tanning in there somewhere? No?..."
    $ __deadsquirrel += 1
    jump __good_camera

label __good_camera:
    jump __editing

label __editing:
    me "Hold on! I'm not done yet. You should also be in charge of editing, yes?"
    show squirrel hmm
    "The squirrel nodded meekly."
    me "Good. Now tell me this; how do you edit film?"
    show squirrel no

    menu:
        squirrel "Well, uhh, you print the film as pictures and then take some scissors, and..."
        "Wrong!":
            squirrel "What then?"
            me "Well, there are two ways of doing it..."
            # Falls out of menu
        "Okay, I'll give you this one.":
            squirrel "What do you mean, \"give me this one\"?"
            me "Uhh, don't worry about it."
            "The squirrel seemed sceptical."
            jump __ghost

    menu:
        "Which of these methods is NOT used for film editing?" #TODO: Have a correct answer
        "Physically cutting film-strips and putting them together.":
            jump __bad_editing
        "Not editing at all, so called cut-in-camera.":
            jump __bad_editing
        "Digitally putting files together.":
            jump __bad_editing

label __bad_editing:
    squirrel "So you're saying that (whatever wrong answer we put here) can be used for editing? I had no idea!"
    me "Indeed! Oh, and did you know that in the seventeenth century..."
    $ __deadsquirrel += 1
    jump __ghost

label __good_editing:
    squirrel "Alright, alright, I admit defeat. Now please, stop this interrogation."
    "I gave the squirrel a smug smirk."
    me "Well, then, let's-.."
    jump __ghost

label __ghost:
    scene town2 foggy_palms
    with dissolve
    "Before I could say anymore, a thick fog started rolling in from the seas."
    show ghost appear at left
    ghost happy "Did someone say \"terrible filmmaking\"?"
    me "Oh no, not again! Let's dash, guys!"
    show fox neutral_sceptic at right with dissolve
    fox "No need to tell me twice!"
    hide fox with dissolve

    if __deadsquirrel >0:
        jump __ripsquirrel
    else:
        jump __post

label __ripsquirrel:
    "As we ran, I suddenly noticed that the squirrel wasn't following us."
    show squirrel hmm at right with dissolve
    me "Come on, squirrel!"
    "The squirrel didn't reply."
    me "We need to get out of here!"
    "The squirrel still didn't reply, simply staring at the fog, covering the place like a blanket."
    squirrel no "I-I... I'll see you later, guys..."
    if __partridge==0:
        show partridge no at center, flip with dissolve
        partridge "We need you on this crew! Snap out of it!"
        squirrel "S-sorry..."
        hide partridge with dissolve
        "The partridge seemed like he wanted to run back and get the squirrel, but the ominous fog was keeping him from rushing in."
    else:
        show fox neutral_normal at center, flip with dissolve
        fox "Come on, squirrel, don't end up like that old partridge!"
        me "Please don't leave me alone with this fox!"
        fox neutral_sceptic "{i}What{/i} did you say, brat?"
        me "Uhhmm.."
        hide fox with dissolve
    "Before we could say anymore, large hands formed from the fog, reaching down to carress the poor squirrel."
    "Strange whispers of \"everything is going to be alright\" kept the squirrel ensnared, allowing him no escape."
    show fox neutral_sceptic at center, flip with dissolve
    fox "We need to get away from here."
    hide fox with dissolve
    if __partridge==0:
        hide squirrel with dissolve
        "The partridge seemed reluctant to leave, but when the fog swallowed the squirrel whole, and he was no longer in sight, the partridge complied."
        show partridge no at right with dissolve
        partridge "She's right... We can't stay here."
        show partridge sad
        "The partridge looked at his feet. On the ground, the squirrel's camera was lying. How did it get there? Maybe it was fate. At any rate, the partridge picked up the camera."
        hide partridge with dissolve
    else:
        me "If only there was a way to save him!"
        hide squirrel with dissolve
        "The fog had finally swallowed the squirrel whole, leaving no trace that he was ever there. The fox snarled at me."
        show fox neutral_sceptic at right with dissolve
        fox "Give up already! I don't feel like dying today."
        hide fox with dissolve
    "As we ran away, the ghost made no move to follow us."
    hide ghost with dissolve

    $ __squirrel = 1
    jump __post

label __post:
    scene town2 underpass
    with fade_scene
    $ __wrongfox = 0
    $ __fox = 0
    #Moved here for rollback purposes
    "We ended up in a tunnel, still being able to see the sea in the distance."
    "This time, I directed my attention at the fox."
    show fox neutral_normal with dissolve
    me "So.. You're the last link."
    "She narrowed her eyes."
    fox neutral_sceptic "What do you want with me?"
    me "Just fix a few mistakes, that's all."
    "She huffed, but otherwise only seemed passive-agressive."
    me "So I take it you were an actor in this film?"
    fox talking_normal "That... Might have been my main role, yes."
    me "So you also did something else?"
    fox neutral_normal "I might have been involved in some... Decisions, yes."
    me "You were involved in post-production, then?"
    "The fox seemed to think about this for a moment before nodding."
    me "Can you tell me what happens during post-production?"
    fox talking_normal "It would be... Great if you could refresh my mind about the matter."

    menu:
        "What does post-production consist of?"
        "Music, credits, editing, VFX, PR etc.":
            fox "Exactly!"
            jump __good_post
        "Casting, synopsis, manuscript, storyboard etc.":
            jump __bad_post
        "Credits, music, VFX, casting, PR etc.":
            jump __bad_post
        "Manuscript, music, VFX, PR etc.":
            jump __bad_post
        "Editing, VFX, credits, manuscript etc.":
            jump __bad_post

label __bad_post:
    fox neutral_sceptic "Really...? I thought we did that in pre."
    me "No, you do it twice. It's doubly important!"
    $ __wrongfox += 1
    jump __good_post

label __good_post:
    me "Was that what you did in this production, then?"
    fox talking_sceptic "I am above such matters."
    "I sighed. I wasn't getting anywhere with this fox."
    jump __pr

label __pr:
    me "What about PR?"
    fox talking_normal "Private records? Mine are spotless!"
    "I raised an eyebow."
    me "No, that wasn't what I meant at all."

    menu:
        "What is PR?"
        "Public Relations":
            fox "Oh, you should just have said so from the beginning."
            jump __good_pr
        "Purple Rollercoaster":
            jump __bad_pr
        "People's Reaction":
            jump __bad_pr
        "Public Reaction":
            jump __bad_pr
        "People's Relations":
            jump __bad_pr

label __bad_pr:
    fox "Oh, you had me worried for a moment. Though I must admit, I've never heard of this before."
    $ __wrongfox += 1
    jump __good_pr

label __good_pr:
    "The voice we had started to anticipate, returned from above."
    show ghost appear
    show ghost happy
    ghost "I have returned, sinners!"
    "It poked its head out of the ceiling before floating down to eye-level."

    if __wrongfox > 0:
        jump __ripfox
    else:
        jump __deciding

label __ripfox:
    "The ghost barely gave us time to react, before he picked up the fox and threw her at a wall. Glaring at me, he spoke."
    ghost meh "I have no qualms with you."
    "As the shape said this, it slowly floated towards the fox who was slumped on the ground."
    if __squirrel==0:
        show squirrel no at right with dissolve
        squirrel "L-leave her alone!"
        hide squirrel with dissolve
    elif __partridge==0:
        show partridge no at right with dissolve
        partridge "What are you doing to her?!"
        hide partridge with dissolve
    else:
        me "S-stop! Don't leave me here alone!"
    "The ghost simply laughed."
    ghost happy "This one... This one deserves it most of all."
    "The ghost raised its spectral hand, clamping it around the fox's throat."
    if __partridge==0:
        show partridge no at right with dissolve
        partridge "Please!"
        "The ghost didn't seem to hear him."
        hide partridge with dissolve
    "As the final light of life left the fox's eyes, the ghost turned its attention towards me."
    $ __fox = 1
    jump __deciding

label __deciding:

    if __fox==0 and __squirrel==0 and __partridge==0:
        jump __everyone_lives
    elif __fox==1 and __squirrel==1 and __partridge==1:
        jump __noone_lives
    else:
        jump __someone_lives

label __noone_lives:
    ghost "I have done all I came to do. At first, I considered whether you were sinful, too. But I have gotten my vengeance for now. I have other, more important places to be."
    "I looked at the discarded body of the fox."
    me "What do I do now..."
    "The ghost shrugged at me, before vanishing.{w} Sighing, I sat down on the ground by the limp and lifeless fox."
    hide ghost with dissolve
    me "This really went badly, didn't it, fox?"
    "The fox, of course, didn't reply."
    "I was just about to get up and leave, when a loud crash came from outside, from the exit I was about to leave out of."
    me "Wha-?..."
    unknown "MWAHAHAHAH! I don't believe my LUCK!"
    show magenta glee
    "A large head slithered through the entrance of the tunnel."
    unknown "That the stench of ROTTEN CORPSES would lead me to you, of all things!"
    me "Wh-who are you?"
    magenta annoyed_talking "You have never heard of me, the fearsome Magenta?!"
    me "But..."
    magenta mad "SILENCE!"
    "The dragon moved its head closer to me, studying me with her eye. Cackling, she drew back her head."
    magenta glee "No doubt about it. You will not leave this place alive, MORTAL! Try and FLEE, if you will."
    "The dragon seemed to wait a bit for me to run. Seeing that I didn't move at all, she narrowed her eyes."
    magenta annoyed_talking "Very well. If you do not move, I might as well BURN YOU WHERE YOU STAND! MWAHAHAHAH!"
    "The dragon opened its huge jaws, a red glow coming from its throat. Finally realising that I should probably move, I stood up and started running for the far exit."
    magenta mad "YOU CANNOT OUTRUN MY FIRE!"
    "The red glow got released as a relentless torrent of fire, drawing ever closer."
    $ die(1)
    "Magenta immediately seemed disinterested."
    magenta annoyed_talking "That was more boring than I thought it would be. Here I spent all this time chasing this one down, and this is the challenge I get?"
    "Magenta sighed, pulling her head out of the tunnel, looking up at the clear skies."
    magenta talking "Oh, well. Time to find somewhere else to spread misery."
    "Magenta flapped her large bat-like wings and took off, leaving a charred tunnel and two corpses behind."

label __someone_lives:
    "The ghost stared me in the eyes."
    ghost meh "I have observed you! And I have decided that you too are a sinner!"
    "The ghost seemed to grin evilly."
    ghost "It is time to get rid of the remaining pests..."
    if __squirrel==1 and __partridge==0:
        show partridge no at right
        partridge "No!"
        show partridge sad
        "The partridge raised the camera he had picked up from the squirrel, the blitz flashing briefly. The ghost raised an arm to cover for its eyes."
        ghost "Bright! Briight!"
        "The partridge kept firing the blitz at the ghost, keeping it occupied."
        partridge no "You there! Pick up my phone and call the police!"
        "The partridge threw his phone to me. The ghost growled in rage."
        me "Are you sure I shouldn't call the ghostbusters instead?"
        show partridge sad
        "The partridge was too busy keeping the ghost at bay to respond. I raised my phone to call the police."
        centered "{size=+10}A few tense moments later...{/size}"
        "A red car arrived. I was almost getting bored of waiting, and the partridge was getting worried that the camera might run out of battery soon."
        "A sloth hurried out of the car, having something akin to a vacuum cleaner strapped to his back."
        me "You're a ghostbuster?!"
        sloth "I have dabbled a bit in these cases, yes. After all, every city needs a jack of all trades!"
        "The sloth raised the vacuum cleaner, pointing it at the ghost."
        ghost "Nooo!"
        sloth "Yes!"
        "The sloth was sucked up into the vacuum cleaner, every trace that it had ever been there, gone."
        me "Thank you mister sloth!"
        sloth "I have a name, you know..."
        "I smiled sheepishly at the sloth. I had totally forgotten his name."
        sloth "At any rate, I'm sorry I got you into this mess, traveler."
        me "You can repay me by showing me the way north! I'm going to the capital, after all."
        sloth "Are you sure you would not like me to drive you there?"
        me "No, it's okay. I'm starting to like this fresh air. It's weird."
        sloth "Okay... I will... Clean up after this mess. I wish you a good journey."
        me "Thank you!"
        if __fox==0:
            "... And with that, I waved goodbye to the partridge, the sloth and the fox, and continued my journey."
        else:
            "... And with that, I waved goodbye to the partridge and the sloth, and continued my journey."
        "I was drawing ever closer to the capital, on this danger-filled journey, but I had a good feeling about the future. After all, what could ever go wrong?"
        scene black
        with fade_scene
        centered "{size=+10}End of Chapter 2.{/size}"
        #jump scene03
    else:
        "The ghost snapped its fingers,{w}"
        scene black
        "and the room was enveloped by pitch-black darkness."
        me "He-hello? Anybody there?"
        "No reply."
        me "Anyone?"
        "The silence was deafening."
        "Suddenly,{w}"
        scene eyes with dissolve
        "two large white eyes opened to stare at me."
        unknown "Don't worry... Don't worry... It's all going to be alright..."
        "The eyes seemed to draw closer, until the whiteness was blinding."
        "I slowly felt my consciousness fade."
        $ die(2)
        unknown "Mwahahahah..."


label __everyone_lives:
    me "Who are you calling sinners? Haven't you seen that these people have learnt from their mistakes? I'm sure they'll produce a fantastic movie now, if only you let them!"
    "The ghostly being seemed to ponder over this for a while."
    ghost "Are you absolutely sure that you will not commit a crime of this scale against mankind again?"
    "The fox, the partridge and the squirrel all nodded enthusiastically. The ghost crossed its arms."
    ghost "Pinky swear?"
    "The three noded again.\nThe ghost sighed exhaustedly."
    ghost "Very well. But if anything like this happens again... At any rate, I have somewhere better to be. I've heard that the scoundrel, Horse Ruecas is making another terrible movie. Adieu, adieu! I wish thee adieu."
    "The ghost seemed to fade away, this time leaving for good."
    hide ghost with dissolve
    me "Looks like we're saved, people!"
    show partridge neutral at right with dissolve
    partridge "Indeed.. And I believe we have you to thank for this! This just shows that I should have taken an education before starting this job..."
    show fox neutral_sceptic at left, flip with dissolve
    fox "That was the last straw. I'm done working with you people!"
    "The fox threw her parasol on the floor, walking away with clenched fists."
    hide fox with dissolve
    show squirrel at left, flip with dissolve
    squirrel talking "That sure was something."
    partridge neutral "Stranger, I believe we have never asked for your name?"
    me "I'm [name]! Just passing by."
    partridge hi "Whatever your reason for being here is, we are forever in your debt."
    squirrel happy "Indeed! Now, does anyone feel like calling for a police officer?"
    centered "A moment later..."
    me "Oh, hello, mister sloth!"
    sloth "I have a name, you know..."
    "I smiled sheepishly at the sloth. I had totally forgotten his name."
    sloth "At any rate, I'm sorry I got you into this mess, traveler."
    me "You can repay me by showing me the way north! I'm going to the capital, after all."
    sloth "Are you sure you would not like me to drive you there?"
    me "No, it's okay. I'm starting to like this fresh air. It's weird."
    sloth "Okay... I will finish up with these two, then. I wish you a good journey."
    me "Thank you!"
    "... And with that, I waved goodbye to the partridge, the sloth and the squirrel, and continued my journey."
    "I was drawing ever closer to the capital, on this danger-filled journey, but I had a good feeling about the future. After all, what could ever go wrong?"
    scene black
    with fade_scene
    centered "{size=+10}End of Chapter 2.{/size}"
    #jump scene03