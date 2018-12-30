import json

#JSON = JavaScript Object Notation

#with open('colors.json') as colorfile:
#    colors = json.load(colorfile)
#    print(colors['blanchedalmond'])

me = {
        'firstname': 'siyamak',
        'lastname': 'abasnezhad'
    }

poingpy = {
    "course": "python",
    "minutes": 1600,
    "activate": True,
    "teacher": me
}



with open('teachers.json', 'a') as teacherfile:
    json.dump([me, poingpy], teacherfile)