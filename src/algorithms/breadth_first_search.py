from collections import deque
import time

people = []






def search():
    sara_f = ["Alex", "Monica,"]
    vika_f = ["George", "Daniel"]
    sam_f = ["Tom", "Gray", "Woodie"]

    george = {"name": "George", "friends": None}
    sara = {"name": "Sara", "friends": sara_f}
    vika = {"name": "Vika", "friends": vika_f}
    sam = {"name": "Sam", "friends": sam_f}

    arr = deque()
    arr += [sara, vika, sam]
    searched = []
    while(arr):
        person = arr.popleft()
        if len(searched) == 0:
            print("I am not here")
            if person["name"] == "George":
                print("found")
                return
            else:
                searched.append(person["name"])
                arr += person
        else:
            for n in range(len(searched)):
                if person["name"] != searched[n]:
                    if person["name"] == "George":
                        print("DONE")
                        return
                    else:
                        searched.append(person["name"])                
                        arr += person.frie




search()
