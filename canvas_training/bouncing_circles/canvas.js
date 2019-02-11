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
function Circle(x,y, vx, vy, radius, color) {
    this.x = x;
    this.y = y;
    this.vx = vx;
    this.vy = vy;
    this.radius = radius;
    this.color = color;
    
    this.draw = function () {
        c.beginPath();
        c.arc(this.x,this.y,this.radius,0,Math.PI * 2,false);
        c.fillStyle = color;
        c.fill();
    }
    
    this.update = function () {
        this.vy += g;
        
        if (this.x > (innerWidth - radius) || this.x < radius) {
            this.vx = -this.vx;
        }
        
        if (this.y > (innerHeight - radius) || this.y < radius) {
            this.vy = -this.vy;
        }
        
        this.x += this.vx;
        this.y += this.vy;
        
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

//  Define Gravity
var g = 0.1;

// Create # amount of circles and append to list
for (var i = 0; i < 40; i++) {

    //      Hyperparameters
    var radius = 10;
    var x = (radius + Math.random() * (innerWidth - 2 * radius));
    var y = (Math.random() * (innerHeight/2) + (innerHeight/2)) - radius;
    var vx = (Math.random() - 0.5);
    var vy = (Math.random() -0.5) * 20;
    var color = pickColor();
    
    circleArray.push(new Circle(x, y, vx, vy, radius, color));
}

//  Animate all the circles present in the array
animate();