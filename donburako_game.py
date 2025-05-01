import tkinter
import random

WIDTH = 283
HEIGHT = 400
MAX_ROCKS = 3
key = ""
collision = False
game_end = False
rock_count = 0


class ImageObject:
    global canvas

    def __init__(self, file_name, tag):
        self.source_file = file_name
        self.tag_words = tag
        self.pos_y = 0
        self.pos_x = 0

    def create_photo_image(self):
        self.photo_image = tkinter.PhotoImage(file=self.source_file)
        print(self.source_file + "のImageを生成")
        print(self.photo_image)

    def draw(self):
        self.draw_image = canvas.create_image(
            self.pos_x, self.pos_y, image=self.photo_image, tag=self.tag_words
        )
        print(self.source_file + "のImageを描画")
        print(self.tag_words)

    def getY(self):
        return self.pos_y

    def setY(self, argument_y):
        self.pos_y = argument_y
        canvas.coords(self.tag_words, self.pos_x, self.pos_y)

    def getX(self):
        return self.pos_x

    def setX(self, argument_x):
        self.pos_x = argument_x
        canvas.coords(self.tag_words, self.pos_x, self.pos_y)


def game_update():
    global collision
    global game_end
    global rock_count
    if (
        car.getY() + 25 >= rock.getY() - 25
        and car.getY() - 25 <= rock.getY() - 25
        and car.getX() + 25 >= rock.getX() - 25
        and car.getX() - 25 <= rock.getX() + 25
    ):
        collision = True
    if collision:
        collision_effect.setX(car.getX())
        collision_effect.setY(car.getY())
        collision_effect.draw()
        rock.draw()
        if not game_end:
            game_end = True
            root.after(500, gameover)
    if not collision and not game_end:
        if road.getY() <= -HEIGHT / 2:
            road.setY(road_2.getY() + HEIGHT)
        if road_2.getY() <= -HEIGHT / 2:
            road_2.setY(road.getY() + HEIGHT)

        road.setY(road.getY() - 10)
        road_2.setY(road_2.getY() - 10)

        rock.setY(rock.getY() - 10)
        if rock_count < MAX_ROCKS:
            if rock.getY() <= -25:
                rock.setX(random.random() * WIDTH)
                rock.setY(HEIGHT + 25)
                rock_count += 1
        if rock_count >= MAX_ROCKS:
            grandma.setY(grandma.getY() - 10)
    if car.getY() + 25 >= grandma.getY() - 25:
        game_end = True
    root.after(100, game_update)


def key_down(e):
    global key
    global car
    global collision
    global game_end
    key = e.keysym
    if not collision and not game_end:
        if key == "Left" and car.getX() >= 0:
            car.setX(car.getX() - 1)
        if key == "Right" and car.getX() <= WIDTH:
            car.setX(car.getX() + 1)


def key_up(e):
    global key
    key = ""


def gameover():
    game_over_logo.setX(WIDTH / 2)
    game_over_logo.setY(HEIGHT / 2)
    game_over_logo.draw()


root = tkinter.Tk()
root.title("高速道路")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT, bg="gray")
canvas.pack()

road = ImageObject("road.png", "ROAD")
road.create_photo_image()
road.setX(WIDTH / 2)
road.setY(HEIGHT / 2)
road.draw()

road_2 = ImageObject("road.png", "ROAD_2")
road_2.create_photo_image()
road_2.setX(WIDTH / 2)
road_2.setY(road.getY() + HEIGHT)
road_2.draw()

car = ImageObject("car.png", "CAR")
car.create_photo_image()
car.setX(WIDTH / 2)
car.setY(100)
car.draw()

rock_pos_x = random.random() * WIDTH
rock = ImageObject("rock.png", "ROCK")
rock.create_photo_image()
rock.setX(rock_pos_x)
rock.setY(HEIGHT + 25)
rock.draw()

collision_effect = ImageObject("collision_effect.png", "COLLISION_EFFECT")
collision_effect.create_photo_image()

game_over_logo = ImageObject("game_over.png", "GAME_OVER_LOGO")
game_over_logo.create_photo_image()

grandma = ImageObject("grandma.png", "GRANDMA")
grandma.create_photo_image()
grandma.setX(WIDTH / 2)
grandma.setY(HEIGHT + 50)
grandma.draw()
rock_count = 1

game_update()
root.mainloop()
