import subprocess

def ping(ip):
    result = subprocess.run(
        ["ping", "-n", "1", ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.returncode == 0