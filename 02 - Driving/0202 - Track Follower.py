from pyjop import *

SimEnv.connect()
env = SimEnvManager.first()
drone = ServiceDrone.first()
env.reset()

while SimEnv.run_main():
    dist_left = drone.get_distance_left()
    dist_right = drone.get_distance_right()
    print(f"left {dist_left:.2f}m")
    print(f"right {dist_right:.2f}m")
    drone.set_thruster_force_right(120)
    drone.set_thruster_force_left(120)

    while dist_left > 1.5 or dist_right > 1.5:
        if dist_left > 1.5:
            drone.set_thruster_force_right(40)
            drone.set_thruster_force_left(80)
            sleep(0.1)
        else:
            drone.set_thruster_force_right(80)
            drone.set_thruster_force_left(40)
            sleep(0.1)
        dist_right = drone.get_distance_right()
        dist_left = drone.get_distance_left()

SimEnv.disconnect()
