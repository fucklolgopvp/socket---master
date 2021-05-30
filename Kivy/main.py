import requests

class Server():

    def get_info(self):
        import json

        url = "http://nexus15.beget.tech/site/mysql"
        req = requests.post(url)
        data = json.loads(req.text)
        return data


    def push_info(self, what_is, person_name = None, place = None, photo_url = None, data_time = None, phone = None, desc = None):
        url = "http://nexus15.beget.tech/site/mysql"

        data = {"what_is": what_is,
                "place": place,
                "person_name": person_name,
                "data_time": data_time,
                "phone": phone,
                "desc": desc,
                "photo_url": photo_url
                }

        req = requests.post(url, data)







