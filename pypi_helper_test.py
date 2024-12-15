from __future__ import annotations

import subprocess
from pathlib import Path

from pypi_helper import Pyproject
from pypi_helper import update_minor_version

pyproject_content = '''
[project]
name = "wwwpy"
version = "0.1.38"
'''


def test_Pyproject_properties():
    target = Pyproject(pyproject_content)

    assert target.version == '0.1.38'
    assert target.content == pyproject_content


def test_Pyproject_version_inc_minor():
    target = Pyproject(pyproject_content)
    target.version_inc_minor()

    assert target.version == '0.1.39'
    assert target.content == pyproject_content.replace('0.1.38', '0.1.39')


def test_Pyproject_without_args__should_load_pyproject_toml(tmp_path):
    target = Pyproject()
    assert target.version
    assert target.content


def test_update_minor_version(tmp_path):
    file = tmp_path / "pyproject.toml"
    file.write_text(pyproject_content)

    result = update_minor_version(file)
    assert result == 'Updated version to 0.1.39'
    updated_content = file.read_text()
    assert 'version = "0.1.39"' in updated_content

def test_do_not_add_cr(tmp_path):
    file = tmp_path / "pyproject.toml"
    file.write_text('[project]\nversion = "0.1.38"\n#comment')

    update_minor_version(file)

    assert file.read_text() == '[project]\nversion = "0.1.39"\n#comment'
