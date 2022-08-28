import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from data.main import main, test_model_params
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# sys.path.append(os.path.join(os.path.dirname(__file__), '/tldr/data'))

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/")
def health_check():
    return {"status": "OK"}


@api.post("/search/{query}/{page}")
def search(query: str, page: int):
    # search_results, search_time = main(query, test_model_params, page, mode)
    search_time = 0.006

    # For testing so I don't waste CO:HERE credits
    search_results = {
        "Braised Short Ribs Recipe - Tastes Better From Scratch": {
            "url": "https://tastesbetterfromscratch.com/braised-short-ribs/",
            "author": "Lauren Allen",
            "date": "2020-02-24",
            "tldr": "The killer whale is a cetacean, a species of cetacean, which is recognized as having threatened its status. It is a member of the dolphin family. It is an orca, or orca, which is an oceanic dolphin. It is recognized as having threatened its status. ",
            "citation": "",
        },
        "Braised Short Ribs Recipe - Tastes Better From Scratch": {
            "url": "https://tastesbetterfromscratch.com/braised-short-ribs/",
            "author": "Lauren Allen",
            "date": "2020-02-24",
            "tldr": "The killer whale is a cetacean, a species of cetacean, which is recognized as having threatened its status. It is a member of the dolphin family. It is an orca, or orca, which is an oceanic dolphin. It is recognized as having threatened its status. ",
            "citation": "",
        },
    }
    return {
        "search_time": search_time,
        "results": search_results,
        "query": query,
        "page": page,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server:api",
        host="0.0.0.0",
        reload=True,
        port=(int(os.environ.get("PORT", 8080)) or 5000),
    )
