function setup() {
    createCanvas(windowWidth, windowHeight, WEBGL);

    red = Math.random() * 255;
    green = Math.random() * 255;
    blue = Math.random() * 255;
  }
  
  function draw(){
    background(255);

    var locX = mouseX - height / 2;
    var locY = mouseY - width / 2;
    
    noStroke();

    ambientLight(60, 60, 60);
    pointLight(255, 255, 255, locX, locY, 100);

    push();
    translate(-100,0);
    rotateZ(frameCount * 0.01);
    rotateX(frameCount * 0.01);
    rotateY(frameCount * 0.01);
    ambientMaterial(red,green,blue);
    box(100,100);
    pop();

    push();
    translate(-300,0);
    rotateZ(frameCount * 0.01);
    rotateX(frameCount * 0.01);
    rotateY(frameCount * 0.01);
    ambientMaterial(red,green,blue);;
    ellipsoid(80);
    pop();

    push();
    translate(100,0);
    rotateZ(frameCount * 0.01);
    rotateX(frameCount * 0.01);
    rotateY(frameCount * 0.01);
    ambientMaterial(red,green,blue);
    torus(60,30);
    pop();

    push();
    translate(300,0);
    rotateZ(frameCount * 0.01);
    rotateX(frameCount * 0.01);
    rotateY(frameCount * 0.01);
    ambientMaterial(red,green,blue);
    cone(80,80);
    pop();
}