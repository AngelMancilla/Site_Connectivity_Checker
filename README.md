# Site Connectivity Checker 🌐

A Python script to check the availability of websites using HTTP requests. This tool is designed to quickly and efficiently determine whether one or more websites are online, making it ideal for monitoring and troubleshooting.

## 📌 Features

- **Website Availability Check:** Verify if one or more websites are online.
- **Flexible Input Options:** Enter URLs manually or read them from a file.
- **Fast Response Time Measurement** Displays how long it takes to get a response from each site.
- **Asynchronous Mode** Uses ```asyncio``` and ```aiohttp``` to check multiple sites simultaneously for better performance.
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
   
3. **Use asynchronous mode for faster checks**
   ```sh
   python -m Site_Checker -u python.org pypi.org peps.python.org -a

4. **Example output**
   ```sh 
   The status of "python.org" is: "Online!, time response: 0.06 Seconds." 👍
   The status of "docs.python.org" is: "Online!, time response: 0.06 Seconds." 👍
   The status of "pypi.org" is: "Online!, time response: 0.06 Seconds." 👍


---

Made with ❤️ by AngelMancilla
