from pyjop import *

SimEnv.connect()
SimEnvManager.first().reset()
platform = MovablePlatform.first()
platform.set_target_location(0,0,5)
sleep(3)
platform.set_target_location(-3.7,0,5)
sleep(3)
platform.set_target_rotation(50,0,0)
SimEnv.disconnect()
