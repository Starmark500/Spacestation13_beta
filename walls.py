from wrap import sprite,world,sprite_text
import wrap

all_id_walls=[]

def sozdanie_many_wallsx(x_wall,y_wall,num_wall):
    sprite_id=0
    while True:
        x_wall=x_wall+30
        made_wall= sprite.add("wall", x_wall, y_wall, "wall")
        sprite_id = sprite_id + 1
        all_id_walls.append(made_wall)

        if sprite_id == num_wall:
            break

def sozdanie_many_wallsy(x_wall,y_wall,num_wall):
    sprite_id=0
    while True:
        y_wall=y_wall+30
        made_wall = sprite.add("wall", x_wall, y_wall, "wall")
        sprite_id = sprite_id + 1
        all_id_walls.append(made_wall)

        if sprite_id == num_wall:
            break
y=16
def wall(s):
    global y
    a=0
    for b in s:
        if b=="X":
            made_wall=sprite.add("wall",a,y,"wall")
            all_id_walls.append(made_wall)
        a+=30
    y+=30


