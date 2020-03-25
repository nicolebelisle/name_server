import requests

r = requests.get("http://vcm-7631.vm.duke.edu:5001/list")
answer = r.json()
for student in answer:
    print("Name of student is {}".format(student["name"]))
