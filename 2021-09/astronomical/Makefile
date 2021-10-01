main : vuln.c
	gcc vuln.c -o vuln && \
	patchelf ./vuln --set-interpreter ./ld-2.31.so --replace-needed libc.so.6 ./libc-2.31.so vuln

clean : vuln
	rm -rf vuln
