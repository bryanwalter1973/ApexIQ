from fastapi import FastAPI

app = FastAPI(
    title="ApexIQ API"
)


@app.get("/")
def home():
    return {
        
        "status":
        "ApexIQ Backend Running!"
    }