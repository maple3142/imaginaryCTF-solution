openssl rsautl -decrypt -in enc.txt -inkey private.pem -out flag.txt && cat flag.txt
