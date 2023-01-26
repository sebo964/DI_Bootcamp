// Instructions

// Prompt the user for several words (separated by commas).
// Put the words into an array.
// Console.log the words one per line, in a rectangular frame as seen below.
// Check out the Hints and Requirements below.
// For example, if the user gives you: 
// Hello, World, in, a, frame
// you will transform it to : ["Hello", "World", "in", "a", "frame"]
// that will get displayed as:

// stars and words


// Hint

// The number of stars that wraps the sentence, must depend on the length of the longest word.


// Requirements

//let userinput = [prompt('enter words seperateg by commas')]


// Prompt user to enters words seperateg by commas
let word=prompt('Enter words seperateg by commas')

starbox(word) // executes the function add starbox.



//---------------

// function to add starbox around words seperateg by commas

function starbox(words) {

let userinput=words;

let userarra=userinput.split(","); // converts the text to array elements
        for (let i=0; i<userarra.length; i++) {

        userarra[i] = userarra[i].trim();  // trims for extra spaces

        };  

//--------------------------
//find the word with the largest number of characters and report how many characters the word has. 
    let arralen=[];
    let maxlenght;

            for (let i=0; i<userarra.length; i++) {
                                                
             arralen.push(userarra[i].length)   

                                            };

            arralen.sort();
                                            
            lastitemposition = arralen.length-1;

            maxlenght = arralen[lastitemposition];
        console.log(maxlenght);
        console.log(arralen);
//---------------------------------------------

//add stars above and below the the group items. 

//print the stars based on the longest word length
   
let star='*'.repeat(maxlenght+10);

console.log(star) // print top row of stars


    for (let i=0; i<userarra.length; i++) {     // displays on multple lines

    let output = [];
    
    output.push("* "+userarra[i].padEnd(maxlenght+4," ").padStart(maxlenght+6," ")+" *");   
    


    console.log(`${output}`);
    };



///print the stars

console.log(star); // print bottom row of stars
};