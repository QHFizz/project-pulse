# #!/usr/bin/env bash
# git log --oneline | wc -l > pulse.txt
# #curl -s "http://worldclockapi.com/api/json/utc/now" \ | sed -n 's/.*"currentDateTime":"\([^"]*\)".*/\1/p' >> pulse.txt

# curl -s "http://worldclockapi.com/api/json/utc/now" \ | sed -n 's/.*"currentDateTime":"\([^"]*\)".*/\1/p' >> pulse.txt

# git ls-files | wc -l >> pulse.txt
# cat pulse.txt 



#!/usr/bin/env bash

# Count commits
git log --oneline | wc -l > pulse.txt

# Get current UTC timestamp (ensure newline)
curl -s "http://worldclockapi.com/api/json/utc/now" | sed -n 's/.*"currentDateTime":"\([^"]*\)".*/\1/p' | awk '{print $1}' >> pulse.txt

# Count tracked files
git ls-files | wc -l >> pulse.txt

# Display the file
cat pulse.txt

