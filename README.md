# Day 91: Advanced Python Keylogger (Educational Simulation) 🛡️

## 📌 Overview
This project is part of my **365 Days of Cybersecurity** challenge. It demonstrates the mechanics of **Input Hooking** and **Data Exfiltration** using Python. The goal is to understand how unauthorized software captures keystrokes and how to defend against such threats.

## ✨ Features
- **Global Keyboard Hooking**: Uses `pynput` to intercept hardware signals.
- **Remote Reporting**: Integrated with **Telegram Bot API** for real-time exfiltration.
- **Offline Caching**: Automatically saves logs to a hidden local file when internet is unavailable and syncs once connection is restored.
- **Forensic Timestamps**: Logs include precise dates and times for event correlation.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Libraries**: `pynput`, `requests`, `threading`, `datetime`

## 🚦 Security & Ethics
> **DISCLAIMER**: This tool is for **educational and authorized security testing purposes only**. Unauthorized use of this script on a computer you do not own is illegal and unethical. 

## 🚀 How to Use
1. Clone the repository.
2. Install dependencies: `pip install pynput requests`.
3. Create a `.env` file or update the `BOT_TOKEN` and `CHAT_ID` variables.
4. Run the script: `python keylogger.py`.
