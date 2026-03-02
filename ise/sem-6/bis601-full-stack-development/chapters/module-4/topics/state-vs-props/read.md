jsx
// Parent Component (Passing the props)
function App() {
return (
<div>
<StudentCard name="Rahul Kumar" usn="1VT20CS001" grade="A" />
<StudentCard name="Priya Singh" usn="1VT20EC045" grade="S" />
</div>
);
}

// Child Component (Receiving and using the props)
function StudentCard(props) {
return (
<div className="card">
<h3>Name: {props.name}</h3>
<p>USN: {props.usn}</p>
<p>Grade: {props.grade}</p>
</div>
);
}
