from wrap import sprite,world,sprite_text
import wrap
x_wall=100
y_wall=100
sprite_id=0
wrap.add_sprite_dir("my_sprites")
world.create_world(1000,1000)
while True:
    x_wall=x_wall+30
    sprite.add("wall", x_wall, 100, "wall")
    sprite_id=sprite_id+1
    print(sprite_id)
    if sprite_id==20:
        break

sprite_id=0
while True:

    y_wall=y_wall+30
    sprite.add("wall", 100, y_wall, "wall")
    sprite_id=sprite_id+1
    print(sprite_id)
    if sprite_id==20:
        break
sprite_id=0
x_wall=730
y_wall=100
while True:
    y_wall=y_wall+30
    sprite.add("wall", x_wall, y_wall, "wall")
    sprite_id = sprite_id + 1
    print(sprite_id)
    if sprite_id == 20:
        break
sprite_id=0
y_wall=730
x_wall=100
while True:
    x_wall=x_wall+30
    sprite.add("wall", x_wall, y_wall, "wall")
    sprite_id = sprite_id + 1
    print(sprite_id)
    if sprite_id == 20:
        break


def sozdanie_1_wall(pos_wall,y_wall,x_wall):
    sprite_id=0
    while True:
        pos_wall=pos_wall+30
        sprite.add("wall", x_wall, y_wall, "wall2")
        sprite_id = sprite_id + 1
        if sprite_id == 20:
            break
f(x_wall,600,50)