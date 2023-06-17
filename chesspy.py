# Created by falopr
# Bug 1: When 6 black pawns are deleted in the same place and you try to delete the 7th, he become undeletable. (only black pawns)
# Bug 2: When all white pawns are deleted, you can only delete 6 black pawns.
# Solution for the bugs: If a piece cannot be deleted with right click, just drag it out of the window.
import pyglet
from pyglet.window import mouse

piece_width = 80
piece_height = 80


def varinit():
    global wqueen
    global bqueen

    global wpawn1x
    global wpawn1y
    global wpawn2x
    global wpawn2y
    global wpawn3x
    global wpawn3y
    global wpawn4x
    global wpawn4y
    global wpawn5x
    global wpawn5y
    global wpawn6x
    global wpawn6y
    global wpawn7x
    global wpawn7y
    global wpawn8x
    global wpawn8y

    global wrook1x
    global wrook1y
    global wrook2x
    global wrook2y

    global wknight1x
    global wknight1y
    global wknight2x
    global wknight2y

    global wbishop1x
    global wbishop1y
    global wbishop2x
    global wbishop2y

    global wking1x
    global wking1y

    global wqueen10x
    global wqueen10y

    global bpawn1x
    global bpawn1y
    global bpawn2x
    global bpawn2y
    global bpawn3x
    global bpawn3y
    global bpawn4x
    global bpawn4y
    global bpawn5x
    global bpawn5y
    global bpawn6x
    global bpawn6y
    global bpawn7x
    global bpawn7y
    global bpawn8x
    global bpawn8y

    global brook1x
    global brook1y
    global brook2x
    global brook2y

    global bknight1x
    global bknight1y
    global bknight2x
    global bknight2y

    global bbishop1x
    global bbishop1y
    global bbishop2x
    global bbishop2y

    global bking1x
    global bking1y

    global bqueen10x
    global bqueen10y

    global wpawn
    global bpawn
    global wrook
    global brook
    global wknight
    global bknight
    global wbishop
    global bbishop
    global wking
    global bking

    global wpawn1sp
    global wpawn2sp
    global wpawn3sp
    global wpawn3sp
    global wpawn4sp
    global wpawn5sp
    global wpawn6sp
    global wpawn7sp
    global wpawn8sp
    global bpawn1sp
    global bpawn2sp
    global bpawn3sp
    global bpawn3sp
    global bpawn4sp
    global bpawn5sp
    global bpawn6sp
    global bpawn7sp
    global bpawn8sp

    global wrook1sp
    global wrook2sp
    global brook1sp
    global brook2sp

    global wknight1sp
    global wknight2sp
    global bknight1sp
    global bknight2sp

    global wbishop1sp
    global wbishop2sp
    global bbishop1sp
    global bbishop2sp

    global wking1sp
    global bking1sp

    global wqueen10sp
    global bqueen10sp

    global wpawn1del
    global wpawn2del
    global wpawn3del
    global wpawn4del
    global wpawn5del
    global wpawn6del
    global wpawn7del
    global wpawn8del
    global bpawn1del
    global bpawn2del
    global bpawn3del
    global bpawn4del
    global bpawn5del
    global bpawn6del
    global bpawn7del
    global bpawn8del

    global wrook1del
    global wrook2del
    global brook1del
    global brook2del

    global wknight1del
    global wknight2del
    global bknight1del
    global bknight2del

    global wbishop1del
    global wbishop2del
    global bbishop1del
    global bbishop2del

    global wking1del
    global bking1del

    global wqueen10del
    global bqueen10del

    wpawn1x = 0
    wpawn1y = 80
    wpawn2x = 80
    wpawn2y = 80
    wpawn3x = 160
    wpawn3y = 80
    wpawn4x = 240
    wpawn4y = 80
    wpawn5x = 320
    wpawn5y = 80
    wpawn6x = 400
    wpawn6y = 80
    wpawn7x = 480
    wpawn7y = 80
    wpawn8x = 560
    wpawn8y = 80

    wrook1x = 0
    wrook1y = 0
    wrook2x = 560
    wrook2y = 0

    wknight1x = 80
    wknight1y = 0
    wknight2x = 480
    wknight2y = 0

    wbishop1x = 160
    wbishop1y = 0
    wbishop2x = 400
    wbishop2y = 0

    wking1x = 320
    wking1y = 0

    wqueen10x = 240
    wqueen10y = 0

    bpawn1x = 0
    bpawn1y = 480
    bpawn2x = 80
    bpawn2y = 480
    bpawn3x = 160
    bpawn3y = 480
    bpawn4x = 240
    bpawn4y = 480
    bpawn5x = 320
    bpawn5y = 480
    bpawn6x = 400
    bpawn6y = 480
    bpawn7x = 480
    bpawn7y = 480
    bpawn8x = 560
    bpawn8y = 480

    brook1x = 0
    brook1y = 560
    brook2x = 560
    brook2y = 560

    bknight1x = 80
    bknight1y = 560
    bknight2x = 480
    bknight2y = 560

    bbishop1x = 160
    bbishop1y = 560
    bbishop2x = 400
    bbishop2y = 560

    bking1x = 320
    bking1y = 560

    bqueen10x = 240
    bqueen10y = 560

    wpawn = pyglet.resource.image('pawn_white.png')
    wrook = pyglet.resource.image('rook_white.png')
    wknight = pyglet.resource.image('knight_white.png')
    wbishop = pyglet.resource.image('bishop_white.png')
    wking = pyglet.resource.image('king_white.png')
    wqueen = pyglet.resource.image('queen_white.png')

    wpawn.width = piece_width
    wpawn.height = piece_height
    wrook.width = piece_width
    wrook.height = piece_height
    wknight.width = piece_width
    wknight.height = piece_height
    wbishop.width = piece_width
    wbishop.height = piece_height
    wking.width = piece_width
    wking.height = piece_height
    wqueen.width = piece_width
    wqueen.height = piece_height

    wpawn1sp = pyglet.sprite.Sprite(wpawn)
    wpawn2sp = pyglet.sprite.Sprite(wpawn)
    wpawn3sp = pyglet.sprite.Sprite(wpawn)
    wpawn4sp = pyglet.sprite.Sprite(wpawn)
    wpawn5sp = pyglet.sprite.Sprite(wpawn)
    wpawn6sp = pyglet.sprite.Sprite(wpawn)
    wpawn7sp = pyglet.sprite.Sprite(wpawn)
    wpawn8sp = pyglet.sprite.Sprite(wpawn)

    wrook1sp = pyglet.sprite.Sprite(wrook)
    wrook2sp = pyglet.sprite.Sprite(wrook)

    wknight1sp = pyglet.sprite.Sprite(wknight)
    wknight2sp = pyglet.sprite.Sprite(wknight)

    wbishop1sp = pyglet.sprite.Sprite(wbishop)
    wbishop2sp = pyglet.sprite.Sprite(wbishop)

    wking1sp = pyglet.sprite.Sprite(wking)

    wqueen10sp = pyglet.sprite.Sprite(wqueen)

    bpawn = pyglet.resource.image('pawn_black.png')
    brook = pyglet.resource.image('rook_black.png')
    bknight = pyglet.resource.image('knight_black.png')
    bbishop = pyglet.resource.image('bishop_black.png')
    bking = pyglet.resource.image('king_black.png')
    bqueen = pyglet.resource.image('queen_black.png')

    bpawn.width = piece_width
    bpawn.height = piece_height
    brook.width = piece_width
    brook.height = piece_height
    bknight.width = piece_width
    bknight.height = piece_height
    bbishop.width = piece_width
    bbishop.height = piece_height
    bking.width = piece_width
    bking.height = piece_height
    bqueen.width = piece_width
    bqueen.height = piece_height

    bpawn1sp = pyglet.sprite.Sprite(bpawn)
    bpawn2sp = pyglet.sprite.Sprite(bpawn)
    bpawn3sp = pyglet.sprite.Sprite(bpawn)
    bpawn4sp = pyglet.sprite.Sprite(bpawn)
    bpawn5sp = pyglet.sprite.Sprite(bpawn)
    bpawn6sp = pyglet.sprite.Sprite(bpawn)
    bpawn7sp = pyglet.sprite.Sprite(bpawn)
    bpawn8sp = pyglet.sprite.Sprite(bpawn)

    brook1sp = pyglet.sprite.Sprite(brook)
    brook2sp = pyglet.sprite.Sprite(brook)

    bknight1sp = pyglet.sprite.Sprite(bknight)
    bknight2sp = pyglet.sprite.Sprite(bknight)

    bbishop1sp = pyglet.sprite.Sprite(bbishop)
    bbishop2sp = pyglet.sprite.Sprite(bbishop)

    bking1sp = pyglet.sprite.Sprite(bking)

    bqueen10sp = pyglet.sprite.Sprite(bqueen)

    wpawn1del = True
    wpawn2del = True
    wpawn3del = True
    wpawn4del = True
    wpawn5del = True
    wpawn6del = True
    wpawn7del = True
    wpawn8del = True

    wrook1del = True
    wrook2del = True

    wknight1del = True
    wknight2del = True

    wbishop1del = True
    wbishop2del = True

    wking1del = True

    wqueen10del = True

    bpawn1del = True
    bpawn2del = True
    bpawn3del = True
    bpawn4del = True
    bpawn5del = True
    bpawn6del = True
    bpawn7del = True
    bpawn8del = True

    brook1del = True
    brook2del = True

    bknight1del = True
    bknight2del = True

    bbishop1del = True
    bbishop2del = True

    bking1del = True

    bqueen10del = True


