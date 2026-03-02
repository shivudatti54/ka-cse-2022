jsx
import { useState } from 'react';

function Counter() {
const [count, setCount] = useState(0); // Initial state is 0

const increment = () => {
// Correct: Using the setter function
setCount(count + 1);

    // WRONG: This will not work
    // count = count + 1;

};

const decrement = () => {
setCount(count - 1);
};

return (
<div>
<p>Count: {count}</p>
<button onClick={increment}>+</button>
<button onClick={decrement}>-</button>
</div>
);
}
export default Counter;
