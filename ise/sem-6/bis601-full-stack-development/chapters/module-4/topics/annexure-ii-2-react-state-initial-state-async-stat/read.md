# **Annexure-II 2 React State: Initial State, Async State Initialization, Updating State, Lifting State Up, Event Handling, Stateless Components, Designin**

## **Table of Contents**

1. [Initial State](#initial-state)
2. [Async State Initialization](#async-state-initialization)
3. [Updating State](#updating-state)
4. [Lifting State Up](#lifting-state-up)
5. [Event Handling](#event-handling)
6. [Stateless Components](#stateless-components)
7. [Designin](#designin)

## **1. Initial State**

The initial state of a React component is the starting point for the component's lifecycle. It is the value of the component's state when the component is first rendered.

**Definition:** Initial state = The state of the component at the beginning of its lifecycle.

**Example:**

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

In this example, the initial state of the `count` variable is `0`.

## **2. Async State Initialization**

Async state initialization refers to the process of initializing state in a React component when it receives data from an external source, such as a server or a database.

**Definition:** Async state initialization = Initializing state in a React component when it receives data from an external source.

**Example:**

```jsx
import React, { useState, useEffect } from 'react';

function FetchData() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  return <div>{data ? <p>Data: {data}</p> : <p>Loading...</p>}</div>;
}
```

In this example, the `fetch` API is used to retrieve data from an external source. The `useState` hook is used to initialize the `data` state variable. The `useEffect` hook is used to handle the async initialization of the state.

## **3. Updating State**

Updating state in a React component refers to the process of changing the value of a component's state.

**Definition:** Updating state = Changing the value of a component's state.

**Example:**

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

In this example, the `setCount` function is used to update the value of the `count` state variable.

## **4. Lifting State Up**

Lifting state up refers to the process of moving state from a child component to a parent component.

**Definition:** Lifting state up = Moving state from a child component to a parent component.

**Example:**

```jsx
import React from 'react';

function Parent() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <Child count={count} />
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

function Child(props) {
  return (
    <div>
      <p>Count: {props.count}</p>
    </div>
  );
}
```

In this example, the state is lifted up from the `Child` component to the `Parent` component.

## **5. Event Handling**

Event handling refers to the process of handling user interactions, such as clicks or form submissions.

**Definition:** Event handling = Handling user interactions, such as clicks or form submissions.

**Example:**

```jsx
import React from 'react';

function Button() {
  const handleClick = () => {
    console.log('Button clicked!');
  };

  return <button onClick={handleClick}>Click me!</button>;
}
```

In this example, the `handleClick` function is used to handle the click event on the button.

## **6. Stateless Components**

Stateless components are components that do not have any state.

**Definition:** Stateless components = Components that do not have any state.

**Example:**

```jsx
import React from 'react';

function Greeting() {
  return (
    <div>
      <h1>Hello, world!</h1>
    </div>
  );
}
```

In this example, the `Greeting` component is a stateless component.

## **7. Designin**

Designin is the process of designing and creating user interfaces for applications.

**Definition:** Designin = Designing and creating user interfaces for applications.

**Best Practices:**

- Use a consistent design language throughout the application.
- Use responsive design to ensure that the application works on different devices.
- Use accessibility features to ensure that the application is usable by everyone.

**Conclusion:**
React is a powerful library for building user interfaces. By understanding the concepts of initial state, async state initialization, updating state, lifting state up, event handling, stateless components, and designin, you can build complex and user-friendly applications.
