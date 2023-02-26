#!/bin/bash

cd ~/repos/project-placeholder;
git stash && git switch main && git fetch --all && git reset --hard origin/main;
source venv/bin/activate;
pip install -q -r requirements.txt;
systemctl daemon-reload;
systemctl restart project-placeholder.service;