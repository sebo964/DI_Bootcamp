// 🌟 Exercise 6 : Vacations Costs

// Instructions

// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel. 

let nights
let dest 
let car

dest= prompt("Enter your destination")
car= prompt("Number of days you want to rent a car ?");
nights=prompt("How many nights will you stay?");


function hotelCost() {

    let numberofnights = nights//prompt("How many nights would you like to stay in the hotel?");


    // if the number of nights is not an integer alert and prompt again with enter a number of only. 


    //returns the hotel cost 
    checkifnumber(numberofnights);

    let hotel = numberofnights*140;

    console.log(hotel);
    return hotel;

    };



// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$ 

function planeRideCost() {

    let destination = dest // prompt("Where would you like to go?")


    if (typeof(destination) == 'string') {

        console.log(typeof(destination))

        }
        else {

        alert('Please enter a destination')

        }   

        //returns the cost of planefare


    switch (destination) {
        
        case "Paris":

            return 220

        case "London":      

            return 183

        default:

            return 300
    }               

}
// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental. 

function rentalCarCost(){
    let carrentdays = car // prompt(`How many days do you want to rent the car?`)
    let carcost
    checkifnumber(carrentdays)
    if (carrentdays>10) {(carrentdays*40)*0.95}
        
    else {carcost = carrentdays*40}


    console.log(carcost)
    return carcost
}


// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z. 
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

// Call the function totalVacationCost()

// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.


function totalVacationCost() {


    totalVacationCost = hotelCost() + planeRideCost() + rentalCarCost();
     ;

}


console.log(totalVacationCost())



function checkifnumber(numberofnights) {


    if (typeof(numberofnights) == 'number'){
        console.log(typeof(numberofnights))
        return(true)
        }
        else {
    
        alert('Please enter a number')
    
        }   
        

    }