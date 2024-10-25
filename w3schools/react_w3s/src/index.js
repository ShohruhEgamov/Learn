import React from 'react';
import { useState, useEffect } from "react";
import { useState } from "react";
import { useState, useCallback } from "react";
import { useState, createContext, useContext } from "react";
import { useState, useEffect, useRef } from "react";
import { useReducer } from "react";
import ReactDOM from 'react-dom/client';
import './index.css';
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Blogs from "./pages/Blogs";
import Contact from "./pages/Contact";
import NoPage from "./pages/NoPage";
import App from './App';
import reportWebVitals from './reportWebVitals';
import Todos from "./Todos"




const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
	<React.StrictMode>
		<App />
	</React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();


// .......................................................................................................


const myFirstElement = <h1>Hello React!</h1>

const root1 = ReactDOM.createRoot(document.getElementById('root'));
root1.render(myFirstElement);

/*
You are now watching
the React file 'index.js'
through our 'Show React' tool.
*/


// .......................................................................................................


const myArray = ['apple', 'banana', 'orange'];

const myList = myArray.map((item) => <p>{item}</p>)

const container1 = document.getElementById('root');
const root2 = ReactDOM.createRoot(container1);
root2.render(myList);

// .......................................................................................................


const containers = document.getElementById('sandy');
const sandy = ReactDOM.createRoot(containers);
sandy.render(<p>Salom mening ismim Shohruh</p>)


// .......................................................................................................


const myelement = (
	<table>
		<tr>
			<th>Name</th>
		</tr>
		<tr>
			<td>John</td>
		</tr>
		<tr>
			<td>Elsa</td>
		</tr>
	</table>
);

const container = document.getElementById('root');
const root3 = ReactDOM.createRoot(container);
root3.render(myelement);


// .......................................................................................................

const olma = 5000
const myElement1 = (
	<ul>
		<li>Apples {olma} so'm</li>
		<li>Bananas</li>
		<li>Cherries</li>
	</ul>
);

const root4 = ReactDOM.createRoot(document.getElementById('root'));
root4.render(myElement1);



// .......................................................................................................

const myElement2 = <input type="text" />;

const root5 = ReactDOM.createRoot(document.getElementById('root'));
root5.render(myElement2);


// .......................................................................................................

const myElement3 = <h1 className="myclass">Salom Dunyo</h1>;

const root6 = ReactDOM.createRoot(document.getElementById('root'));
root6.render(myElement3);


// .......................................................................................................
const x1 = 11;
let text = "Goodbye";
if (x1 < 10) {
	text = "Hello";
}

if (x == 10) {
	text = "Bu juda ajoyib"
}

const myElement5 = <h1>{text}</h1>;

const root7 = ReactDOM.createRoot(document.getElementById('root'));
root7.render(myElement5);

// .......................................................................................................
const x = 5;

const myElement = <h1>{(x) < 10 ? "Hello" : "Goodbye"}</h1>;

const root8 = ReactDOM.createRoot(document.getElementById('root'));
root8.render(myElement);

// .......................................................................................................
function Car() {
	return <h2>Salom, Men bugun ishdaman</h2>
}

const root9 = ReactDOM.createRoot(document.getElementById('root'));
root9.render(<Car />)

function Car(props) {
	return <h2>Salom, Men bugun ishdaman. Ertaga {props.color} Moshina olaman</h2>
}

const root10 = ReactDOM.createRoot(document.getElementById('root'));
root10.render(<Car color='qora' />)


// .......................................................................................................
function Car() {
	return <h2>I am a Car!</h2>;
}

function Garage() {
	return (
		<>
			<h1>Who lives in my Garage?</h1>
			<Car />
		</>
	);
}

const root11 = ReactDOM.createRoot(document.getElementById('root'));
root11.render(<Garage />);


