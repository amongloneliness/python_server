#!/bin/bash/
pyinstaller --onefile main.py
mv dist/main dist/server
mv dist/server .
