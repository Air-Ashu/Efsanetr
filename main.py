import requests
import time
import random
import json
import sys
from anticaptchaofficial.turnstileproxyless import turnstileProxyless
from colorama import Fore, Style, init
from config import *  

init(autoreset=True)

# Banner
def print_banner():
    banner = f"""{Fore.CYAN}

██████╗░░█████╗░░█████╗░███╗░░░███╗
██╔══██╗██╔══██╗██╔══██╗████╗░████║
██████╦╝██║░░██║██║░░██║██╔████╔██║
██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║
██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║
╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝
{Style.RESET_ALL}
{Fore.YELLOW}[*] Efsanetr Bypass Script - Automated Registration
[*] Fully Automated - Just Enter OTP
[*] Developed for educational purposes only!
----------------------------------------------------{Style.RESET_ALL}
"""
    print(banner)
    print("")  


# Fetch Proxy Addresses
def get_proxy_ip(proxy):
    try:
        ipv4 = requests.get("https://api64.ipify.org?format=json", proxies=proxy, timeout=5).json().get("ip", "Unknown")
        ipv6 = requests.get("https://ident.me", proxies=proxy, timeout=5).text
        return ipv4, ipv6
    except:
        return " [✘] Failed to fetch", "Failed to fetch"

# Generate Random Password
def generate_password():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_!"
    return "".join(random.choices(chars, k=12))

# Captcha Solver
def captcha_bypass():
    print(Fore.YELLOW + "[*] Solving Captcha... Please wait.\n")  
    solver = turnstileProxyless()
    solver.set_verbose(1)
    solver.set_key(anticaptcha_api_key)  
    solver.set_website_url("https://efsanetr.com")
    solver.set_website_key("0x4AAAAAAA8edKY9bI4XxjIA")

    token = solver.solve_and_return_solution()

    print("")  
    if token:
        print(Fore.GREEN + "[✔] Captcha solved successfully!\n") 
        return token
    else:
        print(Fore.RED + "[✘] Captcha failed.\n")  
        return None

# Send OTP with Retry Logic
def send_otp(session, country_code, mobile, captcha_token):
    url = "https://efsanetr.com/api/v2/send/mobileCode"
    payload = {'mobile': mobile, 'countryCode': country_code}
    headers = {
        'User-Agent': random.choice(user_agents),  
        'Verification': captcha_token,
        'X-Requested-With': "XMLHttpRequest"
    }

    for attempt in range(3):  
        response = session.post(url, data=payload, headers=headers).json()
        if response.get("code") == 0:
            print(Fore.GREEN + "[✔] OTP sent successfully!\n")  
            return True
        else:
            print(Fore.RED + f"[✘] OTP failed (Attempt {attempt + 1}/3): {response}\n")  
            time.sleep(5)  
    return False  

# Register Account
def register(session, mobile, captcha_token, password, country_code, otp):
    url = "https://efsanetr.com/api/v2/register"
    payload = {
        'mobile': mobile,
        'inviteCode': invite_code, 
        'cf-turnstile-response': captcha_token,
        'passWord': password,
        'confirmPassWord': password,
        'type': "1",
        'countryCode': country_code,
        'validCode': otp
    }
    headers = {
        'User-Agent': random.choice(user_agents), 
        'Verification': captcha_token,
        'X-Requested-With': "XMLHttpRequest"
    }

    response = session.post(url, data=payload, headers=headers).json()
    if response.get("code") == 0:
        print(Fore.GREEN + "[✔] Registration successful!\n") 
        return True
    else:
        print(Fore.RED + f"[✘] Registration failed: {response}\n") 
        return False

# Save Accounts to JSON
def save_account(mobile, password):
    account_data = {"mobile": mobile, "password": password}
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        accounts = []

    accounts.append(account_data)

    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)

# Main Execution
def main():
    print_banner()  

    if len(proxies) < len(numbers): 
        print(Fore.RED + "[✘] Not enough proxies for numbers. Exiting...\n")  
        sys.exit(1)

    for i in range(min(len(numbers), max_accounts)):  
        session = requests.Session()
        proxy = {"http": f"http://{proxies[i]}", "https": f"http://{proxies[i]}"}
        session.proxies.update(proxy)

        ipv4, ipv6 = get_proxy_ip(proxy)
        print(Fore.CYAN + f"[*] Using Proxy: {proxies[i]}")
        print(Fore.BLUE + f"[*] Proxy IPv4 Address: {ipv4}")
        print(Fore.BLUE + f"[*] Proxy IPv6 Address: {ipv6}\n")  

        country_code, mobile = numbers[i].split(",") 

        password = generate_password()
        captcha_token = captcha_bypass()
        if not captcha_token:
            continue

        if not send_otp(session, country_code, mobile, captcha_token):
            continue

        otp = input(Fore.YELLOW + f"[✔] Enter OTP for +{country_code} {mobile}: ").strip()  
        if register(session, mobile, captcha_token, password, country_code, otp):
            save_account(mobile, password)

        print(Fore.CYAN + "[*] Moving to the next account...\n")  
        time.sleep(delay_between_accounts)  

if __name__ == "__main__":
    main()