// .......................................................................................................
class Car extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			brand: " Ford ",
			model: " Mustang ",
			color: " red ",
			year: 1964
		};
	}
	render() {
		return (
			<div>
				<h1>My {this.state.brand}</h1>
				<p>
					It is a {this.state.color}
					{this.state.model}
					from {this.state.year}.
				</p>
			</div>
		)
	}
}

const root12 = ReactDOM.createRoot(document.getElementById('root'));
root12.render(<Car />)


// .......................................................................................................
import Car from './Car.js';

const root13 = ReactDOM.createRoot(document.getElementById('root'))
root13.render(<Car />)



// .......................................................................................................

class Car extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			brand: " Ford ",
			model: " Mustang ",
			color: " red ",
			year: 1964
		};
	}
	changeColor = () => {
		// Bu yerda setState Yangi rang kiritish uchun
		this.setState({ color: "blue" });
	}
	render() {
		return (
			<div>
				<h1>My {this.state.brand}</h1>
				<p>
					It is a {this.state.color}
					{this.state.model}
					from {this.state.year}.
				</p>
				<button
					type="button"
					onClick={this.changeColor}
				>Change color</button>
			</div>
		);
	}
}

const root14 = ReactDOM.createRoot(document.getElementById('root'));
root14.render(<Car />);


// .......................................................................................................
class Header extends React.Component {
	constructor(props) {
		super(props);
		this.state = { favoritecolor: "red" };
	}
	static getDerivedStateFromProps(props, state) {
		return { favoritecolor: props.favcol };
	}
	render() {
		return (
			<h1>My Favorite Color is {this.state.favoritecolor}</h1>
		);
	}
}

const root15 = ReactDOM.createRoot(document.getElementById('root'));
root15.render(<Header favcol="yellow" />);

// .......................................................................................................

class Header extends React.Component {
	constructor(props) {
		super(props);
		this.state = { favoritecolor: "red" };
	}
	componentDidMount() {
		setTimeout(() => {
			this.setState({ favoritecolor: "yellow" })
		}, 2000)
	}
	render() {
		return (
			<h1>My Favorite Color is {this.state.favoritecolor}</h1>
		);
	}
}
const root16 = ReactDOM.createRoot(document.getElementById('root'));
root16.render(<Header />);



// .......................................................................................................

class Header extends React.Component {
	constructor(props) {
		super(props);
		this.state = { favoritecolor: "yelow" };
	}
	static getDerivedStateFromProps(props, state) {
		return { favoritecolor: props.favcol };
	}
	changeColor = () => {
		this.setState({ favoritecolor: "blue" });
	}
	render() {
		return (
			<div>
				<h1>My Favorite Color is {this.state.favoritecolor}</h1>
				<button type="button" onClick={this.changeColor}>Change color</button>
			</div>
		);
	}
}

const root17 = ReactDOM.createRoot(document.getElementById('root'));
root17.render(<Header favcol="yelow" />);


// .......................................................................................................
class Header extends React.Component {
	constructor(props) {
		super(props);
		this.state = { favoritecolor: "red" };
	}
	shouldComponentUpdate() {
		return true;
	}
	changeColor = () => {
		this.setState({ favoritecolor: "blue" });
	}
	render() {
		return (
			<div>
				<h1>My Favorite Color is {this.state.favoritecolor}</h1>
				<button type="button" onClick={this.changeColor}>Change color</button>
			</div>
		);
	}
}

const root18 = ReactDOM.createRoot(document.getElementById('root'));
root18.render(<Header />);


// .......................................................................................................
class Header extends React.Component {
	constructor(props) {
		super(props);
		this.state = { favoritecolor: "red" };
	}
	componentDidMount() {
		setTimeout(() => {
			this.setState({ favoritecolor: "yellow" })
		}, 1000)
	}
	getSnapshotBeforeUpdate(prevProps, prevState) {
		document.getElementById("div1").innerHTML =
			"Before the update, the favorite was " + prevState.favoritecolor;
	}
	componentDidUpdate() {
		document.getElementById("div2").innerHTML =
			"The updated favorite is " + this.state.favoritecolor;
	}
	render() {
		return (
			<div>
				<h1>My Favorite Color is {this.state.favoritecolor}</h1>
				<div id="div1"></div>
				<div id="div2"></div>
			</div>
		);
	}
}

