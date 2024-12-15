from __future__ import annotations

import re
import subprocess
from pathlib import Path


def uncommitted_changes():
    result = subprocess.run(['git', 'diff-index', '--quiet', 'HEAD', '--'], capture_output=True)
    present = result.returncode != 0
    if present:
        print("There are uncommitted changes. Please commit or stash them before running this script.")
        print("")
        subprocess.run(['git', 'diff-index', 'HEAD', '--'])
    return present


def write_build_meta():
    content = f"""__version__ = "{Pyproject().version}"
git_hash_short = "{subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode().strip()}"
git_hash = "{subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()}"
"""
    sep = '=' * 80
    print(sep + ' writing src/wwwpy/_build_meta.py, content: ')
    print(content)
    print(sep)
    Path('src/wwwpy/_build_meta.py').write_text(content)


class Pyproject:
    def __init__(self, content: str | None = None):
        if content is None:
            pyp_toml = Path(__file__).parent / 'pyproject.toml'
            content = pyp_toml.read_text()
        self.content = content

    @property
    def version(self) -> str:
        lines = self.content.splitlines()
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith('version ='):
                match = re.match(r'version\s*=\s*"(.*?)"', stripped_line)
                if match:
                    return match.group(1)
        return ''

    def version_inc_minor(self):
        lines = self.content.splitlines(keepends=True)
        for i, line in enumerate(lines):
            stripped_line = line.strip()
            if stripped_line.startswith('version ='):
                match = re.match(r'version\s*=\s*"(.*?)"', stripped_line)
                if match:
                    version = match.group(1)
                    version_parts = version.split('.')
                    if version_parts[-1].isdigit():
                        version_parts[-1] = str(int(version_parts[-1]) + 1)
                        new_version = '.'.join(version_parts)
                        lines[i] = f'version = "{new_version}"\n'
                        self.content = ''.join(lines)
                        break
                    else:
                        print('Error: Last part of the version is not a digit.')
                else:
                    print('Error: Could not parse the version string.')
                    break
        else:
            print('Error: Version line not found.')


def update_minor_version(filename: str | Path | None = None) -> str | None:
    if filename is None:
        filename = 'pyproject.toml'
    with open(filename, 'r') as f:
        pyproject_content = f.read()

    pyproject = Pyproject(pyproject_content)
    old_version = pyproject.version
    pyproject.version_inc_minor()
    new_version = pyproject.version

    if old_version != new_version:
        with open(filename, 'w') as f:
            f.write(pyproject.content)
        return f'Updated version to {new_version}'
    else:
        return 'Version was not updated'


if __name__ == '__main__':
    write_build_meta()
