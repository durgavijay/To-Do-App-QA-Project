# To-Do List App QA Project

## Overview
This repository contains the Quality Assurance project for the To-Do List Web Application. It includes both manual and automated testing artifacts.

## Contents
- **todo_app/**: Contains the Flask application.
- **ManualTesting/**: Contains the test plan and test cases.
- **AutomatedTesting/**: Contains automated test scripts and test results.
- **README.md**: Project overview and instructions.

## How to Run the Application
1. Navigate to the `todo_app` directory.
2. Install Flask: `pip install flask`
3. Run the application: `flask run`
4. Open `http://localhost:5000` in your web browser.

## How to Run Automated Tests
1. Ensure ChromeDriver is installed and in your PATH.
2. Navigate to the `AutomatedTesting/TestScripts` directory.
3. Install Selenium: `pip install selenium`
4. Run the test scripts:
   ```sh
   python test_add_task.py
   python test_delete_task.py
