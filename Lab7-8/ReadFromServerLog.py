import random
from collections import Counter
from datetime import datetime

# Function to generate a random log line
def generate_log_line():
    # Generate random IP address
    ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    
    # Simulate the current date and time
    date = datetime.now().strftime('%d/%b/%Y:%H:%M:%S +0000')
    
    # Simulate a random HTTP request
    request_method = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
    request_url = random.choice(['/home', '/about', '/contact', '/products'])
    request = f'"{request_method} {request_url} HTTP/1.1"'
    
    # Randomly choose a status code (200, 204, 500)
    status_code = random.choice([200, 204, 500])
    
    # Randomly simulate bytes (between 100 to 5000)
    bytes_sent = random.randint(100, 5000)
    
    # Return the formatted log line
    return f'{ip_address} - - [{date}] {request} {status_code} {bytes_sent}\n'

# Generate a server.log file with random log entries
log_file_name = 'server.log'

with open(log_file_name, 'w') as file:
    for _ in range(100):  # Generate 100 log lines
        file.write(generate_log_line())

# Read the content of the server.log file and process the data
with open(log_file_name, 'r') as file:
    log_lines = file.readlines()

# Initialize counters for status codes and IP addresses
status_codes = {200: 0, 204: 0, 500: 0}
ip_addresses = []

# Parse the log lines
for line in log_lines:
    # Extract the status code
    status_code = int(line.split()[8])
    
    # Increment the status code count if it matches 200, 204, or 500
    if status_code in status_codes:
        status_codes[status_code] += 1
    
    # Extract the IP address (the first part of the line)
    ip_address = line.split()[0]
    ip_addresses.append(ip_address)

# Count the 3 most common IP addresses
ip_counts = Counter(ip_addresses)
most_common_ips = ip_counts.most_common(3)

# Create a new file with the summary information
summary_file_name = 'summary_report.txt'

with open(summary_file_name, 'w') as file:
    # Write the count of specific status codes
    file.write(f"Requests with status code 200: {status_codes[200]}\n")
    file.write(f"Requests with status code 204: {status_codes[204]}\n")
    file.write(f"Requests with status code 500: {status_codes[500]}\n")
    
    # Write the 3 most common IP addresses
    file.write("\nTop 3 IP addresses:\n")
    for ip, count in most_common_ips:
        file.write(f"{ip}: {count} requests\n")
    
    # Write the total number of requests
    total_requests = len(log_lines)
    file.write(f"\nTotal requests: {total_requests}\n")

print(f"Summary report has been created in {summary_file_name}.")
