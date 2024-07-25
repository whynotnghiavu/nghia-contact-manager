# Read the file and get its contents
with open("error.txt", "r", encoding="utf-8") as file:
    contents = file.readlines()

# Print the number of lines before removing duplicates
print(len(contents))

# Remove duplicates by converting to a set and then back to a list
contents = list(set(contents))

# Print the number of lines after removing duplicates
print(len(contents))

# Write the unique lines to a new file
with open("_error.txt", "w", encoding="utf-8") as file:
    file.writelines(contents)
