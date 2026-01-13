# 🔐 Weak Password Checker GUI

**Weak Password Checker GUI** is a beginner-friendly desktop application for analyzing password strength.  
It allows you to check a list of passwords against a weak password dictionary, identify weak passwords, and get recommendations on how to improve them.

---

## 📸 Screenshot

![Weak Password Checker GUI](https://i.ibb.co.com/nq9YbfN0/photo-2026-01-13-21-48-35.jpg)


---

## 🛠 Features

- ✅ Load passwords from a file (`passwords.txt`)
- ✅ Built-in or custom weak password dictionary (`weak.txt`)
- ✅ Analyze each password for strength
- ✅ Show reasons why a password is weak
- ✅ Suggest ways to improve passwords
- ✅ Save analysis report to a text file
- ✅ GUI interface using Python Tkinter
- ✅ Ready for Windows EXE build

---

## 📊 Strength Analysis Criteria

- **VERY WEAK:** Found in weak dictionary
- **WEAK:** Too short (<8 characters)
- **MEDIUM:** Limited character diversity
- **STRONG:** Good length and mix of characters

💡 Suggestions may include:

- Add uppercase letters
- Add lowercase letters
- Add digits
- Add symbols
- Make the password longer

---

## 📁 Project Structure

###weak_password_checker/
├─ app.py # Main GUI application
├─ analyzer.py # Password analysis logic
├─ loader.py # File loader utility
├─ data/
│ └─ weak.txt # Default weak password dictionary
├─ passwords.txt # Example file with passwords to check
├─ README.md
└─ requirements.txt

---

## 💻 How to Run
### 1️⃣ Run via source code (Python required)

1.  Make sure you have Python 3 installed  
2.  Tkinter comes with Python (no extra packages required)  
3.  Open a terminal/command prompt and run: python app.py
4. The GUI will open automatically. Weak password dictionary `data/weak.txt` loads by default.  
5. Load your `passwords.txt` file and click **Analyze**  
6. Save your report if needed

---

### 2️⃣ Run via Windows EXE (no Python needed)

1.  Download `WeakChecker.exe` from the [Releases](#) section  
2.  Double-click `WeakChecker.exe` to open the GUI  
3.  Weak password dictionary is loaded automatically  
4.  Load your passwords file and click **Analyze**  
5.  Save report using **Save Report** button  

> CMD window will not appear in this version

---

## 🔧 How it Works

1. The program loads a list of passwords and a weak password dictionary  
2. Each password is analyzed for:
   - Dictionary matches
   - Length
   - Character diversity
3. Each password is assigned a **strength status**  
4. Reasons for weakness and suggestions are displayed in the GUI  
5. Report can be saved to a `.txt` file

---

## 🎯 Future Improvements

- Add **progress bar** for large files  
- Add **CSV/JSON report export**  
- Add **PDF report export**  
- Add **dark theme** for GUI  
- Integrate **regex rules** to detect common weak patterns  
- Build **cross-platform version** for Mac/Linux  

---

## 📂 Example Files

- `data/weak.txt` — default weak password dictionary  
- `passwords.txt` — example file to test the application

---

## 📫 Contact

**Developer:** Daniil  
**Location:** Aktobe, Kazakhstan  
**GitHub:** [https://github.com/l1noth](https://github.com/l1noth)  
**Telegram:** @no666one  
**Email:** elliotkorobkin@gmail.com


