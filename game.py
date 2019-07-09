import arcade
import random

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

        self.car = arcade.Sprite("PNG/Cars/car_green_3.png", scale= 0.4 ) 
        self.number1 = arcade.Sprite("PNG/1.png", scale= 0.5)
        self.number2 = arcade.Sprite("PNG/2.png", scale= 0.5)
        self.number3 = arcade.Sprite("PNG/3.png", scale= 0.5)
        #added this as an obstacle. Sorry if it was the wrong place
        #self.spikes = arcade.Sprite("PNG/Retractable_floor_spikes_icon.png", scale= 0.05)
        self.number3.center_x = 50
        self.number3.center_y = 50
        self.number2.center_x = 50
        self.number2.center_y = 50
        self.number1.center_x = 50
        self.number1.center_y = 50
        #self.spikes.center_x = 350
        #self.spikes.center_y = 640

        

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.car.draw()
        # Obstacle drawing
        #self.spikes.draw()
        arcade.draw_text("Hello", 100, 100, arcade.color.RED, 20, width=200, align="center")
        if self.health ==  3:
            self.number3.draw()
        if self.health ==  2:
            self.number2.draw()
        if self.health ==  1:
            self.number1.draw()
        

    def on_update(self, deltatime):
        self.car.change_x = 0
        self.car.change_y = 0
        if self.car.direction == "left":
            self.car.change_x = -150 * deltatime
            self.car.angle = 90
        if self.car.direction == "right":
            self.car.change_x = 150 * deltatime
            self.car.angle = 270
        if self.car.direction == "up":
            self.car.angle = 360
            self.car.change_y = 150 * deltatime
        if self.car.direction == "down":
            self.car.angle = 180
            self.car.change_y = -150 * deltatime
        self.car.update()

        squarex = int(self.car.center_x/(128 * SPRITE_SCALING)) 
        squarey = len(self.map[0]) - int(self.car.center_y/(128 * SPRITE_SCALING)) -1
        print(squarex,squarey)
        Height_of_map = len(self.map)
        width_of_map = len(self.map[0])
        try:
            cords = (self.map[squarey][squarex])
            if cords == 16:
                self.health =  self.health -1
                self.car.direction = "left"
                self.car.position = (400,635)
            if  self.health == 0:
                arcade.close_window()  
            
        except:
            pass

    def on_key_press(self,symbol,modifiers):
        if symbol == arcade.key.LEFT:
            self.car.direction = "left"
        if symbol == arcade.key.RIGHT:
            self.car.direction = "right"
        if symbol == arcade.key.UP:
            self.car.direction = "up"
        if symbol == arcade.key.DOWN:
            self.car.direction = "down"

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
        arcade.set_background_color(arcade.color.GREEN)
        self.car.position = (400,635)
        self.car.direction = "left"
        self.health = 3
        arcade.Sprite("PNG/3.png", scale= 0.5)
        

        
MyGame = MyGame()
MyGame.setup()
arcade.run()