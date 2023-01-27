// 🌟 Exercise 4 : Shopping List

// Instructions

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 
// Add the stock and prices objects to your js file.

// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

// Create a function called myBill() that takes no parameters. 

// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.

// Call the myBill() function.

// Bonus: If the item is in stock, decrease the item’s stock by 1


const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

console.log(stock)



//let shoppingList=["banana","orange","apple"]
//list the properties of stock items

const stockarra = Object.keys(stock)

 console.log(stockarra)

 let shoppingList=["banana","orange","apple"]


 function myBill() {
// if shoppingList item is in stock and value is greather than zero then item is prices is added in bill total variable

            let billTotal = 0

            if (stock.banana>0) {

                    billTotal = billTotal + prices.banana}

            if (stock.orange>0) {

                    billTotal = billTotal + prices.orange}

            if (stock.apple>0) {

                    billTotal = billTotal + prices.apple}
        

    console.log(billTotal)

 }

 myBill()