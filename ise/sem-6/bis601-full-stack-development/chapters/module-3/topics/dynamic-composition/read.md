javascript
app.get('/product/:id', (req, res) => {
const productId = req.params.id;
const productData = db.getProductById(productId); // Fetch from DB
res.render('product-template', { product: productData }); // Inject data into template
});