xpw = 0
ypw = 0
xpb = 0
ypb = 0

wpawn1clicked = False
wpawn2clicked = False
wpawn3clicked = False
wpawn4clicked = False
wpawn5clicked = False
wpawn6clicked = False
wpawn7clicked = False
wpawn8clicked = False

wrook1clicked = False
wrook2clicked = False

wknight1clicked = False
wknight2clicked = False

wbishop1clicked = False
wbishop2clicked = False

wking1clicked = False

wqueen10clicked = False

bpawn1clicked = False
bpawn2clicked = False
bpawn3clicked = False
bpawn4clicked = False
bpawn5clicked = False
bpawn6clicked = False
bpawn7clicked = False
bpawn8clicked = False

brook1clicked = False
brook2clicked = False

bknight1clicked = False
bknight2clicked = False

bbishop1clicked = False
bbishop2clicked = False

bking1clicked = False

bqueen10clicked = False

window = pyglet.window.Window(640, 640, 'Chess By falopr')

pyglet.resource.path = ['res']
pyglet.resource.reindex()

backgroundimg = pyglet.resource.image('chess_board.jpg')
chesslogo = pyglet.resource.image("chess_logo.png")
window.set_icon(chesslogo)

varinit()


@window.event
def on_key_press(symbol, modifiers):
    # 65293 is the enter key
    if symbol == 65293:
        varinit()


