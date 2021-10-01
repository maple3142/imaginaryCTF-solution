FROM redpwn/jail

COPY --from=ubuntu / /srv
COPY ./vuln /srv/app/run
COPY ./libc-2.31.so /srv/app/libc-2.31.so
COPY ./ld-2.31.so /srv/app/ld-2.31.so
COPY ./flag.txt /srv/app/flag.txt
RUN chmod 755 /srv/app/run /srv/app/libc-2.31.so /srv/app/ld-2.31.so
RUN chmod 744 /srv/app/flag.txt

ENV JAIL_TIME 60
ENV JAIL_CONNS_PER_IP 1
ENV JAIL_MEM 20M
ENV JAIL_PORT 11000
