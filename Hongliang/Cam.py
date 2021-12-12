#functions
def get_input():
    number_of_segments = input("Please choose the number of segments: ")
    type_of_curve = input("""
    Please choose the type of motion for each segment:
    a) constant acceleration
    b) simple harmonic 
    c) cycloidal
""")
    angle_of_segments = input("Please choose the angular range for each segment: ")



# use this for title screen with "Welcome to HongLiang's Python Project!" 
def batman():
    #initialize method
    #bat = turtle.Turtle()

    #size of pointer and pen
    bat.turtlesize(1, 1, 1)
    bat.pensize(3)

    #screen info
    wn = turtle.Screen()
    wn.bgcolor("dark blue")
    wn.title("BATMAN")

    #colour
    bat.color("yellow", "black")


    #begin filling color
    bat.begin_fill()

    #turn1
    bat.left(90)   # turn pointer direction to left of 90'
    bat.circle(50, 85) #draw circle of radius = 50 and 85'
    bat.circle(15, 110)
    bat.right(180) 

    #turn 2
    bat.circle(30, 150)
    bat.right(5)
    bat.forward(10) #draw forward line of 10 units

    #turn 3
    bat.right(90)
    bat.circle(-70, 140)
    bat.forward(40)
    bat.right(110)

    #turn 4
    bat.circle(100, 30)
    bat.circle(30, 100)
    bat.left(50)
    bat.forward(50)
    bat.right(145)

    #turn5
    bat.forward(30)
    bat.left(55)
    bat.forward(10)

    #reverse

    #turn 5
    bat.forward(10)
    bat.left(55)
    bat.forward(30)

    #turn 4

    bat.right(145)
    bat.forward(50)
    bat.left(50)
    bat.circle(30, 100)
    bat.circle(100, 30)

    #turn 3
    bat.right(90)
    bat.right(20)
    bat.forward(40)
    bat.circle(-70, 140)

    #turn 2
    bat.right(90)
    bat.forward(10)
    bat.right(5)
    bat.circle(30, 150)

    #turn 1
    bat.left(180)
    bat.circle(15, 110)
    bat.circle(50, 85)

    #end color filling
    bat.end_fill()



    #end the turtle method
    turtle.done()

#not sure what to use this for
def spinning():
    #window = Screen()
    window.tracer(1000) 
    window.bgcolor("black")
    
    def spiral():
        size = 1
        for _ in range(300):
            angie.forward(size)
            angie.right(91)
            size += 1

    # Turtle Angie
    #angie = Turtle(shape="turtle")
    angie.color("lightblue")
    angie.pensize(2)
    angie.hideturtle()
    angie.speed(0)  # slightly slower than brad

    while True:
        spiral()
        for angle in range(0,360+1):
            angie.up()
            angie.goto(0,0)
            angie.down()
            angie.clear()
            angie.setheading(angle)
            spiral()
            window.update()



def drawY(gap):
    posX = int(trtl.position()[0])

    trtl.forward(360)
    
    trtl.penup()
    trtl.setx(posX + gap)
    trtl.pendown()
    
    trtl.backward(360)

    trtl.penup()
    trtl.setx(posX + gap + gap)
    trtl.pendown()
        
def drawX(gap):
    posY = int(trtl.position()[1])

    trtl.forward(360)
    
    trtl.penup()
    trtl.sety(posY + gap)
    trtl.pendown()
    
    trtl.backward(360)

    trtl.penup()
    trtl.sety(posY + gap + gap)
    trtl.pendown()

# method to draw y-axis lines
def drawy(val):
     
    # line
    trtl.forward(300)
     
    # set position
    trtl.up()
    trtl.setpos(val,300)
    trtl.down()
     
    # another line
    trtl.backward(300)
     
    # set position again
    trtl.up()
    trtl.setpos(val+10,0)
    trtl.down()
     
# method to draw y-axis lines
def drawx(val):
     
    # line
    trtl.forward(300)
     
    # set position
    trtl.up()
    trtl.setpos(300,val)
    trtl.down()
     
    # another line
    trtl.backward(300)
     
    # set position again
    trtl.up()
    trtl.setpos(0,val+10)
    trtl.down()
     
