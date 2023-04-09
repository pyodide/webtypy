#!/bin/bash

export $(cat .env | xargs)
rm dist/*
python -m build && python -m twine upload dist/*