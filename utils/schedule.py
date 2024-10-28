import datetime

def get_payload_campus(size=500, timeMin=f"{datetime.date.today().year}-{datetime.datetime.today().month}-{datetime.date.today().day - 1}", timeMax=f"{datetime.date.today().year}-{datetime.datetime.today().month}-{datetime.date.today().day}", id=str):
    return {"size": size,
            "timeMin": timeMin + "T21:00:00Z",
            "timeMax": timeMax + "T21:00:00Z",
            "roomId": [
                id,
            ]
            }

def get_payload_person(size=500, timeMin=f"{datetime.date.today().year}-{datetime.datetime.today().month}-{datetime.date.today().day - 1}", timeMax=f"{datetime.date.today().year}-{datetime.datetime.today().month}-{datetime.date.today().day}", id=str):
    return {"size": size,
            "timeMin": timeMin + "T21:00:00Z",
            "timeMax": timeMax + "T21:00:00Z",
            "attendeePersonId": [
                id,
            ]
            }


def get_headers(token):
    return {"Authorization": token}