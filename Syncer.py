from lib.Process.Process import PROC
from datetime import datetime
import time

while True:
    now = datetime.now()
    fout = open('Syncer_log.txt', 'w')
    fout.write(now.strftime('%Y-%m-%d %H:%M:%S') + '\n')
    fout.close()

    process = PROC('rsync -a ')
    process.run().wait()

    time.sleep(3600)