# method to label the graph grid
def lab():
     
    # set position
    trtl.penup()
    trtl.setpos(155,155)
    trtl.pendown()
     
    # write 0
    trtl.write(0,font=("Verdana", 12, "bold"))
     
    # set position again
    trtl.penup()
    trtl.setpos(290,155)
    trtl.pendown()
     
    # write x
    trtl.write("x",font=("Verdana", 12, "bold"))
     
    # set position again
    trtl.penup()
    trtl.setpos(155,290)
    trtl.pendown()
     
    # write y
    trtl.write("y",font=("Verdana", 12, "bold"))

def rect(x,y,w,h):
    trtl.seth(0)
    trtl.pd()
    trtl.fillcolor("lightblue")
    trtl.begin_fill()
    for _ in range(2):
        trtl.fd(w)
        trtl.rt(90)
        trtl.fd(h)
        trtl.rt(90)
    trtl.end_fill()
    trtl.pu()

# if you do not have turtle, type "py -m pip install turtle" in your command prompt

number_of_segments = 0
type_of_curve = 'a'
angle_of_segments = 0



#code


def labels():
    trtl.color("light green")
    init(-10,-10,90)
    trtl.write(0,font=("Verdana", 12, "bold"))
    
    init(0,0,90)
    trtl.forward(360)
    trtl.write("Displacement",font=("Verdana", 12, "bold"))
    
    init(0,0,0)
    trtl.forward(360)
    trtl.write("Angle",font=("Verdana", 12, "bold"))
 
# labeling


def drawLine(a,b):
  trtl.penup()
  for x in range(100,300):
    y = a * x + b
    trtl.goto(x,y)
    trtl.pendown()

def plot_v(curve_type, L, angle_initial, angle_final):
    trtl.penup()
    for theta in range(angle_initial, angle_final +1):
        trtl.goto( theta, v(curve_type, L, angle_initial, angle_final, theta) )
        trtl.pendown()

def harmonic_rise_s(curve_type, L, angle_initial, angle_final, theta):
    if theta < angle_initial:
        return 0
    elif theta > angle_final:
        return 0
    else:
        return L / 2 * (1 - math.cos(math.radians(180*(theta-angle_initial)/(angle_final-angle_initial))))
def harmonic_return_s(curve_type, L, angle_initial, angle_final, theta):
    return L / 2 * (1 - math.cos(math.radians(180*(angle_final-theta)/(angle_final-angle_initial))))
def v(curve_type, L, angle_initial, angle_final, theta, w=100):
    return math.pi * w / (angle_final-angle_initial) * L / 2 * math.sin(math.radians(180*(theta-angle_initial)/(angle_final-angle_initial)))


def drawline(curve_type, L, angle_initial, angle_final):
    trtl.penup()
    for theta in range(angle_initial, angle_final +1):
        trtl.goto(theta, harmonic_rise_s(curve_type, L, angle_initial, angle_final, theta))
        trtl.pendown()
        
def plot_gridlines():
    # set position for Y lines
    init(0,0,90)
    # draw Y lines
    for i in range(18):
        drawY(10)
    # set position for X lines
    init(0,0,0)
    for i in range(18):
        drawX(10)
    labels() 
def plot_cam(theta, L, angle_initial, angle_final, curve_type = 'h', rb = 100):
    x = -(rb + harmonic_rise_s(curve_type, L, angle_initial, angle_final, theta))\
        *math.sin(theta) - v(curve_type, L, angle_initial, angle_final, theta, w=100) * math.cos(theta)
    y = (rb + harmonic_rise_s(curve_type, L, angle_initial, angle_final, theta))\
        * math.cos(theta) - v(curve_type, L, angle_initial, angle_final, theta, w=100) * math.sin(theta)
    return (x,y)
def plot_any(L, angle_initial, angle_final):
    trtl.penup()
    for theta in range(0, 360 +1):
        x,y = plot_cam(theta, L, angle_initial, angle_final)
        trtl.goto(x,y)
        trtl.pendown()







def formulas():
    if curve_type == "harmonic":
        s = L / 2 * (1 - math.cos( math.pi * (theta) / (angle_final - angle_initial)))





#external turtle functions
def move(valx, valy, heading_dir = 0):
    t.penup()
    t.goto(valx, valy)
    t.setheading(heading_dir)
    t.pendown()
    
