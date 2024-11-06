import os
import subprocess
import socket
import shutil

torrc_path = '/etc/tor/torrc'
valid_country_codes = {
        'tr': 'Turkey', 
        'de': 'Germany', 
        'us': 'United States', 
        'fr': 'France', 
        'uk': 'United Kingdom',
        'at': 'Austria', 
        'be': 'Belgium', 
        'ro': 'Romania', 
        'ca': 'Canada', 
        'sg': 'Singapore',
        'jp': 'Japan', 
        'ie': 'Ireland', 
        'fi': 'Finland', 
        'es': 'Spain', 
        'pl': 'Poland'
    }


def clear_screen():
    os.system("clear")

def sinasims():
    print('''\033[1;36m
                                                                    
  _________.__                     .__                
 /   _____/|__| ____ _____    _____|__| _____   ______
 \_____  \ |  |/    \\__  \  /  ___/  |/     \ /  ___/
 /        \|  |   |  \/ __ \_\___ \|  |  Y Y  \\___ \ 
/_______  /|__|___|  (____  /____  >__|__|_|  /____  >
        \/         \/     \/     \/         \/     \/ 
                                                      
          
    \033[0m''')

def install_tor():
    try:
        print("Installing Tor ...\n")
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        subprocess.run(['sudo', 'apt', 'install', '-y', 'tor'], check=True)
        print("[+] Tor has been installed successfully.")
        print("Installing Tor-geoipdb ...\n")
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'tor-geoipdb'], check=True)
        print("[+] Tor-geoipdb has been installed successfully.")
        print("Installing python3-pip ...\n")
        subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-pip'], check=True)
        print("[+] python3-pip has been installed successfully.")
        print("Installing requests ...\n")
        subprocess.run(['pip3', 'install', 'requests'], check=True)
        subprocess.run(['pip3', 'install', 'requests[socks]'], check=True)
        print('[+] python3 requests is installed.')
        print(".")
        print(".")
        print(".")
        print("[+] Tor has been installed successfully.")
        input("Press Enter to continue")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing Tor: {e}")
        input("Press Enter to continue")

def uninstall_tor():
    print("Uninstalling Tor ...\n")
    try:
        subprocess.run(['sudo', 'apt', 'remove', '-y', 'tor'], check=True)
        print("Tor has been uninsalled successfully.")
        input("Press Enter to continue")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while uninsalling Tor: {e}")
        input("Press Enter to continue")

