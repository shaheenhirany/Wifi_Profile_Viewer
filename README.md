# WiFiProfileViewer

A Python script to retrieve Wi-Fi passwords for saved network profiles on Windows using the `netsh` command. The script allows users to view the password for a specified Wi-Fi network and can repeatedly check different networks as needed.

## Features

- Retrieve and display Wi-Fi passwords for saved profiles.
- Interactive command-line interface.
- Easy to use with a simple prompt for user input.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Administrator Privileges**: The script requires admin rights to access Wi-Fi profiles.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shaheenhirany/WiFiProfileViewer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd WiFiProfileViewer
   ```

3. No additional dependencies are required for this script.

## Usage

1. Run the script:

   ```bash
   python wifiprofileviewer.py
   ```

2. Enter the name of the Wi-Fi network when prompted.

3. The script will display the Wi-Fi password if available.

4. You can choose to check other Wi-Fi networks or exit the script.

**Example:**

```
Powered by SHAHEEN HIRANI

Enter the Wi-Fi name: MyNetwork

[Output with Wi-Fi details]
```

## Error Handling

- If the Wi-Fi name does not exist or if there are permission issues, the script will display an error message.

## Author

- **Shaheen Hirani**  
  Email: [shaheen.nhirani@gmail.com](mailto:shaheen.nhirani@gmail.com)

---

*Powered by SHAHEEN HIRANI*
```

This version includes all necessary details with proper formatting and clearer instructions. If you need any more changes, just let me know!
