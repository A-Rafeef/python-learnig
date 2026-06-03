# Step 1: Write the message to the file
file = open("message.txt", "w")
file.write("This is my first time handjnjling files in Python!")
file.close()  # CRITICAL: You must manually close the file to save the data!
print("Message written successfully!\n")

# Step 2: Read the message from the file
file = open("message.txt", "r")
secret_message = file.read()
file.close()  # CRITICAL: Close the file to free up system memory
print("Here is what the file says:")
print(secret_message)