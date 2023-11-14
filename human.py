from wrap import sprite, world, sprite_text
import wrap, walls, random


def analis_wallontheright(id):
    red_wall = sprite.is_collide_any_sprite(id, walls.all_id_walls)
    if red_wall != None:
        leftw = sprite.get_left(red_wall)
        sprite.move_right_to(id, leftw)
        return True
    else:
        return False
def analis_wallontheleft(id):
    red_wall = sprite.is_collide_any_sprite(id, walls.all_id_walls)
    if red_wall != None:
        rightw = sprite.get_right(red_wall)
        sprite.move_left_to(id, rightw)
        return True
    else:
        return False

def analis_wallontheup(id):
    red_wall = sprite.is_collide_any_sprite(id, walls.all_id_walls)
    if red_wall != None:
        bottomw = sprite.get_bottom(red_wall)
        sprite.move_top_to(id, bottomw)
        return True
    else:
        return False

def analis_wallonthedown(id):
    red_wall = sprite.is_collide_any_sprite(id, walls.all_id_walls)
    if red_wall != None:
        topw = sprite.get_top(red_wall)
        sprite.move_bottom_to(id, topw)
        return True
    else:
        return False

def move_human(id, angle, distance):
    if angle == 0:
        sprite.set_costume(id, "human2")
        sprite.move_at_angle(id, angle, distance)
        return analis_wallontheup(id)

    if angle == 180:
        sprite.set_costume(id, "human1")
        sprite.move_at_angle(id, angle, distance)
        return analis_wallonthedown(id)

    if angle == 90:
        sprite.set_costume(id, "human3")
        sprite.move_at_angle(id, angle, distance)
        return analis_wallontheright(id)
    if angle == -90:
        sprite.set_costume(id, "human4")
        sprite.move_at_angle(id, angle, distance)
        return analis_wallontheleft(id)

def random_time_and_angle(human):
    human[2]-=0.1
    if human[2] <= 0:
        human[1]=random.choice([0,90,-90,180])
        human[2]=random.randint(1,3)
