#! /usr/bin/env python3

age = int(input("What is your age in years? "))
end = int(input("How long do you think you'll live until? "))
age_days = age * 365
end_days = end * 365
print(f"You are approximately {age_days} days old.")
remaining = end_days - age_days
print(f"You have approximately {remaining} days remaining in your life.")
