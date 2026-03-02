# Functions - Summary

## Key Definitions and Concepts

- **Function**: Reusable code block defined with `def` that performs specific tasks
- **Parameters**: Variables declared in function definition (inputs)
- **Arguments**: Actual values passed to function during call
- **Return Statement**: Sends data back using `return` (optional)
- **Scope**: Variable visibility (Local vs Global)
- **Lambda**: Anonymous function defined with `lambda arguments: expression`

## Important Formulas and Theorems

```python
# Basic function structure
def function_name(param1, param2=default_value):
    '''Docstring'''
    # Function body
    return result

# Lambda function syntax
lambda x, y: x * y

# Variable arguments
def iot_logger(*sensor_readings):
    for reading in sensor_readings:
        process(reading)
```

## Key Points

1. Functions enable code reuse and modular IoT system design
2. Four parameter types:
   - Positional (required)
   - Keyword (name=value)
   - Default (param=default)
   - Variable-length (\*args, \*\*kwargs)
3. Return vs Print: Return sends data, print only displays it
4. Scope hierarchy: Local > Enclosing > Global > Built-in (LEGB rule)
5. Lambda functions for quick operations: `square = lambda x: x**2`
6. Recursion in IoT: Useful for hierarchical sensor networks
7. Decorators (@ notation) extend function behavior without modification

## Common Mistakes to Avoid

1. Modifying mutable default arguments:
   ```python
   # Wrong
   def add_sensor(sensor, sensors=[]):
   # Right
   def add_sensor(sensor, sensors=None):
       sensors = sensors or []
   ```
2. Confusing return value with print output
3. Ignoring variable scope leading to NameError
4. Incorrect parameter order: Positional args must come before keyword args

## Revision Tips

1. Practice writing IoT functions:
   - Sensor calibration: `calibrate(temp, offset=0.5)`
   - Alert system: `check_threshold(value, min, max)`
   - Data processing: `filter_noise(readings, window_size=3)`
2. Use flashcards for:
   - Parameter types syntax
   - Scope resolution order
   - Lambda vs regular functions
3. Trace execution of nested functions with different scopes
4. Memorize common function patterns:
   ```python
   # IoT data sender pattern
   def send_mqtt(topic, payload, qos=1):
       # Connection handling
       # Error checking
       return success_code
   ```
