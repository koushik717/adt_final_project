# Restaurant Inspections Management System

## Team Members
- Sai Shriya Surla (ssurla)
- Venkata Koushik Nakka (vnakka)
- Neeraj Boyapati (neboya)
- Yamini Srija Koulury (ykoulury)

---

## Project Overview
The **Restaurant Inspections Management System** is a comprehensive web application designed to manage, analyze, and visualize restaurant inspection data. The system allows users to perform CRUD (Create, Read, Update, Delete) operations on inspection records and generate interactive visualizations to identify trends and patterns in restaurant compliance.

## Features
- **User Authentication**: Secure signup and login system.
- **CRUD Operations**: Manage Establishments, Employees, Inspections, and Violations.
- **Data Visualization**: Interactive charts for inspections, fines, and trends.
- **Home Dashboard**: Quick statistics and team overview.

---

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- `pip` package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/koushik717/adt_final_project.git
   cd adt_final_project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: If `requirements.txt` is missing, run: `pip install streamlit pandas`)*

4. **Initialize the Database**
   Run the setup script to create the database and load initial data from CSV files.
   ```bash
   python3 setup_database.py
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

---

## Usage Instructions

1. **Access the App**: Open your browser to `http://localhost:8501`.
2. **Sign Up / Login**:
   - create a new account using the "Sign Up" option in the sidebar.
   - Log in with your new credentials.
3. **Navigation**:
   - Use the **Sidebar** to select a Table (e.g., `establishment`, `inspection`).
   - Select an **Action**:
     - **Read**: View data.
     - **Create/Update/Delete**: Manage records.
     - **Visualize**: Generate charts.
4. **Visualizations**: Select "Visualize" to see graphs like "Inspections Over Time" or "Results Distribution".
