# Katie Grinnan's Octopus
# Team: Katie, Ryan, Cameron, Josh, Sri 

## Setting up I2C config

Copy `config.txt` file into the `/boot/` dir as root.

## Setting script to run on reboot

Run `crontab -e` and add the line:

    @reboot bash /home/pi/octopusbus-launcher.sh

## Connecting to running script via tmux

The launcher script runs the python process in a new tmux session
named "octopusbus". To connect to that session, run:

    tmux attach -t octopusbus

You can kill the tmux session with the shortcut 'C-b x', where
C is the Control key. You can scroll in the tmux window using 'C-b
[', then 'C-c' to stop scrolling.

To kill the python process, run:

    pkill -f '^python.*octopusbus.py'

Logs are created in the `logs` dir in the same directory as the
launcher script. To tail the latest logfile, run:

    tail -f /home/pi/logs/octopusbus-latest.txt
