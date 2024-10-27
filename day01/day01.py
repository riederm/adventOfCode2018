# Open the file input.txt in read mode
with open('input.txt', 'r') as file:
    # Read the file content
    data = file.read()

# Split the file content by new lines into an array
lines = data.split('\n')

# Print the length of the array
print("read " + str(len(lines)) + " lines")

# put your solution here ... 




# print the result here
