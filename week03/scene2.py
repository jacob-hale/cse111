# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random
# 1 = nice landscape, 2 = winter wonderland, 3 = dry desert 
piece = random.randint(1, 3)

if piece == 1:


    def main():
        # Width and height of the scene in pixels
        scene_width = 800
        scene_height = 500

        # Call the start_drawing function in the draw2d.py
        # library which will open a window and create a canvas.
        canvas = start_drawing("Scene", scene_width, scene_height)

        # Call your drawing functions such
        # as draw_sky and draw_ground here.
        draw_ground(canvas, scene_width, scene_height)
        draw_stream(canvas)
        draw_sky(canvas, scene_width, scene_height)
        draw_mountains(canvas)
        draw_house(canvas)
        draw_path(canvas)
        draw_trees(canvas)
        draw_chimney(canvas)
        draw_name(canvas)
        # draw_grid(canvas, scene_width, scene_height, 50)
        
        # Call the finish_drawing function
        # in the draw2d.py library.
        finish_drawing(canvas)


    # Define your functions such as
    # draw_sky and draw_ground here.
    def draw_sky(canvas, scene_width, scene_height):
        # Draw the sky and all objects in the sky
        # sky
        draw_rectangle(canvas, 0, scene_height / 2.5, scene_width, scene_height, width = 0, fill="sky blue")
        # sun
        draw_oval(canvas, 650, 375, 750, 475, width = 0, fill="yellow1")
        # clouds
        for _ in range(16):
            rand_x = random.randint(-50, 850)
            rand_y = random.randint(275, 550)
            draw_oval(canvas, rand_x, rand_y, rand_x + random.randint(100, 175), rand_y + random.randint(35, 75), width = 0, fill="lavenderBlush1")
        # cloud left
        # draw_oval(canvas, 50, 325, 150, 400, width = 0, fill="lavenderBlush1")
        # draw_oval(canvas, 100, 350, 300, 450, width = 0, fill="lavenderBlush1")
        # draw_oval(canvas, 100, 425, 200, 475, width = 0, fill="lavenderBlush1")
        # # cloud right
        # draw_oval(canvas, 525, 375, 675, 425, width = 0, fill="lavenderBlush1")
        # draw_oval(canvas, 475, 350, 600, 400, width = 0, fill="lavenderBlush1")
        # birds
        for _ in range(7):
            lx_start = random.randint(50, 750)
            ly_start = random.randint(350, 475)
            lx_next = lx_start + random.randint(10, 30)
            ly_next = ly_start + random.randint(15, 30)

            wing = random.randint(5, 15)
            widths = random.randint(2,3)
            rx_start = lx_next
            ry_start = ly_start
            rx_next = rx_start + (lx_next - lx_start) 
            ry_next = ly_next

            draw_arc(canvas, lx_start, ly_start, lx_next, ly_next, start=0, extent=180 - wing, width=widths)
            draw_arc(canvas, rx_start, ry_start, rx_next, ry_next, start=wing, extent=180, width=widths)
        # bird lower
        # draw_arc(canvas, 400, 400, 435, 425, start=0, extent=165, width = 3)
        # draw_arc(canvas, 435, 400, 470, 425, start=15, extent=180, width = 3)
        # # bird upper
        # draw_arc(canvas, 450, 415, 475, 440, start=0, extent=155, width = 2)
        # draw_arc(canvas, 475, 415, 500, 440, start=15, extent=180, width= 2)
        # # bird small
        # draw_arc(canvas, 425, 450, 440, 470, start=10, extent=180)
        # draw_arc(canvas, 440, 450, 455, 470, start=-10, extent=170)

    def draw_ground(canvas, scene_width, scene_height):
        # ground
        draw_rectangle(canvas, 0, 0, scene_width, scene_height / 2.5, outline = "", fill = "green4")
        # flowers
        for _ in range(55):
            rand_x = random.randint(0, 800)
            rand_y = random.randint(0, 200)
            colors = ["violetRed3", "darkOrchid3", "lawnGreen", "yellow1", "deepSkyBlue2", "orchid1", "red2", "snow1"]
            draw_oval(canvas, rand_x, rand_y, rand_x + 5, rand_y + 5, outline="", fill=random.choice(colors))

    def draw_stream(canvas):
        # stream
        draw_arc(canvas, 525, 200, 675, 125, start=90, extent=-180, width=25, outline="darkTurquoise")
        draw_arc(canvas, 500, 125, 700, 0, start=90, extent=180, width=25, outline="darkTurquoise")
        # pond
        draw_oval(canvas, 475, -50, 775, 50, width=0, fill="darkTurquoise")

    def draw_house(canvas):
        # house
        draw_oval(canvas, 0, 25, 225, 125, outline="", fill="khaki")
        draw_rectangle(canvas, 25, 50, 175, 125, width=1, outline="black", fill="saddleBrown")
        draw_polygon(canvas, 175, 50, 200, 100, 200, 175, 175, 125, width=0, outline="black", fill="tan4")
        # draw_polygon(canvas, 175, 50, 175, 125, 200, 100, 200, 175, width=0)
        draw_polygon(canvas, 175, 125, 200, 175, 185, 180, width=1, outline="black", fill="tan4")
        draw_polygon(canvas, 172, 100, 185, 180, 34, 180, 21, 100, width=1, outline="black", fill="burlywood4")

    def draw_chimney(canvas):
        draw_rectangle(canvas, 50, 180, 65, 200, fill="brown4")
        # smoke
        colors = ["slateGray4", "slateGray", "lightSlateGray", "gray54"]
        for _ in range(50):
            rand_x = random.randint(25, 100)
            rand_y = random.randint(215, 500)
            draw_oval(canvas, rand_x, rand_y, rand_x + random.randint(10, 35), rand_y + random.randint(10, 25), outline="", fill=random.choice(colors))

    def draw_mountains(canvas):
        draw_polygon(canvas, -100, 200, 900, 200, random.randint(550, 850), random.randint(275, 350), 550, 275, random.randint(300, 550), random.randint(275, 350), 300, 275, random.randint(0, 225), random.randint(275, 350), outline="", fill="cornsilk4")

    def draw_path(canvas):
        x_start = 200
        y_start = 75
        colors = ["gray30", "gray45", "gray54", "gray72"]
        for _ in range(40):
            draw_oval(canvas, x_start, y_start, x_start + 10, y_start + 10, outline="", fill=random.choice(colors))
            x_start += random.randint(15, 20)
            y_start += random.randint(-5, 5)

    def draw_trees(canvas):
        for _ in range(5):
            x_start = random.randint(225, 450)
            y_start = random.randint(50, 175)
            x_next = x_start + random.randint(25, 50)
            y_next = y_start
            x_middle = (x_start + x_next) / 2
            y_middle = y_start + random.randint(50, 100)
            draw_line(canvas, x_middle, y_start - 15, x_middle, y_start, width=5, fill="brown")
            draw_polygon(canvas, x_start, y_start, x_next, y_next, x_middle, y_middle, outline="", fill="darkGreen")
        for _ in range(5):
            x_start = random.randint(700, 825)
            y_start = random.randint(50, 175)
            x_next = x_start + random.randint(25, 50)
            y_next = y_start
            x_middle = (x_start + x_next) / 2
            y_middle = y_start + random.randint(50, 100)
            draw_line(canvas, x_middle, y_start - 15, x_middle, y_start, width=5, fill="brown")
            draw_polygon(canvas, x_start, y_start, x_next, y_next, x_middle, y_middle, outline="", fill="darkGreen")
            
    def draw_name(canvas):
        draw_text(canvas, 750, 25, "Jacob Hale", fill="black")


    def draw_grid(canvas, width, height, interval, color="black"):
        # Draw a vertical line at every x interval.
        label_y = 15
        for x in range(interval, width, interval):
            draw_line(canvas, x, 0, x, height, fill=color)
            draw_text(canvas, x, label_y, f"{x}", fill=color)

        # Draw a horizontal line at every y interval.
        label_x = 15
        for y in range(interval, height, interval):
            draw_line(canvas, 0, y, width, y, fill=color)
            draw_text(canvas, label_x, y, f"{y}", fill=color)
    # Call the main function so that
    # this program will start executing.
    main()


