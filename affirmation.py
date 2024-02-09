import time
import random

# List of affirmations
affirmations = [
    "You are capable of achieving great things.",
    "Every day is a new opportunity to improve.",
    "You are worthy of love and respect.",
    "Believe in yourself and your abilities.",
    "You are strong, brave, and resilient.",
    "Your potential is limitless.",
    "You deserve happiness and fulfillment.",
    "You have the power to create positive change.",
    "Challenges are opportunities for growth.",
    "You are surrounded by abundance and blessings."
]

while True:
    # Choose a random affirmation from the list
    affirmation = random.choice(affirmations)
    
    # Print the affirmation
    print(affirmation)
    
    # Wait for 30 minutes before printing the next affirmation
    time.sleep(30 * 60)  # 30 minutes in seconds

