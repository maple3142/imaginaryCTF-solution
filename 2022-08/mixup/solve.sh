# https://stackoverflow.com/a/63840546
cat flag.txt | LC_ALL=C sed 's/[\x80-\xff]//g'
