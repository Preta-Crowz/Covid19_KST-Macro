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

config = json.load(open('./config.json', 'r'))

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
        res = os.system("python macro.py")
        if res == 0:
            log.info("Done work")
        elif res == 2:
            log.warn("Done work, some problems on result")
        else:
            log.error("Key does not match! Check the key and try again.")
            sys.exit(1)
        next = getNextRun(datetime.datetime.now())
        log.info("Next run on: " + str(next))

