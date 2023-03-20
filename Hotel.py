# fun and simple hotel simulation from the explanation Joost had given
import random
# define the place with 20 rooms over 2 upper floors and a restaurant on floor 0

map_graph = { "lobby" : ["elevator", "restaurant", "exit"],
         "elevator" : ["lobby", "hall_lvl1", "hall_lvl2"],
         "restaurant" : ["lobby", "exit"],
         "hall_lvl1" : ["Room101","Room102","Room103","Room104","Room105","Room106","Room107","Room108","Room109","Room110"],
         "hall_lvl2" : ["Room201","Room202","Room203","Room204","Room205","Room206","Room207","Room208","Room209","Room210"],
         "Room101": "hall_lvl1",
         "Room102": "hall_lvl1",
         "Room103": "hall_lvl1",
         "Room104": "hall_lvl1",
         "Room105": "hall_lvl1",
         "Room106": "hall_lvl1",
         "Room107": "hall_lvl1",
         "Room108": "hall_lvl1",
         "Room109": "hall_lvl1",
         "Room110": "hall_lvl1",
         "Room201": "hall_lvl2",
         "Room202": "hall_lvl2",
         "Room203": "hall_lvl2",
         "Room204": "hall_lvl2",
         "Room205": "hall_lvl2",
         "Room206": "hall_lvl2",
         "Room207": "hall_lvl2",
         "Room208": "hall_lvl2",
         "Room209": "hall_lvl2",
         "Room210": "hall_lvl2"
}

print(map_graph)
# a guest has to be defined
class Guest:
    def __init__(self, _goal : str, _arrival_time : tuple[int, int]):
        # what the guest wants to come and do
        self.goal = _goal
        self.arrival_time = _arrival_time

    def __repr__(self):
        return f"Guest(Goal:{self.goal}, arrived: {self.arrival_time})"

# the guests that come in have to be generated
class Guest_Generator:
    def __init__(self, number_to_generate : int) -> None:
        self.guests = []
        for _ in range(number_to_generate):
            goal = random.choice(["check-in", "goto-restaurant"])
            # between 14:00 and 19:00 the guests will be able to arrive
            # guests that come to check-in come
            arrival_time_hour = random.randint(14, 18)
            arrival_time_minute = random.randint(0, 59)
            self.guests.append(Guest(goal, (arrival_time_hour, arrival_time_minute)))

gGen = Guest_Generator(5)

# is the given time passed
def time_passed(expected_time, now):
    return expected_time[0] < now[0] or (expected_time[0] == now[0] and expected_time[1] < now[1])

# is someone arriving at the given time
def is_arriving(sorted_guests, time):
    arriving = []
    while len(sorted_guests) > 0 and time_passed(sorted_guests[0].arrival_time, time):
        arriving.append(sorted_guests.pop(0))
    return arriving

# simulate this day
def sim_day(arriving_guests):
    # sort the guests on the time they arrive
    arriving_guests.sort(key=lambda x: x.arrival_time[0]*60+x.arrival_time[1])
    print("Today Arriving:", arriving_guests)
    for hour in range(6, 24):
        for min in range(0, 60):
            print(f"Time: {hour, min}")
            # for every moment of the day
            # check if someone is arriving
            guests = is_arriving(arriving_guests, (hour, min))
            for guest in guests:
                print(guest, " is arriving now!")


sim_day(gGen.guests)