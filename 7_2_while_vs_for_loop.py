day=int(input("please enter day\n"))
temp_day=day
while day<365:
    day+=1
    print(day)

print("inside for loop")

day=int(input("please enter day\n"))
for x in range(temp_day,2029,2):
    print(x)
