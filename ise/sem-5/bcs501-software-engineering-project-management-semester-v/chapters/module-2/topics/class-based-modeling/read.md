mermaid
classDiagram
class Customer {
-customerId: String
-name: String
-email: String
+placeOrder() : void
+viewOrderHistory() : List~Order~
}

    class Order {
        -orderId: String
        -orderDate: Date
        -status: String
        +calculateTotal() : double
        +updateStatus() : void
    }

    class Product {
        -productId: String
        -name: String
        -price: double
        -quantityInStock: int
    }

    class OrderItem {
        -quantity: int
        -subtotal: double
    }

    Customer "1" -- "*" Order : places
    Order "1" -- "*" OrderItem : contains
    OrderItem "*" -- "1" Product : refers-to
