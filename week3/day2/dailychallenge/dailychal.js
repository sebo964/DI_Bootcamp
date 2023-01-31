// <!-- Follow these steps :

// Get the value of each of the inputs in the HTML file when the form is submitted. Remember the event.preventDefault()
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly. -->

// <!DOCTYPE html>
// <html>
//  <head>
//   <meta charset="utf-8" />
//   <title>Challenge: Mad Libs</title>
//  </head>
//  <body>

//     <h1>Mad Libs</h1>

//     <form id="libform">
//         <label for="noun">Noun:</label>
//              <input type="text" id="noun"><br>
//         <label for="adjective">Adjective:</label>
                //<input type="text" id="adjective"><br>
//         <label for="person">Someone's Name:</label>
                //<input type="text" id="person"><br>
//         <label for="verb">Verb:</label>
                //<input type="text" id="verb"><br>
//         <label for="place">A place:</label>
                //<input type="text" id="place"><br>

//         <button id="lib-button">Lib it!</button>
//     </form>

//     <p>Generated story: 
//     <span id="story"></span>
//     </p>

//     <script src="..."></script>

//  </body>
// </html> 



let noun
let adjective
let person
let verb
let place

let record=[]

const {forms:[form]}=document;
// const form = document.forms[0];

form.addEventListener("submit", function(event) {
    event.preventDefault();

    // form.elements.noun.value

    libit();
});



// document.getElementById("lib-button").addEventListener("click", libit);

function libit() { 
     

    // grab the values from the text field
     noun = document.getElementById("noun").value;
     adjective = document.getElementById("adjective").value;
     person = document.getElementById("person").value;
     verb = document.getElementById("verb").value;
     place = document.getElementById("place").value;
    
     record.length = 0;
     // push the values of the text field in an array.
     record.push(noun);
     record.push(adjective);
     record.push(person);
     record.push(verb);
     record.push(place);

     console.log(record)
     isempty()         

     // tahe the content of the text fields and add into the sotry text area
     document.getElementById("story").innerHTML = `this is a ${record[0]} once upon a time in the ${record[1]} this was a great ${record[2]} and the ${record[3]} also ${record[4]}`
    
    

     

}


function preventDefault(event) {
    event.preventDefault(event);
}

function isempty (){

for (i=0; i<record.length; i++) {
    if (record[i] == "") {
        
        alert("You forgot something");
        return false;
        break
    }
    else 
    { return true; }}

}
