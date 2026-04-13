from utils.ping import ping

def check_tunnel(target_ip):
    return ping(target_ip)