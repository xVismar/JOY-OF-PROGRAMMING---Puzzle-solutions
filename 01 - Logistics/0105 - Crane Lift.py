#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()

env = SimEnvManager.first()
env.reset()
crane = AirliftCrane.find("crane")
data_center = DataExchange.find("control_center")
data = data_center.get_data("instruction_sets")

def find_balanced_path(strings):
    """
    Find paths where following all instructions returns to the starting position (0,0).

    L (left) decreases x
    R (right) increases x
    F (forward) increases y
    B (backward) decreases y
    P is pickup/place operation
    """
    balanced_paths = []

    for path in strings:
        # Start at origin
        x, y, z = 0, 0, 3

        # Execute each instruction in the path
        for direction in path:
            x, y, z = move_crane(direction, x, y, z)

        # Calculate x and y before letter 'P'
        x_before_p, y_before_p = x, y

        # Check if we returned to the starting position (0,0)
        if x == 0 and y == 0:
            balanced_paths.append(path)

    return balanced_paths


def move_crane(direction, x, y, z):
    if direction == 'L':
        x -= 1
    elif direction == 'R':
        x += 1
    elif direction == 'F':
        y += 1
    elif direction == 'B':
        y -= 1
    elif direction == 'P':
        if z == 3:
            z = 0
        # Set target location before picking up
        crane.set_target_location([x, y, 0])
        sleep(1)
        # Pick up
        crane.pickup()
        sleep(1)
        # Return to starting position
        crane.set_target_location([0, 0, 3])
        sleep(1)
    return x, y, z


while SimEnv.run_main():
    instructions = find_balanced_path(data)
    print(instructions)
    for instruction in instructions:
        for char in instruction:
            crane.set_target_location(move_crane(char, 0, 0, 3),)
            sleep(1)

    crane.set_target_location([1, 0, 3],)

SimEnv.disconnect()