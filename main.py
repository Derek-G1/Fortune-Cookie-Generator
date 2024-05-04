import requests


def load_last_fortune(filename="last_fortune.txt"):
    """Loads a dictionary of seen fortunes with their assigned numbers from a file (if it exists)."""
    seen_fortunes = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                # Check if there's a period before splitting
                if '.' in line:
                    try:
                        number, fortune = line.strip().split(".", 1)  # Split at first period
                        # Convert number to integer before assigning (optional)
                        seen_fortunes[fortune] = int(number)
                    except ValueError:
                        # Ignore lines with non-numeric values (optional)
                        pass  # Ignore lines with non-numeric values (optional)
                else:
                    # Handle lines without a number (optional: ignore or assign a default number)
                    pass  # Ignore lines without a number (optional)
    except FileNotFoundError:
        pass  # Ignore if file doesn't exist
    return seen_fortunes


def save_last_fortune(fortune, number, filename="last_fortune.txt"):
  """Saves a fortune with its assigned number to the end of the file, using a period (.) as separator, with number before fortune."""
  try:
    with open(filename, "a") as file:  # Open the file here
      # Ensure number is an integer before writing
      if isinstance(number, int):
        bytes_written = file.write(f"{number}.{fortune}\n")
        if bytes_written != len(f"{number}.{fortune}\n"):
          print("Error saving fortune to file: Incomplete write.")
  # Proper indentation for the FileNotFoundError handler
  except FileNotFoundError:  # Handle case where filename doesn't exist
    print(f"Error: File '{filename}' not found. Fortune not saved.")
  except Exception as e:  # Catch any other exceptions during writing
    print(f"Error saving fortune to file: {e}")




def get_and_print_fortune(api_url="https://api.adviceslip.com/advice"):
    """Fetches and prints a random fortune from the provided API, assigning a unique number and avoiding duplicates in the output."""
    seen_fortunes = load_last_fortune()
    next_number = len(seen_fortunes) + 1  # Start number based on seen fortunes

    while True:
        # Make a GET request to the API endpoint
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the fortune text
            fortune_text = data["slip"]["advice"]

            # Check if the fortune is new (compared to seen ones)
            if fortune_text not in seen_fortunes:
                # Print the new fortune with its number and a leading space if needed
                print(f"{' ' if seen_fortunes else ''}{next_number}. {fortune_text}")

                # **Debugging Print Statements:**
                print(f"Saving fortune: {next_number}. {fortune_text}")

                # Update the dictionary and save the new fortune with its number (using a period)
                seen_fortunes[fortune_text] = next_number
                save_last_fortune(fortune_text, next_number)  # Call without filename argument
                next_number += 1  # Increment number for next fortune
                break  # Exit the loop after printing a unique fortune
            else:
                print("Duplicate fortune encountered, fetching again...")
        else:
            print("Failed to retrieve fortune. Error:", response.status_code)
            break  # Exit the loop on error


if __name__ == "__main__":
    get_and_print_fortune()