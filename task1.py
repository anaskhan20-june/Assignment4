# 1.   Opens and create a text file named sample.txt.

with open("sample.txt", "wt") as fh:
    fh.write("Reading the contents:\n")
    fh.write("Line1: This is a sample.txt file.\n")
    fh.write("Line2: It contains multiple lines.\n")

# 2. Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist. Using Exception Handling

try:
    with open("sample.txt", 'rt') as fh:
        data = fh.read()
        print(data)
except FileNotFoundError as e:
    print(f"The file {e.filename} was not found.")

