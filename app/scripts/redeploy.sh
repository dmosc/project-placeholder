#!/bin/bash

# Reset environment and update project.
tmux kill-server;
cd "~/repos/project-placeholder";
git stash && git switch main && git fetch --all && git reset --hard origin/main;

# Boot process.
tmux new-session -d -s process "cd ~/repos/project-placeholder && source venv/bin/activate && pip install -q -r requirements.txt && flask run --host=0.0.0.0";
