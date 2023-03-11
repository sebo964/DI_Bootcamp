// Instructions

// <!DOCTYPE html>
//     <html>
//     <head>
//         <style>
//         #container {
//           width: 400px;
//           height: 400px;
//           position: relative;
//           background: yellow;
//         }
//         #animate {
//           width: 50px;
//           height: 50px;
//           position: absolute;
//           background-color: red;
//         }
//         </style>
//     </head>
//     <body>
//         <p><button onclick="myMove()">Click Me</button></p>
//         <div id="container">
//           <div id="animate"></div>
//         </div>
//     </body>
//     </html>


// Copy the code above, to a structured HTML file.
//use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.
// The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions

// get references to the container and animate elements
const container = document.getElementById('container');
const animate = document.getElementById('animate');

// set the initial left position of the animate element
let leftPos = 0;

// function to move the animate element to the right
function myMove() {
  // set an interval to move the element every millisecond
  const interval = setInterval(() => {
    // update the left position by 1px
    leftPos += 1;
    // set the new left position
    animate.style.left = leftPos + 'px';
    // check if the animate element has reached the end of the container
    if (leftPos >= container.clientWidth - animate.clientWidth) {
      // if it has, clear the interval
      clearInterval(interval);
    }
  }, 1);
}
