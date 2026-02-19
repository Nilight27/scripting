
import json
import pwd
import grp
import socket  
import os
import subprocess

def MName():
    try:
        return socket.gethostname()
    except Exception:
        print(f'error getting computer name')
    
#function to get user and group
def UserGroup():
    UserAndGroup = {}
    group = []

    for user_entry in pwd.getpwall():
        username = user_entry.pw_name
        # Get primary group name
        primary_gid = user_entry.pw_gid
        primary_group_name = grp.getgrgid(primary_gid).gr_name

        try:
            # os.getgrouplist returns a list of GIDs
            gids = os.getgrouplist(username, primary_gid)
            for gid in gids:
                try:
                    group.append(grp.getgrgid(gid).gr_name)
                except KeyError:
                    # Fallback to GID if group name not found
                    group.append(str(gid))
            
            UserAndGroup[username] = sorted(group)
            
        except (KeyError, PermissionError):
            # Handle cases where a user might not be found or permissions are an issue
            UserAndGroup[username] = [primary_group_name + " (and potentially other unlisted groups due to permission issues)"]

    return UserAndGroup


def Cpu():
    keys_to_find = ['vendor_id', 'model', 'model name', 'cache size']
    cpu_details = {}
    try:
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                for key in keys_to_find:
                    if line.strip().startswith(key):
                        value = line.split(':')[1].strip()
                        cpu_details[key] = value
                #reading the first processor entry
                if 'cache size' in cpu_details and len(cpu_details) >= 4:
                    break
        return cpu_details
    except FileNotFoundError as x:
        print(f'Cant get file: {x}')





def Services():
    try:

        services = []
        #commands for services
        com = ['systemctl', 'list-units', '--type=service', '--state=running']

        run = subprocess.run(com, capture_output=True, text=True, check=True)

        lines = run.stdout.strip().split('\n')

        if len(lines) > 3:
            for line in lines[1:-3]:
                parts = line.strip().split(maxsplit=4)
                if len(parts) >= 4:
                    services.append({'name': parts[0], 'status': parts[3], 'description': parts[4] if len(parts) > 4 else ''})

        return services

    except FileNotFoundError:
        print(f'couldnt get services')
        return []
    


def main():
    data = {
        'computer_name': MName(),
        'users_and_groups': UserGroup(),
        'cpu_info': Cpu(),
        'services': Services()
    }
    try:
        with open('Project_2.json', 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f'Error writing to file: {e}')




if __name__ == "__main__":
    main()

    




