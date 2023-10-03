from wrap import sprite,world,sprite_text
import wrap,walls

wrap.add_sprite_dir("my_sprites")
world.create_world(1000,1000)
live1=sprite.add("human",200,200,"human1")
angle=sprite.get_angle(live1)
walls.sozdanie_many_wallsx(100,100,6)
walls.sozdanie_many_wallsy(100,70,7)
walls.sozdanie_many_wallsx(100,280,2)
walls.sozdanie_many_wallsy(280,100,6)
walls.sozdanie_many_wallsx(200,280,2)

@wrap.on_key_always(wrap.K_LEFT,wrap.K_RIGHT)
def move_human(keys):
    if wrap.K_RIGHT in keys:
        sprite.set_reverse_x(live1,False)
        sprite.move_at_angle_dir(live1,3)
    else:
        sprite.set_reverse_x(live1,True)
        sprite.move_at_angle_dir(live1,3)

# @wrap.on_key_always(wrap.K_UP,wrap.K_DOWN)
# def move_humanupdown(keys):
#     if wrap.K_UP in keys:
#         sprite.