def new_screen(color):
    sc.bgcolor(color)
    t.clear()
    turtle.delay(0)
    
def plot_axis():
    new_screen("white")
    t.color("lightgreen")
    graphX,graphY = 0, -200 + 200
    move(0, 0, 90)
    plotlines(36)
    move(0, 360, 0)
    plotlines(36)
    
    
def plotlines(num):
    for _ in range(num):
        t.fd(360)
        t.bk(360)
        t.rt(90)
        t.fd(10)
        t.lt(90)

## setting up the turtle
def turtle_init():
    global t
    t = turtle.Turtle()
    global sc
    sc = turtle.Screen()
    sc.setup(800,800)
    sc.title("Cam Design")
    sc.tracer(False)
    t.speed("fastest")
    t.hideturtle()
    ##sc.exitonclick()


















    
## importing modules
modules = ["os", "math", "turtle", "time", "itertools", "click"]
for module in modules:
    try:
        globals()[module] = __import__(module)
    except:
        os.system("py -m pip install "+ module)
        globals()[module] = __import__(module)
            
##turtle_init()
##plot_axis()
















class Cam():


    # constants
    scale = 8
    rb = 32 * scale
    ro = 12
    L = 360 #map L to 360 height
    w = 100
    choose_slope = itertools.cycle(("rise","return"))

    def __init__(self): # put some parameters in here: name
        self.n = 4
        self.s = 0
        self.dir = 0 #CCW
        self.theta = None
        self.lst = []
        self.prev = None #?
        self.cond = None
        self.slope = None
        self.B = None

# to speed things up (might not need)
##        fol = turtle.Turtle()
##        fol.speed("fastest")
##        fol.hideturtle()
##        fol.color("blue")
##        fol.penup()
##        fol.shape("circle")
##        fol.shapesize(1,1)
##        for i in range(self.n):
##            segment = input(f"type for segment {i+1}: ")
##            duration = int(input(f"duration for segment {i+1}: "))
##            self.dct[segment+str(i+1)] = duration 
##        self.lst = [('harmonic_rise', 120), ('dwell', 180), \
##                    ('harmonic_return', 300), ('dwell', 360)]
##        self.lst = [('dwell', 100), ('harmonic_rise', 160), \
##                    ('dwell', 210), ('harmonic_return', 360)]
    #temp: clear shell: remove this after testing
    def __repr__(self):
        return '\n'*100
    
    def harmonic_rise(self, angle_initial, angle_final): #assume harmonic rise
        return self.L / 2 * (1 - math.cos(math.radians(180*\
            (self.theta-angle_initial)/(angle_final-angle_initial))))
    def harmonic_return(self, angle_initial, angle_final):
        return self.L / 2 * (1 - math.cos(math.radians(180*\
            (angle_final-self.theta)/(angle_final-angle_initial))))
    def rise(self, angle_initial, angle_final):
        return self.L*(1-math.cos(math.radians(3*
                self.theta)-5*math.pi/3))
    def return_(self, angle_initial, angle_final):
        return self.L*(1-math.cos(12*math.pi/5-6/5*\
                math.radians(self.theta)))
    def plot_graph_old(self):
        trtl.penup()
        for j in range(self.n):
            for self.theta in range(0,360+1):
                cam_type = self.lst[j][0]
                duration = self.lst[j][1]
                if j == 0:
                    angle_initial = 0
                else:
                    angle_initial = self.lst[j-1][0]
                if cam_type == "harmonic_rise":
                    self.s = self.harmonic_rise(angle_initial, self.lst[j][1])
                    trtl.goto(self.theta, self.s)
                    if j == 0:
                        trtl.pendown()


    
    def harmonic(self, B,cond):
        self.s = L/2*(1 - math.cos(cond * 180 / B))

    def parabolic(self, B,cond):
        self.s = 2*L/B**2*self.cond**2

        function_dict = {"harmonic":    harmonic,
                     "cycloidal":   cycloidal,
                     "parabolic":   parabolic,
                     "uniform":     uniform}

    def find_s(self, cam_type, angle_initial, angle_final):
        if cam_type != "dwell":
                B = angle_final - angle_initial
                cond = theta_slope(self.slope)
                self.s = function_dict[cam_type](B, cond)
        
    def cam_s(self, cam_type, angle_initial, angle_final):
        if cam_type == "dwell":
            self.s = self.s # no change
        elif cam_type == "harmonic":
            self.s = self.harmonic_rise(angle_initial, angle_final)
        elif cam_type == "harmonic_return":
            self.s = self.harmonic_return(angle_initial, angle_final)


    def theta_slope(slope):
        if slope == "rise":
            return (theta - angle_initial)
        elif slope == "return":
            return (angle_final - theta)

    def plot_graph(self):
        plot_axis()
        t.color("black")
        t.penup()
        angle_initial = 0
        angle_final = 0
        
        for j in range(self.n):
            cam_type , duration, slope = self.lst[j]
            angle_final += duration
