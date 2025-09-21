def read_log(file_name):
    with open(file_name, "r") as log_file:
        for line in log_file:
            yield line


def check_errors(logs):
    errs = []
    for num, line in enumerate(logs):
        if "ERROR" in line or "WARNING" in line:
            errs.append((line, num))
    return errs


res = check_errors(read_log("server.txt"))
for i in res:
    print(i)
