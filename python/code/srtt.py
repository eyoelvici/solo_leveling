class Time():
    """time"""
    def __init__(self,hour=00,minute=00,second=00) :
        self.hour=hour
        self.minute=minute
        self.second = second
    def pt(self):
        x = ( "%.2d:%.2d:%.2d") % (self.hour, self.minute, self.second)
        # {self.hour}:{self.minute}:{self.second}
        return x
    def __add__(self,other):
        x = Time(self.hour+other.hour,self.minute+other.minute,self.second+other.second)
        y=Time()
        y.hour,y.minute=divmod(x.minute,60)
        y.hour += x.hour
        minute,y.second=divmod(x.second,60)
        y.minute+=minute
        return(Time.pt(y))

start=Time(23,85,58)
end=Time(12,0,36)
print(start+1337)