const root19 = ReactDOM.createRoot(document.getElementById('root'));
root19.render(<Header />);


// .......................................................................................................
class Container extends React.Component {
	constructor(props) {
		super(props);
		this.state = { show: true };
	}
	delHeader = () => {
		this.setState({ show: false });
	}
	render() {
		let myheader;
		if (this.state.show) {
			myheader = <Child />;
		};
		return (
			<div>
				{myheader}
				<button type="button" onClick={this.delHeader}>Delete Header</button>
			</div>
		);
	}
}

class Child extends React.Component {
	componentWillUnmount() {
		alert("The component named Header is about to be unmounted.");
	}
	render() {
		return (
			<h1>Hello World!</h1>
		);
	}
}

const root20 = ReactDOM.createRoot(document.getElementById('root'));
root20.render(<Container />);


// .......................................................................................................
function Car(props) {
	return <h2>I am a {props.brand.name}!</h2>;
}

function Garage() {
	const carInfo = { name: "Ford", model: "Mustang" };
	return (
		<>
			<h1>Who lives in my garage?</h1>
			<Car brand={carInfo} />
		</>
	);
}

const root21 = ReactDOM.createRoot(document.getElementById('root'));
root21.render(<Garage />);

// .......................................................................................................
function Football() {
	const shoot = () => {
		alert("Reactga hush kelibsiz!");
	}
	return (
		<button onClick={shoot}>Bu yerga bosing!</button>
	);
}
const root22 = ReactDOM.createRoot(document.getElementById('root'));
root22.render(<Football />);

// .......................................................................................................

function Football() {
	const shoot = (a) => {
		alert(a);
	}


	return (
		<button onClick={() => shoot("Goooaal")}>Bu yerni bos</button>
	);
}
function Football() {
	const shoot = (a, b) => {
		alert(b.type);
		/*
		'b' represents the React event that triggered the function.
	In this case, the 'click' event
		*/
	}

	return (
		<button onClick={(event) => shoot("Goal!", event)}>Take the shot!</button>
	);
}
const root23 = ReactDOM.createRoot(document.getElementById('root'));
root23.render(<Football />)


// .......................................................................................................
function MissedGoal() {
	return <h1>Missed</h1>
}

function MadeGoal() {
	return <h1>Goal</h1>
}

function Goal(props) {
	const isGoal = props.isGoal;
	if (isGoal) {
		return <MadeGoal />
	}
	return <MissedGoal />
}

const root24 = ReactDOM.createRoot(document.getElementById('root'));
root24.render(<Goal isGoal={true} />);

// .......................................................................................................
function Garage(props) {
	const cars = props.cars;
	return (
		<>
			<h1>Garage</h1>
			{cars.length > 0 &&
				<h2>
					You have {cars.length} cars in your garage
				</h2>
			}
		</>
	);
}

const cars = ['Ford', 'BMW', 'Audi', 'Ferrari', 'Lambargini'];
const root25 = ReactDOM.createRoot(document.getElementById('root'));
root25.render(<Garage cars={cars} />)


// .......................................................................................................
function MissedGoal() {
	return <h1>Missed</h1>
}

function MadeGoal() {
	return <h1>Goal</h1>
}

function Goal(props) {
	const isGoal = props.isGoal;
	return (
		// Bu yerda esa ture bo'lsa MadeGoal false bo'lsa MissedGoal Chiqarradi.
		<>
			{isGoal ? <MadeGoal /> : <MissedGoal />}
		</>
	)
}

