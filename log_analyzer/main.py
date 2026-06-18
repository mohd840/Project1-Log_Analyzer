failed_ips = {}
Failed_logs = 0
THRESHOLD = 3
with open("logs/sample.log") as file:
    for line in file:
        print(line.strip())

        part = line.split()
        event = part[0]
        user = part[1].split("=")[1]
        ip = part[2].split("=")[1]

        log_data = {
            "event": event,
            "user": user,
            "ip": ip
        }

        # ONLY handle failed logs
        if event == "LOGIN_FAILED":
            Failed_logs += 1

            if ip in failed_ips:
                failed_ips[ip] += 1
            else:
                failed_ips[ip] = 1

print(f"Failed logs = {Failed_logs}")
print(failed_ips)

top_ip = ""
max_failures = 0

for ip in failed_ips:
    if failed_ips[ip] > max_failures:
        max_failures = failed_ips[ip]
        top_ip = ip

print(f"Top attacker: {top_ip}")
print(f"Failed attempts: {max_failures}")

for ip in failed_ips:
   if failed_ips[ip]>=THRESHOLD:
      print("ALERT")
      print(f"{ip} has {failed_ips[ip]} attempts")
   else:
      print(f"{ip} has {failed_ips[ip]} attepmts")

# Creating Report
with open("report.txt", "w") as report:
    report.write("Security Analysis Report\n")
    report.write("========================\n\n")

    report.write(f"Total Failed Logins: {Failed_logs}\n\n")

    report.write("Failed Logins By IP:\n")

    for ip in failed_ips:
        report.write(f"{ip} -> {failed_ips[ip]}\n")

    report.write("\n")

    report.write(f"Top Attacker: {top_ip}\n")
    report.write(f"Failed Attempts: {max_failures}\n")
