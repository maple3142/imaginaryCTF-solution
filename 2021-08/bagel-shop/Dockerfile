FROM redpwn/jail

COPY --from=ubuntu / /srv
COPY ./vuln /srv/app/run
COPY ./libc-2.27.so /srv/app/libc-2.27.so
COPY ./ld-2.27.so /srv/app/ld-2.27.so
COPY ./flag.txt /srv/app/flag.txt
COPY ./max49.txt /srv/app/max49.txt
RUN chmod 755 /srv/app/run /srv/app/libc-2.27.so /srv/app/ld-2.27.so
RUN chmod 744 /srv/app/flag.txt /srv/app/max49.txt

ENV JAIL_TIME 60
ENV JAIL_CONNS_PER_IP 1
ENV JAIL_MEM 20M
