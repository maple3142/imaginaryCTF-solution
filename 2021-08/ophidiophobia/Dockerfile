FROM python

COPY / /srv
RUN mkdir -p /srv/app/run
COPY ./ophidiophobia.py /srv/app/run
COPY ./libc.so.6 /srv/app/libc.so.6
COPY ./flag.txt /srv/app/flag.txt
RUN chmod 755 /srv/app/run /srv/app/libc.so.6
RUN chmod 744 /srv/app/flag.txt

ENV JAIL_TIME 60
ENV JAIL_CONNS_PER_IP 1
ENV JAIL_MEM 20M

ENTRYPOINT [ "python", "/srv/app/run/ophidiophobia.py" ]
