from pyjop import *

SimEnv.connect()
all_convs = ConveyorBelt.find_all()

for conv in all_convs:
    conv.set_target_speed(5)

SimEnv.disconnect()
