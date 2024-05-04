# Fortune-Cookie-Generator

Title: Fortune Cookie Generator Script - Get Unique Daily Inspirations!

Description:

This Python script retrieves unique and inspiring fortunes using the Advice Slip API: https://adviceslip.com/. It prevents repeats by keeping track of seen fortunes in a file named "last_fortune.txt". A perfect tool for a daily dose of motivation!

Features:

Fetches random fortunes from the Advice Slip API.
Tracks seen fortunes to avoid duplicates.
Saves seen fortunes to "last_fortune.txt" for persistence.
Prerequisites:

Python 3 (version 3.3 or later recommended) - Check by running python3 --version in your terminal. Download from https://www.python.org/downloads/ if not installed.
Installation:

Create a virtual environment (recommended): This isolates project dependencies and avoids conflicts.

Open a terminal window.
Create a virtual environment named venv using:
Bash
python -m venv venv
Use code with caution.

Activate the virtual environment:
Windows: venv\Scripts\activate
Linux/macOS: source venv/bin/activate
Install requests library: Within the activated virtual environment:

Bash
pip install requests
Use code with caution.
content_copy
Running the Script:

Navigate to the script directory: Use cd to reach the directory containing the script (e.g., main.py).
Run the script: Execute the script using:
Bash
python3 main.py
Use code with caution.

Example Usage:

Bash
python3 main.py
Use code with caution.

This will fetch a random fortune and display it on your terminal. Subsequent runs will avoid showing previously seen fortunes.

Deactivating the Virtual Environment (if used):

When you're finished working on the script, deactivate the virtual environment using:

Windows: venv\Scripts\deactivate
Linux/macOS: deactivate
Contribution:

We welcome contributions to this project! Feel free to fork the repository and submit pull requests.

License:

(Specify the license you've chosen for your project, e.g., MIT License).

