# Python Modules - Summary

## Key Definitions and Concepts

- **Module**: A `.py` file containing reusable Python code (functions, classes, variables)
- **Import**: Mechanism to access modules using `import module_name`
- **Standard Library**: Built-in modules like `os`, `sys`, `json`, and `time`
- **`__name__`**: Special variable that equals `"__main__"` when file is executed directly
- **Package**: Directory containing modules and `__init__.py` file
- **Module Search Path**: List of directories (`sys.path`) where Python looks for modules

## Important Syntax and Structures

```python
# Basic import
import math
print(math.sqrt(16))

# Selective import
from datetime import datetime
print(datetime.now())

# Module alias
import numpy as np

# Main guard
if __name__ == "__main__":
    print("Executed as script")

# Path modification
import sys
sys.path.append("/custom/modules")
```

## Key Points

1. Modules prevent code duplication through reusable components
2. Use `import module` for whole module access, `from module import x` for specific items
3. Python searches for modules in: script directory → PYTHONPATH → standard library
4. Essential IoT modules:
   - `json` for data serialization
   - `time`/`datetime` for timestamps
   - `os` for file/system operations
5. Packages require `__init__.py` (can be empty) to be recognized
6. `sys.path.append()` temporarily adds directories to module search path
7. `__name__` check prevents code execution when module is imported
8. Common IoT module structure:
   - `sensors.py` (sensor interfaces)
   - `network.py` (MQTT/HTTP communication)
   - `utils.py` (data conversion helpers)

## Common Mistakes to Avoid

1. **Circular imports**: Module A imports B → B imports A → ImportError
2. **Missing `__init__.py`** in package directories
3. **Namespace collisions** when using `from module import *`
4. **Path errors** when importing cross-directory modules without proper path setup

## Revision Tips

1. Practice creating a 3-module IoT system:
   - Sensor simulator module
   - Data logger module
   - Alert generator module
2. Memorize 5 key standard library modules used in IoT and their main functions
3. Use `print(__name__)` in different files to understand execution context
4. Create a custom package with nested directories and test imports
