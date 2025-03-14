# 🚀 Python Workshop - Day 2

## 📌 Session Outline

### 1️⃣ GitHub ও Version Control পরিচিতি 👍

#### 🔹 Git Commands

```bash
git init
git add .
git commit -m "Your commit message"
git remote add origin <Github Repository URL>
git branch -M main
git push origin main
```

#### 🔹 Modifying Code & Updating Repository

```bash
git add <file name>
git commit -m "Update file"
git push origin main
```

#### 🔹 Cloning & Pulling Changes

```bash
git clone <Repository URL>
git pull origin main
```

#### 🔹 Other Version Control Methods

```bash
| Situation                                      | Command                              |
|-----------------------------------------------|--------------------------------------|
| Just browsing an old version                 | `git checkout <commit-hash>`        |
| Go back permanently & delete changes         | `git reset --hard <commit-hash>`    |
| Undo last commit but keep files              | `git reset --soft HEAD~1`           |
| Undo a specific commit safely                | `git revert <commit-hash>`          |
```

---

### 2️⃣ GitHub Codespaces & Python Script Run করা 👍

- GitHub Codespaces ব্যবহার করে Python কোড রান করা
- Cloud-based Development Environment

---

### 3️⃣ GitHub এ প্রজেক্ট সংরক্ষণ 👍

- কিভাবে Python প্রজেক্ট GitHub-এ আপলোড করা যায়
- Version control এর সুবিধা

---

### 4️⃣ Writing & Running Python Project 👍

#### 🔹 পাইথন কি?

- ইন্টারপ্রিটেড ল্যাঙ্গুয়েজ
- অবজেক্ট অরিয়েন্টেড প্রোগ্রামিং ল্যাঙ্গুয়েজ
- হাই লেভেল প্রোগ্রামিং ল্যাঙ্গুয়েজ

#### 🔹 পাইথন কেনো শিখবো?

- **Web Development**: Django, Flask
- **Data Science/ML**: NumPy, Pandas, Matplotlib, Seaborn
- **Automation / Scripting**: Selenium, Scrapy, BeautifulSoup

#### 🔹 Environment Setup

- Python Interpreter Download
- VS Code Setup

---

### 5️⃣ Project: Number Guessing Game with Python 👍

#### 🔹 Code

```python
from random import randint

print("Welcome to Number Guessing Game")

secret_number = randint(1, 10)
attempt = 0

while True:
    guess = int(input("Enter your guess: "))
    attempt += 1

    if guess < secret_number:
        print("You guessed low. Try again!")
    elif guess > secret_number:
        print("You guessed high. Try again!")
    else:
        print("Congrats, You guessed the right number!")
        print(f"You guessed the right number in {attempt} attempts.")
        break

print("Game Over")
```

---

### 6️⃣ Python Package Handling with `pip` 👍

#### 🔹 Installing Packages

```bash
pip install pyttsx3
pip install cowsay
```

#### 🔹 Example Code

```python
import pyttsx3
import cowsay

text = "Thank you for joining our day 2"

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()

cowsay.cow("See you soon!")
```

---

### 🎥 **Workshop Recording**

🔗 **YouTube Video:** [Click here](https://youtu.be/dBSDCewLqTA)

---

🚀 **Thank you for joining Day 2! Stay tuned for more learning!**
