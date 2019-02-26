try:
    years = int(input("Gimme human years, I give dog years: "))

    if years <= 2:
        print(f"{years*10.5} in dog years")
    elif years > 2:
        print(f"{10.5*2 + years*4} in dog years")
    else:
        print("please locate the nearest bridge")
except ValueError: print('please google maps the nearest bridge')