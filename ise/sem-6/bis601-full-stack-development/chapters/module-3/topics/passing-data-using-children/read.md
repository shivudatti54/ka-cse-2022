jsx
// This is a presentational component. It doesn't care about the content.
const Card = (props) => {
return (
<div className="card" style={{ padding: '20px', border: '1px solid #ccc', margin: '10px' }}>
{props.children} {/_ The content from the parent is inserted here _/}
</div>
);
};
export default Card;
