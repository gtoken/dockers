FROM ubuntu:14.04
MAINTAINER Khang Nguyen "khang@gtoken.com"
ENV REFRESHED_AT 2015-04-11

RUN apt-get update
RUN apt-get install -y emacs

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get install -y postgresql-client-9.3 postgresql-contrib-9.3

# Security issues, might not be a good idea for production
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf
RUN sed -i 's/peer/trust/g' /etc/postgresql/9.3/main/pg_hba.conf
RUN sed -i 's/\/var\/lib\/postgresql\/9.3\/main/\/srv\/data/g' /etc/postgresql/9.3/main/postgresql.conf
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf

# So why the fuck I need to put the command in the a script
# and call it from ENTRYPOINT command, I still haven't know
ADD start.sh .
RUN chmod 775 start.sh
ENTRYPOINT ["/start.sh"]

EXPOSE 5432
CMD []