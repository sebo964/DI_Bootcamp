

let sentence= 'The movie is not that bad'
let wordnot= sentence.indexOf("not")

console.log(wordnot)

let wordbad=sentence.indexOf("bad")

console.log(wordbad)

if( wordnot>=0 && wordbad>=wordnot  ){

    console.log('The movie is good')
}

else{

    console.log(sentence) 
}