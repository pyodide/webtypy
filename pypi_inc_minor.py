from __future__ import annotations

import subprocess

from pypi_helper import uncommitted_changes, update_minor_version, write_build_meta


def main():
    if uncommitted_changes():
        return

    msg = update_minor_version()
    if msg:
        print('=== committing changes')
        write_build_meta()
        subprocess.run(['git', 'commit', '-am', msg])


if __name__ == '__main__':
    main()
