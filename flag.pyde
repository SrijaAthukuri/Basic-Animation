
def setup():
    size(700,700)
    background(150)
    
    
def flag():
    #fill(255,0,0);
    stroke(255, 50, 0);
    strokeWeight(50)
    curve(200,250, 150, 150, 400,100 ,300, 50);
    line(150,150,150,200)
    line(400,100,400,150)
    curve(200,300,150,200,400,150,300,100);
    stroke(255);
    strokeWeight(50)
    curve(200,350,150,250,400,200,300,150);
    line(150,250,150,300)
    line(400,200,400,250)
    curve(200,400, 150, 300, 400,250 ,300, 200);
    stroke(0,255,0);
    strokeWeight(55);
    curve(200,455, 150, 350, 400,300 ,300, 255)
    line(150,350,150,400);
    line(400,300,400,350);
    curve(200,455,150,400,400,350,300,305)
    stroke(0,0,255)
    strokeWeight(5)
    ellipse(260,250,100,100)
    
def spokes():
    stroke(0,0,255)
    line(260,200,260,300);
    line(210,250,310,250);
    line(230,208,280,291);
    line(285,210,235,291);

def draw():
    flag()
    spokes()
