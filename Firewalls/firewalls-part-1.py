import random

# generates a random ip address
def generate_random_ip():
    return f"192.168.1.{random.randint(0,20)}"

# takes the random ip address and compares it to the set of rules
def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

def main():
    # dictionary with key-value pairs
    firewall_rules = {
        "192.168.1.1":"block",
        "192.168.1.4":"block",
        "192.168.1.9":"block",
        "192.168.1.13":"block",
        "192.168.1.16":"block",
        "192.168.1.19":"block",
    }

    # simulate random traffic
    for _ in range(12):
        ip_address = generate_random_ip()         
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)     # a unique identifier
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")


# execute main function
if __name__ == '__main__':
    main()