@window.event
def on_draw():
    global wpawn1x
    global wpawn1y
    global wpawn2x
    global wpawn2y
    global wpawn3x
    global wpawn3y
    global wpawn4x
    global wpawn4y
    global wpawn5x
    global wpawn5y
    global wpawn6x
    global wpawn6y
    global wpawn7x
    global wpawn7y
    global wpawn8x
    global wpawn8y

    global wrook1x
    global wrook1y
    global wrook2x
    global wrook2y

    global wknight1x
    global wknight1y
    global wknight2x
    global wknight2y

    global wbishop1x
    global wbishop1y
    global wbishop2x
    global wbishop2y

    global wking1x
    global wking1y

    global wqueen10x
    global wqueen10y
    global bqueen10x
    global bqueen10y

    global bpawn1x
    global bpawn1y
    global bpawn2x
    global bpawn2y
    global bpawn3x
    global bpawn3y
    global bpawn4x
    global bpawn4y
    global bpawn5x
    global bpawn5y
    global bpawn6x
    global bpawn6y
    global bpawn7x
    global bpawn7y
    global bpawn8x
    global bpawn8y

    global brook1x
    global brook1y
    global brook2x
    global brook2y

    global bknight1x
    global bknight1y
    global bknight2x
    global bknight2y

    global bbishop1x
    global bbishop1y
    global bbishop2x
    global bbishop2y

    global bking1x
    global bking1y

    window.clear()
    backgroundimg.blit(xpw, ypw)

    if wpawn1del:
        wpawn1sp.x = wpawn1x
        wpawn1sp.y = wpawn1y
        wpawn1sp.draw()
    else:
        wpawn1x = 1600
        wpawn1y = 1600

    if wpawn2del:
        wpawn2sp.x = wpawn2x
        wpawn2sp.y = wpawn2y
        wpawn2sp.draw()
    else:
        wpawn2x = 1600
        wpawn2y = 1600

    if wpawn3del:
        wpawn3sp.x = wpawn3x
        wpawn3sp.y = wpawn3y
        wpawn3sp.draw()
    else:
        wpawn3x = 1600
        wpawn3y = 1600

    if wpawn4del:
        wpawn4sp.x = wpawn4x
        wpawn4sp.y = wpawn4y
        wpawn4sp.draw()
    else:
        wpawn4x = 1600
        wpawn4y = 1600

    if wpawn5del:
        wpawn5sp.x = wpawn5x
        wpawn5sp.y = wpawn5y
        wpawn5sp.draw()
    else:
        wpawn5x = 1600
        wpawn5y = 1600

    if wpawn6del:
        wpawn6sp.x = wpawn6x
        wpawn6sp.y = wpawn6y
        wpawn6sp.draw()
    else:
        wpawn6x = 1600
        wpawn6y = 1600

    if wpawn7del:
        wpawn7sp.x = wpawn7x
        wpawn7sp.y = wpawn7y
        wpawn7sp.draw()
    else:
        wpawn7x = 1600
        wpawn7y = 1600

    if wpawn8del:
        wpawn8sp.x = wpawn8x
        wpawn8sp.y = wpawn8y
        wpawn8sp.draw()
    else:
        wpawn8x = 1600
        wpawn8y = 1600

    if wrook1del:
        wrook1sp.x = wrook1x
        wrook1sp.y = wrook1y
        wrook1sp.draw()
    else:
        wrook1x = 1600
        wrook1y = 1600

    if wrook2del:
        wrook2sp.x = wrook2x
        wrook2sp.y = wrook2y
        wrook2sp.draw()
    else:
        wrook2x = 1600
        wrook2y = 1600

    if wknight1del:
        wknight1sp.x = wknight1x
        wknight1sp.y = wknight1y
        wknight1sp.draw()
    else:
        wknight1x = 1600
        wknight1y = 1600

    if wknight2del:
        wknight2sp.x = wknight2x
        wknight2sp.y = wknight2y
        wknight2sp.draw()
    else:
        wknight2x = 1600
        wknight2y = 1600

    if wbishop1del:
        wbishop1sp.x = wbishop1x
        wbishop1sp.y = wbishop1y
        wbishop1sp.draw()
    else:
        wbishop1x = 1600
        wbishop1y = 1600

    if wbishop2del:
        wbishop2sp.x = wbishop2x
        wbishop2sp.y = wbishop2y
        wbishop2sp.draw()
    else:
        wbishop2x = 1600
        wbishop2y = 1600

    if wking1del:
        wking1sp.x = wking1x
        wking1sp.y = wking1y
        wking1sp.draw()
    else:
        wking1x = 1600
        wking1y = 1600

    if wqueen10del:
        wqueen10sp.x = wqueen10x
        wqueen10sp.y = wqueen10y
        wqueen10sp.draw()
    else:
        wqueen10x = 1600
        wqueen10y = 1600

    if bpawn1del:
        bpawn1sp.x = bpawn1x
        bpawn1sp.y = bpawn1y
        bpawn1sp.draw()
    else:
        bpawn1x = 1600
        bpawn1y = 1600

    if bpawn2del:
        bpawn2sp.x = bpawn2x
        bpawn2sp.y = bpawn2y
        bpawn2sp.draw()
    else:
        bpawn2x = 1600
        bpawn2y = 1600

    if bpawn3del:
        bpawn3sp.x = bpawn3x
        bpawn3sp.y = bpawn3y
        bpawn3sp.draw()
    else:
        bpawn3x = 1600
        bpawn3y = 1600

    if bpawn4del:
        bpawn4sp.x = bpawn4x
        bpawn4sp.y = bpawn4y
        bpawn4sp.draw()
    else:
        bpawn4x = 1600
        bpawn4y = 1600

    if bpawn5del:
        bpawn5sp.x = bpawn5x
        bpawn5sp.y = bpawn5y
        bpawn5sp.draw()
    else:
        bpawn5x = 1600
        bpawn5y = 1600

    if bpawn6del:
        bpawn6sp.x = bpawn6x
        bpawn6sp.y = bpawn6y
        bpawn6sp.draw()
    else:
        bpawn6x = 1600
        bpawn6y = 1600

    if bpawn7del:
        bpawn7sp.x = bpawn7x
        bpawn7sp.y = bpawn7y
        bpawn7sp.draw()
    else:
        bpawn7x = 1600
        bpawn7y = 1600

    if bpawn8del:
        bpawn8sp.x = bpawn8x
        bpawn8sp.y = bpawn8y
        bpawn8sp.draw()
    else:
        bpawn8x = 1600
        bpawn8y = 1600

    if brook1del:
        brook1sp.x = brook1x
        brook1sp.y = brook1y
        brook1sp.draw()
    else:
        brook1x = 1600
        brook1y = 1600

    if brook2del:
        brook2sp.x = brook2x
        brook2sp.y = brook2y
        brook2sp.draw()
    else:
        brook2x = 1600
        brook2y = 1600

    if bknight1del:
        bknight1sp.x = bknight1x
        bknight1sp.y = bknight1y
        bknight1sp.draw()
    else:
        bknight1x = 1600
        bknight1y = 1600

    if bknight2del:
        bknight2sp.x = bknight2x
        bknight2sp.y = bknight2y
        bknight2sp.draw()
    else:
        bknight2x = 1600
        bknight2y = 1600

    if bbishop1del:
        bbishop1sp.x = bbishop1x
        bbishop1sp.y = bbishop1y
        bbishop1sp.draw()
    else:
        bbishop1x = 1600
        bbishop1y = 1600

    if bbishop2del:
        bbishop2sp.x = bbishop2x
        bbishop2sp.y = bbishop2y
        bbishop2sp.draw()
    else:
        bbishop2x = 1600
        bbishop2y = 1600

    if bking1del:
        bking1sp.x = bking1x
        bking1sp.y = bking1y
        bking1sp.draw()
    else:
        bking1x = 1600
        bking1y = 1600

    if bqueen10del:
        bqueen10sp.x = bqueen10x
        bqueen10sp.y = bqueen10y
        bqueen10sp.draw()
    else:
        bqueen10x = 1600
        bqueen10y = 1600


