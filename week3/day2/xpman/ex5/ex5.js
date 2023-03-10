// Exercise 5 : Event Listeners

// Instructions

// Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.
// Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.
// Get the element you want to add listeners to
const myElement = document.getElementById('myElement');

// Define a function to change the position of the element on click
function changePositionX(event) {
  myElement.style.left = `${event.clientX}px`;
}

// Define a function to change the position of the element on mouseover
function changePositionY(event) {
  myElement.style.top = `${event.clientY}px`;
}

// Define a function to change the color of the element on mouseout
function changeColor(event) {
  myElement.style.color = 'red';
}

// Define a function to change the font size of the element on double click
function changeFontSize(event) {
  myElement.style.fontSize = '2em';
}

// Add event listeners to the element
myElement.addEventListener('click', changePositionX);
myElement.addEventListener('mouseover', changePositionY);
myElement.addEventListener('mouseout', changeColor);
myElement.addEventListener('dblclick', changeFontSize);
