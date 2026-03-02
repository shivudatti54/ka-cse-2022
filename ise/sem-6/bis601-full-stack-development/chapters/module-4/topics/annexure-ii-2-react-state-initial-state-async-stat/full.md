# Annexure-II 2 React State: Initial State, Async State Initialization, Updating State, Lifting State Up, Event Handling, Stateless Components, Designin

**Table of Contents**

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [Understanding State in React](#understanding-state-in-react)
4. [Initial State](#initial-state)
5. [Async State Initialization](#async-state-initialization)
6. [Updating State](#updating-state)
7. [Lifting State Up](#lifting-state-up)
8. [Event Handling](#event-handling)
9. [Stateless Components](#stateless-components)
10. [Designin](#designin)
11. [Conclusion](#conclusion)
12. [Further Reading](#further-reading)

## **Introduction**

In this annexure, we will delve into the world of state management in React. State is a fundamental concept in React, and understanding it is crucial for building complex and interactive user interfaces. In this chapter, we will cover the basics of state, initial state, async state initialization, updating state, lifting state up, event handling, stateless components, and designin.

## **Historical Context**

React, a JavaScript library developed by Facebook, was first released in 2013. Initially, React focused on virtual DOM (a lightweight in-memory representation of the real DOM) and component-based architecture. Over time, React evolved to include a robust state management system.

In React 0.14, the introduction of state and props made React more suitable for building complex, interactive applications. Since then, React has become one of the most popular front-end libraries, with a vast ecosystem of tools and libraries to support building robust and scalable applications.

## **Understanding State in React**

In React, state refers to the data that an application intends to use to determine its behavior. State is used to store information that can change over time, such as user input, API responses, or user data.

State is divided into two types:

- **Local State**: State that is managed by a single component. Local state is used to store data that is specific to a single component.
- **Global State**: State that is shared across multiple components. Global state is used to store data that needs to be accessed by multiple components.

## **Initial State**

Initial state refers to the initial value of state when a component is first rendered. The initial state is set when the component is mounted, and it is used to determine the initial display of the component.

Here's an example of initial state in React:

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

In this example, the initial state of `count` is set to `0`.

## **Async State Initialization**

Async state initialization refers to the process of initializing state in a way that takes into account asynchronous data from APIs or other external sources.

Here's an example of async state initialization in React:

```jsx
import React, { useState, useEffect } from 'react';

function FetchData() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/data')
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => setError(error));
  }, []);

  return (
    <div>
      {data ? <p>Data: {data}</p> : <p>Loading...</p>}
      {error ? <p>Error: {error.message}</p> : null}
    </div>
  );
}
```

In this example, we use `useEffect` to fetch data from an API and update the state accordingly.

## **Updating State**

Updating state refers to the process of changing the value of state over time. This can be done using the `setState` method.

Here's an example of updating state in React:

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

In this example, we use the `setCount` method to update the `count` state.

## **Lifting State Up**

Lifting state up refers to the process of moving state from a component down to a parent component. This is done to share state between multiple components.

Here's an example of lifting state up in React:

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

function App() {
  return (
    <div>
      <Counter />
      <Counter />
    </div>
  );
}
```

In this example, we move the `count` state up to the `App` component to share it between multiple instances of the `Counter` component.

## **Event Handling**

Event handling refers to the process of responding to user interactions, such as clicks or keyboard input.

Here's an example of event handling in React:

```jsx
import React, { useState } from 'react';

function Button() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  return <button onClick={handleClick}>Click me!</button>;
}
```

In this example, we use the `handleClick` function to update the `count` state when the button is clicked.

## **Stateless Components**

Stateless components are components that do not have their own state. They rely on props to determine their behavior.

Here's an example of a stateless component in React:

```jsx
import React from 'react';

function Button() {
  return <button>Click me!</button>;
}
```

In this example, we define a `Button` component without any state.

## **Designin**

Designin refers to the process of designing and organizing the structure of an application.

Here's an example of designin in React:

```jsx
import React from 'react';
import { Container, Button } from './styles';

function Button() {
  return <Button>Click me!</Button>;
}

function App() {
  return (
    <Container>
      <Button />
    </Container>
  );
}
```

In this example, we use styled components to design and organize the structure of the application.

## **Conclusion**

In this annexure, we covered the basics of state management in React, including initial state, async state initialization, updating state, lifting state up, event handling, stateless components, and designin.

By understanding these concepts, developers can build complex and interactive user interfaces using React.

## **Further Reading**

- [React documentation](https://reactjs.org/docs/getting-started.html)
- [React state management](https://reactjs.org/docs/state-and-lifecycle.html)
- [React hooks](https://reactjs.org/docs/hooks-intro.html)
- [Styled components](https://styled-components.com/docs/basics)

Note: The code snippets provided in this annexure are just examples to illustrate the concepts discussed.
