# **React Components Revision Notes**

## **I. React Components**

- A React component is a reusable piece of code that represents a part of the user interface.
- It has its own set of properties and state.
- Components can be functions or classes.

## **II. React Classes**

- A React class component is a class-based component that extends the `React.Component` class.
- It has its own lifecycle methods and state management.
- Example: `class Counter extends React.Component { ... }`

## **III. Composing Components**

- Composing components means combining multiple components to create a new component.
- Can be done using the `JSX` syntax or by creating a new component that renders other components.
- Example: `const Greeting = () => <div>Hello World!</div>; const Counter = () => <div>Count: {count}</div>; const App = () => <Greeting /> <Counter count={10} />`

## **IV. Passing Data Using Properties**

- Components can pass data to each other using properties.
- Properties are read-only and can be accessed using the `props` object.
- Example: `const Parent = () => <Child name="John" age={30} />; const Child = () => <div>Name: {props.name}, Age: {props.age}</div>;`

## **V. Passing Data Using Children**

- Components can pass data to their children using the `children` prop.
- Children are rendered inside the component.
- Example: `const Parent = () => <Child><span>Name: John</span></Child>; const Child = () => <div>{children}</div>;`

## **VI. Dynamic Composition**

- Dynamic composition means composing components at runtime.
- Can be done using the `React.createElement()` method or by using a library like React Router.
- Example: `const App = () => { const routes = ['home', 'about']; return <Route component={Home} route={routes[0]} />; };`

## **Important Formulas and Definitions**

- **React Virtual DOM**: A virtual representation of the real DOM, used for efficient rendering and updating of components.
- **JSX**: A syntax extension for JavaScript that allows you to write HTML-like code in your JavaScript files.

## **Theorems**

- **The Law of Demeter**: A component should only depend on its immediate children and not on its ancestors.
- **The Single Responsibility Principle**: A component should have only one reason to change.
