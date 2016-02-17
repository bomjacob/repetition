label scene02:
    scene town2 cafe
    "As I opened the saloon-like doors, I was greeted by a place furnished like a restaurant. A partridge, a fox and a squirrel (and possibly more) seemed to be arguing about something."
    partridge "No, it should definitely be cut like this! That adds the most suspense!"
    fox "No, this it should be cut like this instead. This shows me from the best angle!"
    squirrel "My professional opinion states that it should be cut like this, for the best dramatic effect!"
    "As the saloon-like doors closed behind me, three pairs of eyes stared intently at me."
    partridge "You there! What do you think? Crossclipping, zooming or an over-shoulder view of our heroine?"
    "The fox scoffed."
    fox "Why do I work with such simpleminded people? Clearly zooming on my face here would be the best option! It’s what the people want!"
    "The partridge crossed its wings."
    partridge "A camera movement like that wouldn’t progress the story in any way! We should cut it just as he runs out the door.."
    "The squirrel shook its head, sighing resignedly."

    menu:
        squirrel "So? What do you think?"
        "Cut! It adds suspense.":
            partridge "Hah! See, this person agrees with me! I kne-.."
        "Zoom! It’s what the people want.":
            fox "See, this person is smart. This person knows what is the right thing to-.."
        "Over-shoulder! It’s dramatic.":
            squirrel "That’s what I thought too. See, people? This is definitely the right cho-.."


    "The lights suddenly flickered off, as the front doors flew open, a gust of wind circling around the room before dying out.{w} A few seconds later, the lights flickered back on."
    fox "I thought you hired proper electricians for this job!"
    partridge "I-.. I did, I swear! I’m not sure what that-.."
    squirrel "Silent everyone! It would seem something is coming."
    "As if waiting for this to happen, a mysterious voice resounded through the wooden walls and fake furniture."
    unknown "Fire? Yes, yes! Fire. You have done me injustice. You have done the world a horrible injustice!"
    ghost "I am the Ghost of Bad Filmmaking here to tell you that you are doing the world a terrible, unjustified injustice! The world weeps!"
    "The fox’s eyes widened, though she seemed to keep her calm, denying the existence of this bodyless voice for the moment. The squirrel kept moving his head around, searching for the voice of the perpetrator. The partridge seemed to have the most calm out of all of them, even daring to speak."
    partridge "Who is this? Show yourself!"
    "A ghostly laugh went through the walls, seeming to come from all directions. A small light flickered in mid-air. {w}The light flickered again, growing a bit larger. It seemed to rotate around itself, swallowing itself, growing larger and larger until it formed a ghastly shape."
    ghost "I have seen your sin! This terrible crime of a movie! I am in disgust!"
    "The ghost seemed to cry out of a strange mix between rage and sadness, the luminescent tears disappearing without a trace as soon as they touched the ground below."
    ghost "I give you this warning! If you do not fix your terrible excuse for a film, this crime against humanity, you will be punished! Nothing less than death will suffice! Now, flee! Tremble in terror and repent! I am a merciful evil!"
    "The ghost snapped what looked like its fingers, making a small spark appear. The small spark jumped around, hopping from the ghostly shape to the floor, and around the furniture. Everywhere it touched, burst into flames."

    scene town2 burning_cafe

    "I, who was standing at the entrance, quickly realised what was happening."
    me "Hurry up, guys! If you stay like this, you'll get charred to ash!"
    "This seemed to snap the three out of their trance, as they ran for the front door. Just as we got to the doorway, the entire inside of the fake restaurent burst into flames. The ghost-like form cackled."
    ghost "You may have escaped your doom this time. But as long as your sin remains, do not expect to avoid the fiery demise that awaits you! The world will have justice from terrible filmmakers like you!"

    scene town2 red_houses

    "We ran outside, leaving behind the burning props. The fox seemed offended that she had to run anywhere. The partridge looked back at the burning building in despair."
    me "Does anyone have a phone? We should probably call the firefighters.."
    "The squirrel took a mobile phone out of his pocket, pressing a few buttons before holding it to his ear."
    squirrel "Yes, hello? We have a fire out here, you might want to send some people."
    "I turned my attention towards the fox and the partridge."
    me "I don't think we're safe yet. Do you know of anywhere we can talk? I get the feeling you guys have some things we need to talk about."
    "The partridge was finally able to draw his eyes away from the burning building, and looked at me."
    partridge "We should probably go somewhere else."
    "We waited a few more moments before the fire department arrived, before going to a nearby playground."

    scene town2 playground

    partridge "We can sit here."
    "I nodded at him, and we all took place around the playground."
    me "So... In a desperate attempt to save your hides, why don't we start at the beggining? That would be pre-production..."
    "Upon hearing this, the fox immediately seemed disinterested. It would seem she didn't have much to do with the pre-production."
    squirrel "We have planned this project meticulously!"
    me "Yeah? So what did your post-production consist of?" # Do you mean pre?

    #I'm not sure this is what you want for this part :/ Like do you wanna go to the "go on" part even if you answer wait? It's kinda hard to decode without /any/ tabs/leading spaces in your text.
    menu:
        partridge "Well, we started out with finding our cast..."
        "Wait!":
            me "You started with /casting/?"
            partridge "Yes? Is there anything wrong with that?"
            me "Yes! Everything is wrong with that!"
        "Go oon...":
            menu:
                partridge "Then we went on with making a storyboard..."
                "Wait!":
                    me "You made a storyboard before you made the actual story??"
                    partridge "Well, we wanted a visual representation..."
                    me "No, no, no. That's completely wrong."
                "Go oooon...":
                    menu:
                        partridge "After that, we found the music we wanted to use."
                        "Wait!":
                            me "So let me get this right.. You haven't even found a genre yet, and you already found music for it?"
                            partridge "Genre is unimportant! We could always decide that after finding some awesome music!"
                            me "That's not how filmmaking works!"
                        "Go oooooon...":
                            partridge "Lastly, we made our synopsis to recap all things we had planned."
                            menu:
                                "Wait!":
                                    me "You made your synopsis last?! You're supposed to make that first!"
                                    partridge "You are? But.. But.."
                                    me "Yes! It's completely wrong!"
                                "That sounds completely fine.":
                                    me "I'm not sure why the ghost is hunting you down, then. This is a stellar example of how to do pre-production!"

    # *if you got that wrong (chose the wrong thing /all/ times) insert horrible death scene*
    # Only if you get them /all/ wrong? I'm more thinking if you get /any/ wrong :P

    # So if /all/ is correct:
    jump __good_pre

