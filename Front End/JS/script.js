// console.log("External JS called");
// var name = "Pratik";
// let amount;     //declaration
// let gender = 'Male';
// name = "pratik";
// amount = 1000;
// const email = "pratik@gmail.com"
// console.log(name, amount, gender,email);
// name = "Pratik";
// console.log(name);
// var name = "Akash"
// console.log(name);

// var name = "puja";
// console.log(name);

// let condition = false;
// if (condition){
//     console.log('Inside the if block.')
// }
// else{
//     console.log('outside of if block');
//     console.log("The addition is = ",20 + 30);
// }


// let age = 21 , gender = "female" ;
// if (age > 18 && gender == "female"){
//     console.log("Eligible to marry!")
// }
// else if (age < 18 && gender == "female"){
//     console.log("Not eligible to marry!")
// }
// else{
//     console.log("Invalid input!")
// }

// let f_name = "Aniket"
// f_name = 10

// f_name = 20;

// let numbers = [1,2,3,4,5,6,7,8,9,10];

// for(let i=0; i<numbers.length ; i++){
//     console.log(numbers[i]);
// }

// for(let i = 1;i <= 10;i++){
//     console.log("10 * i = ",10*i);
// }

// for(let i = 1;i <= 10;i++){
//     console.log(`10 * ${i} = ${10 * i}`);
// }

// for(let i = 1;i <= 10;i++){
//     console.log(`75 * ${i} = ${75 * i}`)
// }

// let address = {
//     house_no : "G102",
//     Lane_no1 : "Green city apartments",
//     Lane_no2 : "Satav nagar, Handewadi road",
//     Town : "Hadapsar",
//     State : "Maharashtra",
//     Country : "India", 
//     Pin_code : 411028,
// }

// let person = [{
//     first_name : "Snehal",
//     last_name : "Chavan",
//     email : "chavansnehalh91@gmail.com",
//     mobile : 9561804664,
//     height : 5.6,
//     address : {
//         house_no : "G102",
//         Lane_no1 : "Green city apartments",
//         Lane_no2 : "Satav nagar, Handewadi road",
//         Town : "Hadapsar",
//         State : "Maharashtra",
//         Country : "India", 
//         Pin_code : 411028,
//     }
// },
// {
//     first_name : "Aparna",
//     last_name : "Chavan",
//     email : "chavanaparnah93@gmail.com",
//     mobile : 9561804665,
//     height : 5.7,
//     address : {
//         house_no : "G202",
//         Lane_no1 : "Insignia",
//         Lane_no2 : "Mohan nagar co op society",
//         Town : "Baner",
//         State : "Maharashtra",
//         Country : "India", 
//         Pin_code : 411029,
//     }
// }
// ]

// for(let element of person){
//     console.log(element)
// }
// person[0].first_name = "snehal";


// console.log(person.first_name + " " +person.last_name+ " "+person['email'])
// console.log(person.address)
// console.log(person.address.State)

// let addition = (a ,b) =>{
//     console.log(a ,b)
//     let addition = a + b;
//     console.log(addition)
// }

// addition(10 ,20)

// function calculation(num1 ,num2,op){
//     if (op == '+'){

//     }

// }

let data = {
    customers : [
        {
            name : '',
            id : '',
            email : '',
            address : {
                house_no : '',
                street_no : '',
                pin_code : '',
            }
        },
        {
            name : '',
            id : '',
            email : '',
        },
        {
            name : '',
            id : '',
            email : '',
        }
    ]
}

function getAge(){
    let age = prompt("Please enter your age");
    isEligibleForVoting(age);
    // console.log(age)
}
function isEligibleForVoting(age){
    if (age > 18){
        alert("Elligible to vote")
    }
    else if (age < 18 && age > 0){
        alert("Not elligible to vote")
    }
    else{
        alert("Enter valid age")
    }
}

function callConfirm(){
    let result = confirm("Are you really want to leave the page?");
    if (result){
        console.log("Ok, Bye!")
    }
    else{
        console.log("Nice to have you on our website!")
    }
}

