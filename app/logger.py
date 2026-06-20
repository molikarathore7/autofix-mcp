import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("app/logs", exist_ok=True)

logging.basicConfig(
    filename="app/logs/error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

print("Logger initialized successfully")