label __pre:
    partridge "Well, how would /you/ do it then?"

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
    "No..."
    jump __storyboard

label __good_pre:
    "Yeah!"
    jump __storyboard

label __storyboard:
    me "And now that we're on the subject of pre-production, why don't we talk about your storyboard?"
    partridge "I would've shown it to you, but our storyboard was too large to carry around."
    me "It sounds like you're planned your story very well, then?"
    partridge "We have? I was just talking about the large sign we have, saying \"Story\". What are you talking about?"
    me "Sign? What exactly do you think a storyboard it?"
    partridge "Exactly what it sounds like! A board that says \"story\"!"

    #It's funny and all, but doesn't the perosn say above that they wanted a visual representation of their story so they created a storyboard?

    "I covered my face with my palm, sighing."
    menu:
        me "No, that's not a storyboard at all! A storyboard is..."
        "Where you plan out the story using pictures":
            partridge "I... Suppose I have learned something today. I thank you, stranger."
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
    "Uhmm nope!"
    jump __good_storyboard

label __good_storyboard:
    "We were suddenly interrupted by an evil cackle. A ghotly voice came from behind us."
    ghost "There you are..."
    "A chill ran down my spine, as the air suddenly seemed colder. The playground suddenly started freezing from one end to the other."
    ghost "Flee, flee, flee in horror!"
    "We all got up and ran."
    me "Squirrel! Call the icefighters!"
    squirrel "Icefighters? What universe do you live in?!"
    me "Less talking, more running!"


    # *if you got any of the above wrong, go to another scene where the partridge dies, that then continues to the following scene, too (but have it remember that the partridge died)*

    jump perspective

label perspective:
    scene town2 underpass #Is that the correct one?

    "When we finally stopped running, we were by the ocean. Large palm trees were standing by the sidewalks, giving us a bit of shade from the harsh sun."
    "After regaining my breath, I I looked at the squirrel."
    me "So... Let's continue where we left off."
    "I looked at the squirrel, who seemed to avoid my gaze."
    me "Let's talk about camera. What did you do when recording?"
    squirrel "Well, we used many cinematic effects to make it into a more interesting watching experience-..."
    "I raised a hand to silence him."
    me "Who's being chased by the Ghost of Bad Filmmaking? You. So let's skip the lying part."
    "The squirrel seemed dejected."
    me "Tell me a bit about the scenes you have."
    squirrel "Well, we have this one scene where this one person tries to look intimidating."
    me "And what perspective did you use?"
    squirrel "We used the, uhh, apple perspective!"

    menu:
        "No, no, that's not right at all.":
            me "I'm pretty sure that the \"apple perspective\" doesn't exist."
            "The squirrel seemed pretty nervous."
            squirrel "Well, uuh.. How would you do it, then?"
        "That sounds correct.":
            me "Let's move on to the next thing, then."
            #(*make it remember that you chose wrong, and jump directly to camera movement*)
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
    "Nope!"
    jump __good_perspective

label __good_perspective:
    jump __camera

label __camera:
    me "What kind of camera movements did you use?"
    squirrel "We used, uhmm, tanning at one point."
    me "I've never heard of a camera movement called \"tanning\"."
    squirrel "......"
    "I crossed my arms."
    me "What do you actually know about camera movement?"
    squirrel "Lots! What do {i}you{/i} know?"

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
    "Uhmm.. no.."
    jump __good_camera

