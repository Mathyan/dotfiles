# mathyan dotfiles

This repo holds my dotfiles

## Yay

**Important**: Execute the following commands as a regular user, NOT as root!

```bash
git clone https://aur.archlinux.org/yay-bin
cd yay-bin
makepkg -si
```

### Required Packages

``` bash
yay -S hyprland polkit-gnome ffmpeg neovim viewnior rofi      \
pavucontrol thunar starship wl-clipboard wf-recorder swaybg   \
grimblast-git ffmpegthumbnailer tumbler playerctl             \
noise-suppression-for-voice thunar-archive-plugin kitty       \
waybar-hyprland wlogout swaylock-effects sddm-git pamixer     \
nwg-look-bin nordic-theme papirus-icon-theme dunst otf-sora   \
ttf-nerd-fonts-symbols-common otf-firamono-nerd inter-font    \
ttf-fantasque-nerd noto-fonts noto-fonts-emoji ttf-comfortaa  \
ttf-jetbrains-mono-nerd ttf-icomoon-feather ttf-iosevka-nerd  \
adobe-source-code-pro-fonts brightnessctl hyprpicker-git
```

## References

- ChrisTitusTech GitHub: <https://github.com/ChrisTitusTech/hyprland-titus>
- Official Hyprland GitHub: <https://github.com/hyprwm/Hyprland>
- Linux Mobiles Hyprland Configuration Files: <https://github.com/linuxmobile/hyprland-dots>