const root26 = ReactDOM.createRoot(document.getElementById('root'));
root26.render(<Goal isGoal={false} />);

// .......................................................................................................
function Car(props) {
	return <li>I am a {props.brand}</li>
}

function Garage() {
	const cars = ['Ford', 'BMW', 'Ferrari']
	return (
		<>
			<h1>Who lives in my garage</h1>
			<ul>
				{cars.map((car) => <Car brand={car} />)}
			</ul>
		</>
	)
}

const root27 = ReactDOM.createRoot(document.getElementById('root'));
root27.render(<Garage />)


// .......................................................................................................
function Car(props) {
	return <li>I am a {props.brand}</li>
}

function Garage() {
	const cars = [
		{ id: 1, brand: 'Ford' },
		{ id: 2, brand: 'Mustang' },
		{ id: 3, brand: 'BMW' },
		{ id: 4, brand: 'Audi' }
	];

	return (
		<>
			<h1>Bu yerda moshinalar</h1>
			<ul>
				{cars.map((car) => <Car key={car.id} brand={car.brand} />)}
			</ul>
		</>
	);
}

const root28 = ReactDOM.createRoot(document.getElementById('root'));
root28.render(<Garage />)


// .......................................................................................................
function MyForm() {
	return (
		<form>
			<label>Enter your name
				<input type='text' />
			</label>
		</form>
	)
}

const root29 = ReactDOM.createRoot(document.getElementById('root'));
root29.render(<MyForm />)


// .......................................................................................................

function HiForm() {
	const [name, setName] = useState("");

	const handleSubmit = (event) => {
		event.preventDefault();
		alert(`The Name You Entered was: ${name}`)
	}

	return (
		<form onSubmit={handleSubmit}>
			<label>Enter your name
				<input
					type="text"
					value={name}
					onChange={(e) => setName(e.target.value)}
				/>
			</label>
			<input type="submit" />
		</form>
	)
}

const root30 = ReactDOM.createRoot(document.getElementById('root'));
root30.render(<HiForm />)



function MyForm() {
	const [name, setName] = useState("");

	const handleSubmit = (event) => {
		event.preventDefault();
		alert(`The name you entered was: ${name}`);
	}

	return (
		<form onSubmit={handleSubmit}>
			<label>Enter your name:
				<input
					type="text"
					value={name}
					onChange={(e) => setName(e.target.value)}
				/>
			</label>
			<input type="submit" />
		</form>
	)
}

const root31 = ReactDOM.createRoot(document.getElementById('root'));
root31.render(<MyForm />);


// .......................................................................................................
function MyForm() {
	const [inputs, setInputs] = useState({});

	const handleChange = (event) => {
		const name = event.target.name;
		const value = event.target.value;
		setInputs(values => ({ ...values, [name]: value }))
	}

	const handleSubmit = (event) => {
		event.preventDefault();
		console.log(inputs);
	}

	return (
		<form onSubmit={handleSubmit}>
			<label>Enter your name:
				<input
					type="text"
					name="username"
					value={inputs.username || ""}
					onChange={handleChange}
				/>
			</label>
			<label>Enter your famile:
				<input
					type="text"
					name="userfamile"
					value={inputs.userfamile || ""}
					onChange={handleChange}
				/>
			</label>
			<label>Enter your age:
				<input
					type="number"
					name="age"
					value={inputs.age || ""}
					onChange={handleChange}
				/>
			</label>
			<input type="submit" />
		</form>
	)
}

const root32 = ReactDOM.createRoot(document.getElementById('root'));
root32.render(<MyForm />);

// {username: 'Shohruh', userfamile: 'Egamov', age: '23'}
// age
// : 
// "23"
// userfamile
// : 
// "Egamov"
// username
// : 
// "Shohruh"
// [[Prototype]]
// : 
// Object