label __good_camera:
    jump __editing

label __editing:
    me "Hold on! I'm not done yet. You should also be in charge of editing, yes?"
    "The squirrel nodded meekly."
    me "Good. Now tell me this; how do you edit film?"
    squirrel "Well, uhh, you print the film as pictures and then take some scissors, and..."

    menu:
        #What's the quesiton?
        "Wrong!":
            squirrel "What then?"
            me "Well, there are two ways of doing it..."
            # Falls out of menu
        "Okay, I'll give you this one.": #That was the answer, right? #And if you choose this, you don't have to answer the question?
            squirrel "What do you mean, \"give me this one\"?"
            me "Uhh, don't worry about it."
            "The squirrel seemed sceptical."
            #(*jump to "Before I could say anymore..*)

    menu:
        "Which of these methods is NOT used for film editing?" #Uhmm.. where is the "correct" answer? All those are methods of editing....
        "Physically cutting film-strips and putting them together.":
            jump __bad_editing
        "Not editing at all, so called cut-in-camera.":
            jump __bad_editing
        "Digitally putting files together.":
            jump __bad_editing

label __bad_editing:
    "Nope, that can definitely be used to edit films."
    jump __ghost

label __good_editing:
    squirrel "Alright, alright, I admit defeat. Now please, stop this interrogation."
    "I gave the squirrel a smug smirk."
    me "Well, then, let's-.."
    jump __ghost

label __ghost:
    "Before I could say anymore, a thick fog started rolling in from the seas."
    ghost "Did someone say \"terrible filmmaking\"?"
    me "Oh, not again! Let's dash, guys!"
    fox "No need to tell me twice!"

    # (*insert extra scene for squirrel dying if any of the above was wrong, then proceed to following scene and remember if the squirrel died*)
    # "Any of the above", which are that? All of them? Or just the ones after the partridge potentially died?

    jump __post

label __post:
    scene town2 underpass #Okay now it's definitely this one... No idea what the previous was then.

    "We ended up in a tunnel, still being able to see the sea in the distance."
    "This time, I directed my attention at the fox."
    me "So.. You're the last link."
    "She crossed her arms"
    fox "What do you want with me?"
    me "Just fix a few mistakes, that's all."
    "She huffed, but otherwise only seemed passive-agressive."
    me "So I take it you were an actor in this film?"
    fox "That... Might have been my main role, yes."
    me "So you also did something else?"
    fox "I might have been involved in some... Decisions, yes."
    me "You were involved in post-production, then?"
    "The fox seemed to think about this for a moment before nodding."
    me "Can you tell me what happens during post-production?"
    fox "It would be... Great if you could refresh my mind about the matter."

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
    "Really... we did that in pre."
    jump __good_post

label __good_post:
    me "Was that what you did, then?"
    fox "I am above such matters."
    "I sighed. I wasn't getting anywhere with this fox."
    jump __pr

label __pr:
    me "What about PR?"
    fox "Private records? Mine are spotless!"
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
    "No... no"
    jump __good_pr

label __good_pr:
    "The voice we had started to anticipate, returned from above."
    ghost "I have returned, sinners!"
    "It poked its head out of the ceiling before floating down to eye-level."

    # if none have died "(*insert two other tags for "if some have died" and "if all have died"*)
    # I have no idea what you mean by that ^

    me "Who are you calling sinners? Haven't you seen that these people have learnt from their mistakes? I'm sure they'll produce a fantastic movie now, if only you let them!"
    "The ghostly being seemed to ponder over this for a while."
    ghost "Are you absolutely sure that you will not commit a crime of this scale against mankind again?"
    "The fox, the partridge and the squirrel all nodded enthusiastically. The ghost crossed its arms."
    ghost "Pinky swear?"
    "The three noded again.\nThe ghost sighed exhaustedly."
    ghost "Very well. But if anything like this happens again... At any rate, I have somewhere better to be. I've heard that the scoundrel, Horse Ruecas is making another terrible movie. Adieu, adieu! I wish thee adieu."
    "The ghost seemed to fade away, this time leaving for good."
    me "Looks like we're saved, people!"
    partridge "Indeed.. And I believe we have you to thank for this! This just shows that I should have taken an education before starting this job..."
    fox "That was the last straw. I'm done working with you people!"
    "The fox threw her parasol on the floor, walking away with clenched fists."
    squirrel "That sure was something."
    partridge "Stranger, I believe we have never asked for your name?"
    me "I'm [name]! Just passing by."
    partridge "Whatever your reason for being here is, we are forever in your debt."
    squirrel "Indeed! Now, does anyone feel like calling for a police officer?"
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
    scene black with fade_scene
    centered "{size=+10}End of chapter 1.{/size}"