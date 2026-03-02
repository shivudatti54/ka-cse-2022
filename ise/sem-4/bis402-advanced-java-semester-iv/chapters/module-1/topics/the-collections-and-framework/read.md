java
List<String> myList = new ArrayList<>();
myList.add("");
myList.add("Java");
myList.add("Collections");

Iterator<String> itr = myList.iterator();
while(itr.hasNext()) {
String element = itr.next();
System.out.println(element);
// itr.remove(); // Can remove the current element safely
}
