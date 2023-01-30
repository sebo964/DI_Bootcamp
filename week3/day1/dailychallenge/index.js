// Create an array which value is the planets of the solar system.
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?


const planetsandmoons = [ 
    {planet:'mercury', moon:'0', color:'red'},
    {planet:'earth', moon:'1', color:'green'}, 
    {planet:'venus', moon:'0', color:'blue'}, 
    {planet:'mars', moon:'2', color:'green'},
    {planet:'jupiter', moon:'57', color:'purple'},
    {planet:'saturn', moon:'63', color: 'cyan'},
    {planet:'uranus', moon:'27', color: 'orange'},
    {planet:'neptune', moon:'14', color: 'brown'}
];

 //    'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'pluto']; // array of planet names and the number of moons in them

// console.log(planetsandmoons.length);

// loop to add a div for a each plannet and change the color according to color attribute of the planets in the array
for (let i=0; i<planetsandmoons.length;i++)
{
    let planets = document.createElement('div');
    planets.classList.add('planet');
    document.querySelector('section').appendChild(planets);
    planets.style.backgroundColor = planetsandmoons[i].color;;
    planets.textContent = planetsandmoons[i].planet;
    planets.style.color=planetsandmoons[i];

    
    // let moons = document.createElement('li');
    // moons.classList.add('moon');
    // document.querySelector('section').appendChild(moons);
    // moons.textContent = planetsandmoons[i].moon;


}
