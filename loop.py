from Selfcheck import check as sc
import json, datetime, os, logging, time
log = logging.getLogger("Macro")
log.setLevel(logging.INFO)

formatter = logging.Formatter("%(name)s@%(asctime)s [%(levelname)s] %(message)s")
streamhandler = logging.StreamHandler()
streamhandler.setFormatter(formatter)
log.addHandler(streamhandler)

filehandler = logging.FileHandler("macro.log")
filehandler.setFormatter(formatter)
log.addHandler(filehandler)

config = json.load(open('./config.json', 'r', encoding='utf-8'))

def getNextRun(current):
    date = current.date() + datetime.timedelta(1)
    return datetime.datetime.combine(date, datetime.time(config["time"]))

if datetime.datetime.now().hour < config["time"]:
    next = datetime.datetime.combine(datetime.date.today(), datetime.time(config["time"]))
else:
    next = getNextRun(datetime.datetime.now())
log.info("Next run on: " + str(next))

while(True):
    remain = (next - datetime.datetime.now()).total_seconds()
    if remain > 1.5:
        log.info("Long times left, sleeps for {} seconds.".format(int(remain)))
        time.sleep(int(remain))
        log.info("Done sleep, start check time")
        continue
    if remain <= 0:
        log.info("Running macro")
        data = sc.selfcheck(*list(config["auth"].values()))
        log.info("Last return data : " + data)
        next = getNextRun(datetime.datetime.now())
        log.info("Next run on: " + str(next))

