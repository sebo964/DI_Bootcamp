// <!-- 🌟 Exercise 2 : Users And Style

// Instructions

// <div>Users:</div>
// <ul>
//     <li>John</li>
//     <li>Pete</li>
// </ul>


// Add the code above, to your HTML file 

// Add a “light blue” background color and some padding to the <div>.

// Do not display the <li> that contains the text node “John”.

// Add a border to the <li> that contains the text node “Pete”.

// Change the font size of the whole body.

// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div). -->


document.querySelector('div').style.backgroundColor='#ADD8E6'

document.querySelector('ul').querySelector('li:nth-child(1)').style.display='none'


document.querySelector('ul').querySelector('li:nth-child(2)').style.border='solid'

document.querySelector('body').style.fontSize='20px'

