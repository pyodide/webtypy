from pathlib import Path

from js_pyi.main_produce import generate_python


def main():
    code = generate_python()
    path = (Path(__file__).parent / 'src/js-stubs/__init__.pyi')
    path.write_text(code)
    print(f'{len(code.splitlines())} lines written in {path}')


if __name__ == '__main__':
    main()
