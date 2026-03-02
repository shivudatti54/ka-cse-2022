java
String message = "Hello, Advanced Java!";

int firstComma = message.indexOf(','); // firstComma = 5
int firstA = message.indexOf('A'); // firstA = 7
int lastA = message.lastIndexOf('a'); // lastA = 17
int notFound = message.indexOf('z'); // notFound = -1

// Search starting from index 10
int secondA = message.indexOf('a', 10); // secondA = 16 (finds 'a' in "Advanced")
