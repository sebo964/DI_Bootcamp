
// Create a function called addTask(). As soon as the user clicks on the button:
// check that the input is not empty,
// then add it to the array (ie. add the text of the task)
// then add it to the DOM, below the form (in the <div class="listTasks"></div>) .
// Each new task added should have (starting from left to right - check out the image at the top of the page)
// a “X” button. Use font awesome for the “X” button.
// an input type="checkbox". The label of the input is the task added by the user.


console.log("testing")
const tasks=[];  // list of items will be contained in this array 

const form = document.getElementById('f1');
form.addEventListener('submit',addTask); // listen to the submit event and add the task

// function add task(task) - adds a task to the list of tasks pushes it to the array and add delete button and checkbox 

function addTask(e) {

e.preventDefault();
let taskadded = document.querySelector('input')

//  the user input is not empty then add the task to the array and add the task to the DOM
    if (taskadded.value!== "") {
        tasks.push(taskadded.value);
        const li = document.createElement("p");
        document.querySelector('div').appendChild(li);

        // adds a check box to the task on the left side
        const tick = document.createElement("input");
        tick.setAttribute("type", "checkbox")
        tick.setAttribute("class", "tick")
        li.appendChild(tick);

        // when the checkbox is clicked the span text will be striked
        tick.addEventListener("click", () => {
            if (tick.checked) {
                span.style.textDecoration = "line-through";
            }
            else {
                span.style.textDecoration = "none";
            }
        })  

        // the task the user enters is added to the dom 

        const span = document.createElement("span");
        span.textContent = taskadded.value;
        li.appendChild(span);

        // adds a delete button to the task on the right side

        const del = document.createElement("button")
        del.textContent = "-";
        li.appendChild(del);
        
        // when the delete button is clicked the task is deleted from the dom

        del.addEventListener("click", () =>
        document.querySelector('div').removeChild(li));
    }
    else {
        alert("task was not found");
    }
}



