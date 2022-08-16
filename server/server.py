from fastapi import FastAPI
import os

api = FastAPI()

@api.get("/")
def health_check():
    return {"status": "OK"}
    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server:api",
        host="0.0.0.0", 
        reload=True,
        port=(int(os.environ.get("PORT", 8080)) or 5000)
    )