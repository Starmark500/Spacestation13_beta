from wrap import sprite, world, sprite_text
import wrap, walls, random


def analis_wallontheright(id):
    red_wall = sprite.is_collide_any_sprite(id, walls.all_id_walls)
    if red_wall != None:
        leftw = sprite.get_left(red_wall)
        sprite.move_right_to(id, leftw)


def analis_wallontheleft(id):
    red_wall = sprite.is_collide_any_sprite(id, walls.all_id_walls)
    if red_wall != None:
        rightw = sprite.get_right(red_wall)
        sprite.move_left_to(id, rightw)


def analis_wallontheup(id):
    red_wall = sprite.is_collide_any_sprite(id, walls.all_id_walls)
    if red_wall != None:
        bottomw = sprite.get_bottom(red_wall)
        sprite.move_top_to(id, bottomw)


def analis_wallonthedown(id):
    red_wall = sprite.is_collide_any_sprite(id, walls.all_id_walls)
    if red_wall != None:
        topw = sprite.get_top(red_wall)
        sprite.move_bottom_to(id, topw)


def move_human(id, angle, distance):
    if angle == 0:
        sprite.set_costume(id, "human2")
        sprite.move_at_angle(id, angle, distance)
        analis_wallontheup(id)
    if angle == 180:
        sprite.set_costume(id, "human1")
        sprite.move_at_angle(id, angle, distance)
        analis_wallonthedown(id)
    if angle == 90:
        sprite.set_costume(id, "human3")
        sprite.move_at_angle(id, angle, distance)
        analis_wallontheright(id)
    if angle == -90:
        sprite.set_costume(id, "human4")
        sprite.move_at_angle(id, angle, distance)
        analis_wallontheleft(id)

def angle_human_change(human,angle,time):

    human[1]=angle
