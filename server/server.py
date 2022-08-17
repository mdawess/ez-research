import os
from fastapi import FastAPI
from data.main import main, test_model_params
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

api = FastAPI()

@api.get("/")
def health_check():
    return {"status": "OK"}

@api.get("/search/{query}/{page}")
def search(query: str, page: int):
    search_results, search_time = main(query, test_model_params, page)
    return {"search_time": search_time, "results": search_results}
    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server:api",
        host="0.0.0.0", 
        reload=True,
        port=(int(os.environ.get("PORT", 8080)) or 5000)
    )
    # print(main("Braised Short Ribs", test_model_params, 1))