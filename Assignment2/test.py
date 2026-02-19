def get_linux_cpu_info():
    keys_to_find = ['vendor_id', 'model', 'model name', 'cache size']
    cpu_details = {}
    
    with open('/proc/cpuinfo', 'r') as f:
        for line in f:
            for key in keys_to_find:
                if line.strip().startswith(key):
                    # Split by colon and take the value
                    value = line.split(':')[1].strip()
                    cpu_details[key] = value
            # Only need to read the first processor entry
            if 'cache size' in cpu_details and len(cpu_details) >= 4:
                break
    return cpu_details

print(get_linux_cpu_info())