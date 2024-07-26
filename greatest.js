// const prompt = require("prompt-sync")();
console.log(`Hello`);
num1 = parseFloat(prompt("Enter first number: "));
num2 = parseFloat(prompt("Enter the second number: "));
num3 = parseFloat(prompt("Enter the third number: "));
let greatest;
if (num1 >= num2 && num1 >= num3) {
    greatest = num1;
}
else if (num2 >= num1 && num2 >= num3) {
    greatest = num2;
}
else {
    greatest = num3;
}
console.log(`The greatest number among ${num1} , ${num2} and ${num3} is ${greatest} `);
console.log("The greatest number is "+greatest);
 
greatest = Math.max(num1 , num2 , num3)
console.log(`The greatest number is ${greatest} .`)