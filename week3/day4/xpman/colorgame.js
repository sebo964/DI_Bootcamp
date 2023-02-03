const grid = document.getElementsByClassName("grid")

let gridsize = '100' //prompt('Enter the size of the canvas')

gridsize = parseInt(gridsize)

    for (let j = 0; j < gridsize; j++) {
        const div = document.createElement("div")
        div.classList.add("box")
        grid[0].appendChild(div)
    }

    
    const buttonclick = document.getElementById("colorselector")


        // on click get the color of the butto and add it to the active color variable 

    let activecolor 

    for (let i = 0; i < 24; i++) {
        const color = document.getElementsByClassName(`color${i}`)
        color.addEventListener("click", () => {
            activecolor = color.style.backgroundColor
        })
    }
    

    console.log(activecolor)