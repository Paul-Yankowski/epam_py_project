import datetime

class Logger:
    def __init__(self,site):
        self.site=site

    def log_site(self):
        n=datetime.datetime.now()
        log_str=str(datetime.date.today())+' | '+str(n.hour)+':'+str(n.minute)+' | '+str(self.site)
        with open('log_file.txt','a') as f:
            f.write(log_str+'\n')