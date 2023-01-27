// 🌟 Exercise 3 : Find The Numbers Divisible By 23

// Instructions

// Create a function call isDivisible() that takes no parameter.

// In the function, loop through numbers 0 to 500.

// Console.log all the numbers divisible by 23.

// At the end, console.log the sum of all numbers that are divisible by 23.

// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
// 391 414 437 460 483
// Sum : 5313


// Bonus: Add a parameter divisor to the function.

// isDivisible(divisor)

// Example:
// isDivisible(3) : Console.log all the numbers divisible by 3, and their sum
// isDivisible(45) : Console.log all the numbers divisible by 45, and their sum

function isDivisible() {
let div_23 =[];
    for (let i = 0; i <500; i++) {
        if (i % 23 === 0) {
            div_23.push(i);

            }
    }
    let sum = 0
    for (let i = 0; i < div_23.length; i++){

        sum += div_23[i];
    }

console.log(`Numbers divisible by 23 are ${div_23} and total is ${sum}}`)
};

isDivisible();

///-----------------------------------------

function isDivisiblevalue(divisor, total) {
    let div =[];
        for (let i = 0; i <total; i++) {
            if (i % divisor === 0) {
                div.push(i);
    
                }
        }
        let sum = 0
        for (let i = 0; i < div.length; i++){
    
            sum += div[i];
        }
    
    console.log(`Numbers divisible by ${divisor} are ${div} and total is ${sum}}`)
    };
    
    isDivisiblevalue(
        
        (prompt(`Enter divisor`)),

        (prompt(`Enter number to be checked`)),
    )
    