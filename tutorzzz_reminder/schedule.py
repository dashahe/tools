import sched, wechat, reminder, config
import time

s = sched.scheduler(time.time, time.sleep)
delay = 60 * 30

def __task():
    msg = reminder.remind()
    if msg == '尚无招募任务':
        return
    for openID in config.openIDList:
        wechat.tempMsgSend(msg, openID)
    s.enter(delay, 0, __task)

def schedule():
    s.enter(delay, 0, __task)
    s.run()

if __name__ == '__main__':
    schedule()