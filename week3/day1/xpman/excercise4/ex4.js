// Exercise 4 : My Book List

// Instructions

// Take a look at this link for help.

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty div: 
// <div class="listBooks"></div>
// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)
// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render the books inside an HTML table (the HTML table must be added to the <div> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.

let allBooks=[
{title: 'Economics book', 
author:'John', 
image: 'https://cdn.icon-icons.com/icons2/2367/PNG/512/file_document_icon_143599.png', 
alreadyread: true},

{title: 'Math book', 
author:'Jack', 
image: 'https://cdn.icon-icons.com/icons2/2367/PNG/512/check_small_icon_143632.png', 
alreadyread: false}
]

//let entry0=[Object.keys(allBooks[0])];

// console.log(entry0);







let table1 = document.createElement('table')
document.querySelector('div').appendChild(table1)

let row = document.createElement('tr')
document.querySelector('table').appendChild(row)

let title = document.createElement('th')
document.querySelector('div').querySelector('table').appendChild(title);
title.textContent = `Title`;

let author1 = document.createElement('th')
document.querySelector('div').querySelector('table').appendChild(author1);
author1.textContent = `author`;


let image1 = document.createElement('th')
document.querySelector('div').querySelector('table').appendChild(image1);
image1.innerHTML = "image"


let alreadyread1 = document.createElement('th')
document.querySelector('div').querySelector('table').appendChild(alreadyread1);
alreadyread1.textContent = `alreadyread`;


for (i=0; i<allBooks.length; i++){
 let row = document.createElement('tr')
document.querySelector('table').appendChild(row)

let title = document.createElement('td')
document.querySelector('div').querySelector('table').appendChild(title);
title.textContent = allBooks[i].title;

let author1 = document.createElement('td')
document.querySelector('div').querySelector('table').appendChild(author1);
author1.textContent = allBooks[i].author;


let image1 = document.createElement('td')
document.querySelector('div').querySelector('table').appendChild(image1);
image1.innerHTML = 


let alreadyread1 = document.createElement('td')
document.querySelector('div').querySelector('table').appendChild(alreadyread1);
alreadyread1.textContent = allBooks[i].alreadyread;
}

   