// .......................................................................................................
function MyForm() {
	const [textarea, setTextarea] = useState("The content of a textarea goes in the value attribute");


	const handleChange = (event) => {
		setTextarea(event.target.value)
	}

	return (
		<form>
			<textarea value={textarea} onChange={handleChange}></textarea>
		</form>
	)
}
const root33 = ReactDOM.createRoot(document.getElementById('root'));
root33.render(<MyForm />);


// .......................................................................................................

function MyForm() {
	const [myCar, setMyCar] = useState("Volvo");

	const handleChange = (event) => {
		setMyCar(event.target.value)
	}

	return (
		<form>
			<select value={myCar} onChange={handleChange}>
				<option value="Ford">Ford</option>
				<option value="Volvo">Volvo</option>
				<option value="Fiat">Fiat</option>
				<option value="Lasetti">Lasetti</option>
				<option value="Ferrari">Ferrari</option>
				<option value="bmw">BMW</option>
				<option value="Audi">Audi</option>
				<option value="Matiz">Matiz</option>
			</select>
		</form>
	)
}

const root34 = ReactDOM.createRoot(document.getElementById('root'));
root34.render(<MyForm />);


export default function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<Layout />}>
					<Route index element={<Home />} />
					<Route path="blogs" element={<Blogs />} />
					<Route path="contact" element={<Contact />} />
					<Route path="*" element={<NoPage />} />
				</Route>
			</Routes>
		</BrowserRouter>
	);
}

const root35 = ReactDOM.createRoot(document.getElementById('root'));
root35.render(<App />);


// .......................................................................................................
const App = () => {
	const [count, setCount] = useState(0);
	const [todos, setTodos] = useState(["todo 1", "todo 2"]);

	const increment = () => {
		setCount((c) => c + 1);
	};

	return (
		<>
			<Todos todos={todos} />
			<hr />
			<div>
				Count: {count}
				<button onClick={increment}>+</button>
			</div>
		</>
	);
};

const root36 = ReactDOM.createRoot(document.getElementById('root'));
root36.render(<App />);

// .......................................................................................................

const Header = () => {
	const myStyle = {
		color: "white",
		backgroundColor: "DodgerBlue",
		padding: "10px",
		fontFamily: "Sans-Serif"
	};
	return (
		<>
			<h1 style={myStyle}>Hello Style!</h1>
			<p>Add a little style!</p>
		</>
	);
}

const root37 = ReactDOM.createRoot(document.getElementById('root'));
root37.render(<Header />);


function FavoriteColor() {
	const [color, setColor] = useState("red");

	const Blue = () => {
		setColor('Blue')
	}
	const Yellow = () => {
		setColor('Yellow')
	}
	return (
		<>
			<div>
				My favorite color is {color}!
				<button onClick={Blue}>Blue</button>
				<button onClick={Yellow}>Yellow</button>
			</div>
		</>
	)
}

const root38 = ReactDOM.createRoot(document.getElementById('root'));
root38.render(<FavoriteColor />);


// .......................................................................................................
function Car() {
	const [car, setCar] = useState({
		brand: "Ford",
		model: "Mustang",
		year: "1964",
		color: "red"
	});

	const updateColor = () => {
		// Obyektni yangilab, faqat color qismini o'zgartiramiz
		setCar({ ...car, color: "blue" });
	};
	const updateModel = () => {
		setCar({ ...car, model: "BMW" })
	}
	const updateYear = () => {
		setCar({ ...car, year: "2005" })
	}

	return (
		<>
			<h1>My {car.brand}</h1>
			<p>
				It is a {car.color} {car.model} from {car.year}.
			</p>
			<button
				type="button"
				onClick={updateColor}
			>Blue</button>
			<button
				type="button"
				onClick={updateModel}
			>BMW</button>
			<button
				type="button"
				onClick={updateYear}
			>Year</button>
		</>
	)
}

const root39 = ReactDOM.createRoot(document.getElementById('root'));
root39.render(<Car />);



