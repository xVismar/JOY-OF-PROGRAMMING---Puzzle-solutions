from pyjop import *

SimEnv.connect()

env = SimEnvManager.first()
env.reset()
runner = HumanoidRobot.first()

while SimEnv.run_main():
    simtime = env.get_sim_time()
    print(f"current time: {simtime} seconds")
    runner.set_walking(0,1)
    sleep(3)
    runner.jump()

SimEnv.disconnect()
