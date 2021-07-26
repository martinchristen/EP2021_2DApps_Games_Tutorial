
import arcade
import json

class EarthQuake(arcade.Window):
    def __init__(self):
        super().__init__(1024, 768)
        arcade.set_background_color((0,0,0))

        with open("earthquakes.geojson", encoding="utf-8") as json_file:
            self.data = json.load(json_file)

        self.center_x = 512
        self.center_y = 384
        self.delta_x = 0
        self.delta_y = 0
        self.zoom = 1

        self.marker = arcade.load_texture("data/marker.png")
        self.world = arcade.load_texture("data/world_hd_1920_960.jpg")

    def get_position(self, lng, lat):
        w = self.width
        h = w / 2

        x = self.zoom * w * (lng + 180) / 360 + self.center_x - w/2 + self.delta_x
        y = self.zoom * h * (lat + 90) / 180 + self.center_y - h/2 + self.delta_y

        return x, y

    def on_draw(self):
        arcade.start_render()

        w = self.width

        arcade.draw_texture_rectangle(self.center_x, 
        self.center_y, 
        self.zoom * w, 
        self.zoom * w/2, 
        self.world)

        for element in self.data["features"]:
            mag = element["properties"]["mag"]
            coord = element["geometry"]["coordinates"]
            x, y = self.get_position(coord[0], coord[1])

            color = (50,0,0)
            if mag>3:
                color = (100,0,0)
            if mag>4:
                color = (150,0,0)
            if mag>5:
                color = (200,0,0)
            if mag>6:
                color = (250,0,0)

            mw = self.marker.width/4
            mh = self.marker.height/4
            arcade.draw_circle_filled(x, y, 1.5*mag, color)
            arcade.draw_texture_rectangle(x, y + mh/2, mw, mh, self.marker)

    def on_mouse_scroll(self, mx, my, scrollx, scrolly):

        w = self.width
        h = w/2

        if scrolly>0:
            self.zoom += 0.1 # zoom in
            self.delta_x -= 0.1 * w/2
            self.delta_y -= 0.1 * h/2 

        if scrolly<0:
            self.zoom -= 0.1 # zoom out
            self.delta_x += 0.1 * w/2
            self.delta_y += 0.1 * h/2 



    def on_mouse_drag(self, mx, my, dx, dy, buttons, mods):
        self.center_x += dx
        self.center_y += dy


w = EarthQuake()
arcade.run()