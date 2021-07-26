import arcade

arcade.open_window(640, 480, "First Window")

arcade.set_background_color([0,255,255])
arcade.start_render()

arcade.draw_rectangle_filled(320, 240, 100, 200, [255,0,0])

mypointlist = ((160, 200), (400, 100), (300, 100), (55,55))

arcade.draw_points(mypointlist, (255,0,0), 10)

arcade.finish_render()

arcade.run()