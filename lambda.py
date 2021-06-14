people=[
    {"Name:":"Harry","House":"Gryffindor"},
    {"Name:":"Ron","House":"Gryffindor"},
    {"Name:":"Draco","House":"Slytherin"},
]
def f(person):
    return person["Name:"]

#people.sort(key=f)
people.sort(key=lambda person:person["Name:"])
print(people)