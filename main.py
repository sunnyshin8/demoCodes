from changes import write
import os

numberOfDays= 31

# #change
# for i in range(numberOfDays):
#     write(f"Day {i+1} of {numberOfDays} days of code\n")

# #git add .
# os.system("git add .")


#git commit
for i in range(1, 32):
    write(f"Day {i+1} of {numberOfDays} days of code\n")
    print("change made to file.txt", i)
    os.system("git add .")
    print("git add .", i)
    os.system(f"git commit --date=\"2023-10-{i} 11:55:43\" -m \"initial commit\"")
    print("git commit", i)

#git push
os.system("git push")
print("git push")