import math
class Time():
    def __init__(self,hour=0,minute=0,second=0) :
        self.hour=hour
        self.minute=minute
        self.second=second

    def time_int(self):
        minutes = self.hour*60
        seconds = self.second + minutes*60
        return seconds
    
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def __add__(self,other):
        """print"""
        second = other.time_int() - self.time_int()
        return int_time(second)



def int_time(self):
    t = Time()
    minute, t.second = divmod(self, 60)
    t.hour, t.minute = divmod(minute, 60)
    print(self,t.hour,t.minute,minute)

    return t

start=Time(10,9)
end=Time(12,9,)
Time.print_time(start+end)

eror=Time(12,56,15)
eror.print_time()

"""
class point():
    def __init__(self,x=0,y=0) -> None:
        self.x=x
        self.y=y
    def print_p(self):
        fout=(self.x,self.y)
        return fout

p=point(12,22)
print(p.print_p())"""