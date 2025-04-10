#Name: Feodor Gornostayev
#ID: 2442384


def toCelsius(n):
    celsius = (n - 32) * (5/9)
    return round(celsius, 2)

read_file = open("data.txt", 'r')

temp_dict = {}
for line in read_file:
    line = line.split()
    if line and line[0].isdigit():
        line = list(map(float, line))
        year = int(line[0])
        line = list(map(toCelsius, line))

        temp_dict[year] = {'JAN':line[1], 'FEB':line[2], 'MAR':line[3], 'APR':line[4], 'MAY':line[5], 'JUN':line[6], 'JUL':line[7], 'AUG':line[8], 'SEP':line[9], 'OCT':line[10], 'NOV':line[11], 'DEC':line[12],}

read_file.close()
#print(temp_dict)

def avgTempYear(d, year):
    try:
        average_temp = round(sum(d[year].values()) / 12, 2)
        return average_temp
    except KeyError:
        print("Year was not found in the dictionnary")
#avgTempYear(temp_dict, 1967)

def topThreeYears(d):
    top_three = [-1000,-1000,-1000]
    for year in d:
        average_temp = avgTempYear(d, year)    
        if average_temp > top_three[0]:
            top_three[2] = top_three[1]
            top_three[1] = top_three[0]
            top_three[0] = average_temp

        elif average_temp > top_three[1]:
            top_three[2] = top_three[1]
            top_three[1] = average_temp

        elif average_temp > top_three[2]:
            top_three[2] = average_temp

    print(top_three)
    return(top_three)

#topThreeYears(temp_dict)
    
def avgTempMonth(d, month):
    month = month.upper()
    sum = 0
    n_years = len(d)
    for year in d:
        sum += d[year][month]
    #print(round(sum/n_years, 2))
    return round(sum/n_years, 2)

#avgTempMonth(temp_dict, 'aug')

def belowFreezing(d):
    freezing_months = set()
    for year in d:
        for month in d[year]:
            if d[year][month] < 0:
                freezing_months.add(month)
    #print(freezing_months)
    return freezing_months
#belowFreezing(temp_dict)

read_file = open('data.txt', 'r')
write_file = open('data_celsius.txt', 'w')

for line in read_file:
    verify_line = line.split()
    if not verify_line or not verify_line[0].isdigit():
        write_file.write(line)
        
for year in temp_dict:
    write_file.write(f"{year}	")
    for month in temp_dict[year]:
        write_file.write(f"{temp_dict[year][month]}   ")
    write_file.write("\n")

read_file.close()
write_file.close()