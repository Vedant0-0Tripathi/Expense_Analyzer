Personal Student Budget & Expense Analyzer

Overview of the project:
The Personal Student Budget & Expense Analyzer is a terminal-based Python application designed to help college students track their daily expenses, categorize their spending, and maintain a monthly budget using interactive text menus and ASCII-based visual analytics.

Features:

Multi-User Support: Creates separate local profiles so multiple people can track finances on the same machine.

Expense Management: Logs the date, amount, category, and description for every transaction.

Automated Analytics: Generates spending reports and dynamic bar charts showing budget versus actual expenditure.

Data Persistence: Automatically saves all user profiles and transaction logs locally using JSON format.

Technologies/tools used:

Programming Language: Python 3.x

Core Libraries: json (data storage), os (file management), datetime (timestamping)

Version Control: Git and GitHub

Steps to install & run the project:

Prerequisites: Ensure you have Python 3.6 or higher installed on your system.

Clone the repository:

git clone https://github.com/Vedant0-0Tripathi/Expense_Analyzer.git

Navigate to the directory:

cd Expense_Analyzer

Execute the program:
Run the main script using Python. No external dependencies or pip install commands are required.

python main.py

Instructions for testing:

Launch the application (python main.py) and enter a new username when prompted.

The system will recognize you as a new user. Enter a test monthly budget (e.g., 500).

From the main menu, select option 1 to log three distinct expenses (e.g., 20 on Food, 50 on Transport, 120 on Books).

Select option 2 to view your analytics. Verify that the total spent is calculated correctly, the remaining budget updates accurately, and the ASCII bar charts render cleanly.

Select option 3 to exit safely.

Restart the application and log in with the same username to verify that your past data was successfully loaded from the local data.json file.

<img width="597" height="707" alt="image" src="https://github.com/user-attachments/assets/6d1cc0b2-3a42-4b10-8fa4-33059aa62516" />
<img width="530" height="412" alt="image" src="https://github.com/user-attachments/assets/139c8385-12f4-4418-80bd-61453d4980c6" />
