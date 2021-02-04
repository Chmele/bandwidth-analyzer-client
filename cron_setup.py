from crontab import CronTab
cron = CronTab(user='root')
job = cron.new(command='python3 /home/su/bandwidth-analyzer-client/client.py')
job.minute.every(1)
cron.write()