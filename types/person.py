import requests
import json


class Person:

    def __init__(self, urlAPI, token, fullName="", sort="+fullName", size=10, page=0):
        # Example url: "https://foo.modeus.org/schedule-calendar-v2/api/people/persons/search"
        self.url = urlAPI + "people/persons/search"
        self.token = token
        self.fullName = fullName
        self.sort = sort
        self.size = size
        self.page = page

    def get_payload(self):
        return {"fullName": self.fullName, "sort": self.sort, "size": self.size, "page": self.page}

    def get_id(self):
        headers = {
            "Authorization": self.token
        }

        payload = self.get_payload()
        response = requests.post(self.url, headers=headers, json=payload).json()

        persons = json.dumps(response["_embedded"]["persons"], sort_keys=True, indent=4).encode().decode(
            'unicode-escape')

        for element in persons.split("\n"):
            if '"id": ' in element:
                return element.split(": ")[1][1:-2:]

    def get_fullName(self):
        headers = {
            "Authorization": self.token
        }

        payload = self.get_payload()
        response = requests.post(self.url, headers=headers, json=payload).json()

        persons = json.dumps(response["_embedded"]["persons"], sort_keys=True, indent=4).encode().decode(
            'unicode-escape')

        for element in persons.split("\n"):
            if '"fullName"' in element:
                return element.split(": ")[1][1:-2:]

    def get_all(self):
        headers = {
            "Authorization": self.token
        }

        payload = self.get_payload()
        response = requests.post(self.url, headers=headers, json=payload).json()

        all_info_person = json.dumps(response["_embedded"], sort_keys=True, indent=4).encode().decode(
            'unicode-escape')

        return all_info_person