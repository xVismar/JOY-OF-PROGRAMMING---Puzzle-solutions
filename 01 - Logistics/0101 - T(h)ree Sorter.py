from pyjop import *

SimEnv.connect()
env = SimEnvManager.first()
env.reset()
belts = ["belt0", "belt1", "belt2", "belt3", "belt4"]

for belt in belts:
    ConveyorBelt.find(belt).set_target_speed(5)

first_sorting_belt = ConveyorBelt.find(belts[1])
second_sorting_belt = ConveyorBelt.find(belts[4])

while SimEnv.run_main():
    first_tag = RangeFinder.find("scan0").get_rfid_tag()
    second_tag = RangeFinder.find("scan1").get_rfid_tag()
    if first_tag != "":
        if first_tag == "Barrel":
            first_sorting_belt.set_target_speed(-5)
        else:
            first_sorting_belt.set_target_speed(5)
    elif second_tag != "":
        if second_tag != "Box":
            second_sorting_belt.set_target_speed(-5)
        elif second_tag == "Cone":
            second_sorting_belt.set_target_speed(5)
    else:
        if (
            not first_sorting_belt.get_is_transporting()
            and not second_sorting_belt.get_is_transporting()
           ):
            ObjectSpawner.first().spawn()
        pass

SimEnv.disconnect()
