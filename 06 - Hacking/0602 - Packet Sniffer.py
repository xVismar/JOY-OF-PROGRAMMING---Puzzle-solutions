from pyjop import *
import re

SimEnv.connect()
env = SimEnvManager.first()
env.reset()
sniffer = MessageSniffer.first()
data_exchange = DataExchange.first()


def extract_passcode(text: str) -> str:
    pattern = r'The passcode is "(\d{5})"'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1)
    alt_pattern = r'The passcode is[:\s"\']*(\d{5})[\'"]*'
    alt_match = re.search(alt_pattern, text, re.IGNORECASE)
    if alt_match:
        return alt_match.group(1)
    return ""


while SimEnv.run_main():
    encrypted = sniffer.get_cipher_text()
    found_passcode = False
    decrypted_message = ""
    used_shift = 0
    for shift in range(1, 100):
        decrypted = sniffer.try_decrypt(shift)
        passcode = extract_passcode(decrypted)
        if passcode:
            print(f"Found passcode with shift {shift}: {passcode}")
            decrypted_message = decrypted
            used_shift = shift
            found_passcode = True
            break
    if found_passcode:
        data_exchange.set_data("passcode", int(passcode))

SimEnv.disconnect()
