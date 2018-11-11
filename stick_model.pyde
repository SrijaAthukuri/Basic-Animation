def setup():
    global viewport;
    size(1500,1000);
    viewport=createGraphics(1000,800);
def draw():
    background(255);
    translate(mouseX,mouseY);
    fill(255,0,0);
    ellipse(330,200,50,100);
    fill(0,0,255);
    rect(300,250,60,150);
    fill(255,0,0);
    line(305,400,305,490);
    fill(255,0,0);
    line(355,400,355,490);
    fill(255,0,0);
    line(300,255,250,300);
    fill(255,0,0);
    line(360,255,410,300);
    
    # viewport.translate(mouseX-300,mouseY-300);
     
