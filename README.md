
## **What This Project Does**

1. Takes an input file (`Table_Input.csv`) containing numerical data.
2. Processes the file to compute new values based on predefined formulas:
   - **Alpha = A5 + A20**
   - **Beta = A15 / A7**
   - **Charlie = A13 * A12**
3. Displays both the original and computed data tables on a clean, styled webpage.

---

## **Key Files You Should Know**

### **1. `app.py`**
   - This is the main file that runs the web application.
   - It does the following:
     - Loads the original (`Table1.csv`) and processed (`Table2.csv`) data files.
     - Passes the data to the HTML page (`index.html`) for display.
     - Handles requests and runs the server.

---

### **2. `process_table.py`**
   - This is a standalone script used to process the input data file (`Table_Input.csv`).
   - It performs calculations to generate the computed results and saves them to `Table2.csv`.
   - You need to run this script first before starting the web app.

---

### **3. `templates/index.html`**
   - The HTML file that defines how the webpage looks.
   - Displays:
     - **Table 1**: The original data from `Table_Input.csv`.
     - **Table 2**: The computed results (`Alpha`, `Beta`, `Charlie`).
   - The page includes a dark theme and row-specific colors for better readability.

---

### **4. `requirements.txt`**
   - Lists all the dependencies required to run the project.
   - Key libraries:
     - `Flask`: Handles the web application.
     - `Gunicorn`: Used for deploying the app to Heroku.

---

### **5. `Procfile`**
   - This file is used by Heroku to run the application.
   - It specifies how to start the app using Gunicorn.

---

### **6. Data Files**
   - **`Table_Input.csv`**:
     - The input file with raw numerical data.
     - Contains two columns: `Index #` (e.g., `A1`, `A2`) and `Value` (numbers).
   - **`Table1.csv`**:
     - A saved copy of the original input data.
   - **`Table2.csv`**:
     - Contains the computed results for `Alpha`, `Beta`, and `Charlie`.

---
