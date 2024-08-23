from changes import write
import os
import datetime

numberOfDays= 3

# #change
# for i in range(numberOfDays):
#     write(f"Day {i+1} of {numberOfDays} days of code\n")

# #git add .
# os.system("git add .")
target_date = datetime.datetime(2024, 8, 22, 11, 55, 43)

#git commit
for i in range(1, numberOfDays+1):
    write(f"Day {i+1} of {numberOfDays} days of code\n")
    print("change made to file.txt", i)
    os.system("git add .")
    print("git add .", i)
    
    os.system(f"git commit --date=\"2024-08-21  b 11:55:43\" -m \"initial commit\"")
    print("git commit", i)

#git push
os.system("git push")
print("git push")