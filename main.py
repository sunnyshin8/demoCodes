from changes import write
import os
import datetime

numberOfDays = 3

# Set the desired date
target_date = datetime.datetime(2024, 8, 21, 11, 55, 43)

for i in range(1, numberOfDays + 1):
    write(f"Day {i+1} of {numberOfDays} days of code\n")
    print("change made to file.txt", i)
    os.system("git add .")
    print("git add .", i)

    # Use the target date for the commit
    commit_message = f"Initial commit (Day {i+1})"
    os.system(f'git commit --date="{target_date.strftime("%2024-%08-%22 %7:%22:%42")}" -m "{commit_message}"')
    print("git commit", i)

# Push to the remote repository
os.system("git push")
print("git push")