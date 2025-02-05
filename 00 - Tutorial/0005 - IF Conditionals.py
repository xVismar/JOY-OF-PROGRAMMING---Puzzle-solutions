from pyjop import *

SimEnv.connect()
env = SimEnvManager.first()
env.reset()
env.set_time_dilation(5)
conv = ConveyorBelt.find("_entityConveyorBelt0")
scanner = RangeFinder.find("_entityRangeFinder0")

while SimEnv.run_main():
    tag = scanner.get_rfid_tag()
    if tag == "Box":
        conv.set_target_speed(-5)
    else:
        conv.set_target_speed(5)

SimEnv.disconnect()
