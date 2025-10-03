
# 💬 Wi-Fi Troubleshooting Chatbot (Python CLI)

A simple command-line chatbot designed to assist users in troubleshooting common Wi-Fi connectivity issues.  
This project was created as part of the eGain SWE Take-Home Assignment for the Customer Service Chatbot Interaction Designer role.

---

## 📦 Features

- Guided conversation flow for diagnosing basic Wi-Fi issues
- User-friendly prompts with built-in error handling
- Modular and well-commented Python code
- Handles unexpected inputs gracefully

---

## 🚀 Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/egain-chatbot.git
cd egain-chatbot
```

2. **Run the chatbot**

Make sure you have Python 3 installed.

```bash
python3 wifi_chatbot.py
```

---

## 🧠 Design Approach

### Scenario: 
> *"My Wi-Fi isn’t working."*

The chatbot guides users through a decision tree:
1. Is the router plugged in?
2. What type of connection is used? (Wi-Fi or Ethernet)
3. Can other devices connect?
4. Has the router been rebooted?
5. If all else fails, suggest contacting ISP.

### Error Handling:
- Re-prompts for unexpected inputs (e.g., "maybe" when "yes/no" is expected)
- Handles casing, spacing, and invalid options

---

## 🖼️ Screenshots

> Add screenshots here after running your chatbot  
> Example:

```
👋 Hi! I'm your Wi-Fi Troubleshooting Assistant.
📶 Is your router plugged in and showing lights? (yes/no): yes
🖥️ Are you using Wi-Fi or Ethernet? (wifi/ethernet): wifi
📱 Can other devices connect to the Wi-Fi? (yes/no): no
🔁 Have you tried rebooting your router? (yes/no): no
🛠️ Please try unplugging the router for 30 seconds, then plug it back in.
```

---

## 📈 Future Improvements

- Add support for voice input/output
- Use NLP to make the bot more conversational
- Add logging for agent handoff or escalation
- Expand scenarios to support more technical issues

---

## 📬 Submission Details

This repository was created for the eGain SWE Take-Home Assignment.  
It demonstrates creativity, user-focused design, and error-resilient interaction in a minimal interface.
