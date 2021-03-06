import subprocess


def execute_command(command):
    """
    Execute command and return a tuple with the return code, the stdout and the stderr
    """

    stdout = ""
    return_code = 0
    stderr = ""
    try:
        stdout  = subprocess.check_output(command.split()).decode()
    except subprocess.CalledProcessError as e:
        return_code = e.returncode
        stderr = e.output.decode()
    return return_code, stdout, stderr

def execute_command_2(command):
    """
    Execute command and return a tuple with the return code, the stdout and the stderr
    """

    p = subprocess.Popen(command.strip(),
                         stdout= subprocess.PIPE,
                         stderr= subprocess.PIPE)

    out, err = p.communicate()
    stdout = out.decode('utf-8')
    stderr = err.decode('utf-8')
    return_code = p.returncode
    return return_code, stdout, stderr


if __name__ == '__main__':
    c, o, e = execute_command("ls -lrt")
    print("Return code:", c, "Stdout:", o, "Stderr:", e)
    print()
    c, o, e = execute_command("cat sdfdkjfkddf")
    print("Return code:", c, "Stdout:", o, "Stderr:", e)
    print()

    c, o, e = execute_command("ls -lrt")
    print("Return code:", c, "Stdout:", o, "Stderr:", e)
    print()
    c, o, e = execute_command("cat sdfdkjfkddf")
    print("Return code:", c, "Stdout:", o, "Stderr:", e)