// .......................................................................................................
function Timer() {
	const [count, setCount] = useState(0);

	useEffect(() => {
		setTimeout(() => {
			setCount((count) => count + 1);
		}, 1000);

		// return () => clearTimeout(timer) 
		//   }, []);                                   <= // Bu yerda esa tozalash uchun
	}); // []); Bu faqat bir marotaba sanaydi

	return <h1>I have rendered {count} times!</h1>;
}

const root40 = ReactDOM.createRoot(document.getElementById('root'));
root40.render(<Timer />);


// .......................................................................................................
function Counter() {
	const [count, setCount] = useState(0);
	const [calculation, setCalculation] = useState(0);

	useEffect(() => {
		setCalculation(() => count * 2);
	}, [count]); // <- add the count variable here

	return (
		<>
			<p>Count: {count}</p>
			<button onClick={() => setCount((c) => c + 1)}>+</button>
			<p>Calculation: {calculation}</p>
		</>
	);
}

const root41 = ReactDOM.createRoot(document.getElementById('root'));
root41.render(<Counter />);


// .......................................................................................................

function Component1() {
	const [user, setUser] = useState("Shohruh EGAMOV");

	return (
		<>
			<h1>{`Hello ${user}!`}</h1>
			<Component2 user={user} />
		</>
	);
}

function Component2({ user }) {
	return (
		<>
			<h1>Component 2</h1>
			<Component3 user={user} />
		</>
	);
}

function Component3({ user }) {
	return (
		<>
			<h1>Component 3</h1>
			<Component4 user={user} />
		</>
	);
}

function Component4({ user }) {
	return (
		<>
			<h1>Component 4</h1>
			<Component5 user={user} />
		</>
	);
}

function Component5({ user }) {
	return (
		<>
			<h1>Component 5</h1>
			<h2>{`Hello ${user} again!`}</h2>
		</>
	);
}

const root42 = ReactDOM.createRoot(document.getElementById('root'));
root42.render(<Component1 />);


// .......................................................................................................

const UserContext = createContext();

function Component1() {
	const [user, setUser] = useState("Jesse Hall");

	return (
		<UserContext.Provider value={user}>
			<h1>{`Hello ${user}!`}</h1>
			<Component2 />
		</UserContext.Provider>
	);
}

function Component2() {
	return (
		<>
			<h1>Component 2</h1>
			<Component3 />
		</>
	);
}

function Component3() {
	return (
		<>
			<h1>Component 3</h1>
			<Component4 />
		</>
	);
}

function Component4() {
	return (
		<>
			<h1>Component 4</h1>
			<Component5 />
		</>
	);
}

function Component5() {
	const user = useContext(UserContext);

	return (
		<>
			<h1>Component 5</h1>
			<h2>{`Hello ${user} again!`}</h2>
		</>
	);
}

const root43 = ReactDOM.createRoot(document.getElementById('root'));
root43.render(<Component1 />);

// .......................................................................................................

function App() {
	const [inputValue, setInputValue] = useState("")
	const count = useRef(0)

	useEffect(() => {
		count.current = count.current + 1;
	});

	return (
		<>
			<input
				type="text"
				value={inputValue}
				onChange={(e) => setInputValue(e.target.value)}
			/>
			<h1>Yozuv soni: {count.current}</h1>
		</>
	);
}
const root44 = ReactDOM.createRoot(document.getElementById('root'));
root44.render(<App />);


function App() {
	const [inputValue, setInputValue] = useState("");
	const previousInputValue = useRef("");

	useEffect(() => {
		previousInputValue.current = inputValue;
	}, [inputValue]);

	return (
		<>
			<input
				type="text"
				value={inputValue}
				onChange={(e) => setInputValue(e.target.value)}
			/>
			<h2>Current Value: {inputValue}</h2>
			<h2>Previous Value: {previousInputValue.current}</h2>
		</>
	);
}

