//zconst prompt = require("prompt-sync")();
// const number = parseFloat(prompt("Enter the number: "));
// let sum = 0;
// for (let i = 1; i <= number; i++) {
//     sum +=i;
// }
// console.log(`The sum of numbers is ${sum} .`);
// let addition = 0, j = 1;
// while(j <= number) {
//     addition += j;
//     j++;
// }
// console.log(`The addition of numbers is ${addition} .`)

function sum(num) {
    if(num > 0) {
        return num + sum(num - 1);
    }
    else {
        return num;
    }
    
}
const num = parseInt(prompt("Enter the number: "));
const result = sum(num);

console.log(`The sum of numbers is : ${result}`);