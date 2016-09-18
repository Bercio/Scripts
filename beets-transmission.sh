#!/usr/bin/env sh
DIR="/data/Crane/$TR_TORRENT_NAME"


if find "$DIR" -name "*.flac" -or -name "*.mp3" -or -name "*.ogg" -or -name "*.eac" -or -name "*.aac"
then
	gnome-terminal -x beet import "$DIR"
fi
