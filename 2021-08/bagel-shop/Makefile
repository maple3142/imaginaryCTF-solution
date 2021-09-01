vuln : vuln.c
	gcc -o vuln vuln.c && \
	patchelf --set-interpreter ./ld-2.27.so --replace-needed libc.so.6 ./libc-2.27.so ./vuln
