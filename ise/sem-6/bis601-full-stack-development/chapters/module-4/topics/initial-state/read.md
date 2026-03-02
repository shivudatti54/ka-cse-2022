jsx
import React, { useState } from 'react';

const UserProfile = () => {
// Defining initial state for a user object
const [user, setUser] = useState({
name: '',
email: '',
isLoggedIn: false
});

// Defining initial state for a list (array)
const [todos, setTodos] = useState([]);

return (
<div>
<p>Welcome, {user.name}</p>
</div>
);
};
