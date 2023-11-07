from wrap import sprite, world, sprite_text
import wrap

world.create_world(1000, 1000)
wrap.add_sprite_dir("my_sprites")
import walls, random, human as alien, levels

live1 = sprite.add("human", 200, 200, "human1")
angle = sprite.get_angle(live1)
a = [100, 200]
all_human = []


def spawn_beggars(a):
    b = a[0]
    c = a[1]
    make_human = sprite.add("human", b, c, "human1")

    all_human.append(
        [
            make_human,
            random.choice([90, 180, -90, 0]),
            1.5
        ]
    )


form = [[400, 200], [400, 300]]
form2 = [[500, 500], [500,200], [200, 200]]


def hhh(b):
    for t in b:
        spawn_beggars(t)


hhh(form2)
hhh(form)
spawn_beggars(a)
sprite.set_angle(live1, 90)


@wrap.always(50)
def all_move():
    for k in all_human:
        g = k[0]
        s = k[1]
        alien.move_human(g, s, 5)


@wrap.on_key_always(wrap.K_LEFT, wrap.K_RIGHT)
def move_humun(keys):
    if wrap.K_RIGHT in keys:
        alien.move_human(live1, 90, 5)

    else:
        alien.move_human(live1, -90, 5)


@wrap.on_key_always(wrap.K_UP, wrap.K_DOWN)
def move_humanupdown(keys):
    if wrap.K_UP in keys:
        alien.move_human(live1, 0, 5)
    else:
        alien.move_human(live1, 180, 5)

@wrap.always(100)
def andle_change():

    for human in all_human:
        human[2]-=0.1
    print(
        all_human
    )





     # for human in all_human:
     #    alien.angle_human_change(human,random.choice([90, 180, -90, 0]))

