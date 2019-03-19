import arcade
import math

WIDTH = 640
HEIGHT = 480


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    def placement(x, y, end, space):
        for tree in range(x, end):
            if x <= end:
                arcade.draw_xywh_rectangle_filled(x, y, 10, 30, arcade.color.GREEN)
                arcade.draw_triangle_filled(x-10,y+30,x+20,y+30,x+5,y+100, arcade.color.BROWN)
            x += space

    placement(1, 25, WIDTH, 25)
    placement(2, 125, WIDTH, math.pi)
    placement(3, 250, WIDTH, 50)

    '''rec_x, rec_y, rec_width, rec_length = 50, 50, 40, 80
    tri_x1, tri_x2, tri_x3, tri_y1, tri_y2, tri_y3 = 50+20, 50+20-50, 50+20+50, 50+80+70, 50+80, 50+80
    for tree in range(6):
        arcade.draw_xywh_rectangle_filled(rec_x, rec_y, rec_width, rec_length, arcade.color.GREEN)
        arcade.draw_triangle_filled(tri_x1, tri_y1, tri_x2, tri_y2, tri_x3, tri_y3, arcade.color.BROWN)
        rec_x += 100
        tri_x1 += 100
        tri_x2 += 100
        tri_x3 += 100'''




def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()