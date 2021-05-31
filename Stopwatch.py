# template for "Stopwatch: The Game"
import simplegui
# define global variables

integer= 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
A=range(0,10)
C=range(0,10)
D=range(0,10)
B=range(0,5)

def format(t):    
    r=t%10
    d=r
    D=str(d)
    n=t/10
    r1=n%10
    c=r1
    C=str(c)
    n1=n/10
    r2=n1%10
    b=r2
    B=str(b)
    n2=n1/10
    r3=n2%10
    a=r3
    A=str(a)
    return (A+":"+B+C+"."+D)
   
# define event handlers for buttons; "Start", "Stop", "Reset"
def start(): 
    timer.start()
    
def stop():
    timer.stop()
    
def reset():
    global integer
    integer=0

# define event handler for timer with 0.1 sec interval
def tick():
    global integer
    integer+=1
    return integer


# define draw handler
def draw(canvas):
    global integer
    canvas.draw_text(format(integer),[120,160],24 ,"White")
     
# create frame
frame=simplegui.create_frame("Stopwatch", 300,300)
timer=simplegui.create_timer(100, tick)
frame.add_button("start", start)
frame.add_button("stop", stop)
frame.add_button("reset", reset)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()