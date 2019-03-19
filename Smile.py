import arcade


arcade.open_window(800,600, "title")
arcade.start_render()
arcade.draw_circle_filled(400,300,200,arcade.color.ANDROID_GREEN)
arcade.draw_circle_filled(300,400,25,arcade.color.BABY_BLUE_EYES)
arcade.draw_circle_filled(500,400,25,arcade.color.BABY_BLUE_EYES)
arcade.draw_arc_outline(400,200,100,50,arcade.color.BLACK,190,350,10)

arcade.finish_render()

arcade.run()