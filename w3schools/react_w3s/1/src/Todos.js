// // import { memo } from "react";
// const Todos = ({ todos }) => {
// 	console.log("bosilgan son");
// 	return (
// 		<>
// 			<h2>My Todos</h2>
// 			{todos.map((todo, index) => {
// 				return <p key={index}>{todo}</p>;
// 			})}
// 		</>
// 	);
// };

// export default Todos;


import { memo } from "react";

// const Todos = ({ todos, addTodo }) => {
// 	console.log("child render");
// 	return (
// 		<>
// 			<h2>My Todos</h2>
// 			{todos.map((todo, index) => {
// 				return <p key={index}>{todo}</p>;
// 			})}
// 			<button onClick={addTodo}>Add Todo</button>
// 		</>
// 	);
// };

// export default memo(Todos);

const Todos = ({ todos, addTodo }) => {
	console.log("child render");
	return (
		<>
			<h2>My Todos</h2>
			{todos.map((todo, index) => {
				return <p key={index}>{todo}</p>;
			})}
			<button onClick={addTodo}>Add Todo</button>
		</>
	);
};

export default memo(Todos);