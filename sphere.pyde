def setup():
    size(1000,800,P3D);
def draw():
    
    translate(mouseX,mouseY);
    rotate(360-mouseX);
    fill(250-mouseX,255,mouseY);
    sphere(150);
