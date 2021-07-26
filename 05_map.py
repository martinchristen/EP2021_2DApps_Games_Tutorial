
import arcade

class EarthQuake(arcade.Window):
    def __init__(self):
        super().__init__(1024, 768)
        arcade.set_background_color((0,0,0))

        self.center_x = 512
        self.center_y = 384

        self.world = arcade.load_texture("data/world_hd_1920_960.jpg")

    def on_draw(self):
        arcade.start_render()

        w = self.width

        arcade.draw_texture_rectangle(self.center_x, self.center_y, w, w/2, self.world)



w = EarthQuake()
arcade.run()