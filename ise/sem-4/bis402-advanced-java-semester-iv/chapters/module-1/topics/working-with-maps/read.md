java
Map<String, Integer> map = new HashMap<>();
map.put("Alice", 95);
map.put("Bob", 85);

for (String key : map.keySet()) {
    Integer value = map.get(key);
    System.out.println(key + ": " + value);
}