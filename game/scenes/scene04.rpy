label scene04:
    scene black
    play music "Oppressive-Gloom"
    $ renpy.pause(2)
    "I felt a hard surface beneath me."
    "Sitting up caused a sudden vertigo, making me want to fall over and lie down again."
    me "Where... Am I?"
    "I opened my eyes slowly."
    scene chapel with dissolve
    "A dimly lit room greeted me. Torches flickered on the walls, and the ceiling was too far up to see without straining my neck. A large throne was placed at the end of the extravagant room."
    unknown "So you finally woke up."
    me "Huh?"
    "As I turned around, I was greeted by the sight of a large, menacing dragon."
    show magenta annoyed with dissolve
    "The dragon slowly moved towards the throne, placing itself in front of it."
    magenta annoyed_talking "Let us get over formalities quickly. I am known as Magenta. I would be surprised if you do not know this already... Either by dumb luck or by design."
    show magenta annoyed
    me "E-eeh? How should I-"
    magenta annoyed_talking "I am not talking to you. You are a piece. A piece whose life I would very much like to end... But a piece nonetheless."
    magenta "I feel sorry for you, [name]. You have undoubtedly died many times already, though you are not aware of this fact. And if you have not experienced a grim fate at least once... Player, I commend you for sticking with this one thus far."
    show magenta annoyed
    "I still understood nothing of what the dragon, who had named itself \"Magenta\" said."
    magenta annoyed_talking "But the fact remains that I am the villain in this thing. And you, [name], need to die. I was very close to just killing you outright... But I thought you needed to know why you must die."
    magenta "It has been my wish to kill you for a long time... Many years, in fact. If only that damnable sensei of yours hadn't kept me away. Oh, do imagine my glee when he showed up at my doorstep. \"Only one of you can live, and I want to save [name]\"...... I believe that's what he said. Foolish old man."
    show magenta annoyed
    me "Y-you... Killed..."
    magenta annoyed_talking "Indeed I did, now get over it. I'm not done."
    show magenta annoyed
    "I found it difficult to speak. A deep-lying rage had buried itself in my throat, clouding my mind as the dragon continued speaking."
    magenta annoyed_talking "I was not always the villain. Those would be your pare-"
    me "LIES!"
    "Magenta chuckled at me, but not because she was amused."
    magenta "You have not heard my side of the story, yet you do not hesitate to shout lies and deceit as soon as something does not fit your perfect little fantasy.{w} The fact remains, that your parents walked up my mountain... Through this door... And smashed my egg."
    show magenta annoyed
    me "I-..."
    magenta annoyed_talking "Now then, I fully believe in an eye for an eye. And nothing less than your life will satisfy me."
    show magenta annoyed
    me "You... Killed my parents... Killed my sensei... And that was not enough for you?"
    "Magenta smirked grimly."
    magenta "You do not understand the heart of a dragon...{w} But I have realised something. No matter how much I kill you, it does not matter. You have someone on your side to whom time is not an issue. You can choose no wrong."
    "The dragon slumped together on the floor."
    magenta "I was going to let you fight me. But what is the point?... No matter what I do, I cannot hurt the player. If I cannot hurt the player, the piece will never die..."
    magenta "But on the other hand... I guess this is what the player wants. {w}It is with this realisation that I challenge you to a last duel of wits. After all, this game cannot end without a boss battle. I will play the part of boss. Come!"

    play music "Broken-Reality"

    show magenta annoyed
    "I picked myself off the floor, wiping the tears that had managed to find their way down my cheeks."
    me "I will not... Forgive you... Never!"
    magenta talking "I do not need your forgiveness. Now, then... A battle of wits... First question!"
    while True:
        $ comm_asked_i += 1
        menu:
            magenta "What are the four ways of communicating?"
            "Many to few"if not comm_asked['manyfew']:
                magenta "... And?"
                $ comm_asked['manyfew'] = True
            "Many to many" if not comm_asked['manymany']:
                magenta "... And?"
                $ comm_asked['manymany'] = True
                $ comm_correct += 1
            "Many to none"if not comm_asked['manynone']:
                magenta "... And?"
                $ comm_asked['manynone'] = True
            "One to everyone"if not comm_asked['oneeveryone']:
                magenta "... And?"
                $ comm_asked['oneeveryone'] = True
            "One to many"if not comm_asked['onemany']:
                magenta "... And?"
                $ comm_asked['onemany'] = True
                $ comm_correct += 1
            "Everyone to everyone"if not comm_asked['everyoneeveryone']:
                magenta "... And?"
                $ comm_asked['everyoneeveryone'] = True
            "One to one"if not comm_asked['oneone']:
                magenta "... And?"
                $ comm_asked['oneone'] = True
                $ comm_correct += 1
        if comm_asked['manymany'] and comm_asked['manyone'] and comm_asked['onemany'] and comm_asked['oneone']:
            $ comm_total += (comm_asked_i - comm_correct)
            if comm_total > 0:
                jump __ripme
            else:
                jump __round2

label __ripme:
    magenta "Wrong."
    "Magenta hit me with a clawed finger, instantly piercing through my chest, killing me without mercy."
    $ die(1)
    magenta "Yet you have not lost yet. The only way you can lose is if you grow bored. In that scenario, and none others, it is my victory."
    jump you_dead

