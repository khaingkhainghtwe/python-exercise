from sys import argv

script, filename = argv
print(f"We're going to erade {filename}.")
print("If you don't want that,hit CTRL-C (AC).")
print("If you do want that, hti RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncatiion the file. GOodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
