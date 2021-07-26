import arcade

class MyWindow(arcade.Window):
    def __init__(self, width, height, windowtitle):
        super().__init__(width, height, windowtitle)
        self.x = 0
        self.y = 0
        self.color = (0,255,255)

        arcade.set_background_color( (0,0,0) )

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.x, self.y, 64, 64, self.color)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.B:
            self.color = (0,0,255)
        elif key == arcade.key.R:
            self.color = (255,0,0)
        
    def on_update(self, dt):
        pass
        #self.x = self.x + 30*dt

    def on_mouse_motion(self, mx, my, dx, dy):
        self.x = mx
        self.y = my

    
window = MyWindow(640,480,"Title")
arcade.run()

# pip install shapely
# conda install shapely