def update_tor():
    try:
        # Check if Tor is installed
        result = subprocess.run(['which', 'tor'], capture_output=True, text=True)
        
        if result.stdout:
            print("Updating Tor...\n")
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            subprocess.run(['sudo', 'apt', 'upgrade', 'tor'], check=True)
            print("Tor has been updated successfully.")
        else:
            print("Tor is not installed. Please install Tor first.")
            _X = input("Do you want to install Tor? [Y/n]: ")
            if _X.lower() in ['y', '']:
                install_tor()

        
        input("Press Enter to continue")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def show_numbers():
    tor_status = check_tor()
    if(tor_status):
        tor = True
    else:
        tor = False
    print(" \033[1;32mSinasims tor management:\033[0m\n")
    print(" \033[0;32mversion: \033[0;33mv1.0\033[0m")
    print(" \033[0;32mgithub: \033[0;33mgithub.com/sinasims/torsina")
    print(" \033[0;32mTelegram ID: \033[0;33mt.me/sinasimss")
    print("\033[0;33m═════════════════════════════════════════════\033[0m")
    if tor:
        print(" \033[0;36mTor: \033[0;32mInstalled")
    else:
        print(" \033[0;36mTor: \033[0;31mNot installed")

    
    socks_port, countries = read_torrc(torrc_path)
    if(socks_port == None):
        socks_port = 9050
    print(f" \033[0;36mYour Tor Server: \033[0;33m127.0.0.1:{socks_port}\033[0m")
    print(f" \033[0;36mYour Tor Countries: \033[0;33m{countries}\033[0m")
    # if get_server_location() != None:
    #     country, ip = get_server_location()
    #     print(f" \033[0;36mServer Location: \033[0m{country}")
    #     print(f" \033[0;36mServer IP: \033[0m{ip}")

    print("\033[0;33m═════════════════════════════════════════════\033[0m\n")

    
    if tor:
        print(" \033[1;32m1 -\033[0m install tor (" + "\033[1;32minstalled\033[0m)")
    else:
        print(" \033[1;32m1 -\033[0m install tor (" + "\033[1;31mnot installed\033[0m)")
    print(" \033[1;32m2 -\033[0m update tor")
    print(" \033[1;32m3 -\033[0;31m uninstall tor\033[0m")
    print("-----------------")
    print(" \033[1;32m4 -\033[0m get tor IP")
    print(" \033[1;32m5 -\033[0m cronjob(set time for change your tor IP)")
    print("-----------------")
    print(" \033[1;32m6 -\033[0m change tor IP")
    print(" \033[1;32m7 -\033[0m change tor Port")
    print(" \033[1;32m8 -\033[0m change tor Countries")
    print("-----------------")
    print(" \033[1;32m9 -\033[0m start tor")
    print(" \033[1;32m10-\033[0m stop tor")
    print(" \033[1;32m11-\033[0m restart tor")
    print(" \033[1;32m12-\033[0m reload tor")
    print(" \033[1;32m13-\033[0m status tor")
    print("-----------------")
    print(" \033[1;32m0 -\033[0m exit\n\n")

def check_tor():
    try:
        # Check if Tor is installed
        result = subprocess.run(['which', 'tor'], capture_output=True, text=True)
        if result.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False
            
