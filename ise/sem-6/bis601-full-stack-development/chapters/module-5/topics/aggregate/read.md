javascript
db.orders.aggregate([
  {
    $match: { total: { $gt: 100 } }
  }
])