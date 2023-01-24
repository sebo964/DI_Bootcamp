// Exercise 3 : Secret Word

// Instruction

// Harder exercise
// Hint : Use Regular Expressions

// Prompt the user for a word and save it to a variable.
// Delete all the vowels of the word and console.log the result.
// Bonus: Replace the vowels with another character and console.log the results


let word=prompt(`Write any word`)

word_lenght=word.length

console.log(word_lenght)

const result1 = (Math.floor(Math.random() * 199))
const result2 = (Math.floor(Math.random() * 199))
const result3 = (Math.floor(Math.random() * 199))
const result4 = (Math.floor(Math.random() * 199))

 let newworda= word.replace(/a/g, result1);
 let newworde= newworda.replace(/e/g, result2);
 let newwordi= newworde.replace(/i/g, result3);
 let newwordo= newwordi.replace(/o/g, result4);
 let newwordu= newwordo.replace(/u/g, result3);



console.log(newwordu)
    
    
