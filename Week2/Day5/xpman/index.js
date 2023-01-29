// Steps

// Explanation of the game : the point of the game is to guess the number that the computer has in “mind”.

// First Part

// Create a JS file and link it to the index.html file.

// Take a look at your html file, you should have a button with an “onclick” event. This event is equal to the function playTheGame(). It means that when you will click on the button, the function playTheGame() will be called. 
// We will learn more about events next week ;)

// Now let’s create the function:

// In the JS file, create a function called playTheGame() that takes no parameter.
// In the function, start by asking the user if they would like to play the game (Hint: use the built-in confirm() function).

// If the answer is false, alert “No problem, Goodbye”.

// If his answer is true, follow these steps:
// Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function). You then have to check the validity of the user’s number :

// If the user didn’t enter a number (ie. if he entered another data type) alert “Sorry Not a number, Goodbye”.
// If the user didn’t enter a number between 0 and 10 alert “Sorry it’s not a good number, Goodbye”.
// Else (ie. he entered a number between 0 and 10), create a variable named computerNumber where the value is a random number between 0 and 10 (Hint: Use the built-in Math.random() function). Make sure that the number is rounded.


// Second Part

// Outside of the playTheGame() function, create a new function named compareNumbers(userNumber,computerNumber) that takes 2 parameters : userNumber and computerNumber

// The point of this function is to check if the userNumber is the same as the computerNumber:
// If userNumber is equal to computerNumber, alert “WINNER” and stop the game.

// If userNumber is bigger than computerNumber, alert “Your number is bigger then the computer’s, guess again” (Hint: use the built-in prompt() function to ask the user for a new number).

// If userNumber is lower than computerNumber, alert “Your number is smaller then the computer’s, guess again” (Hint: use the built-in prompt() function to ask the user for a new number).

// If the user guessed more than 3 times, alert “out of chances” and exit the function.


// Bonus

// In the First Part, instead of stopping the process if the user didn’t enter a valid number. Continue asking for a number until the user enters a valid number.


function playTheGame() {

    confirm ('Do you want to play the game?') 

            // generate a random number from 1 to 10 
            let computerNumber = parseInt(Math.floor(Math.random() * 10 + 0))
            console.log(computerNumber)

        
            let userNumber= parseInt(prompt('Enter a number that is between 0 and 10'))


            // check it is a number
            numbercheck(userNumber) 
            console.log(numbercheck(userNumber))
            // check if it is a valid number
            isNumbervalid(userNumber)  
            console.log(isNumbervalid(userNumber))

    // if it is a number and the number is valid proceed otherwise eend the game
    if (numbercheck(userNumber) && isNumbervalid(userNumber) == true) {

        // check if the number is a winner if not propose the user another 3 tries to get it right
        for (let i = 0; i < 3; i++) {  

            
            if (computerNumber === userNumber) {
                console.log('win')
                return (alert ('You win'))
                }
            else if (computerNumber > userNumber) {
                alert('lose small')

            }
            else if (computerNumber < userNumber) {
                alert('lose big')

                }
             userNumber=  parseInt(prompt('try again'))

        }

           return (alert("Game over!"))
}
else {
    return (alert('out of chances'))
    
}    
        
}       



// check if the userNumber is a number
function numbercheck(quserNumber){
    for(let i=0; i<1; i++) {
        if ( isNaN(quserNumber)) {
            alert('This is not a number. Please enter a number')
            quserNumber= parseInt (prompt('Please enter a number'))
            
        }
        else {
            
            return true
            break
            
        }
    }
   return( alert('You had only 3 tries'))
    

}

// check is the number is between 1 to 10 
function isNumbervalid(userNumber){
    for (i=0;i<1;i++) {

        if (userNumber > 10 || userNumber < 0) {
            alert('Sorry number not valid')
            userNumber= parseInt (prompt('Please enter a number between 0 and 10'))
        }   
        else {
            return true
            break
        }
    }
  return(alert('too many tries'))
    
}


