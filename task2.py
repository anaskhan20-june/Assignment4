# 1.   Taking user input and writing it to a file named output.txt.

initial_text = input("Enter text to write to the file: ")

with open("output.txt", "w") as fh:
    fh.write(initial_text + "\n")

print(f"Data successfully written to output.txt. \n")

# 2.   Appends additional data to the same file.

additional_text = input("Enter additional text to append: ")

with open("output.txt", "a") as fh:
    fh.write(additional_text + "\n")

print(f"Data successfully appended. \n")

# 3.   Reads and displays the final content of the file.

print("Final content of output.txt:")

with open("output.txt", "r") as fh:
    output_txt = fh.read()
    print(output_txt)




