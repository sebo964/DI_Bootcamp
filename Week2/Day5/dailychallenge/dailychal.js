// Instructions

// Have you heard the infamous song “99 Bottles of Beer?”
// In this exercise you need to console.log the lyrics of our own 99 Bottles of Beer song.

// ==============================
// Example
// ==============================

// 99 bottles of beer on the wall
// 99 bottles of beer
// Take 1 down, pass it around
// 98 bottles of beer on the wall

// 98 bottles of beer on the wall
// 98 bottles of beer
// Take 2 down, pass them around
// 96 bottles of beer on the wall

// 96 bottles of beer on the wall
// 96 bottles of beer
// Take 3 down, pass them around
// 93 bottles of beer on the wall

// ect …

// ==============================

// Prompt the user for a number to begin counting down bottles.

// In the song, everytime a bottle drops, 
// the subtracted number should go up by 1. 
// For example,

//     We start the song at 99 bottles
//     -> Take _1_ down, pass it around
//     -> we have now 98 bottles

//     -> then, Take _2_ down, pass them around
//     -> we have now 96 bottles

//     -> then, Take _3_ down, pass them around
//     -> we have now 93 bottles

//     ... ect


// 3. The song should end with “0 bottle of beer on the wall” or “no bottle of beer on the wall”.


// 4. Note : Make sure you get the grammar correct.

// For 1 bottle, you pass “it” around.
// For more than one bottle, you pass “them” around.


let lyrics = "99 bottles of beer on the wall \n99 bottles of beer \nTake 1 down, pass it around \n98 bottles of beer on the wall \n"

console.log(lyrics)

// 3 varialbes 

// let beerbottles = prompt("How many bottles of beer do you have on the wall")

// console.log(beerbottles)



let result = prompt("How many bottles of beer do you have on the wall?")

for (counter = 1; counter < 99 ; counter++) 
{
            
                            const part1 = `${result} ${bottleplurartest(result)} of beer on the wall \n${result} ${bottleplurartest(result)} of beer \n`;

                            let part2 = `Take ${counter} down, pass ${pluralsingualremainingbottles(counter)} around \n`
                            
                            result = result - counter; // updates the result to new value
                            
                            let part3 =`${result} ${bottleplurartest(result)} of beer on the wall \n`; // text song with new result value
                            
                            // if the results is smaller than the counter the loop extis and alternate ending string
                            if  (result <= 0) {
                                result=result+counter;
                                part2 = `Take ${result} down, pass them around \n`
                                part3 = 'Zero bottle of beer on the wall \n'

                                console.log(part1+part2+part3); 
                                
                                break;
                            
                            };
                            ///logs the song iteration
                            console.log(part1+part2+part3);

                           

                            
            

};



function pluralsingualremainingbottles(counter){

    let itthem ;

    if(counter ==1)  {itthem="it"}  else {itthem="them"};

    return(itthem);
        
}


function bottleplurartest(result) {
    
    let bottlestatus
    if (result == 1) {bottlestatus="bottle"} else {bottlestatus=`bottles`}
    return(bottlestatus)

}