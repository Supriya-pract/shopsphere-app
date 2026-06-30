from fastapi import FastAPI


app = FastAPI(
title="Inventory Service"
)


@app.get("/health")
def health():

    return {
        "status":"UP",
        "service":"inventory-service"
    }


@app.get("/inventory/{item}")
def check(item:str):

    return {
        "item":item,
        "available":True
    }

