// 🌟 Exercise 3 : Repeat The Question

// Instructions

// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

let x = (prompt(`Enter a number`))

console.log(x)


while (x<10) {
    
  x = prompt(`Enter a different number`)

}