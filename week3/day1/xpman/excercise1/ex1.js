// Exercise 1 : Users

// Instructions

// <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>


// Add the code above, to your HTML file

// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Change each first name of the two <ul>'s to your name.
// Delete the <li> that contains the text node “Sarah”.

// Bonus - Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.


// let thediv = document.querySelector('div').innerText
debugger
let thediv = document.querySelector('div')

console.log(thediv) 

document.querySelector('ul').querySelector('li:nth-child(2)').remove()

let namerichard= document.createElement('li')
namerichard.textContent = 'Richard'

document.querySelector('ul').appendChild(namerichard)

// document.querySelector('ul').removeChild(namerichard)

//document.querySelector('ul').removeChild()