import time
import random

password = "secret123"
attempts = 0

print("Starting brute force attack...\n")
while True:
    fake_attempt = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=len(password)))
    attempts += 1
    print(f"Trying: {fake_attempt}  | Attempt: {attempts}", end="\r")
    time.sleep(0.05)
    
    if fake_attempt == password:
        print(f"\nPassword cracked: {fake_attempt} in {attempts} attempts!")
        break
