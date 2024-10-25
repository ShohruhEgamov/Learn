"use strict";
// console.log('Hello, TypeScript');
// let firstName1: string = "Shohruh";
// console.log(typeof firstName1);
// //---------------------------------------------------------------------------------------------------
// let firstName: string = "Dylan"; // type string
// // firstName = 33; // attempts to re-assign the value to a different type
// console.log(firstName);
// //---------------------------------------------------------------------------------------------------
// // Implicit any as JSON.parse doesn't know what type of data it returns so it can be "any" thing...
// const json = JSON.parse("55");
// // Most expect json to be an object, but it can be a string or a number like this example
// console.log(typeof json);
// console.log('Salom men shohruh')
// let v: any = true;
// v = "string";
// console.log(Math.round(v));
// // let w: any = 1;
// // w = "number"; // no error
// // w = {
// // 	runANonExistentMethod: () => {
// // 		console.log("I think therefore I am");
// // 	}
// // } as { runANonExistentMethod: () => void }
// // if (typeof w === 'object' && w !== null) {
// // 	(w as { runANonExistentMethod: Function }).runANonExistentMethod();
// // }
// // let x: never = true;
// let w: unknown = 1;
// w = "string"; // no error
// w = {
// 	runANonExistentMethod: () => {
// 		console.log("I think therefore I am");
// 	}
// } as { runANonExistentMethod: () => void }
// // How can we avoid the error for the code commented out below when we don't know the type?
// // w.runANonExistentMethod(); // Error: Object is of type 'unknown'.
// if (typeof w === 'object' && w !== null) {
// 	(w as { runANonExistentMethod: Function }).runANonExistentMethod();
// }
// // Although we have to cast multiple times we can do a check in the if to secure our type and have a safer casting
// // let x: never = true;
// let y: undefined = undefined;
// console.log(typeof y);
// let z: null = null;
// console.log(typeof z);
// // const names: string[] = [];
// // names.push("Dylan"); // no error
// // names.push(3);
// // console.log(names);
// const names: readonly string[] = ["Dylan"];
// // names.push("Jack"); // Error: Property 'push' does not exist on type 'readonly string[]'.
// // try removing the readonly modifier and see if it works?
// console.log(names);
// //---------------------------------------------------------------------------------------------------
// // const car: { type: string, model: string, year: number } = {
// // 	type: "Toyota",
// // 	model: "Corolla",
// // 	year: 2009
// // };
// // car.type = 3
// // console.log(car);
// // const car: { type: string, mileage?: number } = { // Error: Property 'mileage' is missing in type '{ type: string; }' but required in type '{ type: string; mileage: number; }'.
// // 	type: "Toyota",
// // };
// // car.mileage = 2000;
// // console.log(car);
// enum StatusCodes {
// 	NotFound = 404,
// 	Success,
// 	Accepted,
// 	BadRequest
// };
// // logs 404
// console.log(StatusCodes.NotFound);
// // logs 200
// console.log(StatusCodes.Accepted);
// enum CardinalDirections {
// 	North = 'North',
// 	East = "East",
// 	South = "South",
// 	West = "West"
// };
// // logs "North"
// console.log(CardinalDirections.North);
// // logs "West"
// console.log(CardinalDirections.West);
// //---------------------------------------------------------------------------------------------------
// // enum myEnum {
// // 	myFirstConst,
// // 	mySecondConst
// // };
// // console.log(myEnum.myFirstConst);
// // enum myEnum {
// // 	myFirstConst = "first",
// // 	mySecondConst = "second"
// // };
// // console.log(myEnum.mySecondConst);
// //---------------------------------------------------------------------------------------------------
// type CarYear = number;
// type CarType = string;
// type CarModel = string;
// type Car = {
// 	year: CarYear,
// 	type: CarType,
// 	model: CarModel
// };
// const carYear: CarYear = 2001
// const carType: CarType = "Toyota"
// const carModel: CarModel = "Corolla"
// const car: Car = {
// 	year: carYear,
// 	type: carType,
// 	model: carModel
// };
// console.log(car);
// interface Rectangle {
// 	height: number,
// 	width: number
// };
// const rectangle: Rectangle = {
// 	height: 20,
// 	width: 10
// };
// console.log(rectangle);
// //---------------------------------------------------------------------------------------------------
// interface Rectangle {
// 	height: number,
// 	width: number
// }
// interface ColoredRectangle extends Rectangle {
// 	color: string
// }
// const coloredRectangle: ColoredRectangle = {
// 	height: 20,
// 	width: 10,
// 	color: "red"
// };
// console.log(coloredRectangle);
// //---------------------------------------------------------------------------------------------------
// function printCode(code: string | number) {
// 	console.log(`My status code is ${code}.`)
// }
// printCode(404);
// printCode('404');
// //---------------------------------------------------------------------------------------------------
// function getTime(): number {
// 	return new Date().getDate()
// }
// console.log(getTime());
// function printHello(): void {
// 	console.log('Hello!');
// }
// printHello()
// function multiple(a: number, b: number) {
// 	return a * b
// }
// console.log(multiple(5, 4));
// function add(a: number, b: number, c?: number) {
// 	return a + b + (c || 0);
// }
// console.log(add(2, 5, 6))
// function pow(value: number, exponent: number = 5) {
// 	return value ** exponent;
// }
// console.log(pow(10));
// function toplam({ birinchi, ikkinchi }: { birinchi: number, ikkinchi: number }) {
// 	return birinchi / ikkinchi
// }
// console.log(toplam({ birinchi: 10, ikkinchi: 2 }));
// function add(a: number, b: number, ...rest: number[]) {
// 	return a + b + rest.reduce((p, c) => p + c, 0)
// }
// console.log(add(10, 5, 6, 8, 9, 2, 6, 57));
// type Negate = (value: number) => number;
// // in this function, the parameter `value` automatically gets assigned the type `number` from the type `Negate`
// const negateFunction: Negate = (value) => value * -1;
// console.log(negateFunction(10));
// //---------------------------------------------------------------------------------------------------
// let x: unknown = 'salom'
// console.log((x as string).length);
// let x: unknown = 'hello';
// console.log((<string>x).length);
// //---------------------------------------------------------------------------------------------------
class Person {
}
// Bu yerda name: string | undifayned Bo'lishi yoki name?: bolishi kerak bo'lmasa hato berayapdi
const person = new Person();
person.name = "Jane";
console.log(person);
