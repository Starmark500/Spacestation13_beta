from wrap import sprite, world, sprite_text
import wrap, walls

wrap.add_sprite_dir("my_sprites")
world.create_world(1000, 1000)
live1 = sprite.add("human", 200, 200, "human1")
angle = sprite.get_angle(live1)
walls.sozdanie_many_wallsx(100, 100, 6)
walls.sozdanie_many_wallsy(100, 70, 7)
walls.sozdanie_many_wallsx(100, 280, 2)
walls.sozdanie_many_wallsy(280, 100, 6)
walls.sozdanie_many_wallsx(200, 280, 2)
wall_experement1 = sprite.add("wall", 500, 100, "wall2")
# topw = sprite.get_top(walls.all_id_walls)

bottomw = sprite.get_bottom(wall_experement1)
rightw = sprite.get_right(wall_experement1)
sprite.set_angle(live1, 90)


# @wrap.always(100)
# def ctena():
#     if sprite.is_collide_sprite(live1, wall_experement1):
#         sprite.move_right_to(live1, leftw)

@wrap.on_key_always(wrap.K_LEFT, wrap.K_RIGHT)
def move_human(keys):
    sprite.set_costume(live1, "human3")
    sprite.move_at_angle_dir(live1, 5)
    if wrap.K_RIGHT in keys:
        sprite.set_reverse_x(live1, False)
        red_wall = sprite.is_collide_any_sprite(live1, walls.all_id_walls)
        if red_wall != None:
            leftw = sprite.get_left(red_wall)
            sprite.move_right_to(live1, leftw)
    else:
        sprite.set_reverse_x(live1, True)
        if sprite.is_collide_sprite(live1, wall_experement1):
            sprite.move_left_to(live1, rightw)


@wrap.on_key_always(wrap.K_UP, wrap.K_DOWN)
def move_humanupdown(keys):
    if wrap.K_UP in keys:
        sprite.set_costume(live1, "human2")
        sprite.move_at_angle(live1, 0, 5)
        if sprite.is_collide_sprite(live1, wall_experement1):
            sprite.move_top_to(live1, bottomw)
    else:
        sprite.set_costume(live1, "human1")
        sprite.move_at_angle(live1, 180, 5)
        if sprite.is_collide_sprite(live1, wall_experement1):
            sprite.move_bottom_to(live1, topw)
