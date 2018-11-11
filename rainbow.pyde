def setup():
    size(600,600);
    background(60);
    noFill();
def draw():
    
    strokeWeight(random(30,70));
    stroke(random(255),random(255),random(255));
    rainbow_size=random(600,750);
    ellipse(600,600,rainbow_size,rainbow_size);
    