elif piece == 2:
    def main():
        # Width and height of the scene in pixels
        scene_width = 800
        scene_height = 500

        # Call the start_drawing function in the draw2d.py
        # library which will open a window and create a canvas.
        canvas = start_drawing("Scene", scene_width, scene_height)

        # Call your drawing functions such
        # as draw_sky and draw_ground here.
        draw_ground(canvas, scene_width, scene_height)
        draw_stream(canvas)
        draw_sky(canvas, scene_width, scene_height)
        draw_mountains(canvas)
        draw_house(canvas)
        draw_path(canvas)
        draw_trees(canvas)
        draw_chimney(canvas)
        draw_snowman(canvas)
        draw_name(canvas)
        # draw_grid(canvas, scene_width, scene_height, 50)
        
        # Call the finish_drawing function
        # in the draw2d.py library.
        finish_drawing(canvas)


    # Define your functions such as
    # draw_sky and draw_ground here.
    def draw_sky(canvas, scene_width, scene_height):
        # Draw the sky and all objects in the sky
        # sky
        draw_rectangle(canvas, 0, scene_height / 2.5, scene_width, scene_height, width = 0, fill="lightBlue")
        # sun
        # draw_oval(canvas, 650, 375, 750, 475, width = 0, fill="yellow1")
        # clouds
        for _ in range(40):
            rand_x = random.randint(-50, 850)
            rand_y = random.randint(275, 550)
            draw_oval(canvas, rand_x, rand_y, rand_x + random.randint(100, 175), rand_y + random.randint(35, 75), width = 0, fill="gray90")
        # cloud left
        # draw_oval(canvas, 50, 325, 150, 400, width = 0, fill="lavenderBlush1")
        # draw_oval(canvas, 100, 350, 300, 450, width = 0, fill="lavenderBlush1")
        # draw_oval(canvas, 100, 425, 200, 475, width = 0, fill="lavenderBlush1")
        # # cloud right
        # draw_oval(canvas, 525, 375, 675, 425, width = 0, fill="lavenderBlush1")
        # draw_oval(canvas, 475, 350, 600, 400, width = 0, fill="lavenderBlush1")
        # birds
        for _ in range(2):
            lx_start = random.randint(50, 750)
            ly_start = random.randint(350, 475)
            lx_next = lx_start + random.randint(10, 30)
            ly_next = ly_start + random.randint(15, 30)

            wing = random.randint(5, 15)
            widths = random.randint(2,3)
            rx_start = lx_next
            ry_start = ly_start
            rx_next = rx_start + (lx_next - lx_start) 
            ry_next = ly_next

            draw_arc(canvas, lx_start, ly_start, lx_next, ly_next, start=0, extent=180 - wing, width=widths)
            draw_arc(canvas, rx_start, ry_start, rx_next, ry_next, start=wing, extent=180, width=widths)
        # bird lower
        # draw_arc(canvas, 400, 400, 435, 425, start=0, extent=165, width = 3)
        # draw_arc(canvas, 435, 400, 470, 425, start=15, extent=180, width = 3)
        # # bird upper
        # draw_arc(canvas, 450, 415, 475, 440, start=0, extent=155, width = 2)
        # draw_arc(canvas, 475, 415, 500, 440, start=15, extent=180, width= 2)
        # # bird small
        # draw_arc(canvas, 425, 450, 440, 470, start=10, extent=180)
        # draw_arc(canvas, 440, 450, 455, 470, start=-10, extent=170)

    def draw_ground(canvas, scene_width, scene_height):
        # ground
        draw_rectangle(canvas, 0, 0, scene_width, scene_height / 2.5, outline = "", fill = "snow1")
        # flowers

    def draw_stream(canvas):
        # stream
        draw_arc(canvas, 525, 200, 675, 125, start=90, extent=-180, width=25, outline="powderBlue")
        draw_arc(canvas, 500, 125, 700, 0, start=90, extent=180, width=25, outline="powderBlue")
        # pond
        draw_oval(canvas, 475, -50, 775, 50, width=0, fill="powderBlue")

    def draw_house(canvas):
        # house
        draw_oval(canvas, 0, 25, 225, 125, outline="", fill="gray68")
        draw_rectangle(canvas, 25, 50, 175, 125, width=1, outline="black", fill="saddleBrown")
        draw_polygon(canvas, 175, 50, 200, 100, 200, 175, 175, 125, width=0, outline="black", fill="tan4")
        # draw_polygon(canvas, 175, 50, 175, 125, 200, 100, 200, 175, width=0)
        draw_polygon(canvas, 175, 125, 200, 175, 185, 180, width=1, outline="black", fill="tan4")
        draw_polygon(canvas, 172, 100, 185, 180, 34, 180, 21, 100, width=1, outline="black", fill="snow2")
        
        
        for _ in range (20):
            x_start = random.randint(21, 165)
            y_start = 100
            x_next = x_start + 7
            draw_polygon(canvas, x_start, y_start, x_next, y_start, (x_start + x_next) / 2, y_start - (random.randint(10, 20)), outline="", fill="lightSkyBlue2")

    def draw_chimney(canvas):
        draw_rectangle(canvas, 50, 180, 65, 200, fill="brown4")
        # smoke
        colors = ["slateGray4", "slateGray", "lightSlateGray", "gray54"]
        for _ in range(150):
            rand_x = random.randint(25, 100)
            rand_y = random.randint(215, 500)
            draw_oval(canvas, rand_x, rand_y, rand_x + random.randint(10, 35), rand_y + random.randint(10, 25), outline="", fill=random.choice(colors))

    def draw_mountains(canvas):
        draw_polygon(canvas, -100, 200, 900, 200, random.randint(550, 850), random.randint(275, 350), 550, 275, random.randint(300, 550), random.randint(275, 350), 300, 275, random.randint(0, 225), random.randint(275, 350), outline="", fill="snow3")

    def draw_path(canvas):
        x_start = 200
        y_start = 75
        colors = ["gray45", "gray54", "gray72", "gray90"]
        for _ in range(40):
            draw_oval(canvas, x_start, y_start, x_start + 10, y_start + 10, outline="", fill=random.choice(colors))
            x_start += random.randint(15, 20)
            y_start += random.randint(-5, 5)

    def draw_trees(canvas):
        for _ in range(5):
            x_start = random.randint(225, 450)
            y_start = random.randint(50, 175)
            x_next = x_start + random.randint(25, 50)
            y_next = y_start
            x_middle = (x_start + x_next) / 2
            y_middle = y_start + random.randint(50, 100)
            draw_line(canvas, x_middle, y_start - 15, x_middle, y_start, width=5, fill="brown4")
            draw_polygon(canvas, x_start, y_start, x_next, y_next, x_middle, y_middle, outline="slateGray3", fill="azure2")
        for _ in range(5):
            x_start = random.randint(700, 825)
            y_start = random.randint(50, 175)
            x_next = x_start + random.randint(25, 50)
            y_next = y_start
            x_middle = (x_start + x_next) / 2
            y_middle = y_start + random.randint(50, 100)
            draw_line(canvas, x_middle, y_start - 15, x_middle, y_start, width=5, fill="brown4")
            draw_polygon(canvas, x_start, y_start, x_next, y_next, x_middle, y_middle, outline="slateGray3", fill="azure2")
    def draw_snowman(canvas):
        draw_oval(canvas, 200, 50, 225, 75, outline="slateGray3", fill="aliceBlue")
        draw_oval(canvas, 203, 70, 222, 90, outline="slateGray3", fill="aliceBlue")
        draw_oval(canvas, 205, 87, 220, 102, outline="slateGray3", fill="aliceBlue")
        draw_rectangle(canvas, 203, 100, 223, 102, fill="black")
        draw_rectangle(canvas, 208, 100, 218, 110, fill="black")
        draw_line(canvas, 212, 95, 220, 95, width=2, fill="orange")
        draw_rectangle(canvas, 212, 79, 214, 81, fill="black")
        draw_rectangle(canvas, 212, 62, 214, 64, fill="black")
        draw_line(canvas, 205, 79, 195, 85, width=2, fill="brown")
        draw_line(canvas, 220, 79, 230, 85, width=2, fill="brown")

    def draw_name(canvas):
        draw_text(canvas, 750, 25, "Jacob Hale", fill="black")


    def draw_grid(canvas, width, height, interval, color="black"):
        # Draw a vertical line at every x interval.
        label_y = 15
        for x in range(interval, width, interval):
            draw_line(canvas, x, 0, x, height, fill=color)
            draw_text(canvas, x, label_y, f"{x}", fill=color)

        # Draw a horizontal line at every y interval.
        label_x = 15
        for y in range(interval, height, interval):
            draw_line(canvas, 0, y, width, y, fill=color)
            draw_text(canvas, label_x, y, f"{y}", fill=color)
    # Call the main function so that
    # this program will start executing.
    main()


