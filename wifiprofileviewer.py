import subprocess
from colorama import init, Fore, Style

# Initialize colorama
init()

# Function to get and display Wi-Fi password
def get_wifi_password(wifi_name):
    command = f'netsh wlan show profile name="{wifi_name}" key=clear'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
    if result.returncode != 0:
        print(f"{Fore.RED}{Style.BRIGHT}Error: Unable to retrieve Wi-Fi details for '{wifi_name}'{Style.RESET_ALL}")
    else:
        print(result.stdout)

# Get Wi-Fi name from user input with styled message
wifi_name = input(f"""{Style.BRIGHT}{Fore.RED}Powered by SHAHEEN HIRANI{Style.RESET_ALL}

Enter the Wi-Fi name: """)

# Run the Wi-Fi password retrieval
get_wifi_password(wifi_name)

# Keep the script running for further interactions
while True:
    next_action = input(f"{Style.BRIGHT}Would you like to check another Wi-Fi network? (yes/no): {Style.RESET_ALL}").strip().lower()
    if next_action == "yes":
        wifi_name = input(f"{Style.BRIGHT}Enter the Wi-Fi name: {Style.RESET_ALL}")
        get_wifi_password(wifi_name)
    elif next_action == "no":
        print(f"{Fore.RED}{Style.BRIGHT}Exiting the script. Goodbye!{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.RED}{Style.BRIGHT}Please enter 'yes' or 'no'.{Style.RESET_ALL}")