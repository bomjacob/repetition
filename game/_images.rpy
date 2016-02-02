# Auto load images from img folder
init python hide:
    for file in renpy.list_files():
        #Load characters
        if file.startswith('img/characters/'):
            if file.endswith('.png'):
                name = file.replace('img/characters/','').replace('/', ' ').replace('.png','')
                renpy.log(name)
                renpy.image(name, Image(file, yoffset=50))
                continue
            continue
        #Load backgrounds
        if file.startswith('img/bg/'):
            if file.endswith('.jpg'):
                name = file.replace('img/bg/','').replace('/', ' ').replace('.jpg','')
                renpy.log(name)
                renpy.image(name, Image(file))
                continue
            continue
        if file.startswith('ui/overlay/'):
            if file.endswith('.png'):
                name = file.replace('ui/','').replace('/', ' ').replace('.png','')
                renpy.log(name)
                renpy.image(name, Image(file))
                continue
            continue

