
let displayList = [];
let commands = [];

let currentNum = '';

const display = document.querySelector('.display');

function setCommand() {

    if (displayList.length > 0) {

        display.innerHTML = displayList.join('');
    }
    else {

        display.innerHTML = '0';
    }
    // console.log(commands);
}

function getCommandValue() {

    lastCommand = '';

    const result = commands.reduce(function (reduced, value) {

        switch (value) {

            case 'x':
            case '/':
            case '+':
            case '-': {

                lastCommand = value;
            } break;

            default: {

                const currentValue = parseFloat(value);

                switch (lastCommand) {

                    case 'x': {

                        reduced *= currentValue;
                    } break;

                    case '/': {

                        reduced /= currentValue;
                    } break;

                    case '+': {

                        reduced += currentValue;
                    } break;

                    case '-': {

                        reduced -= currentValue;
                    } break;

                    default: {

                        reduced = currentValue;
                    } break;
                }

            } break;
        }

        return reduced;
    }, 0);

    return result;
}

setCommand();

const buttons = document.querySelectorAll('.btn');


function onButtonClick(e) {

    const value = e.target.innerHTML;

    switch (value.toLowerCase()) {

        case 'x':
        case '/':
        case '+':
        case '-': {
            commands.push(currentNum);
            commands.push(value);
            currentNum = '';

            displayList.push('<span style="font-size: calc(var(--display-font-size) * 0.7); padding: 0 20px;">' + value + '</span>')
        } break;

        case '=': {
            commands.push(currentNum);

            displayList.length = 0;

            const result = getCommandValue();
            currentNum = `${result}`;
            displayList.push(currentNum);
            commands.length = 0;
            commands.push(currentNum);
        } break;

        case 'clear': {

            currentNum = '';
            commands.length = 0;
            displayList.length = 0;
        } break;

        default: {
            currentNum += value;
            displayList.push(value);
        } break;
    }

    setCommand();
}

buttons.forEach(function (btn) {

    btn.addEventListener('click', onButtonClick);
});