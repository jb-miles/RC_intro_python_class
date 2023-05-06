# function for printing a log message
def log_message(*, message, level="INFO", **kwargs):
    print(f"[{level}] {message}")
    for key, value in kwargs.items():
        print(f"----{key} = {value}")

# function call for producing a log message
log_message(message="Task completed", comment="PID 635")