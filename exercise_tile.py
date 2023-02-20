from datetime import datetime
from flask import abort

EXERCISE_TILE = {
    "0" : {
        "inlineIcon" : "https://cs210032000a530a4b5.blob.core.windows.net/lumblyimage/Physiotherapy.png?sv=2021-10-04&st=2023-02-20T05%3A11%3A41Z&se=2023-02-21T05%3A11%3A41Z&sr=b&sp=r&sig=JU9hfpsfpyvRcz2nBv0QN%2FRv6ItBzqOze61IwY80lls%3D",
        "exerciseName" : "Bird Dog",
        "reps" : "10 Repetitions (per side)",
        "exerciseImage" : "https://cs210032000a530a4b5.blob.core.windows.net/lumblyimage/Rectangle%208.png?sv=2021-10-04&st=2023-02-20T05%3A12%3A06Z&se=2023-02-21T05%3A12%3A06Z&sr=b&sp=r&sig=%2FzlHkdkS8dbdiP46jBFvx3KRasY8mOFuNmGVvuBBmfI%3D"
    }
}

def read_all():
    return list(EXERCISE_TILE.values())