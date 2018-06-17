
def handle(event, context):
    state = {
        "directory":"home/voicenotes",
        "appState":{
            "status":"OK"
        }
    }

    body = {
        "actionType":"record_notes",
        "actionDetail": "recording",
        # "actionDetail":{
        #     "url_key" :random.choice(catUrls),
        # }
        "state":state
    }

    return body

#start voice notes app.
def start(event, context):
    state = {
        "directory":"home/voicenotes",
        "appState":{
            "status":"OK"
        }
    }

    body = {
        "actionType":"start",
        "actionDetail":"on start",
        "state":state
    }

    return body