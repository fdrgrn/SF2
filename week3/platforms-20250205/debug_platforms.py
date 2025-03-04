def covers(platform, horizontal_pos):
    '''
    :param platform: a platform as defined by the input of the question
    :param horizonal_pos: an integer
    :return : True if platform covers horizontal_post; False otherwise. 
    '''
    return platform[0] - 0.5 <= horizontal_pos and platform[1] - 0.5 >= horizontal_pos


def pillar_from(platforms, height, horizontal_pos):
    '''
    :param platforms: a list of platforms (as lists)
    :param height: vertical position
    :param horizontal_pos: horizontal position
    :return : minimum length of pillar from heigh and horizontal_pos to the platform/ground below
    '''
    for platform in platforms:
        bottom = 0              
        if (platform[0] < height and covers(platform, horizontal_pos)):
            bottom = platform[0]
    return height - bottom


n = int(input())

platforms = []

# read input from user as lists of integers
for i in range(n):
    platform = input().split()
    platforms.append(platform)

int_plat = [[int(char) for char in int_plat] for int_plat in platforms]

print("hi")
print(int_plat)
print(type(int_plat[0][0]))

total = 0

for platform in int_plat: 
    for i in range(1,3):   
        total = total + pillar_from(int_plat, platform[0], platform[i])

print(total)
