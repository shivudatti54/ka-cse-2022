python
# Pseudo-code for testing a Stack's push and pop operations
def test_stack_operations():
    stack = new Stack()  # Create a new stack instance

    # Test 1: Push an element and check top
    stack.push(10)
    assert stack.top() == 10  # This should be true

    # Test 2: Push another element, then pop and check
    stack.push(20)
    popped_value = stack.pop()
    assert popped_value == 20  # This should be true
    assert stack.top() == 10   # This should be true

    # Test 3: Pop the last element and check if empty
    stack.pop()
    assert stack.isEmpty() == True  # This should be true

    print("All tests passed!")