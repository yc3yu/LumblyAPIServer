from datetime import datetime
from flask import abort

EXERCISE_TILE = {
    "0" : {
        "inlineIcon" : "https://cs210032000a530a4b5.blob.core.windows.net/lumblyimage/Physiotherapy.pdf?sv=2021-10-04&st=2023-02-20T04%3A15%3A54Z&se=2023-02-21T04%3A15%3A54Z&sr=b&sp=r&sig=KcxXy7KcIQPnf8%2FUCA%2BQL%2BZ6xd78U1f0xfY7nR%2BH7cw%3D",
        "exerciseName" : "Bird Dog",
        "reps" : "10",
        "exerciseImage" : "https://cs210032000a530a4b5.blob.core.windows.net/lumblyimage/Rectangle%208.pdf?sv=2021-10-04&st=2023-02-20T04%3A17%3A03Z&se=2023-02-21T04%3A17%3A03Z&sr=b&sp=r&sig=na2YfcN%2FlkuICpg8osimULXLUZPeum1O6IsFu%2BmazGk%3D"
    }
}

def read_all():
    return list(EXERCISE_TILE.values())