import requests

request_json = {
    "name": "Nicole Belisle",
   "net_id": "nb202",
   "e-mail": "nicole.belisle@duke.edu"
}
p = requests.post("http://vcm-7631.vm.duke.edu:5001/student",json=request_json)
print(p)
print(p.status_code)
print(p.text)
if p.status_code == 200:
    print(p.json)

r = requests.get("http://vcm-7631.vm.duke.edu:5001/list")
answer = r.json()
for student in answer:
    print("Name of student is {}".format(student["name"]))

sum_json = {
   "a": 1,
   "b": 2
}
s = requests.post("http://vcm-7631.vm.duke.edu:5001/sum",json=sum_json)
print(s.json)
