'''
Python Assignment: Cam Project
Done by: Hongliang
'''

# install and / or import modules
modules = ["sys", "os", "json", "math", "turtle", "time", "itertools", "click"]
for module in modules:
    try:
        globals()[module] = __import__(module)
    except:
        os.system("py -m pip install "+ module)
        globals()[module] = __import__(module)

# helper function to slow down and view turtle movements (for debugging)
def watch_turtle():
    myScreen.tracer(True,1)
    for t in myScreen.turtles():
        t.speed("slowest")
        t.showturtle()

# plot gridlines and label axes
def plot_axis(pos_x, pos_y, scale):
    rad = itertools.cycle(("0","π/6","π/3","π/2","2π/3","5π/6","π","7π/6","4π/3","3π/2","5π/3","11π/6","2π"))
    t = myTurtle
    t.pensize(1)
    #plot x-axis
    move_turtle(pos_x, pos_y, 90, color = "lightgreen")
    for _ in range(37):
        t.seth(90)
        t.fd(360*scale)
        t.bk(360*scale)
        if _%3 == 0:
            t.penup()
            t.seth(270)
            t.fd(30)
            t.color("black")
            if angle_unit == "degrees":
                t.write(f"{_*10}",align = "center", font = ("Lemon", 8, "normal"))
            else:
                t.write(f"{next(rad)}",align = "center", font = ("Lemon", 8, "normal"))
            t.color("lightgreen")
            t.rt(180)
            t.fd(30)
            t.pendown()
        t.seth(0)
        t.fd(10*scale)
        if _ == 18:
            t.penup()
            t.seth(270)
            t.fd(60)
            t.color("black")
            if angle_unit == "degrees":
                t.write("Cam Angle in Degrees [ ° ]",align = "center", font = ("Lemon", 8, "normal"))
            else:
                t.write("Cam Angle in Radians [ rad ]",align = "center", font = ("Lemon", 8, "normal"))
            t.color("lightgreen")
            t.rt(180)
            t.fd(60)
            t.pendown()
        t.rt(270)
            
    #plot y-axis
    move_turtle(pos_x, pos_y+360*scale+10, 0, color = "black")
    t.color("black")
    t.write("Follower Displacement [ cm ]",align = "center", font = ("Lemon", 8, "normal"))
    move_turtle(pos_x, pos_y+360*scale, 0, color = "lightgreen")
    for i in range(10):
        t.penup()
        t.rt(90)
        t.fd(10)
        t.color("black")
        t.write(f"{int(L - i*L/10)} ", align = "right", font = ("Lemon", 8, "normal"))
        t.color("lightgreen")
        t.rt(180)
        t.fd(10)
        t.pendown()
        t.rt(90)
        t.fd(360*scale)
        t.bk(360*scale)
        t.rt(90)
        t.fd(36*scale)
        t.lt(90)

# function to add a rectangle anywhere on the screen
def draw_button(pos_x, pos_y, size, color):
    move_turtle(pos_x, pos_y)
    myTurtle.color("black", color)
    myTurtle.begin_fill()
    for _ in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
    myTurtle.end_fill()

# draw all buttons for each screen
def display_button(func_name): 
    global current_func
    current_func = func_name
    if func_name == "preview_screen":
        draw_button(GRAPH_X, GRAPH_Y, GRAPH_SIZE, GRAPH_COLOR)
        myTurtle.penup()
        myTurtle.seth(0)
        myTurtle.fd(GRAPH_SIZE/2)
        myTurtle.write("GRAPH", align = "Center", font = ("Lemon", 12, "normal"))
        draw_button(CAM_X, CAM_Y, CAM_SIZE, CAM_COLOR)
        myTurtle.penup()
        myTurtle.seth(0)
        myTurtle.fd(CAM_SIZE/2)
        myTurtle.write("Cam", align = "Center", font = ("Lemon", 12, "normal"))
    if func_name in ("plot_screen", "preview_screen"):
        draw_button(ANGLE_X, ANGLE_Y, ANGLE_SIZE, ANGLE_COLOR)
        myTurtle.penup()
        myTurtle.seth(0)
        myTurtle.fd(ANGLE_SIZE*3/4)
        myTurtle.write("Change Angle", align = "Center", font = ("Lemon", 12, "normal"))
    draw_button(END_X, END_Y, END_SIZE, END_COLOR)
    myTurtle.penup()
    myTurtle.seth(0)
    myTurtle.fd(END_SIZE/2)
    myTurtle.seth(270)
    myTurtle.fd(END_SIZE*3/4)
    myTurtle.write("End", align = "Center", font = ("Lemon", 12, "normal"))
    draw_button(BACK_X, BACK_Y, BACK_SIZE, BACK_COLOR)
    myTurtle.penup()
    myTurtle.seth(0)            
    myTurtle.fd(BACK_SIZE/2)
    myTurtle.seth(270)
    myTurtle.fd(BACK_SIZE*3/4)
    myTurtle.write("Back", align = "Center", font = ("Lemon", 12, "normal"))
    myScreen.onclick(mouse_click)

