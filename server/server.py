import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data.main import main, test_model_params
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# sys.path.append(os.path.join(os.path.dirname(__file__), '/tldr/data'))

api = FastAPI()

origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/")
def health_check():
    return {"status": "OK"}


@api.post("/search/{query}/{page}")
def search(query: str, page: int):
    search_results, search_time = main(query, test_model_params, page, mode)
    return {
        "search_time": search_time,
        "results": search_results,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server:api",
        host="0.0.0.0",
        reload=True,
        port=(int(os.environ.get("PORT", 8080)) or 5000),
    )
