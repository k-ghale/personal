#!/usr/bin/env bash

selected=$(printf "javascript\npython\njava\nnodejs\nsed\nmove" | fzf)
read -p "query: " query

if [[ "$selected" =~ ^(javascript|python|java|nodejs)$ ]]; then
	  url="cht.sh/$selected/$(echo "$query" | tr ' ' '+')"
  else
	    url="cht.sh/$selected~$query"
fi

tmux neww bash -c "curl $url; while true; do sleep 1; done"
