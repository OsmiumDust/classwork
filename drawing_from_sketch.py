import arcade


WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
# Begin drawing

#Grass
arcade.draw_lrtb_rectangle_filled(0, WIDTH, 100, 0, arcade.color.GREEN)

#Sun
arcade.draw_circle_filled(WIDTH - 100, HEIGHT - 100, 50, arcade.color.YELLOW)

#Tree1
arcade.draw_triangle_filled(200, 200, 200-40, 200-75, 200 + 40, 200-75, arcade.color.DARK_GREEN)
arcade.draw_xywh_rectangle_filled(190, 50, 20, 150-75, arcade.color.BROWN)

#Tree2
arcade.draw_triangle_filled(WIDTH-125, 200, WIDTH-125-40, 200-75, WIDTH-125 + 40, 200-75, arcade.color.DARK_GREEN)
arcade.draw_xywh_rectangle_filled(WIDTH-125-10, 50, 20, 150-75, arcade.color.BROWN)

#Tree3
arcade.draw_triangle_filled(WIDTH-200, 200, WIDTH-200-40, 200-75, WIDTH-200 + 40, 200-75, arcade.color.DARK_GREEN)
arcade.draw_xywh_rectangle_filled(WIDTH-200-10, 50, 20, 150-75, arcade.color.BROWN)

#Random text I input
arcade.draw_text("A forest that has only three trees", 50, HEIGHT - 50, arcade.color.BLACK)

# End drawing
arcade.finish_render()
arcade.run()