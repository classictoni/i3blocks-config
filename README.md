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
cp statusbar ~/.local/bin/
```

## Music metadata
Some internet radio stations don't provide the metadata.
So I've written a little python script to fetch artist and title from several radio stations by reading their web resources.
To listen to those stations, I use the playlist `radio.m3u` with clementine or mpv so I can change the stations with previous/next buttons.
