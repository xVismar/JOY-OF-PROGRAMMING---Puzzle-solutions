from pyjop import *

SimEnv.connect()

env = SimEnvManager.first()
env.reset()
car = RaceCar.first()
car.set_throttle(1)
car.set_gear(1)
gear = car.get_gear()

while SimEnv.run_main():
    simtime = env.get_sim_time()
    print(f"current time: {simtime} seconds")
    if car.get_rpm() > 6000:
        gear += 1
        car.set_gear(gear)
        sleep(0.1)
    else:
        car.apply_boost()
        sleep(0.1)

SimEnv.disconnect()
