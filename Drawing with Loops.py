import arcade


WIDTH = 640
HEIGHT = 480


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    rec_x, rec_y, rec_width, rec_length = 100, 100, 40, 80
    tri_x1, tri_x2, tri_x3, tri_y1, tri_y2, tri_y3 = 120, 70, 170, 250, 180, 180
    for tree in range(5):
        arcade.draw_xywh_rectangle_filled(rec_x, rec_y, rec_width, rec_length, arcade.color.GREEN)
        arcade.draw_triangle_filled(tri_x1, tri_y1, tri_x2, tri_y2, tri_x3, tri_y3, arcade.color.BROWN)
        rec_x += 100
        tri_x1 += 100
        tri_x2 += 100
        tri_x3 += 100




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