@window.event
def on_mouse_press(x, y, button, modifiers):
    global rndx
    global rndy
    global wpawn1clicked
    global wpawn2clicked
    global wpawn3clicked
    global wpawn4clicked
    global wpawn5clicked
    global wpawn6clicked
    global wpawn7clicked
    global wpawn8clicked
    global bpawn1clicked
    global bpawn2clicked
    global bpawn3clicked
    global bpawn4clicked
    global bpawn5clicked
    global bpawn6clicked
    global bpawn7clicked
    global bpawn8clicked

    global wrook1clicked
    global wrook2clicked
    global brook1clicked
    global brook2clicked

    global wknight1clicked
    global wknight2clicked
    global bknight1clicked
    global bknight2clicked

    global wbishop1clicked
    global wbishop2clicked
    global bbishop1clicked
    global bbishop2clicked

    global wking1clicked
    global bking1clicked

    global wqueen10clicked
    global bqueen10clicked

    global wqueen
    global bqueen

    rndx = x - x % 80
    rndy = y - y % 80
    # 1 is the left button on mouse
    if button == 1:
        if wpawn1x < x < wpawn1x + wpawn.width and wpawn1y < y < wpawn1y + wpawn.height:
            wpawn1clicked = True
        if wpawn2x < x < wpawn2x + wpawn.width and wpawn2y < y < wpawn2y + wpawn.height:
            wpawn2clicked = True
        if wpawn3x < x < wpawn3x + wpawn.width and wpawn3y < y < wpawn3y + wpawn.height:
            wpawn3clicked = True
        if wpawn4x < x < wpawn4x + wpawn.width and wpawn4y < y < wpawn4y + wpawn.height:
            wpawn4clicked = True
        if wpawn5x < x < wpawn5x + wpawn.width and wpawn5y < y < wpawn5y + wpawn.height:
            wpawn5clicked = True
        if wpawn6x < x < wpawn6x + wpawn.width and wpawn6y < y < wpawn6y + wpawn.height:
            wpawn6clicked = True
        if wpawn7x < x < wpawn7x + wpawn.width and wpawn7y < y < wpawn7y + wpawn.height:
            wpawn7clicked = True
        if wpawn8x < x < wpawn8x + wpawn.width and wpawn8y < y < wpawn8y + wpawn.height:
            wpawn8clicked = True
        if bpawn1x < x < bpawn1x + bpawn.width and bpawn1y < y < bpawn1y + bpawn.height:
            bpawn1clicked = True
        if bpawn2x < x < bpawn2x + bpawn.width and bpawn2y < y < bpawn2y + bpawn.height:
            bpawn2clicked = True
        if bpawn3x < x < bpawn3x + bpawn.width and bpawn3y < y < bpawn3y + bpawn.height:
            bpawn3clicked = True
        if bpawn4x < x < bpawn4x + bpawn.width and bpawn4y < y < bpawn4y + bpawn.height:
            bpawn4clicked = True
        if bpawn5x < x < bpawn5x + bpawn.width and bpawn5y < y < bpawn5y + bpawn.height:
            bpawn5clicked = True
        if bpawn6x < x < bpawn6x + bpawn.width and bpawn6y < y < bpawn6y + bpawn.height:
            bpawn6clicked = True
        if bpawn7x < x < bpawn7x + bpawn.width and bpawn7y < y < bpawn7y + bpawn.height:
            bpawn7clicked = True
        if bpawn8x < x < bpawn8x + bpawn.width and bpawn8y < y < bpawn8y + bpawn.height:
            bpawn8clicked = True

        if wrook1x < x < wrook1x + wrook.width and wrook1y < y < wrook1y + wrook.height:
            wrook1clicked = True
        if wrook2x < x < wrook2x + wrook.width and wrook2y < y < wrook2y + wrook.height:
            wrook2clicked = True
        if brook1x < x < brook1x + brook.width and brook1y < y < brook1y + brook.height:
            brook1clicked = True
        if brook2x < x < wrook2x + brook.width and brook2y < y < brook2y + brook.height:
            brook2clicked = True

        if wknight1x < x < wknight1x + wknight.width and wknight1y < y < wknight1y + wknight.height:
            wknight1clicked = True
        if wknight2x < x < wknight2x + wknight.width and wknight2y < y < wknight2y + wknight.height:
            wknight2clicked = True
        if bknight1x < x < bknight1x + bknight.width and bknight1y < y < bknight1y + bknight.height:
            bknight1clicked = True
        if bknight2x < x < bknight2x + bknight.width and bknight2y < y < bknight2y + bknight.height:
            bknight2clicked = True

        if wbishop1x < x < wbishop1x + wbishop.width and wbishop1y < y < wbishop1y + wbishop.height:
            wbishop1clicked = True
        if wbishop2x < x < wbishop2x + wbishop.width and wbishop2y < y < wbishop2y + wbishop.height:
            wbishop2clicked = True
        if bbishop1x < x < bbishop1x + bbishop.width and bbishop1y < y < bbishop1y + bbishop.height:
            bbishop1clicked = True
        if bbishop2x < x < bbishop2x + bbishop.width and bbishop2y < y < bbishop2y + bbishop.height:
            bbishop2clicked = True

        if wking1x < x < wking1x + wking.width and wking1y < y < wking1y + wking.height:
            wking1clicked = True
        if bking1x < x < bking1x + bking.width and bking1y < y < bking1y + bking.height:
            bking1clicked = True

        if wqueen10x < x < wqueen10x + wqueen.width and wqueen10y < y < wqueen10y + wqueen.height:
            wqueen10clicked = True
        if bqueen10x < x < bqueen10x + bqueen.width and bqueen10y < y < bqueen10y + bqueen.height:
            bqueen10clicked = True
    # 4 is the middle button on mouse
    if button == 2:
        global wpawn1sp
        global wpawn2sp
        global wpawn3sp
        global wpawn4sp
        global wpawn5sp
        global wpawn6sp
        global wpawn7sp
        global wpawn8sp
        global bpawn1sp
        global bpawn2sp
        global bpawn3sp
        global bpawn4sp
        global bpawn5sp
        global bpawn6sp
        global bpawn7sp
        global bpawn8sp

        global wpawn1del
        global wpawn2del
        global wpawn3del
        global wpawn4del
        global wpawn5del
        global wpawn6del
        global wpawn7del
        global wpawn8del
        global bpawn1del
        global bpawn2del
        global bpawn3del
        global bpawn4del
        global bpawn5del
        global bpawn6del
        global bpawn7del
        global bpawn8del

        global wrook1del
        global wrook2del
        global brook1del
        global brook2del

        global wknight1del
        global wknight2del
        global bknight1del
        global bknight2del

        global wbishop1del
        global wbishop2del
        global bbishop1del
        global bbishop2del

        global wking1del
        global bking1del

        global wqueen10del
        global bqueen10del

        if wpawn1x < x < wpawn1x + wpawn.width and wpawn1y < y < wpawn1y + wpawn.height:
            wpawn1sp = pyglet.sprite.Sprite(wqueen)
        if wpawn2x < x < wpawn2x + wpawn.width and wpawn2y < y < wpawn2y + wpawn.height:
            wpawn2sp = pyglet.sprite.Sprite(wqueen)
        if wpawn3x < x < wpawn3x + wpawn.width and wpawn3y < y < wpawn3y + wpawn.height:
            wpawn3sp = pyglet.sprite.Sprite(wqueen)
        if wpawn4x < x < wpawn4x + wpawn.width and wpawn4y < y < wpawn4y + wpawn.height:
            wpawn4sp = pyglet.sprite.Sprite(wqueen)
        if wpawn5x < x < wpawn5x + wpawn.width and wpawn5y < y < wpawn5y + wpawn.height:
            wpawn5sp = pyglet.sprite.Sprite(wqueen)
        if wpawn6x < x < wpawn6x + wpawn.width and wpawn6y < y < wpawn6y + wpawn.height:
            wpawn6sp = pyglet.sprite.Sprite(wqueen)
        if wpawn7x < x < wpawn7x + wpawn.width and wpawn7y < y < wpawn7y + wpawn.height:
            wpawn7sp = pyglet.sprite.Sprite(wqueen)
        if wpawn8x < x < wpawn8x + wpawn.width and wpawn8y < y < wpawn8y + wpawn.height:
            wpawn8sp = pyglet.sprite.Sprite(wqueen)

        if bpawn1x < x < bpawn1x + bpawn.width and bpawn1y < y < bpawn1y + bpawn.height:
            bpawn1sp = pyglet.sprite.Sprite(bqueen)
        if bpawn2x < x < bpawn2x + bpawn.width and bpawn2y < y < bpawn2y + bpawn.height:
            bpawn2sp = pyglet.sprite.Sprite(bqueen)
        if bpawn3x < x < bpawn3x + bpawn.width and bpawn3y < y < bpawn3y + bpawn.height:
            bpawn3sp = pyglet.sprite.Sprite(bqueen)
        if bpawn4x < x < bpawn4x + bpawn.width and bpawn4y < y < bpawn4y + bpawn.height:
            bpawn4sp = pyglet.sprite.Sprite(bqueen)
        if bpawn5x < x < bpawn5x + bpawn.width and bpawn5y < y < bpawn5y + bpawn.height:
            bpawn5sp = pyglet.sprite.Sprite(bqueen)
        if bpawn6x < x < bpawn6x + bpawn.width and bpawn6y < y < bpawn6y + bpawn.height:
            bpawn6sp = pyglet.sprite.Sprite(bqueen)
        if bpawn7x < x < bpawn7x + bpawn.width and bpawn7y < y < bpawn7y + bpawn.height:
            bpawn7sp = pyglet.sprite.Sprite(bqueen)
        if bpawn8x < x < bpawn8x + bpawn.width and bpawn8y < y < bpawn8y + bpawn.height:
            bpawn8sp = pyglet.sprite.Sprite(bqueen)

    # 4 is the right button on mouse
    if button == 4:
        if wpawn1x < x < wpawn1x + wpawn.width and wpawn1y < y < wpawn1y + wpawn.height:
            wpawn1del = False
        elif wpawn2x < x < wpawn2x + wpawn.width and wpawn2y < y < wpawn2y + wpawn.height:
            wpawn2del = False
        elif wpawn3x < x < wpawn3x + wpawn.width and wpawn3y < y < wpawn3y + wpawn.height:
            wpawn3del = False
        elif wpawn4x < x < wpawn4x + wpawn.width and wpawn4y < y < wpawn4y + wpawn.height:
            wpawn4del = False
        elif wpawn5x < x < wpawn5x + wpawn.width and wpawn5y < y < wpawn5y + wpawn.height:
            wpawn5del = False
        elif wpawn6x < x < wpawn6x + wpawn.width and wpawn6y < y < wpawn6y + wpawn.height:
            wpawn6del = False
        elif wpawn7x < x < wpawn7x + wpawn.width and wpawn7y < y < wpawn7y + wpawn.height:
            wpawn7del = False
        elif wpawn8x < x < wpawn8x + wpawn.width and wpawn8y < y < wpawn8y + wpawn.height:
            wpawn8del = False

        elif wrook1x < x < wrook1x + wrook.width and wrook1y < y < wrook1y + wrook.height:
            wrook1del = False
        elif wrook2x < x < wrook2x + wrook.width and wrook2y < y < wrook2y + wrook.height:
            wrook2del = False

        elif wknight1x < x < wknight1x + wknight.width and wknight1y < y < wknight1y + wknight.height:
            wknight1del = False
        elif wknight2x < x < wknight2x + wknight.width and wknight2y < y < wknight2y + wknight.height:
            wknight2del = False

        if wbishop1x < x < wbishop1x + wbishop.width and wbishop1y < y < wbishop1y + wbishop.height:
            wbishop1del = False
        if wbishop2x < x < wbishop2x + wbishop.width and wbishop2y < y < wbishop2y + wbishop.height:
            wbishop2del = False

        if wking1x < x < wking1x + wking.width and wking1y < y < wking1y + wking.height:
            wking1del = False

        if wqueen10x < x < wqueen10x + wqueen.width and wqueen10y < y < wqueen10y + wqueen.height:
            wqueen10del = False

        elif bpawn1x < x < bpawn1x + bpawn.width and bpawn1y < y < bpawn1y + bpawn.height:
            bpawn1del = False
        elif bpawn2x < x < bpawn2x + bpawn.width and bpawn2y < y < bpawn2y + bpawn.height:
            bpawn2del = False
        elif bpawn3x < x < bpawn3x + bpawn.width and bpawn3y < y < bpawn3y + bpawn.height:
            bpawn3del = False
        elif bpawn4x < x < bpawn4x + bpawn.width and bpawn4y < y < bpawn4y + bpawn.height:
            bpawn4del = False
        elif bpawn5x < x < bpawn5x + bpawn.width and bpawn5y < y < bpawn5y + bpawn.height:
            bpawn5del = False
        elif bpawn6x < x < bpawn6x + bpawn.width and bpawn6y < y < bpawn6y + bpawn.height:
            bpawn6del = False
        elif wpawn7x < x < bpawn7x + bpawn.width and bpawn7y < y < bpawn7y + bpawn.height:
            bpawn7del = False
        elif wpawn8x < x < bpawn8x + bpawn.width and bpawn8y < y < bpawn8y + bpawn.height:
            bpawn8del = False

        elif brook1x < x < brook1x + brook.width and brook1y < y < brook1y + brook.height:
            brook1del = False
        elif brook2x < x < brook2x + brook.width and brook2y < y < brook2y + brook.height:
            brook2del = False

        elif bknight1x < x < bknight1x + bknight.width and bknight1y < y < bknight1y + bknight.height:
            bknight1del = False
        elif bknight2x < x < bknight2x + bknight.width and bknight2y < y < bknight2y + bknight.height:
            bknight2del = False

        if bbishop1x < x < bbishop1x + bbishop.width and bbishop1y < y < bbishop1y + bbishop.height:
            bbishop1del = False
        if bbishop2x < x < bbishop2x + bbishop.width and bbishop2y < y < bbishop2y + bbishop.height:
            bbishop2del = False

        if bking1x < x < bking1x + bking.width and bking1y < y < bking1y + bking.height:
            bking1del = False

        if bqueen10x < x < bqueen10x + bqueen.width and bqueen10y < y < bqueen10y + bqueen.height:
            bqueen10del = False

        else:
            pass


