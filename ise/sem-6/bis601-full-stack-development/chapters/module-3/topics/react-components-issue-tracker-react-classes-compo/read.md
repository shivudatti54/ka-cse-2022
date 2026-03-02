# **React Components: Issue Tracker, React Classes, Composing Components, Passing Data Using Properties, Passing Data Using Children, Dynamic Composition**

## **Introduction**

In this section, we will explore the various aspects of React components, including Issue Tracker, React Classes, Composing Components, Passing Data Using Properties, Passing Data Using Children, and Dynamic Composition.

## **Issue Tracker**

An issue tracker is a component that displays a list of issues or bugs that need to be fixed. It typically includes features such as:

- A list of issues
- Filtering and sorting capabilities
- Ability to mark issues as resolved
- Ability to assign issues to specific users

### Example:

```jsx
import React, { useState } from 'react';
import './issueTracker.css';

function IssueTracker() {
  const [issues, setIssues] = useState([
    { id: 1, title: 'Bug 1', description: 'This is bug 1' },
    { id: 2, title: 'Bug 2', description: 'This is bug 2' },
    { id: 3, title: 'Bug 3', description: 'This is bug 3' },
  ]);

  const handleResolve = (id) => {
    const updatedIssues = issues.map((issue) => {
      if (issue.id === id) {
        issue.resolved = true;
      }
      return issue;
    });
    setIssues(updatedIssues);
  };

  return (
    <div>
      <h1>Issue Tracker</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Description</th>
            <th>Resolved</th>
          </tr>
        </thead>
        <tbody>
          {issues.map((issue) => (
            <tr key={issue.id}>
              <td>{issue.id}</td>
              <td>{issue.title}</td>
              <td>{issue.description}</td>
              <td>
                <button onClick={() => handleResolve(issue.id)}>Resolve</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default IssueTracker;
```

## **React Classes**

React classes are a way to create React components using classes instead of functions. They provide more features and flexibility than functional components.

### Key Features:

- Lifecycle methods (e.g. `componentDidMount`, `componentWillUnmount`)
- State management
- Methods (e.g. `this.setState`, `this.props`)

### Example:

```jsx
import React, { Component } from 'react';

class Counter extends Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>Increment</button>
      </div>
    );
  }
}

export default Counter;
```

## **Composing Components**

Composing components is a technique where you create a new component by combining multiple existing components. This allows you to create complex components by breaking them down into smaller, more manageable pieces.

### Example:

```jsx
import React from 'react';
import Header from './Header';
import Footer from './Footer';

function Layout({ children }) {
  return (
    <div>
      <Header />
      <main>{children}</main>
      <Footer />
    </div>
  );
}

export default Layout;
```

## **Passing Data Using Properties**

React components can pass data to other components using properties. There are two types of properties: props (short for "properties") and ref.

### Props:

- Can be passed from a parent component to a child component
- Can be used to pass data from a parent component to a child component

### Example:

```jsx
import React from 'react';

function Parent() {
  const [name, setName] = React.useState('John Doe');

  return (
    <div>
      <Child name={name} />
      <button onClick={() => setName('Jane Doe')}>Update Name</button>
    </div>
  );
}

function Child(props) {
  return (
    <div>
      <p>Hello, {props.name}!</p>
    </div>
  );
}

export default Parent;
```

## **Passing Data Using Children**

React components can also pass data to other components using the `children` prop. The `children` prop is a special prop that represents the content of the component.

### Example:

```jsx
import React from 'react';

function Parent() {
    return (
        <div>
            <Child>John Doe</Child>
            <ChildJane Doe</Child>
        </div>
    );
}

function Child(props) {
    return (
        <div>
            <p>Hello, {props}</p>
        </div>
    );
}

export default Parent;
```

## **Dynamic Composition**

Dynamic composition is a technique where you create a component by combining multiple components at runtime. This allows you to create complex components by dynamically adding or removing components.

### Example:

```jsx
import React from 'react';

function DynamicComponent() {
  const components = [<ComponentA />, <ComponentB />, <ComponentC />];

  return <div>{components}</div>;
}

export default DynamicComponent;
```

In this study material, we have covered the key aspects of React components, including Issue Tracker, React Classes, Composing Components, Passing Data Using Properties, Passing Data Using Children, and Dynamic Composition. These concepts form the foundation of building complex React applications.
