# test.py

from app_logger import app_logger_instance

app_logger_instance.info("This is an info message")
app_logger_instance.error("This is an error message")

print(dir(app_logger_instance))  # This will show you the available methods and attributes