##            print(angle_initial, angle_final, duration)
            for self.theta in range(angle_initial,angle_final+1):
                self.cam_s(cam_type, angle_initial, angle_final)
                t.goto(self.theta, self.s)
                t.pendown()
            angle_initial += duration

            
    def plot_rb(self):
        trtl.penup()
        trtl.goto(0,-self.rb)
        trtl.pendown()
        trtl.circle(self.rb)
        
    def plot_cam(self, angle=0):
        trtl.color("black")
        trtl.penup()
        for j in range(self.n):
            if j == 0:
                angle_initial = 0
            else:
                angle_initial = self.lst[j-1][1]
            angle_final = self.lst[j][1]
            for self.theta in range(angle_initial,angle_final+1):
                cam_type = self.lst[j][0]
                if cam_type == "harmonic_rise":
                    self.s = self.harmonic_rise(angle_initial, angle_final)
                elif cam_type == "harmonic_return":
                    self.s = self.harmonic_return(angle_initial, angle_final) 
                trtl.goto((self.rb+self.s)*math.cos(math.radians(self.theta+ angle)),\
                          (self.rb+self.s)*math.sin(math.radians(self.theta+ angle)))
                if -3 <= trtl.xcor() <= 3 and trtl.ycor() > 0:
                    fol.showturtle()
                    fol.sety(trtl.ycor()+12)
                trtl.pendown()
    def animation(self):
        while True:
            self.plot_cam(0)
            for angle in range(0,360+1):             
                trtl.clear()
                self.plot_cam(angle)
##                sc.update()
    ## input screen
    def get_input(self):
        sc.clear()
        sc.bgcolor("cyan")
        
        height = 200
        move(-370,height)
        myFont = ("Verdana", 18, "bold")
        t.write("Please choose the number of segments: ", font = myFont)
        self.n = int(sc.numinput("Number of segments" , "Please choose the number of segments", 2, 1, 6))
        move(260,height)
        t.write(self.n, font = myFont)
        move(-400,height-200)
        t.write("""
        Please choose the type of motion for each segment:
            a) Constant acceleration
            b) Simple harmonic 
            c) Cycloidal
            d) Dwell
        """, font = myFont)

        myDict = {'a':"acceleration",
                  'b':"harmonic",
                  'c':"cycloidal",
                  'd':"dwell"}

        length = 360
        for i in range(1, self.n+1):
            move(-370,height -200 - 50*i) 
            t.write(f"Segment {i}:",font = myFont)
            type_input = self.valid_input(title = f"Segment {i}: Type",
                                     prompt = "Pick an answer from A to C",
                                     allowed = ('a', 'b', 'c', 'd'),
                                     default = 'd').lower()   
            t.write(f"\t\t{myDict[type_input]}",font = myFont)
            duration_input = int(sc.numinput(title = f"Segment {i}: Duration",
                                             prompt = f"Please choose the duration for Segment {i}",
                                             default = 360/self.n,
                                             minval = 0,
                                             maxval = length)) #cannot exceed after sum
            length -= duration_input
            t.write(f"\t\t\t\t{duration_input}",font = myFont)
            if type_input.lower() == 'd':
                self.lst.append(("dwell",duration_input,"")) #change to actual final or smth
            else:
                self.slope = next(self.choose_slope)
                self.lst.append((f"{myDict[type_input]}",duration_input,f"{self.slope}"))
        print(self.lst)
        self.plot_graph()

    def valid_input(self, title, prompt, allowed, default):
        while True:
            user_input = sc.textinput(title, prompt)
            if user_input.lower() in allowed:
                return user_input
            if user_input == "":
                return default
    
    

