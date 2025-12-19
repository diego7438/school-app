# key is meeting time
# value is a list of pairs where 
# a pair is: (rotation_day, period)

data1 = { "8:30":[ (1,1), (2,2), (3,1), (4,2), (5,1), (6,2) ], 
         "10:35" : [ (1, 3), (3, 3), (5, 7), (2,4), (4,6), (6,8)],  
         "12:30" : [ (1, 5), (3, 7), (5,3), (2,6), (4,8), (6,4)], 
         "1:55" : [ (1,7), (3, 3), (5,5), (2,8), (4,4), (6,6)]} 
# what rotation day is class 4 at period 5
PERIOD_1 = "8:30"
PERIOD_2 = "10:35"
PERIOD_3 = "12:30"
PERIOD_4 = "1:55"

class_by_tod = {
    # class_number: [(rotation_day, period_time)]
    2: [(2, PERIOD_1), (4, PERIOD_1), (6, PERIOD_1)],
    4: [(2, PERIOD_2), (4, PERIOD_4), (6, PERIOD_3)],
    6: [(2, PERIOD_3), (4, PERIOD_2), (6, PERIOD_4)],
    5: [(1, PERIOD_3), (3, PERIOD_2), (5, PERIOD_4)]
}

target_class = 4
target_period = PERIOD_4

rotations = class_by_tod[target_class]
result = []
for rotation, period in rotations:
    if period == PERIOD_4:
        result.append(rotation)

print(f"Rotation day(s) for class {target_class} during period {target_period}: {result}")

# be able to take a time and tell you what period it is

time_hour = input("Enter the hour: ")
time_minute = input("Enter the minute: ")

def what_period_hour(time_hour):
    if time_hour > 1 and time_hour < 10:
        print("Looking like it might be period 1")
        return PERIOD_1
    elif time_hour > 10 and time_hour < 11:
        print("Looking like it might be period 2")
    elif time_hour > 10 and time_hour < 13:
        print("Looking like it might be period 3") 
    elif time_hour < 2:
        print("Looking like it might be period 4")

def minutes_left_in_class(time_minute): 
    


