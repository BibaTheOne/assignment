# Ask the user for a filename
input_filename = input("Enter the filename to read: ")
output_filename = "modified_" + input_filename  # Create a new filename

try:
    # Open the file and read its content
    with open(input_filename, "r") as file:
        content = file.read()

    # Modify the content (convert text to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open(output_filename, "w") as file:
        file.write(modified_content)

    print(f"Modified content has been saved to '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied when accessing '{input_filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
