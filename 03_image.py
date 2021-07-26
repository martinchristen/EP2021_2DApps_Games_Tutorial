import arcade

class MyWindow(arcade.Window):
    def __init__(self, width, height, windowtitle):
        super().__init__(width, height, windowtitle)
        self.x = width/2
        self.y = height/2
        self.color = (0,255,255)
        self.zoom = 1
        self.sign = 1

        self.texture = arcade.load_texture("assets/misc/python.png")

        arcade.set_background_color( (0,0,0) )

    def on_draw(self):
        arcade.start_render()
        #arcade.draw_rectangle_filled(self.x, self.y, 64, 64, self.color)
        arcade.draw_texture_rectangle(self.x, self.y,
                    self.zoom*self.texture.width, 
                    self.zoom*self.texture.height, 
                    self.texture)

        arcade.draw_text(f"Hello World {self.x} {self.y}", 200, 300, arcade.color.WHITE, 40)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.B:
            self.color = (0,0,255)
        elif key == arcade.key.R:
            self.color = (255,0,0)

    def on_update(self, dt):
        self.zoom += dt*self.sign
        if self.zoom > 1:
            self.sign = -1
        
        if self.zoom < 0:
            self.sign = 1

    def on_mouse_motion(self, mx, my, dx, dy):
        self.x = mx
        self.y = my

    
window = MyWindow(1024,768,"Title")
arcade.run()

# pip install shapely
# conda install shapely