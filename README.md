# GarageDoorOrders: CSV Editor Application

#### This Python Flask application provides a simple web interface to perform CRUD (Create, Read, Update, Delete) operations on a CSV file. The CSV file being manipulated is "data.csv".

### Overview
The main interface of the application displays the contents of the CSV file in a table, with dynamic filter options for fields 'Type', 'Material', and 'Bottom Bar'. Additional filter input fields exist for 'Gage' and 'Weight'. The interface allows the user to add new entries, delete existing entries, or modify current entries within the CSV file.

The application has four main functionalities:

- View Data: The home page ('/' route) loads the CSV file into a pandas DataFrame and sends the data to the front-end to be displayed in a table format.
- Add Data: The '/add' and '/add_record' routes are used to add a new entry to the CSV file. The user is redirected to a new page ('add_record.html') to input the details of the new record.
- Update Data: The '/update' route is used to update an existing entry in the CSV file. The entry to be updated is determined based on the 'Invoice' column.
- Delete Data: The '/delete' route is used to delete an existing entry from the CSV file. The entry to be deleted is also determined based on the 'Invoice' column.


### Requirements
- Python 3.6 or higher
- Flask
- Pandas


### How to run the application locally
Clone the repository to your local machine.
Make sure you have the required packages (Flask, pandas) installed in your Python environment. If not, you can install them using this pip command:
pip install flask pandas

Then, navigate to the directory where the app.py file resides. 
Run the application using the commands:
- cd *your project folder path goes here*
- python app.py

Open a web browser and navigate to http://localhost:5000 to view and interact with the application.

  
### File Structure
- app.py: This is the main Python script that runs the Flask server and defines the routes for the application.
- index.html: This is the main HTML file that renders the user interface for the application. It displays the CSV data in a table format and provides options to filter the data, add new data, and delete existing data.

### Code Structure
Each route in the app.py corresponds to a different functionality of the web application.
The main route ('/') reads the CSV data, prepares the filter parameters, and sends them along with the data to index.html to be displayed.
The '/update', '/delete', and '/add' routes each take form data from the user interface and use it to modify the CSV data accordingly.
The JavaScript code in the index.html file handles the interaction between the user and the data table. It sends AJAX requests to the appropriate routes when data is to be added, deleted, or updated.

### Notes
Please note that you need a CSV file named data.csv in the same directory as app.py for the application to run. Make sure the CSV file has columns named 'Type', 'Material', 'Bottom Bar', 'Invoice', and 'Dealer Name'.
The data filtering in the front-end currently uses static column indices. Be careful to update these indices in the JavaScript code if your CSV structure changes.
