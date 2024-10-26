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
// // interface Rectangle {
// // 	height: number,
// // 	width: number
// // };
// // const rectangle: Rectangle = {
// // 	height: 20,
// // 	width: 10
// // };
// // console.log(rectangle);
// //---------------------------------------------------------------------------------------------------
// // interface Rectangle {
// // 	height: number,
// // 	width: number
// // }
// interface ColoredRectangle extends Rectangle {
// 	color: string
// }
// // const coloredRectangle: ColoredRectangle = {
// // 	height: 20,
// // 	width: 10,
// // 	color: "red"
// // };
// // console.log(coloredRectangle);
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
// // function add(a: number, b: number, c?: number) {
// // 	return a + b + (c || 0);
// // }
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
// // let x: unknown = 'salom'
// // console.log((x as string).length);
// // let x: unknown = 'hello';
// // console.log((<string>x).length);
// //---------------------------------------------------------------------------------------------------
// // class Person {
// // 	name?: string;
// // }
// // Bu yerda name: string | undifayned Bo'lishi yoki name?: bolishi kerak bo'lmasa hato berayapdi
// // const person = new Person();
// // person.name = "Jane";
// // console.log(person);
// // class Person {
// 	// public name: string; // - (standart) sinf a'zosiga istalgan joydan kirish imkonini beradi
// 	// private name: string; // - sinf a'zosiga faqat sinf ichidan kirishga ruxsat beradi
// // 	protected name: string; // - sinf a'zosiga o'zidan va uni meros qilib olgan har qanday sinfdan kirishga ruxsat beradi, bu quyidagi meros bo'limida yoritilgan
// // 	public constructor(name: string) {
// // 		this.name = name;
// // 	}
// // 	public getName(): string {
// // 		return this.name
// // 	}
// // }
// // const person = new Person("shohruh");
// // console.log(person.getName());
// // class Person {
// // 	public constructor(private name: string) { }
// // 	public getName(): string {
// // 		return this.name;
// // 	}
// // }
// // const person = new Person("Farrux");
// // console.log(person.getName());
// // class Person {
// // 	public constructor(private readonly name: string) { }
// // 	public getName(): string {
// // 		return this.name;
// // 	}
// // }
// // const person = new Person("Farrux");
// // console.log(person.getName());
// // interface Shape {
// // 	getArea: () => number;
// // }
// // class Rectangle implements Shape {
// // 	public constructor(protected readonly width: number, protected readonly height: number) { }
// // 	public getArea(): number {
// // 		return this.width * this.height;
// // 	}
// // }
// // const myRect = new Rectangle(10, 20);
// // console.log(myRect.getArea());
// // interface Shape {
// // 	getArea: () => number;
// // }
// // class Rectangle implements Shape {
// // 	public constructor(protected readonly width: number, protected readonly height: number) { }
// // 	public getArea(): number {
// // 		return this.width * this.height;
// // 	}
// // }
// // class Square extends Rectangle {
// // 	public constructor(width: number) {
// // 		super(width, width);
// // 	}
// // 	// getArea gets inherited from Rectangle
// // }
// // const mySq = new Square(20);
// // console.log(mySq.getArea());
// // interface Shape {
// // 	getArea: () => number;
// // }
// // class Rectangle implements Shape {
// // 	// using protected for these members allows access from classes that extend from this class, such as Square
// // 	public constructor(protected readonly width: number, protected readonly height: number) { }
// // 	public getArea(): number {
// // 		return this.width * this.height;
// // 	}
// // 	public toString(): string {
// // 		return `Rectangle[width=${this.width}, height=${this.height}]`;
// // 	}
// // }
// // class Square extends Rectangle {
// // 	public constructor(width: number) {
// // 		super(width, width);
// // 	}
// // 	// this toString replaces the toString from Rectangle
// // 	public override toString(): string {
// // 		return `Square[width=${this.width}]`;
// // 	}
// // }
// // const mySq = new Square(20);
// // console.log(mySq.toString());
// // Abstrakt sinf
// abstract class Shape {
// 	// Abstrakt metod - faqat nomi va tipi ko‘rsatilgan, lekin bajarilishi yozilmagan
// 	abstract getArea(): number;
// 	// Oddiy metod - bajarilishi yozilgan
// 	// Bu yerda esa agar number yoki string bo'lsa shularni qaytaradi. void esa faqat konsolga chiqaradi
// 	public printArea(): void {
// 		console.log(`Area: ${this.getArea()}`);
// 	}
// }
// // Abstrakt sinfni kengaytiruvchi sinf
// class Rectangle extends Shape {
// 	public constructor(private width: number, private height: number) {
// 		super();
// 	}
// 	// getArea metodini qayta yozish - u bu sinfda bajarilishi kerak
// 	public getArea(): number {
// 		return this.width * this.height;
// 	}
// }
// // Yangi obyekt yaratamiz
// const myRectangle = new Rectangle(10, 20);
// myRectangle.printArea(); // Natijada "Area: 200" chiqariladi
// //---------------------------------------------------------------------------------------------------
// function createPair<S, T>(v1: S, v2: T): [S, T] {
// 	return [v1, v2];
// }
// console.log(createPair<string, number>('hello', 42)); // ['hello', 42]
// class NamedValue<T> {
// 	private _value: T | undefined;
// 	constructor(private name: string) { }
// 	public setValue(value: T) {
// 		this._value = value;
// 	}
// 	public getValue(): T | undefined {
// 		return this._value;
// 	}
// 	public toString(): string {
// 		return `${this.name}: ${this._value}`;
// 	}
// }
// const value = new NamedValue<number>('myNumber');
// value.setValue(10);
// console.log(value.toString()); // myNumber: 10
// type Wrapped<T> = { value: T };
// const wrappedValue: Wrapped<number> = { value: 10 };
// const wrappedString: Wrapped<string> = { value: "Hello" };
// console.log(wrappedString);
// console.log(wrappedValue);
// class IsmQiymati<T = string | number> {
// 	private _value: T | undefined;
// 	constructor(private name: string | number) { }
// 	public setValue(value: T) {
// 		this._value = value;
// 	}
// 	public getValue(): T | undefined {
// 		return this._value;
// 	}
// 	public toString(): string {
// 		return `${this.name}: ${this._value}`;
// 	}
// }
// let value = new IsmQiymati('Son');
// value.setValue(56);
// console.log(value.toString()); // myNumber: myValue
// function createLoggedPair<S extends string | number, T extends string | number>(v1: S, v2: T): [S, T] {
// 	console.log(`creating pair: v1='${v1}', v2='${v2}'`);
// 	return [v1, v2];
// }
// const pair = createLoggedPair(10, "hello");
// //---------------------------------------------------------------------------------------------------
// interface Rang {
// 	x: number;
// 	y: number;
// }
// let rangTuri: Partial<Rang> = {}; // `Partial` allows x and y to be optional
// rangTuri.x = 10;
// rangTuri.y = 20;
// console.log(rangTuri);
// interface Moshina {
// 	make: string;
// 	model: string;
// 	mileage: number;
// }
// let meningMoshinam: Required<Moshina> = {
// 	make: "Chevralet",
// 	model: "Lasetti",
// 	mileage: 12000,
// };
// console.log(meningMoshinam);
// const nameAgeMap: Record<string, number> = {
// 	'Alice': 21,
// 	'Bob': 25
// };
// console.log(nameAgeMap);
// interface Person {
// 	name: string;
// 	age: number;
// 	location?: string;
// }
// const bob: Omit<Person, 'age' | 'location'> = {
// 	name: 'Bob'
// 	// `Omit` has removed age and location from the type and they can't be defined here
// };
// console.log(bob);
// interface Person {
// 	name: string;
// 	age: number;
// 	location?: string;
//   }
//   const bob: Pick<Person, 'name'> = {
// 	name: 'Bob'
// 	// `Pick` has only kept name, so age and location were removed from the type and they can't be defined here
//   };
//   console.log(bob);
// type PointGenerator = () => { x: number; y: number; };
// const point: ReturnType<PointGenerator> = {
// 	x: 10,
// 	y: 20
// };
// //---------------------------------------------------------------------------------------------------
// interface Person {
// 	name: string;
// 	age: number;
// }
// // `keyof Person` here creates a union type of "name" and "age", other strings will not be allowed
// function printPersonProperty(person: Person, property: keyof Person) {
// 	console.log(`Printing person property ${property}: "${person[property]}"`);
// }
// let person = {
// 	name: "Max",
// 	age: 27
// };
// printPersonProperty(person, "age"); // Printing person property name: "Max"s
// let value: string | undefined | null = null;
// console.log(typeof value);
// value = 'hello';
// console.log(typeof value);
// value = undefined;
// console.log(typeof value);
// interface House {
// 	sqft: number;
// 	yard?: {
// 		sqft: number;
// 	};
// }
// function printYardSize(house: House) {
// 	const yardSize = house.yard?.sqft;
// 	if (yardSize === undefined) {
// 		console.log('No yard');
// 	} else {
// 		console.log(`Yard is ${yardSize} sqft`);
// 	}
// }
// let home: House = {
// 	sqft: 500
// };
// printYardSize(home); // Prints 'No yard'
// function getValue() {
//     return 'hello';
// }
// let value = getValue();
// console.log('value length: ' + value.length);
