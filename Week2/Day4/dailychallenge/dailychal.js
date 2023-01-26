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

let word=prompt('Enter words seperateg by commas')

starbox(word)


function starbox(words) {


userinput=words;

let userarra=userinput.split(","); // covnerts to array form
        for (let i=0; i<userarra.length; i++) {

        userarra[i] = userarra[i].trim();

        };  

//--------------------------
//find the word with the longest length
    let arralen=[];
    let maxlenght;

            for (let i=0; i<userarra.length; i++) {
                                                
             arralen.push(userarra[i].length)   

                                            };

            arralen.sort();

            lastitemposition = arralen.length-1;

            maxlenght = arralen[lastitemposition];
        console.log(maxlenght)
        console.log(arralen)
//---------------------------------------------

//add stars above and below the the group items. 

//print the stars
   
let star='*'.repeat(maxlenght+10);

console.log(star)


    for (let i=0; i<userarra.length; i++) {     // displays on multple lines

    let output = []
    
    output.push("* "+userarra[i].padEnd(maxlenght+4," ").padStart(maxlenght+6," ")+" *");   
    


    console.log(`${output}`)
    };



///print the stars

console.log(star)
}