import time
import yaml

from vpn.vpn_check import check_tunnel
from vpn.vpn_restart import restart_vpn
from utils.logger import log
from utils.alert import alert


def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)


def run():
    config = load_config()

    targets = config["check_targets"]
    devices = config["vpn_devices"]
    interval = config["interval"]

    while True:
        for t in targets:
            name = t["name"]
            ip = t["ip"]

            if check_tunnel(ip):
                log(f"[OK] VPN tunnel to {name} is UP")
            else:
                log(f"[FAIL] VPN tunnel to {name} is DOWN")
                alert(f"{name} unreachable - restarting VPN")

                for d in devices:
                    success, msg = restart_vpn(d)
                    log(f"Restart VPN on {d['name']}: {msg}")

        time.sleep(interval)


if __name__ == "__main__":
    run()