# cam profile and graph is displayed
# scale is set to 1 for each view, would be adjusted for enlarged views
def preview_screen(myTurtle):
    scale = 1
    pos_x, pos_y = (0, 0)

    plot_axis(pos_x, pos_y, scale)
    move_turtle(pos_x, pos_y)
    class_.plot_s(pos_x, pos_y, scale)

    scale = 1
    pos_x, pos_y = (-200, -200)
    class_.draw_cam(pos_x, pos_y, scale)
    class_.draw_follower(pos_x, pos_y)
    display_button(sys._getframe().f_code.co_name)

# define button coordinates and color
# will be used in both the drawing of button and checking whether button is clicked
GRAPH_X, GRAPH_Y, GRAPH_SIZE, GRAPH_COLOR = [ -70,  300,  20, "green"]
ANGLE_X, ANGLE_Y, ANGLE_SIZE, ANGLE_COLOR = [ 320, -100,  20, "dodger blue"]
CAM_X, CAM_Y, CAM_SIZE, CAM_COLOR         = [ -70, -300,  20, "blue" ]
END_X, END_Y, END_SIZE, END_COLOR         = [ 320, -150,  50, "red"  ]
BACK_X, BACK_Y, BACK_SIZE, BACK_COLOR     = [-350,  370,  50, "pink" ]

# defines which button is active and what program does for each button press
def mouse_click(x, y):
    global angle_unit

    GRAPH_X0, GRAPH_Y1, GRAPH_X1, GRAPH_Y0 = (GRAPH_X, GRAPH_Y, GRAPH_X + GRAPH_SIZE, GRAPH_Y - GRAPH_SIZE)
    ANGLE_X0, ANGLE_Y1, ANGLE_X1, ANGLE_Y0 = (ANGLE_X, ANGLE_Y, ANGLE_X + ANGLE_SIZE, ANGLE_Y - ANGLE_SIZE)
    CAM_X0, CAM_Y1, CAM_X1, CAM_Y0 = (CAM_X, CAM_Y, CAM_X + CAM_SIZE, CAM_Y - CAM_SIZE)
    END_X0, END_Y1, END_X1, END_Y0 = (END_X, END_Y, END_X + END_SIZE, END_Y - END_SIZE)
    BACK_X0, BACK_Y1, BACK_X1, BACK_Y0 = (BACK_X, BACK_Y, BACK_X + BACK_SIZE, BACK_Y - BACK_SIZE)
    
    if GRAPH_X0 <= x <= GRAPH_X1 and GRAPH_Y0 <= y <= GRAPH_Y1 and current_func == "preview_screen":
        getscreen(plot_screen, "AliceBlue")
    elif CAM_X0 <= x <= CAM_X1 and CAM_Y0 <= y <= CAM_Y1 and current_func == "preview_screen":
        getscreen(class_.animation, "chartreuse")
    elif END_X0 <= x <= END_X1 and END_Y0 <= y <= END_Y1:
        myScreen.bye()
        return
    elif BACK_X0 <= x <= BACK_X1 and BACK_Y0 <= y <= BACK_Y1 and current_func == "preview_screen":
        myScreen.clear()
        main()
    elif BACK_X0 <= x <= BACK_X1 and BACK_Y0 <= y <= BACK_Y1:
        myFollower.hideturtle()
        getscreen(preview_screen, "beige")
    elif ANGLE_X0 <= x <= ANGLE_X1 and ANGLE_Y0 <= y <= ANGLE_Y1 and current_func == "preview_screen":
        angle_unit = next(choose_angle)
        getscreen(preview_screen, "beige")
    elif ANGLE_X0 <= x <= ANGLE_X1 and ANGLE_Y0 <= y <= ANGLE_Y1 and current_func == "plot_screen":
        angle_unit = next(choose_angle)
        getscreen(plot_screen, "AliceBlue")
    myScreen.tracer(True)
    myScreen.tracer(False)

