//const prompt = require("prompt-sync")();
const number = parseFloat(prompt("Enter the number: "));
let sum = 0;
for (let i = 1; i <= number; i++) {
    sum +=i;
}
console.log(`The sum of numbers is ${sum}`);