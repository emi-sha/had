
import pyglet

window = pyglet.window.Window()

window.width = 800
window.height = 600

smery = {
    'x': 1,
    'y': 1
}

RYCHLOST_HADA = 500
ROTACE_HADA = 300

def tik(t):
    if had.y >= 600:
        smery['y'] = -1
    if had.x >= 800:
        smery['x'] = -1
    if had.y <= 0:
        smery['y'] = 1
    if had.x <= 0:
        smery['x'] = 1
    had.x += RYCHLOST_HADA * t * smery['x']
    had.y += RYCHLOST_HADA * t * smery['y']
    had.rotation += ROTACE_HADA * t


pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
    print(text)

obrazek = pyglet.image.load('had.png')
obrazek.anchor_x =  obrazek.width//2
obrazek.anchor_y = obrazek.height//2

obrazek2 = pyglet.image.load('had2.png')
obrazek2.anchor_x =  obrazek.width//2
obrazek2.anchor_y = obrazek.height//2

def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen2, 0.1)

def zmen2(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.1)

pyglet.clock.schedule_once(zmen, 0.1)
# pyglet.clock.schedule_once(zmen2, 1)

had = pyglet.sprite.Sprite(obrazek)
had.x = 100
had.y = 100

def vykresli():
    window.clear()
    had.draw()

def klik(x, y, tlacitko, mod):
    had.x = x
    had.y = y


window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
    on_mouse_press=klik
)

pyglet.app.run()