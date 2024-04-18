# Python CRUD Operations Script Overview

The script is structured to handle a series of CRUD (Create, Read, Update, Delete) operations involving three different CSV files (`Sales.csv`, Customers.csv, Parts.csv`) as a simple database system. The main functionality is distributed into three sections based on the `option parameter to add new records to the respective CSV file. Here's a breakdown of each part along with some suggested improvements:

## Install & Run
1. Install Python (https://www.python.org/downloads/)
2. Clone the repository
3. pip install -r requirements.txt
4. Run the script using the command `python main.py`
5. Follow the on-screen instructions to use the CLI application

## General Observations
- `app_border` Function: This function is presumably used to print a decorative border and a message. However, its definition is not included. Ensure that it's defined elsewhere in your code to avoid runtime errors.
- Code Repetition: The code for reading from and appending to CSV files is repeated multiple times. This could be refactored into separate functions to reduce redundancy and improve maintainability.
- Error Handling: The script lacks comprehensive error handling, especially for file operations and user input validation. Adding try-except blocks would make the code more robust.
- Performance: For each operation, the entire CSV file is loaded and then rewritten. For large datasets, this might be inefficient. Consider using a database system if scalability is a concern.

## Specific Sections Breakdown

### Option 1: Adding a Sales Record
- Checks if the customer exists in Customers.csv before adding a sales record.
- The script allows adding a sales record even if the customer does not exist in the database, which might not be intended based on usual business rules.
- Improvement: Validate the new sales record data before appending it to ensure data integrity.

### Option 2: Adding a Customer Record
- Checks if the part associated with the customer exists in Parts.csv before adding a customer.
- The condition seems reversed—it checks if the part exists and proceeds only if it doesn't, which is likely a logic error.
- Improvement: Reverse the condition to check if the part exists before adding the customer.

### Option 3: Adding a Part Record
- Adds a new part record without additional validation.
- Improvement: Similar to other sections, validate part details (e.g., unique part_id, non-negative cost) before adding.

