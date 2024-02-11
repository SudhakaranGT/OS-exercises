import os
import time

def child_process():
    print("Child Process - PID:", os.getpid())
    print("Child Process - Parent PID:", os.getppid())
    time.sleep(2)
    print("Child Process - Exiting")
    os._exit(0)

def main():
    print("Parent Process - PID:", os.getpid())
    print("Parent Process - Forking a Child Process...")

    child_pid = os.fork()

    if child_pid == 0:
        child_process()
    else:
        print("Parent Process - Waiting for the child process to complete...")
        _, status = os.wait()
        print("Parent Process - Child Process has exited with status", status)

if __name__ == "__main__":
    main()