def user_input(correct=0, prompt=0):
    correct = ('a','h','c','d')
    prompt = print("""
    Please choose the type of motion for each segment:
        a) constant acceleration
        h) simple harmonic 
        c) cycloidal
        d) dwell
    """)
    type_of_curve = click.prompt('\n', type=click.Choice(correct, case_sensitive=False))
    return type_of_curve


            

#-------------------------------------




#user_input()

def main():
    hello = Cam()
    turtle_init()
    hello.get_input()
    hello.plot_cam()
main()

##sc.addshape("cam.gif")
##myImage = turtle.Turtle()
##myImage.speed(0) #so it will draw the image instantly
##myImage.shape("cam.gif") #give your object the image
##myImage.penup() #if you dont do this, it will draw a line
##myImage.goto(0,0) #give your image a location
##while True:
##  sc.update() #update your window

## # intro screen
##turtle_init()
####time.sleep(1)
##sc.bgcolor("beige")
##sc.bgpic('python4.gif')
### set position
##trtl = t
##trtl.penup()
##trtl.setpos(-240,-100)
##trtl.speed(3)
##trtl.showturtle() 
##rect(-200,0,560,40)
##trtl.hideturtle()
##sc.update()
##trtl.seth(270) #0: right, 90: up
##trtl.fd(35)
##trtl.pendown()
### write 0
##trtl.write(" Welcome to HongLiang's Python Project!" ,font=("Verdana", 18, "bold"))



##main()
##collect = [('Acceleration', 180), ('Harmonic', 180)]

### GUI: welcome
### input -> sc.textinput("NIM", "Name of first player:"), numinput, if reach end of shell, cls()
### display: plotlines, graph, cam - (relative) position on screen
### extract data from txt or excel
### plot with data
### next time: animation /
### plot("harmonic") -> if x: return x, if y return y
### myPen.write(equation, None, None, "14pt bold")
### split turtle for faster movement (async) first_init() -> speed, hide, color
### init change to move() -> pu, goto, pd
### screen.setworldcoordinates(-1000,-1000,1000,1000)
### turtle.bgcolor('midnight blue')
### square button to go back / exit
### check turtle code: trtl.speed("slowest");trtl.showturtle()
### turtle.exitonclick()
### input trtl in class as self.trtl
### labels: displacement, theta symbol, segment theta value, L, eqn at top, label segments "} dwell"
### screen.onclick() -> look for box coord if pressed restart
### sc.bye() -> screen to shell
### import modules -> install(['click,turtle'])


##B = angle_final-angle_initial
##
##uniform:    s = L / B * cond
##            v = L/B
##            a = 0
##            j = 0
##
##parabolic:  s = -L + (4*L/B) * cond + (-2*L/B**2) * cond**2
##return 1    v = (4*L/B) + 2*(-2*L/B**2)*cond
##rise 2      a = 2 * (-2*L/B**2)
##            j = 0
##
##parabolic:  s = 2*L/B**2*cond**2
##return 2    v = 4*L/B**2*cond
##rise 1      a = 4*L/B**2
##            j = 0
##
##harmonic:   s = L/2*(1 - math.cos(cond * 180 / B))
##            v = L/2*(180/B)*math.sin(cond * 180 / B)
##            a = L/2*(180/B)**2*math.cos(cond * 180 / B)
##            j = -L/2*(180/B)**3*math.sin(cond * 180 / B)
##                  
##cycloidal:  s = L * (cond/B - (1/(2*math.pi)) * math.sin(cond * 360 / B))
##            v = L * (1/B - ((360/B)/(2*math.pi)) * math.cos(cond * 360 / B) 
##            a = L * ((360/B)**2/(2*math.pi)) * math.sin(cond * 360 / B) 
##            j = L * ((360/B)**3/(2*math.pi)) * math.cos(cond * 360 / B)
##
##if _ == "rise": cond = (theta - angle_initial)
##elif _ == return:  cond = (angle_final - theta)
        
