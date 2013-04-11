ACHE_HOME:-"$HOME/.cache"}
if [ -d "$cachedir" ]; then
    cache=$cachedir/dmenu_run
else
    cache=$HOME/.dmenu_cache # if no xdg dir, fall back to dotfile in ~
fi
APP=$(
    IFS=:
    if stest -dqr -n "$cache" $PATH; then
        stest -flx $PATH | sort -u | tee "$cache" | dmenu "$@"
    else
        dmenu "$@" < "$cache"
    fi
)

grep -q -w "$APP" ~/.dmenu_term && urxvtc -e $APP || echo $APP | ${SHELL:-"/bin/sh"} &