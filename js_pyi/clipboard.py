import datetime
import platform


def clip_copy(data: str):
    system = platform.system()
    cmd = {"Linux": "xclip -sel c", "Darwin": "pbcopy"}.get(system, "")
    if cmd == "":
        raise Exception(f"System platform not supported {system}")
    _process(cmd, data)


def _process(cmd: str, data: str):
    import shlex

    args = shlex.split(cmd)
    from subprocess import Popen, PIPE, STDOUT

    p = Popen(args, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    p.stdin.write(data.encode())


if __name__ == "__main__":
    clip_copy(f"ciao {datetime.datetime.now()}")
