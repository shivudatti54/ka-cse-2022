java
@Test
void testPopOnEmptyStack() {
    Stack stack = new Stack(5);
    assertThrows(StackEmptyException.class, () -> {
        stack.pop();
    });
}

@Test
void testPopOnFullStack() {
    Stack stack = new Stack(2);
    stack.push(10);
    stack.push(20);
    int result = stack.pop();
    assertEquals(20, result); // Check if correct value is returned
    assertEquals(1, stack.size()); // Check if size is updated correctly
}