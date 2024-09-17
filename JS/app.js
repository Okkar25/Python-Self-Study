const a = 30;
const b = 20;

// a > b ? console.log("a is greater") : console.log("b is greater");

const myInfo = {};

myInfo.name = "Okkar";
myInfo["age"] = 23;
myInfo[1] = "hello";

// console.log(myInfo);

const freshFruits = ["apple", "banana", "cherry", "kiwi", "mango"];

const newFruits = freshFruits.map((fruit) =>
  fruit === "banana" ? "dragon fruit" : fruit
);
// console.log(newFruits);

// const arr = Array.from({ length: 5 }, () => console.log("This is js"));

// const [x : value , y, ...z] = freshFruits
const [x, y, ...z] = freshFruits;

// console.log(x);
// console.log(y);
// console.log(z);

const numArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const filterItems = numArr.filter((num) => num % 2 === 1);
// console.log(filterItems);

const fruits = [
  "apple",
  "hello",
  "Orange",
  "world",
  "Earth",
  "psycho",
  "umbrella",
];

const vowels = "aeiouAEIOU";
const vowels_fruits = [];

// for (fruit of fruits) {
//   console.log(fruit);
// }

// for (fruit in fruits) {
//   console.log(fruits[fruit]);
// }

// const result = fruits.filter((fruit) => vowels.includes(fruit[0]));
// console.log(result);

// for (fruit in fruits){
//   for (v in vowels){
//     if fruit[0] ===
//   }
// }

const d = new Date();
// console.log(d.getFullYear());

const myInfo1 = {
  name: "Okkar Aung",
  age: 23,
  RS: false,
};

json = JSON.stringify(myInfo1);
// console.log(myInfo1);
// console.log(json);

// localStorage.setItem("myInfo", JSON.stringify(myInfo1))
// localStorage.setItem("myInfo", myInfo1)
