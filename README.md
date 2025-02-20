# 📖 Quest Master Bot

A **self-hosted Discord bot** designed to help scanlation groups efficiently manage their assignment data. The bot automates the input of assignment data into a progress sheet and logs updates.

---

## 🚀 Features
- **Assignment Data Management**: Automates the input of assignments into a progress sheet.
- **Automated Logging**: Keeps track of assignments in designated channels.
- **Hiatus Handling**: Prevents members with a specific role from receiving assignments.
- **Customizable Settings**: Configure features, roles, and channels via `settings.toml`.

---

## 🛠️ Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/Quest_Master.git
cd Quest_Master
```

### **2️⃣ Install Dependencies**
The bot requires multiple Python packages. Install them using:
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**
Create a `.env` file in the root directory with the following content:
```ini
STAFF=YOUR_STAFF_SHEET
DATA=SHEET_WHERE_ALL_THE_SERIES_ARE_STORED
ID=ID_OF_THE_DATA_SHEET
TOKEN=YOUR_DISCORD_BOT_TOKEN
```

### **4️⃣ Configure `settings.toml`**
Customize bot behavior by modifying `settings.toml`:
```toml
[features]
check_old_entries = false  # Toggle checking old assignments

[channels]
assignment_log = 1219030657955794954
assignment_channel= 1218705159614631946
checkup_channel = 1224453260543266907

[assignments]
hiatus = "Hungover"  # Role that prevents assignment

[roles]
RP = ["B", "C"]
TL = ["D", "E"]
PR = ["F", "G"]
CLRD = ["H", "I"]
TS = ["J", "K"]
QC = ["L", "M"]
UPD = ["N", "O"]
```

### **5️⃣ Run the Bot**
```bash
python bot_brewery.py
```

---

## 🔧 Usage
The bot provides various Discord commands to manage assignment data. Here are some key commands:
```
/assign [series] [chapter] [role] [user] - Logs an assignment into the progress sheet.
/check - Lists current assignments.
```
For a full list of commands, use:
```
/help
```

## 📬 Contact & Support
If you have any issues or suggestions, feel free to open an **issue** on GitHub!

