class Logger:
    def log(self, message, msg_type="info"):
        msg_type = msg_type.lower() 

        if msg_type == "error":
            print(f"[ERROR] {message}")
        elif msg_type == "warning":
            print(f"[WARNING] {message}")
        elif msg_type == "info":
            print(f"[INFO] {message}")
        else:
            print(f"[UNKNOWN TYPE] {message}")

logger = Logger()

logger.log("This is an informational message")  
logger.log("This is a warning message", "warning")
logger.log("This is an error message", "error")
logger.log("This is a debug message", "debug")