# enlarged view of graph is displayed
def plot_screen(myTurtle):
    scale = 1.9
    pos_x, pos_y = -370, -320
    plot_axis(pos_x, pos_y, scale)

    move_turtle(pos_x, pos_y)
    class_.plot_s(pos_x, pos_y, scale)

    display_button(sys._getframe().f_code.co_name)

# this function reprompts user if input is not from a list of allowed results
def valid_input(title, prompt, allowed):
    while True:
        user_input = myScreen.textinput(title, prompt)
        if user_input.lower() in allowed:
            return user_input

# this function helps to "pick up" myTurtle and place it anywhere on the screen
def move_turtle(valx=0, valy=0, heading_dir = 0, color="black"):
    myTurtle.penup()
    myTurtle.color(color)
    myTurtle.goto(valx, valy)
    myTurtle.setheading(heading_dir)
    myTurtle.pendown()

# this function helps to "pick up" myFollower and place it anywhere on the screen
def move_follower(valx=0, valy=0, heading_dir = 0, color="black"):
    myFollower.penup()
    myFollower.color(color)
    myFollower.goto(valx, valy)
    myFollower.setheading(heading_dir)
    myFollower.pendown()

# this is a class that uses user input to define cam parameters and perform multiple operations
class Cam:
    # cycles through slope states and well as colors when called
    choose_slope = itertools.cycle(("rise","return"))
    choose_color = itertools.cycle(("blue","red","brown","hotpink"))
    slope = None
    s = 0

    # takes in data from text file
    def __init__(self, data):
        if input_choice == 'd':
            global L
            self.rb = data["rb"]
            self.ro = data["ro"]
            self.L = data["L"]
            L = self.L
            self.segment_list = data["segment_list"]
            self.n = len(self.segment_list)

    # main screen used for handling user input and displaying details for each segment
    def input_screen(self, myTurtle):
        i = 0
        turtle_x = -370
        turtle_y = 200
        remaining_duration = 360
        prompt_rb = "Base Radius, rb: "
        prompt_ro = "Follower Radius, ro: "
        prompt_n = "Please choose the number of segments: "
        prompt_dur = "Please choose the duration for Segment {i}"
        
        myDict = {'d' :"Dwell",
                  'c' :"Cycloidal",
                  'h' :"Harmonic",
                  'a' :"Parabolic",
                  'c1':"Cubic",
                  'c2':"Cubic Alternative",
                  'dh':"Double Harmonic",
                  'n1':"3-4-5 Polynomial",
                  'n2':"4-5-6-7 Polynomial",
                  'u' :"Uniform"}
        allowed_char = list(myDict.keys())
        
        self.rb = int(myScreen.numinput("Defining Cam parameters", prompt_rb, 80, 10, 90))
        self.ro = int(myScreen.numinput("Defining Cam parameters", prompt_ro, 12, 1))

        move_turtle(turtle_x,turtle_y)
        myTurtle.penup()
        myTurtle.write(prompt_n, move = True, font=myFont)
        self.n = int(myScreen.numinput("Defining segment parameters", prompt_n, 2, 1, 6))
        myTurtle.write(self.n, font = myFont)

        move_turtle(turtle_x,turtle_y - 30)
        myTurtle.write(f"\nPlease choose the type of motion for each segment:", font = myFont)

        for index,(key,value) in enumerate(myDict.items()):
            move_turtle(turtle_x, turtle_y - 30 * (index+2))
            myTurtle.write(f"\n\n\t{key}: {value}", font = myFont)


        self.segment_list = []
        for segment_num in range(1, self.n +1):
            move_turtle(turtle_x, turtle_y - 320 - 45*segment_num)
            myTurtle.write(f"Segment{segment_num}:", font=myFont)

            type_ = valid_input(title = f"Segment {segment_num}: Type",
                                prompt = f"Pick an answer from {allowed_char}",
                                allowed = allowed_char).lower() 
            myTurtle.write(f"\t\t{myDict[type_]}", font=myFont)

            if segment_num != self.n:
                duration = int(myScreen.numinput(title="Defining segment parameters",
                                             prompt = f"Please choose the duration for Segment {segment_num}",
                                             default = 360/self.n,
                                             minval = 0,
                                             maxval = remaining_duration)) #cannot exceed 360 degrees
                if segment_num == 1:
                    starting_duration = 0
                else:
                    starting_duration += duration
                remaining_duration -= duration
            else:
                starting_duration += duration
                duration = remaining_duration
                
            if segment_num == self.n:
                remaining_duration = 0
            myTurtle.write(f"\t\t\t\t{starting_duration} to {360 - remaining_duration}", font=myFont)
            
            self.segment_list.append((type_, starting_duration, duration))

            num_dwell = sum(x.count('d') for x in self.segment_list)
            num = self.n - num_dwell
            if segment_num == self.n-1 and num%2 == 0:
                allowed_char.remove('d')
            elif segment_num == self.n-1 and num%2 == 1:
                allowed_char = ['d']
            if segment_num == self.n:
                time.sleep(1)
                print(self.segment_list)

    # plotting cam displacement graph
    def plot_s(self, pos_x, pos_y, scale):
        self.L = 360  * scale

        # this is the main looping function used multiple times when handling data
        # loop for each segment
        for segment_num in range(self.n):
            # alternate the line color
            myTurtle.color(next(self.choose_color))

            # split the data and assign the type of curve, initial angle, and beta
            self.type_, self.angle_i, self.B = self.segment_list[segment_num]
            self.angle_f = self.angle_i + self.B

            # automatically define rise and return when type of curve is not dwell          
            if self.type_ != "d":
                self.slope = next(self.choose_slope)

            # for each angle from 0 to 360 degrees
            for self.theta in range(self.angle_i, self.angle_f + 1):
                self.theta_slope()

                # calculate cam displacement based on type of curve
                self.eqn_s_v2()

                # draw curve based on cam displacement vs angle
                myTurtle.goto(pos_x + self.theta * scale, pos_y + self.s)
                myTurtle.pendown()
            myTurtle.color("black")
            myTurtle.seth(270)

            # draw dotted lines to x-axis
            if segment_num != self.n-1 and myTurtle.ycor()!=0 and myTurtle.ycor()!=-320:
                for i in range(45):
                    myTurtle.fd(8*scale)
                    if i % 2 == 0:
                        myTurtle.penup()
                    if i % 2 == 1:
                        myTurtle.pendown()
                myTurtle.penup()
                myTurtle.sety(pos_y+self.s)

    # calculate cam displacement (depreciated)  
    def eqn_s(self):
        L = self.L
        B = self.B
        if      self.type_ == 'c':
                self.s = L * (self.cond/B - (1/(2*math.pi)) * math.sin(math.radians(self.cond * 360 / B)))
        elif    self.type_ == 'h':
                self.s = L/2*(1 - math.cos(math.radians(self.cond * 180 / B))) 
        elif    self.type_ == 'u':
                self.s = L / B * self.cond

    # calculate cam displacement for each type of curve     
    def eqn_s_v2(self):
        L = self.L
        B = self.B
        if self.type_ == 'a':
            # for some curve, half of the curve is defined by one equation while the other half is defined by another to achieve a smoother gradient
            if self.cond < (B/2):
                self.s = 2*L* (self.cond / B)** 2
            else:
                self.s = L*(1-2*(1-(self.cond / B))**2)
        elif self.type_ == 'h':
            self.s = L * (1- math.cos(math.pi*self.theta/B))/2
        elif self.type_ == 'c':
            self.s = L*(self.cond/B - math.sin(2*math.pi*self.cond/B)/(2*math.pi))
        elif self.type_ == 'u':
            self.s = L / B * self.cond
        elif self.type_ == 'p':
            if self.cond < B/2:
                self.s = 2*L*(self.cond/B)**2
            else:
                self.s = L*(1-2*(1-self.cond/B)**2)
        elif self.type_ == 'cu':
            if self.cond < B/2:
                self.s = 4*L*(self.cond/B)**3
            else:
                self.s = L*(1-4*(1-self.cond/B)**3)
        elif self.type_ == 'pc':
            self.s = L*(self.cond/B)**2 * (3-2*self.cond/B)
        elif self.type_ == 'dh':
            self.s = L/2*(1-math.cos(math.pi*self.cond/B)-(1-math.cos(2*math.pi*self.cond/B))/4)
        elif self.type_ == 'n1':
            self.s = L*(self.cond/B)**3*(10-15*self.cond/B+6*(self.cond/B)**2)
        elif self.type_ == 'n2':
            self.s = L*(self.cond/B)**4*(35-84*self.cond/B+70*(self.cond/B)**2-20*(self.cond/B)**3)

    # define self.cond as the angle difference which varies from rise to run
    def theta_slope(self):
        if      self.slope == "rise":
                self.cond = (self.theta - self.angle_i)
        elif    self.slope == "return":
                self.cond = (self.angle_f - self.theta)

    # draws the cam profile on the preview and cam screens
    def draw_cam(self, pos_x, pos_y, scale, angle=int(0)):
        self.L = self.rb
        myFollower.penup()
        myFollower.goto(0,0)

        move_turtle(pos_x + self.rb, pos_y)
        myTurtle.penup()
        myTurtle.color("darkorchid")
        myTurtle.begin_fill()
        for segment_num in range(self.n):
            self.type_, self.angle_i, self.B = self.segment_list[segment_num]
            self.angle_f = self.angle_i + self.B
            if self.type_ != 'd':
                self.slope = next(self.choose_slope)
            for self.theta in range(self.angle_i, self.angle_f + 1):
                self.theta_slope()
                self.eqn_s_v2()

                # draws out the cam profile based on these equations
                cam_x = (self.rb+self.s)*math.cos(math.radians(self.theta + angle)) * scale
                cam_y = (self.rb+self.s)*math.sin(math.radians(self.theta + angle)) * scale
 
                myTurtle.goto(pos_x + cam_x, pos_y + cam_y)
                myTurtle.pendown()

                # labels the cam profile
                if scale == 1 and self.theta == 90:
                    myTurtle.penup()
                    myTurtle.sety(pos_y+cam_y-60)
                    myTurtle.color("black")
                    myTurtle.write("Cam Profile", align = "Center", font = myFont)
                    myTurtle.sety(pos_y+cam_y)
                    myTurtle.pendown()
                    myTurtle.color("darkorchid")

                # during animation, moves the follower along the surface of the cam
                if scale == 2 and -3 <= myTurtle.xcor() <= 3 and myTurtle.ycor() > 0:
                    myFollower.showturtle()
                    myFollower.sety(myTurtle.ycor()+12)
        myTurtle.end_fill()
        myTurtle.penup()

        # labels the other components of the cam (base circle and pitch curve)
        if scale == 1:
            myTurtle.color("black")
            move_turtle(pos_x, pos_y - self.rb)
            myTurtle.pendown()
            
            # use different colors to differentiate different aspects of the cam profile
            myTurtle.color("green")
            myTurtle.circle(self.rb,270)
            myTurtle.write("   Base Circle", font = myFont)
            myTurtle.circle(self.rb,90)
            myTurtle.penup()
            for segment_num in range(self.n):
                self.type_, self.angle_i, self.B = self.segment_list[segment_num]
                self.angle_f = self.angle_i + self.B
                if self.type_ != 'd':
                    self.slope = next(self.choose_slope)
                for self.theta in range(self.angle_i, self.angle_f + 1):
                    self.theta_slope()
                    self.eqn_s_v2()

                    cam_x = (self.rb+self.s+self.ro)*math.cos(math.radians(self.theta + angle)) * scale
                    cam_y = (self.rb+self.s+self.ro)*math.sin(math.radians(self.theta + angle)) * scale

                    myTurtle.color("blue")
                    myTurtle.goto(pos_x + cam_x, pos_y + cam_y)
                    myTurtle.pendown()

                    if self.theta == 45:
                        myTurtle.write(" Pitch Curve", font = myFont)

    # this functions draws all the features of the follower for the cam profile on the preview screen
    def draw_follower(self, pos_x, pos_y):
        self.L = self.rb
        fol_x0 = pos_x + self.ro
        fol_y0 = pos_y 
        move_turtle(fol_x0, fol_y0)

        for segment_num in range(self.n):
            self.type_, self.angle_i, self.B = self.segment_list[segment_num]
            self.angle_f = self.angle_i + self.B
            if self.type_ != 'd':
                self.slope = next(self.choose_slope)
            for self.theta in range(self.angle_i, self.angle_f + 1):
                self.theta_slope()
                self.eqn_s_v2()

                # set starting position of follower
                if self.theta == 90:
                    fol_x1 = pos_x
                    fol_y1 = (self.rb+self.s)+ fol_y0
                    myFollower.goto(fol_x1, fol_y1)
                    myFollower.pendown()
                    height = 50
                    
        # draws the follower
        myFollower.color("blue")
        myFollower.begin_fill()
        myFollower.circle(self.ro)
        myFollower.end_fill()

        # draws the other features of the cam profile (follower holder)
        height = 300
        holder_x = fol_x1 - self.ro/4
        holder_y = fol_y1 + self.ro/2 + height
        rect(holder_x, holder_y, self.ro/2, height)
        width = self.ro
        gap = self.ro / 2
        rect(fol_x0 + gap, holder_y *3/4, width, height/4)
        rect(pos_x - 2* self.ro - gap, holder_y *3/4, width, height/4)

        # draws vertical dotted lines along the center axis
        myFollower.penup()
        myFollower.goto(pos_x, 370)
        myFollower.seth(270)
        myFollower.color("black")
        for i in range(75):
            myFollower.fd(10)
            if i % 2 == 0:
                myFollower.penup()
            if i % 2 == 1:
                myFollower.pendown()

        # draws horizontal dotted lines along the center axis
        myFollower.penup()
        myFollower.goto(-200-self.rb, -200)
        myFollower.seth(0)
        for i in range(int(self.rb/5)):
            myFollower.fd(10)
            if i % 2 == 0:
                myFollower.penup()
            if i % 2 == 1:
                myFollower.pendown()
        myFollower.penup()

    # uses draw_cam function to animation rotation by incrementing angle and clearing the screen after each screen
    def animation(self, myTurtle):
        if state == "test":
            rev = 1
        else:
            rev = 5
        scale = 2
        for _ in range(rev):
            self.draw_cam(0,0,scale)
            for angle in range(0,360+1):             
                myTurtle.clear()
                self.draw_cam(0,0,scale,angle)
                myScreen.update()
        display_button(sys._getframe().f_code.co_name) 

