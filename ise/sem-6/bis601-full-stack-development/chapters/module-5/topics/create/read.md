jsx
function AddProductForm() {
const [name, setName] = useState('');
const [price, setPrice] = useState('');

const handleSubmit = async (event) => {
event.preventDefault(); // Prevent page reload
const newProduct = { name, price: parseFloat(price) };

    try {
      const response = await fetch('/api/products', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newProduct) // Data sent as JSON in the request body
      });
      if (response.ok) {
        alert('Product added successfully!');
      }
    } catch (error) {
      console.error('Error:', error);
    }

};

return (
<form onSubmit={handleSubmit}>
<input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Product Name" required />
<input type="number" value={price} onChange={(e) => setPrice(e.target.value)} placeholder="Price" required />
<button type="submit">Add Product</button>
</form>
);
}
