# Site Connectivity Checker 🌐

A Python script to check the availability of websites using HTTP requests. This tool is designed to quickly and efficiently determine whether one or more websites are online, making it ideal for monitoring and troubleshooting.

## 📌 Features

- **Website Availability Check:** Verify if one or more websites are online.
- **Flexible Input Options:** Enter URLs manually or read them from a file.
- **Efficient HTTP Requests:** Utilizes `HEAD` requests for faster checks.
- **Multi-Port Support:** Supports checking on ports 80 (HTTP) and 443 (HTTPS).
- **User-Friendly Output:** Provides clear and concise status messages.

## ⚙️ Installation

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/AngelMancilla/site-connectivity-checker.git
   cd site-connectivity-checker

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate     # Windows
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt

## 🚀 Usage
1. **Check websites manually**
   ```sh 
   python -m Site_Checker -u python.org pypi.org peps.python.org
2. **Read URLs from a file**
   ```sh
   python -m Site_Checker -f sites.txt
3. **Example output**
   ```sh 
   The status of "python.org" is: "Online!" 👍
   The status of "pypi.org" is: "Online!" 👍
   The status of "peps.python.org" is: "Online!" 👍

---

Made with ❤️ by AngelMancilla
