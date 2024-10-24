import requests
import json


class Campus:

    def __init__(self, urlAPI, token, name=str, sort="+building.name,+name", size=10, page=0, deleted="false"):
        # Example url: "https://foo.modeus.org/schedule-calendar-v2/api/people/persons/search"
        self.url = urlAPI + "/campus/rooms/search"
        self.token = token
        self.name = name
        self.sort = sort
        self.size = size
        self.page = page
        self.deleted = deleted

    def get_payload(self):
        return {"name": self.name, "sort": self.sort, "size": self.size, "page": self.page, "deleted": self.deleted}

    def get_id(self):
        headers = {
            "Authorization": self.token
        }

        payload = self.get_payload()
        response = requests.post(self.url, headers=headers, json=payload).json()

        persons = json.dumps(response["_embedded"]["rooms"], sort_keys=True, indent=4).encode().decode(
            'unicode-escape')

        for element in persons.split("\n"):
            if '"id": ' in element:
                return element.split(": ")[1][1:-2:]

    def get_name(self):
        headers = {
            "Authorization": self.token
        }

        payload = self.get_payload()
        response = requests.post(self.url, headers=headers, json=payload).json()

        persons = json.dumps(response["_embedded"]["rooms"], sort_keys=True, indent=4).encode().decode(
            'unicode-escape')
        is_deletedAtUtc = False
        for element in persons.split("\n"):
            if "deletedAtUtc" in element:
                is_deletedAtUtc = True
            if '"name": ' in element and is_deletedAtUtc:
                return element.split(": ")[1][1:-2:]

    # TODO: add get_nameShort, get_address(), check get_id()

    def get_all(self):
        headers = {
            "Authorization": self.token
        }

        payload = self.get_payload()
        response = requests.post(self.url, headers=headers, json=payload).json()

        all_info_person = json.dumps(response["_embedded"]["rooms"], sort_keys=True, indent=4).encode().decode(
            'unicode-escape')

        return all_info_person

