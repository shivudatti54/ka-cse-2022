javascript
const express = require('express');
const app = express();
app.use(express.json()); // Middleware to parse JSON bodies

// In-memory array for demonstration (data is lost on server restart)
let products = [
{ id: 1, name: 'Laptop', price: 80000 },
{ id: 2, name: 'Smartphone', price: 30000 }
];

// Stateless GET endpoint to fetch a product
// All necessary data is in the request: the `id` parameter
app.get('/products/:id', (req, res) => {
const productId = parseInt(req.params.id); // Get data from the request
const product = products.find(p => p.id === productId); // Process using only request data

    if (!product) {
        return res.status(404).json({ message: 'Product not found' });
    }
    res.json(product); // Send response

});

// Stateless POST endpoint to create a new product
// All necessary data is in the request body
app.post('/products', (req, res) => {
const newProduct = {
id: products.length + 1,
name: req.body.name, // Data from request body
price: req.body.price // Data from request body
};
products.push(newProduct); // Update resource (in a real app, this would be a database)
res.status(201).json(newProduct); // Send response
});

app.listen(3000, () => console.log('Server running on port 3000'));
