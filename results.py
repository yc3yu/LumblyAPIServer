from datetime import datetime
from flask import abort

RESULTS = { 
    "0": {
        "id": 40001,
        "exercises": ["Bird dog", "Deadlift", "Cat cow"],
        "summaryGraphTitle": "AVERAGE FORM CORRECTNESS",
        "summaryGraphXLabel": "graph x label",
        "summaryGraphYLabel": "graph y label",
        # "problems": [
        #     {
        #         "icon": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/63130508-c575-4c8d-8055-4bc58cc9e71d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T210305Z&X-Amz-Expires=86400&X-Amz-Signature=44df28c426d3405f7340c0139d480ee709631582957fedb26aa49c54863f6671&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject",
        #         "name": "Leg lifted too high",
        #     },
        #     {
        #         "icon": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fccf2da3-94fb-4c3b-b7b2-1980028bbd86/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T210301Z&X-Amz-Expires=86400&X-Amz-Signature=defaceb1cb83ed101c5fc9597ddd874f87f4abd7d082cc4be6584eed7c1f0004&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject",
        #         "name": "Arm lifted too high",
        #     },
        #     {
        #         "icon": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/63130508-c575-4c8d-8055-4bc58cc9e71d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T210305Z&X-Amz-Expires=86400&X-Amz-Signature=44df28c426d3405f7340c0139d480ee709631582957fedb26aa49c54863f6671&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject",
        #         "name": "Leg lifted too low",
        #     },
        #     {
        #         "icon": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fccf2da3-94fb-4c3b-b7b2-1980028bbd86/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T210301Z&X-Amz-Expires=86400&X-Amz-Signature=defaceb1cb83ed101c5fc9597ddd874f87f4abd7d082cc4be6584eed7c1f0004&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject",
        #         "name": "Arm lifted too low",
        #     },
        #     {
        #         "icon": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/63130508-c575-4c8d-8055-4bc58cc9e71d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T210305Z&X-Amz-Expires=86400&X-Amz-Signature=44df28c426d3405f7340c0139d480ee709631582957fedb26aa49c54863f6671&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject",
        #         "name": "Back arched",
        #     },
        #     {
        #         "icon": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fccf2da3-94fb-4c3b-b7b2-1980028bbd86/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T210301Z&X-Amz-Expires=86400&X-Amz-Signature=defaceb1cb83ed101c5fc9597ddd874f87f4abd7d082cc4be6584eed7c1f0004&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject",
        #         "name": "Neck overextended",
        #     },
        # ],
    }
}

def read_all():
    return list(RESULTS.values())

def read_one(id):
    if id in RESULTS:
        return RESULTS[id]
    else:
        abort(
            404, f"Results with id {id} not found"
        )

def create(results):
    id = results.get("id")
    summaryGraphTitle  = results.get("summaryGraphTitle", "")
    summaryGraphXLabel = results.get("summaryGraphXLabel", "")
    summaryGraphYLabel = results.get("summaryGraphYLabel", "")
    problems           = results.get("problems", [])

    if id and id not in RESULTS:
        RESULTS[id] = {
            "id": id,
            "summaryGraphTitle" : summaryGraphTitle,
            "summaryGraphXLabel": summaryGraphXLabel,
            "summaryGraphYLabel": summaryGraphYLabel,
            "problems"          : problems,
        }
        return RESULTS[id], 201
    else:
        abort(
            406,
            f"Results with id {id} already exist",
        )

def update(id, results):
    if id in RESULTS:
        RESULTS[id]["summaryGraphTitle"]  = results.get("summaryGraphTitle",  RESULTS[id]["summaryGraphTitle"])
        RESULTS[id]["summaryGraphXLabel"] = results.get("summaryGraphXLabel", RESULTS[id]["summaryGraphXLabel"])
        RESULTS[id]["summaryGraphYLabel"] = results.get("summaryGraphYLabel", RESULTS[id]["summaryGraphYLabel"])
        RESULTS[id]["problems"]           = results.get("problems",           RESULTS[id]["problems"])
        return RESULTS[id]
    else:
        abort(
            404,
            f"Results with id {id} not found"
        )

def delete(id):
    if id in RESULTS:
        del RESULTS[id]
        return make_response(
            f"{id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Results with id {id} not found"
        )