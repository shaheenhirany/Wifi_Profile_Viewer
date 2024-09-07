import subprocess

# ANSI escape codes for color and font size
RED_TEXT = '\033[91m'
BOLD_TEXT = '\033[1m'
RESET = '\033[0m'

# Function to get and display Wi-Fi password
def get_wifi_password(wifi_name):
    command = f'netsh wlan show profile name="{wifi_name}" key=clear'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
    if result.returncode != 0:
        print(f"{RED_TEXT}Error: Unable to retrieve Wi-Fi details for '{wifi_name}'{RESET}")
    else:
        print(result.stdout)

# Get Wi-Fi name from user input with styled message
wifi_name = input(f"""{BOLD_TEXT}{RED_TEXT}Powered by SHAHEEN HIRANI{RESET}

Enter the Wi-Fi name: """)

# Run the Wi-Fi password retrieval
get_wifi_password(wifi_name)

# Keep the script running for further interactions
while True:
    next_action = input(f"{BOLD_TEXT}Would you like to check another Wi-Fi network? (yes/no): {RESET}").strip().lower()
    if next_action == "yes":
        wifi_name = input(f"{BOLD_TEXT}Enter the Wi-Fi name: {RESET}")
        get_wifi_password(wifi_name)
    elif next_action == "no":
        print(f"{RED_TEXT}Exiting the script. Goodbye!{RESET}")
        break
    else:
        print(f"{RED_TEXT}Please enter 'yes' or 'no'.{RESET}")