elif piece == 3:
    def main():
        # Width and height of the scene in pixels
        scene_width = 800
        scene_height = 500

        # Call the start_drawing function in the draw2d.py
        # library which will open a window and create a canvas.
        canvas = start_drawing("Scene", scene_width, scene_height)

        # Call your drawing functions such
        # as draw_sky and draw_ground here.
        draw_ground(canvas, scene_width, scene_height)
        draw_stream(canvas)
        draw_sky(canvas, scene_width, scene_height)
        draw_mountains(canvas)
        draw_house(canvas)
        draw_path(canvas)
        draw_chimney(canvas)
        draw_trees(canvas)
        draw_name(canvas)
        
        # draw_grid(canvas, scene_width, scene_height, 50)
        
        # Call the finish_drawing function
        # in the draw2d.py library.
        finish_drawing(canvas)


    # Define your functions such as
    # draw_sky and draw_ground here.
    def draw_sky(canvas, scene_width, scene_height):
        # Draw the sky and all objects in the sky
        # sky
        draw_rectangle(canvas, 0, scene_height / 2.5, scene_width, scene_height, width = 0, fill="gold1")
        # sun
        draw_oval(canvas, 600, 325, 750, 475, width = 0, fill="yellow2")
        # clouds
        for _ in range(5):
            rand_x = random.randint(-50, 850)
            rand_y = random.randint(350, 550)
            draw_oval(canvas, rand_x, rand_y, rand_x + random.randint(100, 175), rand_y + random.randint(35, 75), width = 0, fill="papayaWhip")
        # cloud left
        # draw_oval(canvas, 50, 325, 150, 400, width = 0, fill="lavenderBlush1")
        # draw_oval(canvas, 100, 350, 300, 450, width = 0, fill="lavenderBlush1")
        # draw_oval(canvas, 100, 425, 200, 475, width = 0, fill="lavenderBlush1")
        # # cloud right
        # draw_oval(canvas, 525, 375, 675, 425, width = 0, fill="lavenderBlush1")
        # draw_oval(canvas, 475, 350, 600, 400, width = 0, fill="lavenderBlush1")
        # birds
        for _ in range(4):
            lx_start = random.randint(50, 750)
            ly_start = random.randint(350, 475)
            lx_next = lx_start + random.randint(10, 30)
            ly_next = ly_start + random.randint(15, 30)

            wing = random.randint(5, 15)
            widths = random.randint(2,3)
            rx_start = lx_next
            ry_start = ly_start
            rx_next = rx_start + (lx_next - lx_start) 
            ry_next = ly_next

            draw_arc(canvas, lx_start, ly_start, lx_next, ly_next, start=0, extent=180 - wing, width=widths)
            draw_arc(canvas, rx_start, ry_start, rx_next, ry_next, start=wing, extent=180, width=widths)
        # bird lower
        # draw_arc(canvas, 400, 400, 435, 425, start=0, extent=165, width = 3)
        # draw_arc(canvas, 435, 400, 470, 425, start=15, extent=180, width = 3)
        # # bird upper
        # draw_arc(canvas, 450, 415, 475, 440, start=0, extent=155, width = 2)
        # draw_arc(canvas, 475, 415, 500, 440, start=15, extent=180, width= 2)
        # # bird small
        # draw_arc(canvas, 425, 450, 440, 470, start=10, extent=180)
        # draw_arc(canvas, 440, 450, 455, 470, start=-10, extent=170)

    def draw_ground(canvas, scene_width, scene_height):
        # ground
        draw_rectangle(canvas, 0, 0, scene_width, scene_height / 2.5, outline = "", fill = "khaki1")
        # bushes
        for _ in range(15):
            rand_x = random.randint(0, 800)
            rand_y = random.randint(0, 200)
            colors = ["burlywood4", "khaki4", "goldenrod4"]
            draw_oval(canvas, rand_x, rand_y, rand_x + 8, rand_y + 8, outline="", fill=random.choice(colors))

    def draw_stream(canvas):
        # stream
        draw_arc(canvas, 525, 200, 675, 125, start=90, extent=-180, width=18, outline="darkKhaki")
        draw_arc(canvas, 500, 125, 700, 0, start=90, extent=180, width=18, outline="darkKhaki")
        # pond
        draw_oval(canvas, 475, -50, 775, 50, width=0, fill="darkKhaki")

    def draw_house(canvas):
        # house
        draw_oval(canvas, 0, 25, 225, 125, outline="", fill="bisque4")
        draw_rectangle(canvas, 25, 50, 175, 125, width=1, outline="black", fill="saddleBrown")
        draw_polygon(canvas, 175, 50, 200, 100, 200, 175, 175, 125, width=0, outline="black", fill="tan4")
        # draw_polygon(canvas, 175, 50, 175, 125, 200, 100, 200, 175, width=0)
        draw_polygon(canvas, 175, 125, 200, 175, 185, 180, width=1, outline="black", fill="tan4")
        draw_polygon(canvas, 172, 100, 185, 180, 34, 180, 21, 100, width=1, outline="black", fill="burlywood4")

    def draw_chimney(canvas):
        draw_rectangle(canvas, 50, 180, 65, 200, fill="brown4")
        
        
    def draw_mountains(canvas):
        draw_polygon(canvas, -100, 200, 900, 200, random.randint(550, 850), random.randint(275, 350), 550, 275, random.randint(300, 550), random.randint(275, 350), 300, 275, random.randint(0, 225), random.randint(275, 350), outline="", fill="sienna")

    def draw_path(canvas):
        x_start = 200
        y_start = 75
        colors = ["sienna4", "orangered4", "sandyBrown", "tan4"]
        for _ in range(40):
            draw_oval(canvas, x_start, y_start, x_start + 10, y_start + 10, outline="", fill=random.choice(colors))
            x_start += random.randint(15, 20)
            y_start += random.randint(-5, 5)

    def draw_trees(canvas):
        for _ in range(13):
            x_start = random.randint(225, 800)
            y_start = random.randint(0, 175)
            x_next = x_start
            y_next = y_start + random.randint(30, 50)
            branch1 = random.randint(y_start + 15, y_next)
            branch2 = random.randint(y_start + 15, y_next)
            draw_line(canvas, x_start, y_start, x_next, y_next, width=4, fill="paleGreen4")
            draw_line(canvas, x_start, branch1, x_start + 7, branch1, width=4, fill="paleGreen4")
            draw_line(canvas, x_start, branch2, x_start - 7, branch2, width=4, fill="paleGreen4")

    def draw_name(canvas):
        draw_text(canvas, 750, 25, "Jacob Hale", fill="black")

    def draw_grid(canvas, width, height, interval, color="black"):
        # Draw a vertical line at every x interval.
        label_y = 15
        for x in range(interval, width, interval):
            draw_line(canvas, x, 0, x, height, fill=color)
            draw_text(canvas, x, label_y, f"{x}", fill=color)

        # Draw a horizontal line at every y interval.
        label_x = 15
        for y in range(interval, height, interval):
            draw_line(canvas, 0, y, width, y, fill=color)
            draw_text(canvas, label_x, y, f"{y}", fill=color)
    # Call the main function so that
    # this program will start executing.
    main()