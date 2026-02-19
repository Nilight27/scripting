import json

def load():
    try:
        with open('Project_2.json', 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print('File not found: Project_2.json') 
        return None
    

def PrintCompName(name):
        print(f'Computer Name: {name}')

    
def PrintUsersAndGroups(users_and_groups):
        for user, groups in users_and_groups.items():
            print(f'  {user}:')
            for group in groups:
                print(f'      - Group: {group}')

def PrintCpuInfo(cpu_info):
        for key, value in cpu_info.items():
            print(f'  {key}: {value}')

def PrintServices(services):
        for service in services:
            print(f" \n - Name: {service['name']}, Status: {service['status']}, Description: {service['description']}")

def header(title):
        print('\n' + '=' * 30)
        print(f'  {title}')
        print('=' * 30)
            
def main():
    data = load()
    if data is None:
        print("Failed to load data.")
        return
    
    header('Machine Name')
    PrintCompName(data.get('computer_name', 'N/A'))
    header('Users and Groups')
    PrintUsersAndGroups(data.get('users_and_groups', []))
    header('CPU Information')
    PrintCpuInfo(data.get('cpu_info', {}))
    header('Running Services')
    PrintServices(data.get('services', []))
    header('End of Report')


if __name__ == "__main__":
    main()