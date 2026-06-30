from fastapi import FastAPI

app = FastAPI(
    title="ShopSphere Order Service"
)


@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "order-service"
    }


@app.post("/orders")
def create_order(order: dict):

    return {
        "message": "Order created",
        "order": order
    }

