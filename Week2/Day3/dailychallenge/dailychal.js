// Write a JavaScript program that recreates the pattern below.
// Do this Daily Challenge by youself, without looking at the answers on the internet.



let stars='*'

for (let t=0; t<6;t++){  
    console.log(stars)

stars=stars + " *"

}

// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).


let star='*';

for (let i=0; i<star.length;i++){  
    while(star.length<12){
        console.log(star);
        star=star + " *";
    };
};

for (let i = 0; i < 6; i++) {
    const len = i+1;  
    
    // console.log('* '.repeat(len));

    let tolog = '';
    for (let j = 0; j < len; j++) {
        tolog += '* ';
    }

    console.log(tolog);
}