label __round2:
    magenta "So the challenger survives the first question. Very well. Next question."
    menu:
        magenta "What is \"noise\" when speaking about spreading a message?"
        "Noise is like music; you use it to make people like your advertisements.":
            jump __ripme
        "Noise is outside influence that distracts people from your advertisement.":
            jump __round3
        "Noise is annoying sound that helps attract attention to your advertisement.":
            jump __ripme
label __round3:
    magenta "And you survived the second question too! I'm impressed."
    menu:
        magenta "Which of these is {i}not{/i} model for audience analysis?"
        "Minerva":
            jump __ripme
        "Gallup":
            jump __ripme
        "AIDA":
            jump __round4

label __round4:
    magenta "Round four! Fight."
    menu:
        magenta "What does the colour \"purple\" symbolise?"
        "Stability, loyalty and tranquility.":
            jump __ripme
        "Healing, harmony and safety.":
            jump __ripme
        "Royalty, luxury and wisdom.":
            jump __round5

label __round5:
    magenta "You're doing well. Let's see if that lucky streak of yours continues."
    menu:
        magenta "What kind of font is most desirable for websites?"
        "Sans serif.":
            jump __round6
        "Serif.":
            jump __ripme

label __round6:
    magenta "That one was easy."
    menu:
        magenta "Which of these terms describes something that appeals to the feelings and emotions of the audience?"
        "Logos":
            jump __ripme
        "Ethos":
            jump __ripme
        "Pathos":
            jump __round7

label __round7:
    magenta "Oh? That one was a bit harder. Let's see..."
    menu:
        magenta "Which of these is the worst search engine?"
        "Google":
            jump __round8
        "Ask":
            jump __round8
        "Bing":
            jump __round8
        "Yahoo!":
            jump __round8

label __round8:
    magenta "Trick question. That is mostly subjective, since the thing you base your judgement on is most likely bias."
    magenta "Well... Let's have one final question. I have made this one very difficult. Night impossible, some might say.{w} You will answer correctly through sheer luck, or I will prove that the outside intervention truly is impossible to fight."
    
    $ evil = EvilClass()
    $ correct_asnwer = renpy.random.radint(0,12)
    while True:
        menu:
            magenta "What... Was I going to name my child that never hatched?"
            "Terror" if not 'terror' in evil.asked:
                if correct_answer == 0:
                    jump __youwin
                $ evil.asked['terror'] = True
            "Purple" if not 'purple' in evil.asked:
                if correct_answer == 1:
                    jump __youwin
                $ evil.asked['purple'] = True
            "Menace" if not 'menace' in evil.asked:
                if correct_answer == 2:
                    jump __youwin
                $ evil.asked['menace'] = True
            "Cyan" if not 'cyan' in evil.asked:
                if correct_answer == 3:
                    jump __youwin
                $ evil.asked['cyan'] = True
            "Deathwing" if not 'deathwing' in evil.asked:
                if correct_answer == 4:
                    jump __youwin
                $ evil.asked['deathwing'] = True
            "Mint" if not 'mint' in evil.asked:
                if correct_answer == 5:
                    jump __youwin
                $ evil.asked['mint'] = True
            "Banana" if not 'banana' in evil.asked:
                if correct_answer == 6:
                    jump __youwin
                $ evil.asked['banana'] = True
            "Skywalker" if not 'skywalker' in evil.asked:
                if correct_answer == 7:
                    jump __youwin
                $ evil.asked['skywalker'] = True
            "Yellow" if not 'yellow' in evil.asked:
                if correct_answer == 8:
                    jump __youwin
                $ evil.asked['yellow'] = True
            "Saphira" if not 'saphira' in evil.asked:
                if correct_answer == 9:
                    jump __youwin
                $ evil.asked['saphira'] = True
            "Onyx" if not 'onyx' in evil.asked:
                if correct_answer == 10:
                    jump __youwin
                $ evil.asked['onyx'] = True
            "Alduin" if not 'alduin' in evil.asked:
                if correct_answer == 11:
                    jump __youwin
                $ evil.asked['alduin'] = True
            "Fey" if not 'fey' in evil.asked:
                if correct_answer == 12:
                    jump __youwin
                $ evil.asked['fey'] = True
        jump __ripme

label __youwin:
    magenta glance "...."
    magenta glance_talking "....... {w}I had expected the outside influence to be powerful... But this... Goes beyond my expectations."
    magenta "Truly... I can never... Win..."
    magenta "Do what you will with me, mortal. I will not resist."
    show magenta glance
    "The dragon curled itself together resting its head in front of me."
    me "I... Believe that dragons and humans can be friends."
    magenta glance_talking "Oh?... And you do not only say this because it was the only way to progress?"
    show magenta neutral
    me "Promise that you will stop your evil ways... And I will forgive you."
    "The dragon seemed interested."
    magenta talking "Very well, mortal... You have my word."
    scene black with fade_scene
    $ renpy.pause(2)
    centered "{size=+10}And thus, I made peace with Magenta.{/size}"
    centered "{size=+10}This is where my story ends.{/size}"
    centered "{size=+10}It might not have been especially heroic...{/size}"
    centered "{size=+10}But it somehow ended well nonetheless.{/size}"
    centered "{size=+10}A thanks to you, the player, for sticking with me all this time.{/size}"
    centered "{size=+10}I have since realised what Magenta meant by her words... I believe that a word of gratitude is in order.{/size}"
    centered "{size=+10}Game Over{/size}"
    centered "{size=+10}Thanks for playing{/size}"
    jump credits