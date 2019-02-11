var canvas = document.querySelector('canvas');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var c = canvas.getContext('2d');

// Moving circles

//  Pick a random color
function pickColor() {
    red = Math.random() * 255;
    green = Math.random() * 255;
    blue = Math.random() * 255;
    alpha = 0.7;
    color = "rgb(" + red + "," + green + "," + blue + "," + alpha + ")";
    return color
}

//  Create Circle objects
function Circle(x,y, dx, dy, radius, color) {
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.radius = radius;
    this.color = color;
    
    this.draw = function () {
        c.beginPath();
        c.arc(this.x,this.y,this.radius,0,Math.PI * 2,false);
        c.fillStyle = color;
        c.fill();
    }
    
    this.update = function () {
        if (this.x > innerWidth || this.x < 0) {
            this.dx = -this.dx;
        }
        
        if (this.y > innerHeight || this.y < 0) {
            this.dy = -this.dy;
        }
        
        this.x += this.dx;
        this.y += this.dy;
        
        this.draw();
    }
    
}

//  Animate each of the circles in the array
function animate() {
    requestAnimationFrame(animate);
    c.clearRect(0,0,innerWidth,innerHeight);
    
    for (var i = 0; i< circleArray.length; i++) {
        circleArray[i].update();
    }
}

//  Initiate an array 
var circleArray = [];

// Create # amount of circles and append to list
for (var i = 0; i < 25; i++) {

    //      Hyperparameters
    var radius = 400;
    var x = Math.random() * innerWidth;
    var y = Math.random() * innerHeight;
    var dx = (Math.random() - 0.5) * 20;
    var dy = (Math.random() -0.5) * 20;
    var color = pickColor();
    
    circleArray.push(new Circle(x, y, dx, dy, radius, color));
}

//  Animate all the circles present in the array
animate();