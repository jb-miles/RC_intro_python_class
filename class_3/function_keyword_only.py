# function for printing a log message
def log_message(*, message, level="INFO"):
    print(f"[{level}] {message}")


# function call for producing a log message
log_message(message="Task completed")
log_message(message="Temperature outside range", level="WARNING")
