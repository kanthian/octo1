# Katie Grinnan's Octopus
# Team: Katie, Ryan, Cameron, Josh, Sri, Hike, Bin

## Setting up Raspberry PI

### Install packages

    sudo apt install git tmux

### Clone repo

    git clone https://github.com/kanthian/octo1.git
    cd octo1

### Setup I2C

Copy `config.txt` file into the `/boot/` dir as root to configure I2C:

    sudo cp config.txt /boot/

### Run on boot

Set script to run on reboot using cron:

    crontab -e # pick an editor, or use EDITOR=... env var

    # add the following into the editor and save
    # you may need to change /home/pi/octo1 to whereever you cloned the repo
    @reboot bash /home/pi/octo1/octopusbus-launcher.sh

### Reboot safely

    sudo reboot

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

    tail -n+0 -f /home/pi/logs/octopusbus-latest.txt
