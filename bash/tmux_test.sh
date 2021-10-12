#!/bin/bash

# Script vars
SESSION_NAME="TEST"
WINDOW_1_NAME="test_bash"
WINDOW_1_COMMAND="ls"
WINDOW_2_NAME="HTOP"
WINDOW_2_COMMAND="htop"

SESSION_EXISTS=$(tmux list-sessions | grep $SESSION_NAME)

if [ "$SESSION_EXISTS" = "" ]
then
    # Start new Session with our name
    tmux new-session -d -s $SESSION_NAME

    # Name first Window and start run command
    tmux rename-window -t 0 $WINDOW_1_NAME
    tmux send-keys -t $WINDOW_1_NAME $WINDOW_1_COMMAND C-m

    # Create second window and run htop command
    tmux new-window -t $session_name:1 -n $WINDOW_2_NAME
    tmux send-keys -t $WINDOW_2_NAME $WINDOW_2_COMMAND C-m
fi
