```java
// Demonstration of String manipulation methods in Java

public class StringMethodsDemo {
 public static void main(String[] args) {

 // 1. trim() and strip() - Removing whitespace
 String withSpaces = " Hello World ";
 System.out.println("Original: '" + withSpaces + "'");
 System.out.println("trim(): '" + withSpaces.trim() + "'");

 String withUnicode = "\u2003Hello\u2003"; // Unicode em space
 System.out.println("strip(): '" + withUnicode.strip() + "'");

 // 2. substring() - Extracting portions of strings
 String message = "Welcome to Advanced Java Programming";
 System.out.println("\nOriginal: " + message);
 System.out.println("substring(11): " + message.substring(11));
 System.out.println("substring(0, 7): " + message.substring(0, 7));

 // 3. split() - Parsing strings into arrays
 String csvData = "apple,banana,cherry,date";
 String[] fruits = csvData.split(",");
 System.out.println("\nSplit result:");
 for (String fruit : fruits) {
 System.out.println(" - " + fruit);
 }

 // Handling edge cases with limit parameter
 String numbers = "one:two:three:four:five";
 String[] limited = numbers.split(":", 3);
 System.out.println("Split with limit=3:");
 for (String num : limited) {
 System.out.println(" - " + num);
 }

 // 4. replace() and replaceAll()
 String text = "The quick brown fox jumps over the lazy dog";
 System.out.println("\nOriginal: " + text);
 System.out.println("replace('o', 'X'): " + text.replace('o', 'X'));
 System.out.println("replaceAll(\"\\\\w{4}\", \"XXXX\"): " +
 text.replaceAll("\\w{4}", "XXXX"));

 // 5. matches() - Regular expression validation
 String email = "student@university.edu";
 String emailPattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";
 System.out.println("\nEmail: " + email);
 System.out.println("Matches email pattern: " + email.matches(emailPattern));

 String phone = "123-456-7890";
 String phonePattern = "\\d{3}-\\d{3}-\\d{4}";
 System.out.println("Phone: " + phone);
 System.out.println("Matches phone pattern: " + phone.matches(phonePattern));

 // 6. format() - Creating formatted output
 String formatted = String.format("Name: %-10s | Age: %3d | Grade: %5.2f",
 "Alice", 21, 85.567);
 System.out.println("\nFormatted: " + formatted);

 // Using format with different specifiers
 System.out.println(String.format("Hex: %x", 255));
 System.out.println(String.format("Octal: %o", 255));
 System.out.println(String.format("Scientific: %e", 1234.56));

 // 7. contains() - Substring checking
 String javaString = "Welcome to Advanced Java";
 System.out.println("\nString: " + javaString);
 System.out.println("contains(\"Java\"): " + javaString.contains("Java"));
 System.out.println("contains(\"Python\"): " + javaString.contains("Python"));
 }
}
```
