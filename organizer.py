import os, sys
import jdatetime
import time

NAME_FORMAT = "FirstName.LastName.cap.cn.%s.%s.%s.pdf" # Change details based on course description

# # Check for user prompt: Split single pdf, or Normal Mode.
# print(
#     "How should be the operation mode?"\
#     "1. Split files from a single pdf"\
#     "2. Name pdf files in numeric order"
# )
# opr_mode = input("Choose (default 2): ").strip()
# if not opr_mode:
#     opr_mode = '1'


print()
# Get the current date. Day and Month only
month, day = str(jdatetime.date.today()).split('-')[1:]
print(f"Current date: {month}/{day}")
# print(month, day)

to_split = [f for f in os.listdir('./assets') if os.path.isfile(f) and f.endswith('.pdf')]
if to_split:
    print("Some pdf files found in assets directory, \nyou sure nothing needs to be splitted?")
    user_in = input("Yes (Continue without splitting) or No (End the program)?").lower()
    if user_in == 'no':
        sys.exit()
    elif user_in == 'yes':
        pass
    else:
        raise ValueError("Input not understood")

# List the files
print()
print("Reading files from directory...")
time.sleep(.5)
files = set([f for f in os.listdir() if os.path.isfile(f)])

# Remove the script
files.remove("organizer.py")

# Filter the files that are already named
unnamed = set(filter(lambda f: NAME_FORMAT.split('.')[0] not in f, files))

print(f"Total number of files found: {len(files)}")
print(f"Number of Unnamed files: {len(unnamed)}")
time.sleep(.5)


# Check unnamed files to see if they match the instructions
print()
print("Procesing file names...")
time.sleep(.5)


for file in unnamed:
    try:
        int(file.split('.')[0])
    except ValueError as e:
        print(f"\nFile name error detected in directory: {file}")
        print("Terminating program...")
        os.abort()

named = files - unnamed
unnamed = sorted(unnamed, key=lambda f: int(f.split('.')[0]))
named = sorted(named, key=lambda f: int(f.split('.')[4]))

# print(unnamed)
# print(named)

# Get the latest file number
print()
print("Finding the lates numbered file...")
time.sleep(.5)
if named:
    named = [name.split('.') for name in named]
    latest = int(max(named, key=lambda x: int(x[4]))[4])
else:
    latest = 0

print(f"Found: {latest}")
time.sleep(.5)

# Rename the unnamed files
print()
print("Naming new files...")
time.sleep(.5)
for i, file in enumerate(unnamed, start=latest+1):
    old_name = file
    new_name = NAME_FORMAT % (i, month, day)
    os.rename(old_name, new_name)

print(f"All unnamed files are named in range: {latest}-{latest+len(unnamed)}")