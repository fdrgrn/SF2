def combine2(d1, d2):
    new_d = {}
    for key in d1:
        if key in d2:
            inner_d1 = d1[key]
            inner_d2 = d2[key]
            for k in inner_d1:
                if k in inner_d1:
                    new_d[k] = sum(inner_d1[k]) + sum(inner_d2[k])
    return new_d

def readBirthday():
    birthday_dct = {}

    while True:
        birthdate = input("month day name: ")
        if birthdate == 'stop':
            print(birthday_dct)
            return birthday_dct
        else:
            birthdate = birthdate.split()
            month, day, person = birthdate[0], birthdate[1], birthdate[2]

            if month in birthday_dct:
                if day in birthday_dct[month]:
                    birthday_dct[month][day].append(person)
                else:
                    birthday_dct[month][day] = [person]
            else:
                birthday_dct[month] = {day : person}

#readBirthday()

def mostCovered(d):
    current_best = ['None', 0]
    for month in d:
        sum_dates = 0
        for day in d[month]:
            sum_dates += len(d[month][day])
        if current_best[1] < sum_dates:
            current_best = [month, sum_dates]
    print(current_best[0])
    return current_best

#mostCovered({ 'February': {'23': ['Bob']}, 'May': {'3': ['Katie'], '8': ['Paul', 'Lucy']} })

def invert(d):
    invert_d = {}
    for month in d:
        for day in d[month]:
            for person in d[month][day]:
                invert_d[person] = (month, day)
    print(invert_d)
    return invert_d

#invert({ 'February': {'23': ['Bob']}, 'May': {'3': ['Katie'], '8': ['Paul', 'Lucy']} })

