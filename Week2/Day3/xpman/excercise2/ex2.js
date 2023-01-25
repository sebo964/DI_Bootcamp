// 🌟 Exercise 2 : Your Favorite Colors

// Instructions

// Create an array called colors where the value is a list of your five favorite colors.

let colors=['red','blue','yellow','green','black']

// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .

for (let i = 0; i <colors.length; i++) {

    let color=colors[i];
    favcolor =`My #${i+1} choice is ${color}`

    console.log(favcolor)

}

// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus


for (let i = 0; i <colors.length; i++) {
    let th=[`st`,`nd`,`rd`,`th`,`th`]
    let color=colors[i];
    favcolor =`My ${i+1}${th[i]} choice is ${color}`

    console.log(favcolor)

}




