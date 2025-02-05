from pyjop import *

SimEnv.connect()
SimEnvManager.first().reset()
arm = RobotArm.first()
arm.set_grabber_location([1.6,0.3,0.6])
sleep(2)
arm.pickup()
sleep(1)
arm.set_grabber_location([-3, 1, 3])
sleep(2)
arm.release()
SimEnv.disconnect()
