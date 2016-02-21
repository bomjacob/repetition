label scene04:
    scene black
    $ renpy.pause(2)
    "I felt a hard surface beneath me."
    "Sitting up caused a sudden vertigo, making me want to fall over and lie down again."
    me "Where... Am I?"
    "I opened my eyes slowly."
    scene chapel
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
    magenta "It has been my wish to kill you for a long time... Many years, in fact. If only that damnable sensei of yours hadn't kept me away. Oh, do imagine my glee when he showed up at my doorstep. \"Only one of you can live, and I want to save [name]\"...... I believe that he said. Foolish old man."
    show magenta annoyed
    me "Y-you... Killed..."
    magenta annoyed_talking "Indeed I did, now get over it. I'm not done."
    "I found it difficult to speak. A deep-lying rage had buried itself in my throat, clouding my mind as the dragon continued speaking."
    magenta "I was not always the villain. Those would be your pare-"
    me "LIES!"
    "Magenta chuckled at me, but not because she was amused."
    magenta "You have not yet heard my side of the story, yet you do not hesitate to shout lies and deceit as soon as something does not fit your perfect little fantasy.{w} The fact remains, that your parents walked up my mountain... Through this door... And smashed my eggs."
    show magenta annoyed
    me "I-..."
    magenta annoyed_talking "Now then, I fully believe in an eye for an eye. And nothing less than your life will satisfy me."
    show magenta annoyed
    me "You... Killed my parents... Killed my sensei... And that was not enough to quell your rage?"
    "Magenta smirked grimly."
    magenta "You do not understand the heart of a dragon...{w} But I have realised something. No matter how much I kill you, it does not matter. You have someone on your time to whom time is not an obstacle. You can choose no wrong."
    "The dragon slumped together on the floor."
    magenta "I was going to let you fight me. But what is the point?... No matter what I do, I cannot hurt the player. If I cannot hurt the player, the piece will never die.{w} And it is with this realisation... That I challenge you to a last duel of wits. After all, this game cannot end without a boss battle. I will play the part of boss. Come!"
    show magenta annoyed
    "I picked myself off the floor, wiping the tears that had managed to find their way down my cheeks."
    me "I will not... Forgive you.. Never!"
    magenta talking "I do not need your forgiveness. Now, then... A battle of wits..."
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
            "Many to one"if not comm_asked['manyone']:
                magenta "... And?"
                $ comm_asked['manyone'] = True
                $ comm_correct += 1
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
        if comm_total >0:
            jump __ripme
        else:
            jump __nextround

label __ripme:
    magenta "Wrong."
    "Magenta hit me with a clawed finger, instantly piercing through my chest, killing me without mercy."
    $ die(1)
    magenta "Yet you have not lost yet. The only way you can lose is if you grow bored. In that scenario, it is my victory."
    jump you_dead

label __nextround:
    magenta "So the challenger survives the first question. Very well. Next question."
    menu:
        