# this function is used to draw customisable rectangles on the screen. mainly used in cam profile
def rect(x,y,w,h):
    move_turtle(x,y)
    myTurtle.seth(0)
    myTurtle.pd()
    myTurtle.fillcolor("lightblue")
    myTurtle.begin_fill()
    for _ in range(2):
        myTurtle.fd(w)
        myTurtle.rt(90)
        myTurtle.fd(h)
        myTurtle.rt(90)
    myTurtle.end_fill()
    myTurtle.pu()

# this displays the introduction screen, showing an animation
def intro_screen(myTurtle):
    #initialize method
    myTurtle.pensize(3)
    move_turtle()
    myTurtle.color("yellow", "black")
    myTurtle.begin_fill()

    #lower wing (left)
    myTurtle.left(90);myTurtle.circle(50, 85);myTurtle.circle(15, 110);myTurtle.right(180);myTurtle.circle(30, 150);myTurtle.right(5);myTurtle.forward(10) 

    #upper wing (left)
    myTurtle.right(90);myTurtle.circle(-70, 140);myTurtle.forward(40);myTurtle.right(110);myTurtle.circle(100, 30);myTurtle.circle(30, 100);myTurtle.left(50);

    #head
    myTurtle.forward(50);myTurtle.right(145);myTurtle.forward(30);myTurtle.left(55);myTurtle.forward(20);myTurtle.left(55);myTurtle.forward(30)

    #upper wing (right)
    myTurtle.right(145);myTurtle.forward(50);myTurtle.left(50);myTurtle.circle(30, 100);myTurtle.circle(100, 30);myTurtle.right(90);myTurtle.right(20);myTurtle.forward(40);myTurtle.circle(-70, 140)

    #lower wing (right)
    myTurtle.right(90);myTurtle.forward(10);myTurtle.right(5);myTurtle.circle(30, 150);myTurtle.left(180);myTurtle.circle(15, 110);myTurtle.circle(50, 85)
    myTurtle.end_fill()    
    
    #set position
    myTurtle.penup()
    myTurtle.color("black")
    myTurtle.setpos(-240,-100)
    if state == "test":
        pass
    else:
        myScreen.tracer(True)
        turtle.delay(1)
        myTurtle.speed(3)
        myTurtle.showturtle() 
        rect(-270,-50,560,40)
        myTurtle.hideturtle()
        myScreen.update()
        myTurtle.seth(270) #0: right, 90: up
        myTurtle.fd(35)
        myTurtle.pendown()
        myScreen.tracer(False)
        
    #write introduction message
    myTurtle.write(" Welcome to HongLiang's Python Project!" ,font=("Verdana", 18, "bold"))

    if state == "test":
        pass
    else:
        time.sleep(1)
    turtle.delay(0)

