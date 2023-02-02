// 🌟 Exercise 2 : Work With Forms

// Instructions

// Copy the code below, into a structured HTML file:

// Retrieve the form and console.log it.

// Retrieve the inputs by their id and console.log them.

// Retrieve the inputs by their name attribute and console.log them.

// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
// The output should be :

// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>


// // code to retrieve the form. 
let formelements = document.getElementsByTagName('form')[0];
let elements=formelements

console.log(elements)


// code to retrieve the inputs by their id.

let inputelements = document.getElementsByTagName('input');

console.log(inputelements)


// code to retrieve the inputs by their name attribute.


// code to append the li elements to the ul.

// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
// The output should be :

// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>


document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault()
loguser()
});



function loguser() {

//prevent defaut submit



let formtest = document.querySelector('form');


let fname = document.getElementById('fname').value;

let lname = document.getElementById('lname').value;


let createli = document.createElement('li');

createli.innerHTML = 'first name of the user ' + fname;

document.querySelector('ul').appendChild(createli);

let createli2= document.createElement('li');

createli2.innerHTML = 'last name of the user ' + lname;

document.querySelector('ul').appendChild(createli2);

}