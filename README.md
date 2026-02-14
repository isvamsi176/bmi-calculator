# 🧮 BMI Calculator (Python GUI Application)

## 📌 Project Overview

This project is a modern GUI-based BMI (Body Mass Index) Calculator developed using Python and Tkinter.

The application allows users to enter personal details such as:

- User Name
- Mobile Number
- Age
- Gender (Male/Female)
- Height (in centimeters)
- Weight (in kilograms)

The system calculates BMI using the standard formula and classifies it into predefined health categories. All user records are stored locally for reference.

---
## Demo app  images
<img width="521" height="912" alt="image" src="https://github.com/user-attachments/assets/48f0da81-58d8-485d-b7f7-b0c3b8c6e824" />



## 🎯 Objectives

- Develop a user-friendly BMI Calculator.
- Implement proper input validation.
- Classify BMI results into health categories.
- Store user data in a file.
- Demonstrate GUI programming concepts.

---

## 🧮 BMI Formula

BMI = Weight (kg) / (Height (m))²

Height entered in centimeters is automatically converted into meters.

---

## 📊 BMI Categories

| BMI Range        | Category            |
|------------------|--------------------|
| Less than 18.5   | Underweight        |
| 18.5 – 24.9      | Normal Weight      |
| 25 – 29.9        | Overweight         |
| 30 and above     | Extremely Obese    |

---

## 🚀 Features

- Clean and modern GUI
- User input validation
- 10-digit mobile number verification
- Age numeric validation
- Gender selection using radio buttons
- Automatic BMI calculation
- Health category display with color indication
- Data saved in `bmi_records.txt`
- SMS simulation popup message
- Error handling using try-except

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter (GUI Framework)
- File Handling
- Exception Handling

---

## 📂 Project Structure
BMI_Calculator_Project/
│
├── bmi_calculator.py
├── bmi_records.txt
└── README.md
