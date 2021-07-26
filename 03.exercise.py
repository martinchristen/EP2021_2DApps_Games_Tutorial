import arcade

class MyWindow(arcade.Window):
    def __init__(self, width, height, windowtitle):
        super().__init__(width, height, windowtitle)
        self.x = width/2
        self.y = height/2
        self.dx = 0
        self.dy = 0
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
        if key == arcade.key.UP:
            self.dy = 1
        if key == arcade.key.DOWN:
            self.dy = -1
        if key == arcade.key.RIGHT:
            self.dx = 1
        if key == arcade.key.LEFT:
            self.dx = -1

    def on_key_release(self, key, mods):
        if key == arcade.key.UP:
            self.dy = 0
        if key == arcade.key.DOWN:
            self.dy = 0
        if key == arcade.key.RIGHT:
            self.dx = 0
        if key == arcade.key.LEFT:
            self.dx = 0

    def on_update(self, dt):
        self.x += 1*self.dx
        self.y += 1*self.dy

        if self.x > self.width - 32:
            self.x = self.width - 32
            self.dx = -self.dx
        
        if self.x < 32:
            self.x = 32
            self.dx = -self.dx

        if self.y > self.height - 32:
            self.y = self.height - 32
            self.dy = -self.dy
        
        if self.y < 32:
            self.y = 32
            self.dy = -self.dy
        

    
window = MyWindow(640,480,"Title")
arcade.run()

# pip install shapely
# conda install shapely