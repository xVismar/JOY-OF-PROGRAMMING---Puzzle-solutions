from pyjop import *

SimEnv.connect()
env = SimEnvManager.first()
env.reset()
hacker = PinHacker.first()
low = 0
high = 999

def binary_pin(low, high):
    pin = (low + high) // 2
    hacker.enter_pin(pin)
    hacker.check_pin(pin)
    if hacker.get_is_correct():
        print(f'Pin is correct - {pin}')
        return pin
    else:
        if hacker.get_is_greater():
            print(f'Pin - {pin} is greater than required')
            return binary_pin(low, pin - 1)
        else:
            print(f'Pin - {pin} is less than required')
            return binary_pin(pin + 1, high)

while SimEnv.run_main():
    correct_pin = binary_pin(low, high)
    print(f"Found the correct PIN: {correct_pin}")
    break

SimEnv.disconnect()