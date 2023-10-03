from wrap import sprite,world,sprite_text
import wrap


def sozdanie_many_wallsx(x_wall,y_wall,num_wall):
    sprite_id=0
    while True:
        x_wall=x_wall+30
        sprite.add("wall", x_wall, y_wall, "wall")
        sprite_id = sprite_id + 1
        if sprite_id == num_wall:
            break

def sozdanie_many_wallsy(x_wall,y_wall,num_wall):
    sprite_id=0
    while True:
        y_wall=y_wall+30
        sprite.add("wall", x_wall, y_wall, "wall")
        sprite_id = sprite_id + 1
        if sprite_id == num_wall:
            break
