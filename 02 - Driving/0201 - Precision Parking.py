from pyjop import *

SimEnv.connect()
env = SimEnvManager.first()
env.reset()
drone = ServiceDrone.first()
scanner = RangeFinder.first()
target_distance = 3.0
thrust_force = 180

while SimEnv.run_main():
    dist = scanner.get_distance()
    print(f"current distance: {dist:.3f}m")
    if dist > target_distance + 5:
        drone.set_thruster_force_right(thrust_force*2)
        drone.set_thruster_force_left(thrust_force*2)
    elif dist > target_distance + 2.5:
        drone.set_thruster_force_right(thrust_force/1.5)
        drone.set_thruster_force_left(thrust_force/1.5)
    elif dist < target_distance + 1.6:
        drone.set_thruster_force_right(thrust_force/6)
        drone.set_thruster_force_left(thrust_force/6)
        if dist < target_distance + 0.16:
            drone.set_thruster_force_right(0)
            drone.set_thruster_force_left(0)
            drone.apply_thruster_impulse_right(-11)
            drone.apply_thruster_impulse_left(-11)
            break
SimEnv.disconnect()
