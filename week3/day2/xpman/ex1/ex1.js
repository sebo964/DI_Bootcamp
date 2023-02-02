// 🌟 Exercise 1 : Change The Article

// Instructions

// Copy the code below, into a structured HTML file:


// Using a DOM property, retrieve the h1 and console.log it.

// Using DOM methods, remove the last paragraph in the <article> tag.

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

let a = document.querySelector('h1').innerHTML

console.log(a)




// let plast = document.querySelector('article' 'p:nth-child(3)').innerHTML

// console.log(plast)


let x = document.querySelector('h3')
x.addEventListener("click", isred )

function isred(){

    x.style.backgroundColor='red'
}


let y = document.querySelector('h3')
x.addEventListener("click", disappear )


function disappear(){

    y.style.display='none'
}

// add a button "toggle" to the element article. 

let w = document.createElement('button')

document.querySelector('h2').appendChild(w)

w.innerHTML='togglebtn'

w.addEventListener('click',isbold)

function isbold(){
    document.querySelector('article').style.fontWeight='bold' }