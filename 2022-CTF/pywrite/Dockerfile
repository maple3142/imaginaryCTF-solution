FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install python3 python3-pip gdb -y
RUN pip install pwntools

CMD [ "/usr/bin/id" ]
# docker build . -t pywrite-exp
# docker run -v $PWD:/wd -it --rm pywrite-exp bash
