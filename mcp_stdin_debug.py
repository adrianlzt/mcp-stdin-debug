#!/usr/bin/env python
import subprocess
import sys
import threading

LOG_FILE = "mcp_session.log"


def log_write(log_f, prefix, data):
    log_f.write(f"{prefix}: {data}")
    log_f.flush()


def read_from_stdin(proc_stdin, log_f):
    try:
        while True:
            user_input = sys.stdin.readline()
            if not user_input:
                break
            proc_stdin.write(user_input.encode())
            proc_stdin.flush()
            log_write(log_f, "STDIN", user_input)
    except Exception as e:
        pass


def read_from_proc(proc_stdout, log_f):
    try:
        while True:
            server_response = proc_stdout.readline()
            if not server_response:
                break
            decoded = server_response.decode()
            sys.stdout.write(decoded)
            sys.stdout.flush()
            log_write(log_f, "STDOUT", decoded)
    except Exception as e:
        pass


def main():
    if len(sys.argv) < 2:
        print("Usage: mcp-stdin-debug <command to run>", file=sys.stderr)
        sys.exit(1)
    command = sys.argv[1:]
    with open(LOG_FILE, "a") as log_f:
        proc = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
        )
        t_stdin = threading.Thread(
            target=read_from_stdin, args=(proc.stdin, log_f), daemon=True
        )
        t_stdout = threading.Thread(
            target=read_from_proc, args=(proc.stdout, log_f), daemon=True
        )
        t_stdin.start()
        t_stdout.start()
        t_stdin.join()
        proc.stdin.close()
        t_stdout.join()
        proc.wait()


if __name__ == "__main__":
    main()
