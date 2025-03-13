# Getting Started with Python in GitHub Codespaces

## 📌 **Day 1: Introduction to Python & GitHub Codespaces**  
**⏳ Duration:** 1 Hour  
**🎯 Goal:** Understand Python's versatility and learn how to set up and use GitHub Codespaces for development.


## **📝 Understanding Python's Versatility**
Python is one of the most widely used programming languages today due to its simplicity and flexibility. It is used across various domains, making it a must-know language for beginners and professionals alike.

### **🔹 1. Python in Different Fields**

#### **🔸 Web Development**
- Python has powerful web frameworks like Django and Flask that make web development faster and easier.
- **Example:** Developing dynamic websites, web applications, and RESTful APIs.
- **Live Demo Idea:** Show how a simple Flask API works in less than 5 minutes.

#### **🔸 Data Science & Machine Learning**
- Python is widely used in data analysis, AI, and machine learning with libraries like Pandas, NumPy, TensorFlow, and Scikit-learn.
- **Example:** Predicting stock prices using historical data.
- **Live Demo Idea:** Show basic data manipulation using Pandas.

#### **🔸 Automation & Scripting**
- Python is excellent for automating repetitive tasks such as renaming files, sending emails, or scraping web pages.
- **Example:** Automating Excel reports or filling out online forms.
- **Live Demo Idea:** Create a Python script that renames multiple files at once.

#### **🔸 Microcontroller Programming & IoT**
- Python (especially MicroPython) is used to program microcontrollers like ESP32 and Raspberry Pi.
- **Example:** Collecting sensor data and sending it to the cloud.
- **Live Demo Idea:** Show a simple Python script controlling an LED on Raspberry Pi.

#### **🔸 Cybersecurity & Ethical Hacking**
- Python is used for penetration testing, security analysis, and ethical hacking.
- **Example:** Writing scripts to detect open ports on a network.
- **Live Demo Idea:** Demonstrate a simple password generator.

#### **🔸 Game Development**
- Python has game development libraries like Pygame for creating 2D games.
- **Example:** Creating a simple Flappy Bird-style game.
- **Live Demo Idea:** Show basic sprite movement in Pygame.

Python’s adaptability makes it an essential tool for multiple industries, allowing you to build anything from a personal project to a large-scale enterprise application.


## **📝 Why Use GitHub Codespaces?**
GitHub Codespaces provides a **cloud-based development environment**, allowing you to write, run, and test Python code without any local installation.

### **🔹 1. Benefits of GitHub Codespaces**
✅ **No Local Setup Required** – No need to install Python or manage dependencies on your computer.  
✅ **Consistent Environment** – Ensures all users have the same libraries and configurations.  
✅ **Accessible from Any Device** – Works on laptops, tablets, and even mobile phones.  
✅ **Pre-installed Extensions** – Comes with VS Code and essential Python extensions.  
✅ **Seamless GitHub Integration** – Easily syncs projects with GitHub repositories.

### **🔹 2. Setting Up GitHub Codespaces**

#### **Step 1: Creating a GitHub Repository**
1. Go to [GitHub](https://github.com/)
2. Click **New Repository**
3. Name it **python-webinar**
4. Choose **Public** or **Private**
5. Click **Create Repository**

#### **Step 2: Launching GitHub Codespaces**
1. Open the repository
2. Click the `<> Code` button
3. Select **Codespaces** > **New Codespace**
4. Wait for VS Code in the cloud to launch

#### **Step 3: Exploring the VS Code Interface**
- **File Explorer** (left sidebar) for managing files
- **Terminal** (`Ctrl + ~` to open) for running commands
- **Checking Python installation:**
  ```sh
  python --version
  ```


## **🔹 Hands-on: Python Basics in Codespaces**
#### **1. Writing Your First Python Program**
```python
print("Hello, World!")
```
#### **2. Understanding Variables & Data Types**
```python
name = "Abid"  # String
age = 21       # Integer
height = 5.10   # Float
is_student = True  # Boolean
```
#### **3. Basic User Input**
```python
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")
```

#### **4. Conditional Statements (if-else)**
```python
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
```

#### **5. Loops (for and while)**
**For Loop:**
```python
for i in range(5):
    print("Iteration", i)
```
**While Loop:**
```python
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
```


## **🔹 Mini Project: Simple Calculator**
#### **6. Building a Calculator**
```python
while True:  
    print("\nSimple Python Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting Calculator. Thank you!")
        break  # Exit the loop

    if choice in ['1', '2', '3', '4']:  
        num1 = float(input("Enter first number: "))  
        num2 = float(input("Enter second number: "))  

        if choice == '1':  
            result = num1 + num2  
            print(num1, "+", num2, "=", result)  

        elif choice == '2':  
            result = num1 - num2  
            print(num1, "-", num2, "=", result)  

        elif choice == '3':  
            result = num1 * num2  
            print(num1, "*", num2, "=", result)  

        elif choice == '4':  
            if num2 == 0:  
                print("Error: Cannot divide by zero!")  
            else:  
                result = num1 / num2  
                print(num1, "/", num2, "=", result)  

    else:  
        print("Invalid choice! Please enter a number between 1-5.")  
```
#### **7. How to Run:**
1. Copy-paste the code into `calculator.py`
2. Run the program:
   ```sh
   python calculator.py
   ```
3. Test different operations