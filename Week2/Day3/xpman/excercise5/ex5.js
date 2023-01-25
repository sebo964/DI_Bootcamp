// 🌟 Exercise 5 : Family

// Instructions

// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

let fam={
    size: 4,
    fathername: 'John',
    mothername: 'Mary',
    fatherage: 20,
    motherage: 30,
    sonname:'Ted',
    sonage:12,
    daughtername:'Judy',
    daughterage:'10'

}

for (key in fam) {
    console.log(key)
        
    }

for (let value in fam )  {
    console.log(fam[value])
        
    }