# this function is used to clear the screen and load the next screen
def getscreen(screen, color = "white"):
    myTurtle.clear()
    myFollower.clear()
    myScreen.bgcolor(color)
    turtle.delay(0)
    screen(myTurtle)
    myScreen.tracer(True)
    myScreen.tracer(False)

# this function is used to define initial turtle parameters
def turtle_init():
    global myTurtle, myFollower, myScreen, myFont
    myTurtle = turtle.Turtle()
    myTurtle.speed("fastest")
    myTurtle.hideturtle()

    myFollower = turtle.Turtle()
    myFollower.speed("fastest")
    myFollower.hideturtle()
    myFollower.penup()
    myFollower.color("blue")
    myFollower.shape("circle")
    myFollower.shapesize(1,1)

    
    myScreen = turtle.Screen()
    myScreen.setup(800,800)
    myScreen.title("Cam Design")
    myScreen.tracer(False)

    myFont = ("Lemon", 18, "normal")
    
# defining global variables so it can be accessed by any function when needed
global angle_unit, choose_angle
# cycles through being in degrees and radians mode when called
choose_angle = itertools.cycle(("degrees","radians"))
angle_unit = next(choose_angle)

# this is the main program, where the code starts
def main():
    # defining global variables so it can be accessed by any function when needed
    global class_, state, L, input_choice

    # state is changed to "test" for testing, removing any animation, and inputting default parameters as needed
    state = ""

    # opens the txt file using json dictionary data handling
    with open('data.txt', 'r') as handle:
        data = [json.loads(line) for line in handle]

    #initialise turtle and force screen to appear on top
    turtle_init()
    rootwindow = myScreen.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

    # displays introduction screen
    getscreen(intro_screen, "lightblue")
    
    
    if state == "test":
        L = 80
        data_num = 1
    else:
        # user chooses whether they want to use data from txt file or use their own input conditions
        input_choice = valid_input(title = f"Choose choice of input: ",
                                prompt = f"Pick an answer from \nu: user input \nd: data",
                                allowed = ('u','d')).lower()
        if input_choice == 'u': 
            prompt_L = "Cam Displacement, L: "
            L  = int(myScreen.numinput("Defining Cam parameters", prompt_L, 10, 1))
            class_ = Cam(data[0])
            getscreen(class_.input_screen, "lightblue")
        else:
            data_num  = int(myScreen.numinput("Defining Cam Parameters: ", "Select data: ", 1, 1, len(data)))
            class_ = Cam(data[data_num - 1])
            
    # display main screen where cam and graph is displayed
    getscreen(preview_screen,"beige")
    return angle_unit, input_choice
    
    









main()
