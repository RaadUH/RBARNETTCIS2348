def get_age():
    age = int(input())
    if(age>=75 or age<=18):
        raise ValueError('Invalid age.')
    return age

def fat_burning_heart_rate(age):
    return 70*(220-age)/100

try:
    age = get_age()
    rate = fat_burning_heart_rate(age)
    print("Fat burning heart rate for a "+str(age)+" year-old: "+str(rate)+" bpm")
except ValueError as ex:
    print(ex)
    print("Could not calculate heart rate info.\n")
