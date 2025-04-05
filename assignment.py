# Create a file and write content to it
with open('python/week 4/assignment4.txt', 'w') as file:
    file.write("This is a newly created file.\n")
    file.write("It contains some sample text.\n")
    file.write("This is the third line of the file.\n")

print("File 'assignment4.txt' created successfully in the 'week 4' directory!")

# Read content from the existing file
with open('python/week 4/assignment4.txt', 'r') as file:
    content = file.readlines()
    print(content)

# Modify the content of the file
modified_content = [f"Modified: {line}" for line in content]

# Write the modified content to a new file
with open('python/week 4/assignment4_modified.txt', 'w') as new_file:
    new_file.writelines(modified_content)

print("Modified content written to 'assignment4_modified.txt' successfully in the 'week 4' directory!")

filename = input("Enter the name of a file to read:")

try:
    with open(filename, 'r') as file:
        content = file.readlines()
        print(content)
except FileNotFoundError:
    print("Error!: The file '{filename}' was not found")
    