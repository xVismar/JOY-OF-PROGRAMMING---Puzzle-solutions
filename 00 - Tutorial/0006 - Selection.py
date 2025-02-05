#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()

# In this tutorial you need to combine what you learned in the previous two tutorials:
# iterate all conveyor belts, check each belt if it is transporting something or not and then set the speed > 0 if (and only if) that is True
belts = ConveyorBelt.find_all()
for conv in belts:
    if conv.get_is_transporting():
        conv.set_target_speed(5)
    else:
        None

#cleanup close code
SimEnv.disconnect()
