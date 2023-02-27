import requests
import json

class GetPrograms:
    def __init__(self):
        pass

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        response = requests.get(URL)
        return response.content

    def program_school(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list

# programs = GetPrograms.get_programs()
# print(programs)

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)

# # You can modify the code as follows to accept a URL through an 
# # initialize method and use a general load_json method to retrieve JSON 
# # from any provided URL:

# import requests

# class JSONLoader:
#     def __init__(self, url):
#         self.url = url
        
#     def load_json(self):
#         response = requests.get(self.url)
#         return response.json()
    
# # Now you can create an instance of the JSONLoader class by passing in a URL, 
# # and call the load_json method on the instance to retrieve the JSON data 
# # from that URL:

# json_loader = JSONLoader("http://data.cityofnewyork.us/resource/uvks-tn5n.json")
# json_data = json_loader.load_json()