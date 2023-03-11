// Instructions

// <!DOCTYPE html>
//     <html>
//     <head>
//         <style>
//         #target {
//           width: 200px;
//           height: 200px;
//           position: relative;
//           background: yellow;
//         }
//         #box {
//           width: 50px;
//           height: 50px;
//           position: absolute;
//           background-color: red;
//         }
//         </style>
//     </head>
//     <body>
//         <div id="target"></div>
//         <br>
//         <div id="box"></div>
//     </body>
//     </html>


// Copy the code above, to a structured HTML file.
// In your Javascript file add the functionality which will allow you to drag the box and drop it into the target. Check out the Course Notes named DOM animations.

// Get the box and target elements
const box = document.getElementById('box');
const target = document.getElementById('target');

// Set some initial variables for tracking the mouse position and box offset
let offsetX = 0;
let offsetY = 0;
let mouseX = 0;
let mouseY = 0;

// Add a mousedown event listener to the box element
box.addEventListener('mousedown', function(e) {
  // Prevent the default mousedown behavior
  e.preventDefault();

  // Calculate the initial mouse position and box offset
  offsetX = e.clientX - box.offsetLeft;
  offsetY = e.clientY - box.offsetTop;

  // Add event listeners for mousemove and mouseup events
  document.addEventListener('mousemove', mouseMoveHandler);
  document.addEventListener('mouseup', mouseUpHandler);
});

// Define the mousemove event handler
function mouseMoveHandler(e) {
  // Calculate the new mouse position
  mouseX = e.clientX;
  mouseY = e.clientY;

  // Update the box position based on the mouse position and box offset
  box.style.left = (mouseX - offsetX) + 'px';
  box.style.top = (mouseY - offsetY) + 'px';
}

// Define the mouseup event handler
function mouseUpHandler(e) {
  // Remove the mousemove and mouseup event listeners
  document.removeEventListener('mousemove', mouseMoveHandler);
  document.removeEventListener('mouseup', mouseUpHandler);

  // Check if the box is inside the target
  const boxRect = box.getBoundingClientRect();
  const targetRect = target.getBoundingClientRect();
//   if (boxRect.right >= targetRect.left && boxRect.left <= targetRect.right && boxRect.bottom >= targetRect.top && boxRect.top <= targetRect.bottom)  
  
//     else {
//     // If the box is not inside the target, reset the box position
//     box.style.left = '';
//     box.style.top = '';
//   }
}
