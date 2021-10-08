#!/bin/bash

# Session Name
session="Tester"
window="MAIN"

# Start new Session with our name
tmux new-session -d -s $session

# Name first Window and start htop
tmux rename-window -t 0 $window
tmux send-keys -t $window 'htop' C-m
