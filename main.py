from wrap import sprite, world, sprite_text
import wrap, walls, random

wrap.add_sprite_dir("my_sprites")
world.create_world(1000, 1000)
live1 = sprite.add("human", 200, 200, "human1")
angle = sprite.get_angle(live1)
a = [100, 200]
all_human = []


def spawn_beggars(a):
    b = a[0]
    c = a[1]
    make_human = sprite.add("human", b, c, "human1")

    all_human.append([make_human, random.choice([90, 180, -90, 0])])
    print(all_human)


form = [[400, 200], [400, 300]]
form2 = [[500, 500], [100, 100], [200, 200]]


def hhh(b):
    for t in b:
        spawn_beggars(t)


hhh(form2)
hhh(form)
spawn_beggars(a)


# all_human=[[0,90],[1,180],[2,-90]]





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

@wrap.always(50)
def all_move():
    for k in all_human:
        g = k[0]
        s = k[1]
        move_human(g,s,5)

@wrap.on_key_always(wrap.K_LEFT, wrap.K_RIGHT)
def move_humun(keys):
    if wrap.K_RIGHT in keys:
        move_human(live1,90,5)

    else:
        move_human(live1,-90,5)


@wrap.on_key_always(wrap.K_UP, wrap.K_DOWN)
def move_humanupdown(keys):
    if wrap.K_UP in keys:
        move_human(live1,0,5)
    else:
       move_human(live1,180,5)

