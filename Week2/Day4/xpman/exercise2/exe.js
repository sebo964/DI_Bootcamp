// 🌟 Exercise 2 : Tips

// Instructions

// John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

// Create a function named calculateTip() that takes no parameter.

// Inside the function, use prompt to ask John for the amount of the bill. 

// Here are the rules
// If the bill is less than $50, tip 20%.
// If the bill is between $50 and $200, tip 15%.
// If the bill is more than $200, tip 10%.

// Console.log the tip amount and the final bill (bill + tip).

// Call the calculateTip() function.

function calculateTip() {
    let bill = prompt("What is your bill?");
    if (bill < 50) {
        console.log(`Your bill is ${bill}, your tip is ${0.2*bill} and your total amount is ${bill*1.2}`)
    } 
    else if (bill>50 && bill<200) {

        console.log(`Your bill is ${bill}, your tip is ${0.15*bill} and your total amount is ${bill*1.15}`)

    }  
    else    {

        console.log(`Your bill is ${bill}, your tip is ${0.1*bill} and your total amount is ${bill*1.1}`)    
    }
}


calculateTip();