from wrap import sprite, world, sprite_text
import wrap, walls

wrap.add_sprite_dir("my_sprites")
world.create_world(1000, 1000)
live1 = sprite.add("human", 200, 200, "human1")
angle = sprite.get_angle(live1)
a = [100, 200]

def spawn_beggars(a):
    b = a[0]
    c = a[1]
    sprite.add("human", b, c, "human1")

form=[[400,200],[400,300]]
form2=[[500,500],[100,100],[200,200]]
def hhh(b):
    for t in b:
        spawn_beggars(t)
spawn_beggars(a)
hhh(form2)
hhh(form)

# walls.sozdanie_many_wallsx(100, 100, 6)
#
# walls.sozdanie_many_wallsy(100, 70, 7)
# walls.sozdanie_many_wallsx(100, 280, 2)
# walls.sozdanie_many_wallsy(280, 100, 6)
# walls.sozdanie_many_wallsx(200, 280, 2)
#
# walls.sozdanie_many_wallsx(500, 500, 6)
# walls.sozdanie_many_wallsy(500, 350, 7)
# walls.sozdanie_many_wallsx(500, 280, 2)
# walls.sozdanie_many_wallsy(280, 500, 6)
# walls.sozdanie_many_wallsx(150, 280, 2)

walls.wall("     XXXXX     XXXXX              ")
walls.wall("     X   X     X   X              ")
walls.wall("    XX   XXXXXXX   XX             ")
walls.wall("XXXXX       X       XXXXXXXXXXXXXX")
walls.wall("X           X                    X")
walls.wall("X           X                    X")
walls.wall("XXXXX       X                    X")
walls.wall("X           XXXXXXXXXX     XXXXXXX")
walls.wall("X           X                    X")
walls.wall("XXXXXXXXX   X                    X")
walls.wall("X           X                    X")
walls.wall("X           X            X   XXXXX")
walls.wall("X                        X       X")
walls.wall("X                        X       X")
walls.wall("XXXXXXXXXXXXX            XXXXXXXXX")
walls.wall("X           X            X       X")
walls.wall("X                                X")
walls.wall("X                                X")
walls.wall("XXXXXXXX  XXX     XXXXXXXXXXXXXXXX")
walls.wall("XXXXXXXX  XXX         X        XXX")
walls.wall("XXXXXXXX  XXX         X        XXX")
walls.wall("XXXX        X         X        XXX")
walls.wall("XXXX        X       XXXXX      XXX")
walls.wall("XXXX        X                  XXX")
walls.wall("XXXXXXX  XXXX                  XXX")
walls.wall("XXXXXXX  XXXX       XXXXX      XXX")
walls.wall("XXXXXXX  XXXX         X        XXX")
walls.wall("XX         XX         X        XXX")
walls.wall("XX         XX         X        XXX")
walls.wall("XXXXXXXXXXXXX     XXXXXXXXXXXXXXXX")
walls.wall("X                                X")
walls.wall("X                                X")
walls.wall(" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ")
sprite.set_angle(live1, 90)


def analis_wallontheright():
    red_wall = sprite.is_collide_any_sprite(live1, walls.all_id_walls)
    if red_wall != None:
        leftw = sprite.get_left(red_wall)
        sprite.move_right_to(live1, leftw)


def analis_wallontheleft():
    red_wall = sprite.is_collide_any_sprite(live1, walls.all_id_walls)
    if red_wall != None:
        rightw = sprite.get_right(red_wall)
        sprite.move_left_to(live1, rightw)


def analis_wallontheup():
    red_wall = sprite.is_collide_any_sprite(live1, walls.all_id_walls)
    if red_wall != None:
        bottomw = sprite.get_bottom(red_wall)
        sprite.move_top_to(live1, bottomw)


def analis_wallonthedown():
    red_wall = sprite.is_collide_any_sprite(live1, walls.all_id_walls)
    if red_wall != None:
        topw = sprite.get_top(red_wall)
        sprite.move_bottom_to(live1, topw)


@wrap.on_key_always(wrap.K_LEFT, wrap.K_RIGHT)
def move_human(keys):
    sprite.set_costume(live1, "human3")

    if wrap.K_RIGHT in keys:
        sprite.set_reverse_x(live1, False)
        sprite.move_at_angle_dir(live1, 5)
        analis_wallontheright()

    else:
        sprite.set_reverse_x(live1, True)
        sprite.move_at_angle_dir(live1, 5)
        analis_wallontheleft()


@wrap.on_key_always(wrap.K_UP, wrap.K_DOWN)
def move_humanupdown(keys):
    if wrap.K_UP in keys:
        sprite.set_costume(live1, "human2")
        sprite.move_at_angle(live1, 0, 5)
        analis_wallontheup()
    else:
        sprite.set_costume(live1, "human1")

        sprite.move_at_angle(live1, 180, 5)
        analis_wallonthedown()


a = [1, 2]


def spawn_beggars(a):
    print(a)
