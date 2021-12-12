'''
Remove if state == "test" section
Remove watch_turtle, cls, input_screen_test, plot_s, eqn_v
'''

modules = ["sys", "os", "json", "math", "turtle", "time", "itertools", "click"]
for module in modules:
    try:
        globals()[module] = __import__(module)
    except:
        os.system("py -m pip install "+ module)
        globals()[module] = __import__(module)


def cls():
    print("\n"*49)

def watch_turtle():
    myScreen.tracer(True)
    for t in myScreen.turtles():
        t.speed("slowest")
        t.showturtle()


# for L=10, this axis lets us see the variation from 0-10 in the y-axis
def plot_axis(pos_x, pos_y, scale, L=10):
    t = myTurtle
    t.pensize(1)
    #plot x-axis
    move_turtle(pos_x, pos_y, 90, color = "lightgreen")
    for _ in range(36):
        t.fd(360*scale)
        t.bk(360*scale)
        t.rt(90)
        t.fd(10*scale)
        t.lt(90)
    #plot y-axis
    move_turtle(pos_x, pos_y+360*scale, 0, color = "lightgreen")
    for _ in range(L):
        t.fd(360*scale)
        t.bk(360*scale)
        t.rt(90)
        t.fd(360*scale/L)
        t.lt(90)

def draw_button(pos_x, pos_y, size, color):
    move_turtle(pos_x, pos_y)
    myTurtle.color("black", color)
    myTurtle.begin_fill()
    for _ in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
    myTurtle.end_fill()

def display_button(func_name): 
    global current_func
    current_func = func_name
    if func_name == "preview_screen":
        draw_button(GRAPH_X, GRAPH_Y, GRAPH_SIZE, GRAPH_COLOR)
        draw_button(CAM_X, CAM_Y, CAM_SIZE, CAM_COLOR)
        draw_button(END_X, END_Y, END_SIZE, END_COLOR)
        draw_button(BACK_X, BACK_Y, BACK_SIZE, BACK_COLOR)
        myScreen.onclick(mouse_click)
    else:
        draw_button(END_X, END_Y, END_SIZE, END_COLOR)
        draw_button(BACK_X, BACK_Y, BACK_SIZE, BACK_COLOR)
        myScreen.onclick(mouse_click)

def preview_screen(myTurtle):
    scale = 1
    pos_x, pos_y = (0, 0)

    plot_axis(pos_x, pos_y, scale)
    move_turtle(pos_x, pos_y)
    class_.plot_s(pos_x, pos_y, scale)

    scale = 1
    pos_x, pos_y = (-200, -200)
    class_.draw_cam(pos_x, pos_y, scale)
    display_button(sys._getframe().f_code.co_name)

GRAPH_X, GRAPH_Y, GRAPH_SIZE, GRAPH_COLOR = [-300,  300, 200, "green"]
CAM_X, CAM_Y, CAM_SIZE, CAM_COLOR         = [ 100, -100, 200, "blue" ]
END_X, END_Y, END_SIZE, END_COLOR         = [ 320, -150,  50, "red"  ]
BACK_X, BACK_Y, BACK_SIZE, BACK_COLOR     = [-350,  370,  50, "pink" ]

def mouse_click(x, y):
    GRAPH_X0, GRAPH_Y1, GRAPH_X1, GRAPH_Y0 = (GRAPH_X, GRAPH_Y, GRAPH_X + GRAPH_SIZE, GRAPH_Y - GRAPH_SIZE)
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
    myScreen.tracer(True)
    myScreen.tracer(False)
    
def plot_screen(myTurtle):
    scale = 2
    pos_x, pos_y = -370, -370
    plot_axis(pos_x, pos_y, scale)

    move_turtle(pos_x, pos_y)
    class_.plot_s(pos_x, pos_y, scale)

    display_button(sys._getframe().f_code.co_name)

def valid_input(title, prompt, allowed):
    while True:
        user_input = myScreen.textinput(title, prompt)
        if user_input.lower() in allowed:
            return user_input

def move_turtle(valx=0, valy=0, heading_dir = 0, color="black"):
    myTurtle.penup()
    myTurtle.color(color)
    myTurtle.goto(valx, valy)
    myTurtle.setheading(heading_dir)
    myTurtle.pendown()

