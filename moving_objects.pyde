#c=color(0,0,255);
x=200.0
y=90.0
xd=1.0
yd=1.0
x1=500.0
y1=500.0
speed=2.0

def setup():
    size(1000,800)

def display1():
    background(255);
    fill(0);
    rect(x1,y1,50,60);

def keyReleased():
  global x1,y1;
  if (key==CODED):
    if (keyCode==RIGHT):
          background(255);
          x1=x1+10;
          if(x1==750):
              x1=700;

    elif(keyCode==LEFT):
      background(255);
      x1=x1-10;
      if(x1==50):
          x1=100;
      
def move():
    global x,xd;
    x=x+(speed*xd);
    if(x>width or x<0):
      xd*=-1;
            

def move1():
    global y,yd;
    y=y+(speed*yd);
    if(y>height or y<0):
        yd*=-1;

    
    
def display():
    fill(255,0,0);
    ellipse(x,y,50,50);
    
def draw():   
    background(255);
    move();
    move1();
    display();
    keyReleased();
    display1();
