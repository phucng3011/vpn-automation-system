import paramiko

def restart_vpn(device):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=device["host"],
            username=device["username"],
            password=device["password"],
            timeout=5
        )

        stdin, stdout, stderr = ssh.exec_command("restart vpn")

        output = stdout.read().decode()
        ssh.close()

        return True, output

    except Exception as e:
        return False, str(e)