class Cam:
    choose_slope = itertools.cycle(("rise","return"))
    slope = None
    s = 0
    v = 0
    L = 32
    def __init__(self, data):
        self.rb = data["rb"]
        self.ro = data["ro"]
        self.segment_list = data["segment_list"]
    def input_screen_test(self,myTurtle):
        self.rb = 80 
        self.ro = 12
        self.n = 4
        self.segment_list = [('c', 0, 90), ('d', 90, 90), ('d', 180, 90), ('c', 270, 90)]
        json.dump(class_.__dict__, open("log.txt",'w'))

    def plot_s_v2(self, pos_x, pos_y, scale):
        self.L = 360 * scale
        
        for segment_num in range(self.n):
            self.type_, self.angle_i, self.B = self.segment_list[segment_num]
            Ls = [0, 180, 180, 360, 0]
            l_elem = Ls[segment_num]
            self.angle_f = self.angle_i + self.B
            if Ls[segment_num]-Ls[segment_num-1] > 0:
                self.slope = "rise"
            elif Ls[segment_num]-Ls[segment_num-1] < 0:
                self.slope = "return"
            print(self.slope)
            for self.theta in range(self.angle_i, self.angle_f + 1):
                self.theta_slope()
                self.eqn_s_v2(l_elem)

                myTurtle.goto(pos_x + self.theta * scale, pos_y + self.s)
                myTurtle.pendown()

    def eqn_s_v2(self, l_elem):
        L = l_elem
        B = self.B
        if      self.type_ == 'c':
                self.s = L * (self.cond/B - (1/(2*math.pi)) * math.sin(math.radians(self.cond * 360 / B)))
        elif    self.type_ == 'h':
                self.s = L/2*(1 - math.cos(math.radians(self.cond * 180 / B))) 
        elif    self.type_ == 'u':
                self.s = L / B * self.cond
        elif    self.type_ == 'p1':
                self.s = -L + (4*L/B) * self.cond + (-2*L/B**2) * self.cond**2
        
    def input_screen(self, myTurtle):
        i = 0
        turtle_x = -370
        turtle_y = 200
        remaining_duration = 360
        prompt_rb = "Base Radius, rb: "
        prompt_ro = "Follower Radius, ro: "
        prompt_n = "Please choose the number of segments: "
        prompt_dur = "Please choose the duration for Segment {i}"
        allowed_char = ['c','h','u','d']
        myDict = {'c':"cycloidal",
                  'h':"harmonic",
                  'u':"uniform",
                  'd':"dwell"}

        self.rb = int(myScreen.numinput("Defining Cam parameters", prompt_rb, 80, 10, 90))
        self.ro = int(myScreen.numinput("Defining Cam parameters", prompt_ro, 12, 1))
        
        move_turtle(turtle_x,turtle_y)
        myTurtle.penup()
        myTurtle.write(prompt_n, move=True, font=myFont)
        self.n = int(myScreen.numinput("Defining segment parameters", prompt_n, 2, 1, 6))
        myTurtle.write(self.n, font = myFont)

        move_turtle(turtle_x,turtle_y - 30)
        myTurtle.write(f"\nPlease choose the type of motion for each segment:", font = myFont)

        for index,(key,value) in enumerate(myDict.items()):
            move_turtle(turtle_x, turtle_y - 30 * (index+2))
            myTurtle.write(f"\n\n\t{key}: {value}", font = myFont)


        self.segment_list = []
        for segment_num in range(1, self.n +1):
            move_turtle(turtle_x, turtle_y - 180 - 50*segment_num)
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
                                             maxval = remaining_duration)) #cannot exceed after sum
                if segment_num == 1:
                    starting_duration = 0
                else:
                    starting_duration += duration
                remaining_duration -= duration
            else:
                starting_duration += duration
                duration = remaining_duration
                
            
            myTurtle.write(f"\t\t\t\t{starting_duration} to {duration}", font=myFont)
            self.segment_list.append((type_, starting_duration, duration))

            num_dwell = sum(x.count('d') for x in self.segment_list)
            num = self.n - num_dwell
            if segment_num == self.n-1 and num%2 == 0:
                allowed_char.remove('d')
            elif segment_num == self.n-1 and num%2 == 1:
                allowed_char = ['d']
            if segment_num == self.n:
                time.sleep(1)

    def plot_s(self, pos_x, pos_y, scale):
        self.L = 360 * scale
        
        for segment_num in range(self.n):
            self.type_, self.angle_i, self.B = self.segment_list[segment_num]
            self.angle_f = self.angle_i + self.B
            if self.type_ != "d":
                self.slope = next(self.choose_slope)
            for self.theta in range(self.angle_i, self.angle_f + 1):
                self.theta_slope()
                self.eqn_s()

                myTurtle.goto(pos_x + self.theta * scale, pos_y + self.s)
                myTurtle.pendown()
                
    def eqn_s(self):
        L = self.L
        B = self.B
        if      self.type_ == 'c':
                self.s = L * (self.cond/B - (1/(2*math.pi)) * math.sin(math.radians(self.cond * 360 / B)))
        elif    self.type_ == 'h':
                self.s = L/2*(1 - math.cos(math.radians(self.cond * 180 / B))) 
        elif    self.type_ == 'u':
                self.s = L / B * self.cond
        elif    self.type_ == 'p1':
                self.s = -L + (4*L/B) * self.cond + (-2*L/B**2) * self.cond**2

    def eqn_v(self):
        L = self.L
        B = self.B
        
        if      self.type_ == 'c':
                self.v = L * (1/B - ((360/B)/(2*math.pi)) * math.cos(self.cond * 360 / B))
        elif    self.type_ == 'h':
                self.v = L/2*(180/B)*math.sin(self.cond * 180 / B)
        elif    self.type_ == 'u':
                self.v = L/B
        elif    self.type_ == 'p1':
                self.v = (4*L/B) + 2*(-2*L/B**2)*self.cond        
                                
    def theta_slope(self):
        if      self.slope == "rise":
                self.cond = (self.theta - self.angle_i)
        elif    self.slope == "return":
                self.cond = (self.angle_f - self.theta)
        else:
                self.cond = self.theta

    def draw_cam(self, pos_x, pos_y, scale, angle=int(0)):
        self.L = self.rb

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
                self.eqn_s()

                cam_x = (self.rb+self.s)*math.cos(math.radians(self.theta + angle)) * scale
                cam_y = (self.rb+self.s)*math.sin(math.radians(self.theta + angle)) * scale
 
                myTurtle.goto(pos_x + cam_x, pos_y + cam_y)
                myTurtle.pendown()
                if scale == 2 and -3 <= myTurtle.xcor() <= 3 and myTurtle.ycor() > 0:
                    myFollower.showturtle()
                    myFollower.sety(myTurtle.ycor()+12)
        myTurtle.end_fill()
        
                    
    def animation(self, myTurtle):
        if state == "test":
            rev = 1
        else:
            rev = 2
        scale = 2
        for _ in range(rev):
            self.draw_cam(0,0,scale)
            for angle in range(0,360+1):             
                myTurtle.clear()
                self.draw_cam(0,0,scale,angle)
                myScreen.update()
        display_button(sys._getframe().f_code.co_name) #remove others conditions using global

