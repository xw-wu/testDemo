import  datetime
now = datetime.datetime.now()
c_time = now.strftime("%Y%m%d_%H%M%S")
print(c_time)

log_time=c_time+'.log'
with open(log_time,'w+',encoding='utf-8') as f :
    #时间[level] line:13 this is a log message
    f.write("ryuf")