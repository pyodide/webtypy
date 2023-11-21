import os
import shutil
from pathlib import Path

self_folder = Path(__file__).parent
web_sys = self_folder / "web-sys"


def main():
    svn_websys_crate()
    copy_webidls()


def svn_websys_crate():
    print("running `svn export ...` this may take a while...")
    if web_sys.exists():
        shutil.rmtree(web_sys)
    trunk = "https://github.com/rustwasm/wasm-bindgen/trunk"
    os.system(f"svn export {trunk}/crates/web-sys")
    licenses = ["LICENSE-APACHE", "LICENSE-MIT"]
    for licence in licenses:
        os.system(
            f"svn export {trunk}/{licence} web-sys/webidls"
        )  # get licence from the repo root


def copy_webidls():
    src = web_sys / "webidls"
    dst = self_folder / "webidls"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


if __name__ == "__main__":
    main()
