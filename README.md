# Toni's Statusbar

## This is how it looks:

BBC6: The Who - I'm Free | 🔊16% | 🔆18% | 93.8% 🐏1.83G 💾54G | myssid 75% | Morgen ☁️☁️❄️ 0 / 0 °C | 🔌 100% ❔99% | 02.01.2021 🌍 14:15:40

## How to set it up
* I assume that i3blocks is installed and running
    * you can always output i3blocks to the terminal using the `i3blocks` command
* clone repository and enter it
``` bash
git clone https://github.com/gh-toni/i3blocks-config.git
cd i3blocks-config
```
* copy the files to where they will be read
``` bash
mkdir -p ~/.config/i3blocks
cp i3blocks ~/.config/i3blocks/config
mkdir -p ~/.local/bin
cp -r statusbar ~/.local/bin/
```
* now you might have the problem that some **blocks don't get updated**
    * for example when increasing the volume, the volume value won't change
    * some blocks don't update periodically but listen for a certain signal
    * the number of the signal is defined in [i3blocks](i3blocks)
    * e.g. in the `[volume]` block there is the line `signal=1`, hence you can execute the command `pkill -SIGRTMIN+1 i3blocks` to trigger the status bar to update the volume block
    * So in your i3config (or wherever you define your shortcuts) you can add the following line to increase the volume when pressing the volume up key (it will then immediately update the value in the statusbar):
```
bindsym XF86AudioRaiseVolume exec amixer -q sset 'Master' 1%+ && pkill -SIGRTMIN+1 i3blocks
```

## Music metadata
Some internet radio stations don't provide the metadata.
So I've written a little python script to fetch artist and title from several radio stations by reading their web resources.
To listen to those stations, I use the playlist `radio.m3u` with clementine or mpv so I can change the stations with previous/next buttons.

## Weather
* shows weather with emojis and min/max temperature in °C
* shows current day from 00:00 to 14:00, and next day afterwards
* currently it's optimized for Zurich, but you can replace the URL in the script by opening it in a browser and searching for a city of you choice and pasting the new URL in the script.
* it's updated periodically according to [i3blocks](i3blocks) and when you click on it.
* on click it also opens the web page where the info came from in brave (TODO: change this in [weather](statusbar/weather) to your favorite browser)
