const number = parseInt(prompt("Enter the number : "));
function factorial(number) {
    if(number > 0) {
        return number * factorial(number - 1);
    }
    else {
        return number;
    }
}
const result = factorial(number);
console.log(`The factorial of a given number is  : ${result}`);