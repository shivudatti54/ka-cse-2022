python
# A simple unit test in Python-like pseudocode
def test_stack():
    s = Stack()
    s.push(10)
    s.push(20)
    
    # Test 1: Check if pop returns the last element pushed (LIFO)
    assert s.pop() == 20, "Test 1 Failed: LIFO property violated"
    
    # Test 2: Check if the stack is not empty after one pop
    assert s.is_empty() == False, "Test 2 Failed: Stack should not be empty"
    
    # Test 3: Check if pop returns the next element
    assert s.pop() == 10, "Test 3 Failed: Element mismatch"
    
    # Test 4: Check if stack is empty after all pops
    assert s.is_empty() == True, "Test 4 Failed: Stack should be empty"
    
    print("All unit tests passed!")