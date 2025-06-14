#!/bin/bash
set -e
python3 webapp.py &
python3 -m bot