def rect(x,y,w,h):
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

def intro_screen(myTurtle):
    #initialize method
    myTurtle.pensize(3)
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

    
    if state == "test":
        pass
    else:
        myScreen.tracer(True)
        time.sleep(1)
        myTurtle.reset()


    myScreen.bgcolor("beige")
    turtle.delay(0)
    
    
    myScreen.bgpic('python4.gif')
     #set position
    myTurtle.penup()
    myTurtle.color("black")
    myTurtle.setpos(-240,-100)
    if state == "test":
        pass
    else:
        turtle.delay(1)
        myTurtle.speed(3)
        myTurtle.showturtle() 
        rect(-200,0,560,40)
        myTurtle.hideturtle()
        myScreen.update()
        myTurtle.seth(270) #0: right, 90: up
        myTurtle.fd(35)
        myTurtle.pendown()
    # write 
    myTurtle.write(" Welcome to HongLiang's Python Project!" ,font=("Verdana", 18, "bold"))

    if state == "test":
        pass
    else:
        time.sleep(1)
    myScreen.bgpic("nopic")
    turtle.delay(0)






def getscreen(screen, color = "white"):
    myTurtle.clear()
    myScreen.bgcolor(color)
    turtle.delay(0)
    screen(myTurtle)
    myScreen.tracer(True)
    myScreen.tracer(False)







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
    



    

def main():
    global class_, state
##    class_ = Cam()
    cls()
    turtle_init()

    state = ""

    with open('data.txt', 'r') as handle:
        data = [json.loads(line) for line in handle]

    print(data)
    data_num =  2 #input("Select data: ")
    class_ = Cam(data[data_num - 1])
    
    getscreen(intro_screen, "darkblue")
    if state == "test":
        getscreen(class_.input_screen_test)
    else:
        getscreen(class_.input_screen, "lightblue")
    getscreen(preview_screen,"beige")
    
    
    









main()
