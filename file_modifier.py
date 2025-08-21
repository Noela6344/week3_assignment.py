def main():
    # Ask user for file name
    filename = input("Enter the file name to read: ")

    try:
        # Try opening the file for reading
        with open(filename, "r") as infile:
            content = infile.read()
    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
        return
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
        return
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Define new file name
    new_filename = "modified_" + filename

    try:
        # Write modified content to a new file
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)
        print(f"✅ Modified file has been saved as '{new_filename}'")
    except Exception as e:
        print(f"❌ Could not write to file: {e}")


if __name__ == "__main__":
    main()