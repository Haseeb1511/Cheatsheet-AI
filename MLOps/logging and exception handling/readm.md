## ✅ How to Use Logger and Custom Exception

### 📜 Logger Setup

```python
from logger import configure_logger

# Configure your logger with a specific name
logger = configure_logger("your_logger_name")

# Example usage
logger.info("This is an info message.")
logger.error("This is an error message.")
```

---

### ⚡ Handling Exceptions with a Custom Exception

```python
import sys
from exception import MyException

try:
    # Your code that may raise an exception
    pass

except Exception as e:
    # Raise your custom exception with original traceback
    raise MyException(e, sys) from e
```


