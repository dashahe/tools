import sched, wechat, reminder, config
import time

s = sched.scheduler(time.time, time.sleep)
delay = 60 * 30

def __task():
    wechat.tempMsgSend(reminder.remind(), config.openID1)
    wechat.tempMsgSend(reminder.remind(), config.openID2)
    s.enter(delay, 0, __task)

def schedule():
    s.enter(delay, 0, __task)
    s.run()

if __name__ == '__main__':
    schedule()