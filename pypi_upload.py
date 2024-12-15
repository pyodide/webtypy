import glob
import os
import subprocess
import sys

from pypi_helper import uncommitted_changes


def main():
    if uncommitted_changes():
        return
    # Load environment variables from .env
    with open('.env') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

    # Remove all files in dist/
    dist_files = glob.glob('dist/*')
    for file in dist_files:
        os.remove(file)

    # Build the package
    try:
        subprocess.run([sys.executable, '-m', 'build'], check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)

    # Upload the package to PyPI
    dist_files = glob.glob('dist/*')
    if dist_files:
        subprocess.run([sys.executable, '-m', 'twine', 'upload'] + dist_files, check=True)
        subprocess.run(['git', 'push'])
    else:
        print("No files found in dist/ to upload.")


if __name__ == '__main__':
    main()
