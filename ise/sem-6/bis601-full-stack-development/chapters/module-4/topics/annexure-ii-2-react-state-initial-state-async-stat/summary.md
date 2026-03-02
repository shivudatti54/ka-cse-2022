# Annexure-II 2 React State: Initial State, Async State Initialization, Updating State, Lifting State Up, Event Handling, Stateless Components, Designin

## Initial State

- Initial state: The initial value of a state variable
- Examples:
  - `const initialState = { count: 0 };`
  - `const initialState = ["apple", "banana", "cherry"];`

## Async State Initialization

- Async state initialization: Initializing state in an async function
- Example:
  - `const [data, setData] = useState(async () => {
  const response = await fetch('https://api.example.com/data');
  return response.json();
});`

## Updating State

- Updating state: Changing the value of a state variable
- Rules:
  - Only update state in a React function component
  - Use the `useState` hook to update state
  - Use the `useEffect` hook to handle side effects
- Example:
  - `const [count, setCount] = useState(0);`
  - `setCount(count + 1);`

## Lifting State Up

- Lifting state up: Moving state to a parent component
- Examples:
  - Using `useState` in a child component and passing it to a parent component
  - Using `useContext` to access context from a parent component

## Event Handling

- Event handling: Handling events in React
- Examples:
  - `const handleClick = (e) => {
  console.log(`Button clicked!`);
  e.preventDefault();
}`

## Stateless Components

- Stateless components: Functional components without state
- Examples:
  - `const Greeting = (props) => {
  return <h1>Hello, {props.name}!</h1>;
}`

## Designin

- Designin: Design principles for React components
- Examples:
  - Keep it simple and stupid (KISS)
  - Don't repeat yourself (DRY)
  - Single responsibility principle (SRP)

Note: This summary is not exhaustive. Please refer to the React documentation for more information.
