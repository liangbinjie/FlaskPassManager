import os
import subprocess


def shutdown():
    output = 'netstat -ano | findstr :8080'
    port = subprocess.check_output(output, shell=True)
    pid = port.decode('utf-8').split()[-1]
    print(pid)
    kill = f'taskkill /PID {pid} /F'
    os.system(kill)
    print("Server shutdown...")

shutdown()