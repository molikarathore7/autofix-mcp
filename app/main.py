from fastapi import FastAPI
import logging
import app.logger

app = FastAPI()

# Test log entry when application starts
logging.error("Application Started - Test Log Entry")

# Temporary in-memory storage
customers = []


@app.get("/")
def home():
    return {
        "message": "Customer Service Running"
    }


@app.post("/customer")
def add_customer(name: str, email: str):

    customers.append(
        {
            "name": name,
            "email": email
        }
    )

    return {
        "status": "added",
        "customer": {
            "name": name,
            "email": email
        }
    }


@app.get("/customers")
def get_customers():
    return customers


# INTENTIONAL BUG ENDPOINT
# This endpoint is purposely broken
# for the AI AutoFix demonstration.

@app.get("/customer-email")
def get_email():

    try:

        customer = customers[0]

        # Intentional Bug
        return customer["email_address"]

    except Exception as e:

        logging.error(f"Customer Email Error: {str(e)}")

        return {
            "error": str(e)
        }