const root45 = ReactDOM.createRoot(document.getElementById('root'));
root45.render(<App />);


// .......................................................................................................
const initialTodos = [
	{
		id: 1,
		title: "Todo 1",
		complete: false,
	},
	{
		id: 2,
		title: "Todo 2",
		complete: false,
	},
];

const reducer = (state, action) => {
	switch (action.type) {
		case "COMPLETE":
			return state.map((todo) => {
				if (todo.id === action.id) {
					return { ...todo, complete: !todo.complete };
				} else {
					return todo;
				}
			});
		default:
			return state;
	}
};

function Todos() {
	const [todos, dispatch] = useReducer(reducer, initialTodos);

	const handleComplete = (todo) => {
		dispatch({ type: "COMPLETE", id: todo.id });
	};

	return (
		<>
			{todos.map((todo) => (
				<div key={todo.id}>
					<label>
						<input
							type="checkbox"
							checked={todo.complete}
							onChange={() => handleComplete(todo)}
						/>
						{todo.title}
					</label>
				</div>
			))}
		</>
	);
}

const root46 = ReactDOM.createRoot(document.getElementById('root'));
root46.render(<Todos />);


// .......................................................................................................

const App = () => {
	const [count, setCount] = useState(0);
	const [todos, setTodos] = useState([]);

	const increment = () => {
		setCount((c) => c + 1);
	};
	const addTodo = () => {
		setTodos((t) => [...t, "New Todo"]);
	};

	return (
		<>
			<Todos todos={todos} addTodo={addTodo} />
			<hr />
			<div>
				Count: {count}
				<button onClick={increment}>+</button>
			</div>
		</>
	);
};

const root48 = ReactDOM.createRoot(document.getElementById('root'));
root48.render(<App />);

const App = () => {
	const [count, setCount] = useState(0);
	const [todos, setTodos] = useState([]);

	const increment = () => {
		setCount((c) => c + 1);
	};
	const addTodo = useCallback(() => {
		setTodos((t) => [...t, "New Todo"]);
	}, [todos]);

	return (
		<>
			<Todos todos={todos} addTodo={addTodo} />
			<hr />
			<div>
				Count: {count}
				<button onClick={increment}>+</button>
			</div>
		</>
	);
};

const root47 = ReactDOM.createRoot(document.getElementById('root'));
root47.render(<App />);

// .......................................................................................................
const App = () => {
	const [count, setCount] = useState(0);
	const [todos, setTodos] = useState([]);
	const calculation = expensiveCalculation(count);

	const increment = () => {
		setCount((c) => c + 1);
	};
	const addTodo = () => {
		setTodos((t) => [...t, "New Todo"]);
	};

	return (
		<div>
			<div>
				<h2>My Todos</h2>
				{todos.map((todo, index) => {
					return <p key={index}>{todo}</p>;
				})}
				<button onClick={addTodo}>Add Todo</button>
			</div>
			<hr />
			<div>
				Count: {count}
				<button onClick={increment}>+</button>
				<h2>Expensive Calculation</h2>
				{calculation}
			</div>
		</div>
	);
};

const expensiveCalculation = (num) => {
	console.log("Calculating...");
	for (let i = 0; i < 1000000000; i++) {
		num += 1;
	}
	return num;
};

const root49 = ReactDOM.createRoot(document.getElementById('root'));
root49.render(<App />);

//.......................................................................................................
const Home = () => {
	const [data, setData] = useState(null);

	useEffect(() => {
		fetch("https://jsonplaceholder.typicode.com/todos")
			.then((res) => res.json())
			.then((data) => setData(data));
	}, []);

	return (
		<>
			{data &&
				data.map((item) => {
					return <p key={item.id}>{item.title}</p>;
				})}
		</>
	);
};

const root50 = ReactDOM.createRoot(document.getElementById('root'));
root50.render(<Home />);