def modify_torrc(file_path, new_socks_port=None, new_exit_nodes=None):
    try:
        if(check_tor()):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Flags to check if SocksPort and ExitNodes are present
            socks_port_found = False
            exit_nodes_found = False

            modified_lines = []
            for line in lines:
                stripped_line = line.strip()
                if stripped_line.startswith('SocksPort'):
                    socks_port_found = True
                    if new_socks_port is not None:
                        modified_lines.append(f"SocksPort {new_socks_port}\n")
                    else:
                        modified_lines.append(line)
                elif stripped_line.startswith('ExitNodes'):
                    exit_nodes_found = True
                    if new_exit_nodes is not None:
                        modified_lines.append(f"ExitNodes {new_exit_nodes}\n")
                    else:
                        modified_lines.append(line)
                else:
                    modified_lines.append(line)

            # Add new entries if they were not found
            if not socks_port_found and new_socks_port is not None:
                modified_lines.append(f"SocksPort {new_socks_port}\n")
            
            if not exit_nodes_found and new_exit_nodes is not None:
                modified_lines.append(f"ExitNodes {new_exit_nodes}\n")

            with open(file_path, 'w') as file:
                file.writelines(modified_lines)

            print("The torrc file has been updated successfully.")
        else:
            print("\033[31mTor is not installed.\033[0m\nPlease install it first.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_torrc(file_path):
    try:
        if(check_tor()):
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Extract values for 'SocksPort' and 'ExitNodes'
            socks_port = None
            exit_nodes = None
            
            for line in lines:
                line = line.strip()
                if line.startswith('SocksPort'):
                    parts = line.split()
                    if len(parts) > 1:
                        socks_port = parts[1]
                elif line.startswith('ExitNodes'):
                    parts = line.split(maxsplit=1)
                    if len(parts) > 1:
                        exit_nodes = parts[1]
            
            return socks_port, exit_nodes
        else:
            print("\033[31mTor is not installed.\033[0m\nPlease install it first.")
            return None, None
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def reload_tor():
    if(check_tor()):
        os.system("service tor reload")
    else:
        print("\033[31mTor is not installed.\033[0m\nPlease install it first.")

def restart_tor():
    print("\n")
    if(check_tor()):
        try:
            subprocess.run(['sudo', 'systemctl', 'restart', 'tor'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while restarting Tor: {e}")
    else:
        print("\033[31mTor is not installed.\033[0m\nPlease install it first.")

def start_tor():
    print("\n")
    if(check_tor()):
        try:
            subprocess.run(['sudo', 'systemctl', 'start', 'tor'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while starting Tor: {e}")
    else:
        print("\033[31mTor is not installed.\033[0m\nPlease install it first.")

def stop_tor():
    print("\n")
    if(check_tor()):
        try:
            subprocess.run(['sudo', 'systemctl', 'stop', 'tor'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while stopping Tor: {e}")
    else:
        print("\033[31mTor is not installed.\033[0m\nPlease install it first.")

def status_tor():
    print("\n")
    if(check_tor()):
        try:
            result = subprocess.run(['sudo', 'systemctl', 'status', 'tor'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("Tor status:")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Tor is stopped.\n{e.stderr}")
    else:
        print("\033[31mTor is not installed.\033[0m\nPlease install it first.")


def create_cron_job():
    while True:
        clear_screen()
        sinasims()
        print("Select an option for change your IP on tor:\n")
        print("\033[1;32m0\033[0m - Exit\n")
        print("\033[1;32m1\033[0m - 1 minute")
        print("\033[1;32m2\033[0m - 30 minutes")
        print("\033[1;32m3\033[0m - 1 hour")
        print("\033[1;32m4\033[0m - 4 hours")
        print("\033[1;32m5\033[0m - 12 hours")
        print("\033[1;32m6\033[0m - 24 hours\n")

        option = input("Select your option [0-6]: ")

        # تنظیم زمان‌بندی بر اساس انتخاب کاربر
        delay_map = {
            '1': 1,
            '2': 30,
            '3': 60,
            '4': 240,
            '5': 720,
            '6': 1440
        }

        if option == '0':
            print("Exiting...")
            return  # خروج از تابع

        elif option in delay_map:
            delay_minutes = delay_map[option]
            print(f"Cron job set for every {delay_map[option]} minutes.")
            break  # خروج از حلقه while
        
        else:
            print("Invalid option selected.")
            input("Press Enter to continue...")

    # دستوراتی که می‌خواهیم زمان‌بندی کنیم
    commands = [
        "service tor reload",
        "systemctl restart tor"
    ]
    
    # مسیر جدید: پوشه خانگی کاربر روت
    script_path = "/usr/bin/restart_tor.sh"
    
    # ایجاد فایل شل برای اجرای دستورات
    with open(script_path, 'w') as script_file:
        script_file.write("#!/bin/bash\n")
        for command in commands:
            script_file.write(f"{command}\n")
    
    # قابل اجرا کردن فایل شل
    subprocess.run(["chmod", "+x", script_path])

    # زمان‌بندی cron job
    cron_time = f"*/{delay_minutes} * * * *"
    cron_job = f"{cron_time} {script_path}\n"

    # دریافت crontab فعلی و حذف خطوط مربوط به اسکریپت قبلی
    result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
    current_crontab = result.stdout
    new_crontab = []
    for line in current_crontab.splitlines():
        if script_path not in line:
            new_crontab.append(line)

    # اضافه کردن cron job جدید
    new_crontab.append(cron_job)
    with open("temp_cron", "w") as temp_cron_file:
        temp_cron_file.write("\n".join(new_crontab) + "\n")

    subprocess.run(['crontab', 'temp_cron'])
    subprocess.run(['rm', 'temp_cron'])


def get_tor_ip(port=None):
    try:
        if(check_tor()):
            if(port == None):
                socks_port, countries = read_torrc(torrc_path)
                if(socks_port == None):
                    port = 9050
                else:
                    port = socks_port

            import requests
            url = 'http://checkip.amazonaws.com'
            get_ip = requests.get(url, proxies={
                'http': f'socks5://127.0.0.1:{port}',
                'https': f'socks5://127.0.0.1:{port}'
            })
            node_ip = get_ip.text.strip()

            return node_ip
        else:
            print("\033[31mTor is not installed.\033[0m\nPlease install it first.")
    except requests.RequestException as e:
        print(f"An error occurred while trying to get the IP: {e}")
        return None


def check_portNumber(port):
    port = int(port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex(('127.0.0.1', port))
        return result != 0

def update_tor_country():
    input_codes = input("Enter country codes (e.g., tr, de) separated by commas or spaces: ")
    items = input_codes.split(',')
    output_string = ''.join(f"{{{item.strip()}}}" for item in items)

    codes = [code.strip() for code in input_codes.replace(',', ' ').split()]
    invalid_codes = [code for code in codes if code not in valid_country_codes]

    if invalid_codes:
        print(f"Invalid country codes: \033[0;31m{', '.join(invalid_codes)}\033[0m")
        return False
    else:
        #return output_string
        modify_torrc(torrc_path,new_exit_nodes=output_string)
        print(f"ExitNodes has been updated successfully with {output_string}")


def get_server_location():
    try:
        import requests
        response = requests.get('https://ipinfo.io')
        response.raise_for_status()
        data = response.json()
        country = data.get('country', 'Country not found')
        ip = data.get('ip', 'ip not found')
        return country, ip
        
    except requests.exceptions.RequestException as e:
        return None














def main():
    while True:
        clear_screen()
        sinasims()
        show_numbers()
        
        # Get Input Number
        choice = input("Enter Your Choice [1-13]:")
        
        # Check input number
        if choice == "0":
            clear_screen()
            break
        elif choice == "1":
            install_tor()
        elif choice == "2":
            update_tor()
        elif choice == "3":
            uninstall_tor()
        elif choice == "4":
            node_ip = get_tor_ip()
            print(f"Tor Server IP: {node_ip}")
            input("press Enter to continue")
        elif choice == "5":
            create_cron_job()
        elif choice == "6":
            reload_tor()
            restart_tor()
            print("Your Tor ip has been changed.")
            input("Press Enter to continue...")
        elif choice == "7":
            port = input("Enter Your Tor Port: ")
            check = False
            while True:
                if not port.isdigit():
                    print("Your input is \033[1;31mnot valid\033[0m...")
                elif check_portNumber(port) == False:
                    print(f"Port {port} is \033[1;31mBusy033[0m...")
                else:
                    break  
                port = input("Enter Your Tor Port: ")

            modify_torrc(torrc_path, new_socks_port=str(port))
            reload_tor()
            restart_tor()
            input("Your port has been change\nPress Enter to continue....")
        elif choice == "8":
            print("You can use these Countries:")
            for code, country in valid_country_codes.items():
                print(f"{country} -> \033[0;32m{code}\033[0m")
            country_data = update_tor_country()
            while country_data == False:
                country_data = update_tor_country()
            reload_tor()
            restart_tor()
            input(f"Countries of tor has been updated with: {country_data}\nPress Enter to continue....")
        elif choice == "9":
            start_tor()
            input("Tor has been started\nPress Enter to continue...")
        elif choice == "10":
            stop_tor()
            input("Tor has been stoped\nPress Enter to continue...")
        elif choice == "11":
            restart_tor()
            input("Tor has been restarted\nPress Enter to continue...")
        elif choice == "12":
            reload_tor()
            input("Tor has been reloaded\nPress Enter to continue...")
        elif choice == "13":
            status_tor()
            input("\nPress Enter to continue...")
        else:
            print("Your input is invalid...")
            input("Press Enter to continue...")



    
if __name__ == "__main__":
    main()
