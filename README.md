

---

# **Quest\_Master**

*A self-hosted Discord bot for managing scanlation assignments*

## **📌 Overview**

Quest\_Master is a self-hosted Discord bot designed to assist scanlation groups in efficiently managing their assignment workflow. The bot automates the input of assignment data into a progress sheet and logs updates, reducing manual work and ensuring accuracy.

## **⚡ Key Features**

✔ Automates task assignments and tracking for scanlation projects.\
✔ Seamlessly integrates with Google Sheets for real-time updates.\
✔ Supports bulk assignments and multi-user collaboration.\
✔ Configurable roles, channels, and assignment statuses.\
✔ Designed to streamline management and improve efficiency.

---

## **📥 Installation & Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/Quest_Master.git
cd Quest_Master
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Configure Environment Variables**

Create a `.env` file and add the following:

```
STAFF=YOUR_STAFF_SHEET
DATA=SHEET_WHERE_ALL_THE_SERIES_ARE_STORED
ID=ID_OF_THE_DATA_SHEET
TOKEN=YOUR_DISCORD_BOT_TOKEN
```

### **4. Configure Settings**

Modify the `settings.toml` file to match your server’s setup:

```toml
[features]
check_old_entries = false

[channels]
assignment_log = 1219030657955794954
assignment_channel = 1218705159614631946
checkup_channel = 1224453260543266907
oneshot_channel = 1225634854390206494

[assignments]
hiatus = "Hungover"

[roles]
RP = ["B", "C"]
TL = ["D", "E"]
PR = ["F", "G"]
CLRD = ["H", "I"]
TS = ["J", "K"]
QC = ["L", "M"]
UPD = ["N", "O"]
```

### **5. Start the Bot**

```bash
python bot.py
```

---

## **🛠 Available Commands**

| Command              | Description                                                       |
| -------------------- | ----------------------------------------------------------------- |
| `/channel`           | Links a Discord channel to a series in the progress sheet.        |
| `/updatechannelid`   | Updates the stored channel ID when a channel is changed.          |
| `/updatechannelname` | Updates the sheet name if it has been renamed.                    |
| `/findid`            | Manually logs a Discord user’s ID for tracking.                   |
| `/assign`            | Assigns a scanlation task to a team member and updates the sheet. |
| `/bulkassign`        | Assigns multiple chapters at once.                                |
| `/create`            | Creates a new Discord channel and a corresponding sheet.          |

For a **detailed command guide**, refer to the [Wiki](https://github.com/yourusername/Quest_Master/wiki).

---

## **📩 Feature Requests & Issue Reporting**

If you have suggestions for new features or encounter any issues, please open a **GitHub Issue** in this repository. Provide detailed information, including steps to reproduce any problems, expected behavior, and logs if applicable.

[📌 Submit a Feature Request](https://github.com/krammarkro/Quest_Master/issues)\
[🐛 Report an Issue](https://github.com/krammarkro/Quest_Master/issues)

---

## **📜 License**

This project is licensed under **GPL 3.0**.

---
