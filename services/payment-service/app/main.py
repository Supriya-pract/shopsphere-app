from fastapi import FastAPI


app = FastAPI(
title="Payment Service"
)


@app.get("/health")
def health():

    return {
        "status":"UP",
        "service":"payment-service"
    }


@app.post("/payments")
def payment(data:dict):

    return {
        "message":"payment processed",
        "data":data
    }

