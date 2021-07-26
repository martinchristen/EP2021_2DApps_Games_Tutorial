
import arcade

class EarthQuake(arcade.Window):
    def __init__(self):
        super().__init__(1024, 768)
        arcade.set_background_color((0,0,0))

        self.center_x = 512
        self.center_y = 384

        self.world = arcade.load_texture("data/world_hd_1920_960.jpg")

    def get_position(self, lng, lat):
        w = self.width
        h = w / 2

        x = w * (lng + 180) / 360 + self.center_x - w/2
        y = h * (lat + 90) / 180 + self.center_y - h/2

        return x, y

    def on_draw(self):
        arcade.start_render()

        w = self.width

        arcade.draw_texture_rectangle(self.center_x, self.center_y, w, w/2, self.world)

        x, y = self.get_position(180, 0)
        arcade.draw_circle_filled(x, y, 6, (255, 0, 0))


w = EarthQuake()
arcade.run()