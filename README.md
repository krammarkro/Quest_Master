

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

### **3. Set Up Google API Service Account**

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable the **Google Sheets API** and **Google Drive API**.
3. Navigate to **IAM & Admin > Service Accounts** and create a new service account.
4. Generate a JSON key file and save it in your project directory (rename to `service_account.json`).
5. Share your Google Sheets document with the service account email (`example@yourproject.iam.gserviceaccount.com`) with **Editor** permissions.
   
### **4. Configure Environment Variables**

Create a `.env` file and add the following:

```
STAFF=YOUR_STAFF_DOCUMENT
DATA=YOUR_PROGRESS_DOCUMENT
ID=ID_OF_DATA_SHEET
TOKEN=YOUR_DISCORD_BOT_TOKEN
```

### **Find Your Google Spreadsheet and Data Sheet ID**

- **Google Spreadsheet ID** (for *DATA=* and *STAFF=*): Found in the URL of your Google Sheet.

  - **Example Staff Document:**\
    https://docs.google.com/spreadsheets/d/1fwX6xHKACtr-61pCsQUVVmDM3rjIkDPDLShFY9o5npY/edit?usp=sharing
  - **Example Progress Document:**\
    https://docs.google.com/spreadsheets/d/1CV44SsLShporYYjFS_esFALAfrKZ_Wpd-jyc6RCyZbo/edit?gid=88965702
  - **Spreadsheet ID:** `1CV44SsLShporYYjFS_esFALAfrKZ_Wpd-jyc6RCyZbo`

- **Data Sheet ID** (ID=): Found after `gid=` in the URL when the DATA sheet is open.

  - **Data Sheet ID:** `88965702`

---


### **5. Configure Settings**

Modify the `settings.toml` file to match your server’s setup:

```toml
[features]
check_old_entries = false

[channels]
assignment_log = #Channel were Extentions Accepted, Decliened and Finished messages are Send
assignment_channel = #Channel were Staff can interact with their assignments
checkup_channel = #If turned on will send a checkup message X days after Assignment
oneshot_channel = #Currently Not used

[assignments]
hiatus = "Hungover" #Hiatus Role

[roles]
RP = ["B", "C"]
TL = ["D", "E"]
PR = ["F", "G"]
CLRD = ["H", "I"]
TS = ["J", "K"]
QC = ["L", "M"]
UPD = ["N", "O"]
```

### **6. Start the Bot**

```bash
python bot_brewery.py
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