@window.event
def on_mouse_release(x, y, button, modifiers):
    global wpawn1x
    global wpawn1y
    global wpawn2x
    global wpawn2y
    global wpawn3x
    global wpawn3y
    global wpawn4x
    global wpawn4y
    global wpawn5x
    global wpawn5y
    global wpawn6x
    global wpawn6y
    global wpawn7x
    global wpawn7y
    global wpawn8x
    global wpawn8y

    global wrook1x
    global wrook1y
    global wrook2x
    global wrook2y

    global wknight1x
    global wknight1y
    global wknight2x
    global wknight2y

    global wbishop1x
    global wbishop1y
    global wbishop2x
    global wbishop2y

    global wking1x
    global wking1y

    global wqueen10x
    global wqueen10y

    global wpawn1clicked
    global wpawn2clicked
    global wpawn3clicked
    global wpawn4clicked
    global wpawn5clicked
    global wpawn6clicked
    global wpawn7clicked
    global wpawn8clicked

    global wrook1clicked
    global wrook2clicked

    global wknight1clicked
    global wknight2clicked

    global wbishop1clicked
    global wbishop2clicked

    global wking1clicked

    global wqueen10clicked

    global bpawn1x
    global bpawn1y
    global bpawn2x
    global bpawn2y
    global bpawn3x
    global bpawn3y
    global bpawn4x
    global bpawn4y
    global bpawn5x
    global bpawn5y
    global bpawn6x
    global bpawn6y
    global bpawn7x
    global bpawn7y
    global bpawn8x
    global bpawn8y

    global brook1x
    global brook1y
    global brook2x
    global brook2y

    global bknight1x
    global bknight1y
    global bknight2x
    global bknight2y

    global bbishop1x
    global bbishop1y
    global bbishop2x
    global bbishop2y

    global bking1x
    global bking1y

    global bqueen10x
    global bqueen10y

    global bpawn1clicked
    global bpawn2clicked
    global bpawn3clicked
    global bpawn4clicked
    global bpawn5clicked
    global bpawn6clicked
    global bpawn7clicked
    global bpawn8clicked

    global brook1clicked
    global brook2clicked

    global bknight1clicked
    global bknight2clicked

    global bbishop1clicked
    global bbishop2clicked

    global bking1clicked

    global bqueen10clicked

    global rndx
    global rndy
    rndx = x - x % 80
    rndy = y - y % 80
    if wpawn1clicked:
        wpawn1x = rndx
        wpawn1y = rndy
        wpawn1clicked = False
    if wpawn2clicked:
        wpawn2x = rndx
        wpawn2y = rndy
        wpawn2clicked = False
    if wpawn3clicked:
        wpawn3x = rndx
        wpawn3y = rndy
        wpawn3clicked = False
    if wpawn4clicked:
        wpawn4x = rndx
        wpawn4y = rndy
        wpawn4clicked = False
    if wpawn5clicked:
        wpawn5x = rndx
        wpawn5y = rndy
        wpawn5clicked = False
    if wpawn6clicked:
        wpawn6x = rndx
        wpawn6y = rndy
        wpawn6clicked = False
    if wpawn7clicked:
        wpawn7x = rndx
        wpawn7y = rndy
        wpawn7clicked = False
    if wpawn8clicked:
        wpawn8x = rndx
        wpawn8y = rndy
        wpawn8clicked = False

    if wrook1clicked:
        wrook1x = rndx
        wrook1y = rndy
        wrook1clicked = False
    if wrook2clicked:
        wrook2x = rndx
        wrook2y = rndy
        wrook2clicked = False

    if wknight1clicked:
        wknight1x = rndx
        wknight1y = rndy
        wknight1clicked = False
    if wknight2clicked:
        wknight2x = rndx
        wknight2y = rndy
        wknight2clicked = False

    if wbishop1clicked:
        wbishop1x = rndx
        wbishop1y = rndy
        wbishop1clicked = False
    if wbishop2clicked:
        wbishop2x = rndx
        wbishop2y = rndy
        wbishop2clicked = False

    if wking1clicked:
        wking1x = rndx
        wking1y = rndy
        wking1clicked = False

    if wqueen10clicked:
        wqueen10x = rndx
        wqueen10y = rndy
        wqueen10clicked = False

    if bpawn1clicked:
        bpawn1x = rndx
        bpawn1y = rndy
        bpawn1clicked = False
    if bpawn2clicked:
        bpawn2x = rndx
        bpawn2y = rndy
        bpawn2clicked = False
    if bpawn3clicked:
        bpawn3x = rndx
        bpawn3y = rndy
        bpawn3clicked = False
    if bpawn4clicked:
        bpawn4x = rndx
        bpawn4y = rndy
        bpawn4clicked = False
    if bpawn5clicked:
        bpawn5x = rndx
        bpawn5y = rndy
        bpawn5clicked = False
    if bpawn6clicked:
        bpawn6x = rndx
        bpawn6y = rndy
        bpawn6clicked = False
    if bpawn7clicked:
        bpawn7x = rndx
        bpawn7y = rndy
        bpawn7clicked = False
    if bpawn8clicked:
        bpawn8x = rndx
        bpawn8y = rndy
        bpawn8clicked = False

    if brook1clicked:
        brook1x = rndx
        brook1y = rndy
        brook1clicked = False
    if brook2clicked:
        brook2x = rndx
        brook2y = rndy
        brook2clicked = False

    if bknight1clicked:
        bknight1x = rndx
        bknight1y = rndy
        bknight1clicked = False
    if bknight2clicked:
        bknight2x = rndx
        bknight2y = rndy
        bknight2clicked = False

    if bbishop1clicked:
        bbishop1x = rndx
        bbishop1y = rndy
        bbishop1clicked = False
    if bbishop2clicked:
        bbishop2x = rndx
        bbishop2y = rndy
        bbishop2clicked = False

    if bking1clicked:
        bking1x = rndx
        bking1y = rndy
        bking1clicked = False

    if bqueen10clicked:
        bqueen10x = rndx
        bqueen10y = rndy
        bqueen10clicked = False


pyglet.app.run()
