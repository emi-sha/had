# Import a otevření okna
import pyglet
window = pyglet.window.Window()

# Velikost okna
window.width = 640
window.height = 640

# Směr hada
smery = {
    'x': 1,
    'y': 1
}

obrazek = pyglet.image.load('green.png')
obrazek.anchor_x =  obrazek.width//2
obrazek.anchor_y = obrazek.height//2

had = pyglet.sprite.Sprite(obrazek)
had.x = 100
had.y = 100

def zpracuj_text(text):
    print(text)
    
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
# Zavolání okna
pyglet.app.run()
