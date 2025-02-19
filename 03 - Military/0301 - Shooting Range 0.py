from pyjop import *

SimEnv.connect()
env = SimEnvManager.first()
env.reset()
rifle = SniperRifle.first()

while SimEnv.run_main():
    dects = rifle.get_object_detections()
    for target_id in dects:
        if target_id.entity_name.startswith("TargetRed"):
            rifle.fire()
        else:
            continue

SimEnv.disconnect()
