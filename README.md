# 🚀 Efsane Bypass Script  

This script automates the registration process on **EfsaneTR** by solving captchas, sending OTP requests, and submitting registration forms.  

## ⚠ Disclaimer  
This script is developed **for educational purposes only**. Misuse of this script is **strictly prohibited**. Use at your own risk!  

---

## ✨ Features  
✔ **Captcha Bypass** (Cloudflare Turnstile)  
✔ **Automated OTP Request**  
✔ **Proxy Support** (Uses random proxies from `config.py`)  
✔ **User-Agent Randomization**  
✔ **Automated Registration**  

---

## 📜 Requirements  

Make sure you have **Python 3.7+** installed on your system.  

### 🔧 Install Dependencies  

Run the following command to install required Python modules:  

```bash
pip install requests colorama anticaptchaofficial
```

---

## 🚀 How to Use  

1. **Clone the Repository**  

```bash
git clone https://github.com/Air-Ashu/Efsanetr.git
cd Efsanetr
```

2. **Configure Settings**  

Edit `config.py` to update the following:  

- **Invite Code**  
- **AntiCaptcha API Key**  
- **Proxy List**  
- **Phone Numbers**  

3. **Run the Script**  

```bash
python main.py
```

4. **Follow On-Screen Instructions**  

- Enter your **invite code** (only once).  
- Provide **Country Code** and **Mobile Number**.  
- The script will solve the captcha and send an OTP request.  
- Enter the **OTP received** on your mobile.  
- The script will attempt to complete the registration.  

---

## 🛠 Troubleshooting  

1. **Proxies Not Found?**  
   - Ensure `config.py` contains working proxies.  
   
2. **Captcha Not Solving?**  
   - Ensure your **AntiCaptcha API key** is valid.  
   - If needed, update the API key in `config.py`.  

3. **Registration Fails?**  
   - Ensure the phone number format is correct.  
   - Verify that the invite code is still active.  

---

## 👨‍💻 Developer Notes  

- The script uses **random user-agents** to mimic real users.  
- The password is **randomly generated** for security.  
- The script **exits gracefully** on `CTRL+C`.  

---

### 🏴‍☠️ Warning  

Using this script to spam, exploit, or bypass security systems **may violate legal policies**. The author is **not responsible** for any misuse.  

---

## 📜 License  

**MIT License** - Feel free to modify and distribute!  

---

## 📢 Credits  

- **Developed by:** [Ashuxd-X](https://telegram.im/lootersera_th)  
- **Configuration Updated by:** [Shivam](https://t.me/Shivam_jaiswal0011)  
