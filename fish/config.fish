
# >>> mamba initialize >>>
# !! Contents within this block are managed by 'mamba init' !!
set -gx MAMBA_EXE "/home/admin/.micromamba/bin/micromamba"
set -gx MAMBA_ROOT_PREFIX "/home/admin/micromamba"
$MAMBA_EXE shell hook --shell fish --prefix $MAMBA_ROOT_PREFIX | source
# <<< mamba initialize <<<

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/admin/micromamba/bin/conda
    eval /home/admin/micromamba/bin/conda "shell.fish" "hook" $argv | source
end
# <<< conda initialize <<<

