from datetime import datetime as dt
from sys import argv as argv


# write to log_file.log
def write_to_log(details, level="INFO"):
    log = open("log_file.log", "w", encoding="utf_8")
    log.write(str(dt.now()) + f" {level} {details}\n")
    log.close()


def append_to_log(details, level="INFO"):
    log = open("log_file.log", "a")
    log.write(str(dt.now()) + f" {level} {details}\n")
    log.close()


def read_log():
    log = open("log_file.log", "r")
    lines = log.readlines()
    log.close()

    for line in lines:
        line_content = line.rstrip()
        print(line_content)


def read_line(line):
    with open("log_file.log", "r") as log:
        lines = log.readlines()
        if line in ["end", "last"]:
            line = -1
        elif line in ["start", "first"]:
            line = 1
        else:
            line = int(line)
        if 0 < line <= len(lines):
            line_content = lines[line - 1].rstrip()
            print(line_content)
        elif line == -1 and lines:
            last_line = lines[-1].rstrip()
            print(last_line)
        else:
            print("Line number out of range.")


def script(mode, *args):
    if mode == "w":
        write_to_log(*args)
    if mode == "a":
        append_to_log(*args)
    if mode == "r":
        read_log()
    if mode == "l":
        read_line(*args)


if __name__ == "__main__":
    num_args = len(argv)
    if num_args >= 2:
        script(argv[1], *argv[2:num_args])
    else:
        print("Invalid number of arguments.")
