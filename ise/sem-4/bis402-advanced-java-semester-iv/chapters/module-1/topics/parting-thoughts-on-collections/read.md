java
List<String> list = new ArrayList<>();
list.add("");
list.add("Java");
list.add("Collections");

Iterator<String> itr = list.iterator();
while (itr.hasNext()) {
String element = itr.next();
if (element.equals("Java")) {
itr.remove(); // Safe removal using Iterator
}
}
