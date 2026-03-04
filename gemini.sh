#!/usr/bin/env bash

selected=$(printf "general\nbash\npython\njavascript\nrust\nexplain-code\noptimize" | fzf)

[[ -z "$selected" ]] && exit 0

read -p "ask gemini ($selected): " query

if [[ "$selected" == "general" ]]; then
  full_prompt="$query"
elif [[ "$selected" == "explain-code" ]]; then
  full_prompt="Explain this code in detail: $query"
elif [[ "$selected" == "optimize" ]]; then
  full_prompt="How can I make this code faster/cleaner? $query"
else
  full_prompt="In the context of $selected, how do I $query? Provide clear code examples."
fi

tmux neww bash -c "
  echo '--- Gemini is thinking... ---';
  GOOGLE_API_KEY="your api key"
  response=\$(curl -s \"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=\$GOOGLE_API_KEY\" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d \"\$(jq -n --arg msg '$full_prompt' '{contents: [{parts: [{text: \$msg}]}]}')\");

  # Check if we got a valid response or an error
  echo \"\$response\" | jq -e '.candidates[0]' > /dev/null
  if [ \$? -eq 0 ]; then
      echo \"\$response\" | jq -r '.candidates[0].content.parts[0].text' | glow -s dark -
  else
      echo 'ERROR FROM API:'
      echo \"\$response\" | jq -r '.error.message // \"Unknown error\"'
  fi

  echo -e '\n\033[1;32m--- Press q to close this window ---\033[0m';
  while read -n 1 char; do [[ \$char == 'q' ]] && break; done
"
