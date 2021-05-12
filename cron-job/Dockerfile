FROM python:3.6
RUN apt-get update && apt-get -y install cron vim
WORKDIR /cron-job
COPY . /cron-job
RUN pip install --no-cache-dir -r requirements.txt
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

# run crond as main process of container
CMD ["cron", "-f"]


