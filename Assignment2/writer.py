
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





def services():
    services = []




