output_file = open('cities_states_input', 'w')
TEST_CASES = 5
for _ in range(TEST_CASES):
    n = int(input('Number of city states parings: '))
    for _ in range(n):
        line = input("CITY STATE: ").split()
        output_file.write(line[0] + ',' + line[1] + '\n')
output_file.close()

combo_set = set()
read_file = open('cities_states_input', 'r')
for line in read_file:
    city, state = line.split()
    if city.lower()[:2] != state.lower():
        combo_set.add((city.lower()[:2], state.lower()))
read_file.close()

found_list = []

