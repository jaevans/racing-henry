import arcade

screen_width =  768
screen_height = 768
screen_title = "Sprite collect coins example"

SPRITE_SCALING = 0.3

tile_id_mapping = [
    "PNG/Tiles/Dirt road/road_dirt90.png",
    "PNG/Tiles/Dirt road/road_dirt02.png",
    "PNG/Tiles/Dirt road/road_dirt04.png",
    "PNG/Tiles/Dirt road/road_dirt38.png",
    "PNG/Tiles/Dirt road/road_dirt40.png",
    "PNG/Tiles/Dirt road/road_dirt01.png",
    "PNG/Tiles/Grass/land_grass01.png",
    "PNG/Tiles/Grass/land_grass02.png",
    "PNG/Tiles/Grass/land_grass03.png",
    "PNG/Tiles/Grass/land_grass04.png",
    "PNG/Tiles/Grass/land_grass05.png",
    "PNG/Tiles/Grass/land_grass06.png",
    "PNG/Tiles/Grass/land_grass07.png",
    "PNG/Tiles/Grass/land_grass08.png",
    "PNG/Tiles/Grass/land_grass09.png",
    "PNG/Tiles/Grass/land_grass10.png",
    "PNG/Tiles/Grass/land_grass11.png",
    "PNG/Tiles/Grass/land_grass12.png",
    "PNG/Tiles/Grass/land_grass13.png",
    "PNG/Tiles/Grass/land_grass14.png",
    "PNG/Tiles/Dirt/land_dirt05.png",
]

class MyGame(arcade.Window):
    """ our custom window class """

    def __init__(self):
        super().__init__(screen_width, screen_height, screen_title,antialiasing=False)

        self.car = arcade.Sprite("PNG/Cars/car_green_3.png", scale= 0.4)

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.car.draw()

    def on_update(self,deltatime):
        self.car.change_x = 0
        self.car.change_y = 0
        if self.car.dir == "left":
            self.car.change_x = -150 * deltatime
            self.car.angle = 90
        if self.car.dir == "right":
            self.car.change_x = 150 * deltatime
            self.car.angle = 270
        if self.car.dir == "up":
            self.car.angle = 360
            self.car.change_y = 150 * deltatime
        if self.car.dir == "down":
            self.car.angle = 180
            self.car.change_y = -150 * deltatime
        self.car.update()
        squarex = int(self.car.center_x//38) 
        squarey = int(self.car.center_y//38) 
        print(squarex,squarey)
        print(self.map[squarey][squarex])

    def on_key_press(self,symbol,modifiers):
        if symbol == arcade.key.LEFT:
            self.car.dir = "left"
        if symbol == arcade.key.RIGHT:
            self.car.dir = "right"
        if symbol == arcade.key.UP:
            self.car.dir = "up"
        if symbol == arcade.key.DOWN:
            self.car.dir = "down"

    def setup(self):
        my_map = []
        with open("track.csv") as my_map_file:
            for line in my_map_file.readlines():
                my_map.append([int(x) for x in line.strip().split(",")])
        self.map = my_map
        self.background = arcade.SpriteList()

        for row in range(len(my_map)):
            for col in range(len(my_map[row])):
                sprite = arcade.Sprite(tile_id_mapping[my_map[row][col]],SPRITE_SCALING)
                sprite.left = col * sprite.width
                sprite.top = self.get_size()[1] - (row * sprite.height)
                self.background.append(sprite)
        arcade.set_background_color(arcade.color.RED)
        self.car.position = (400,635)
        self.car.dir = "left"
MyGame = MyGame()
MyGame.setup()
arcade.run()