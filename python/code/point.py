class Name():
    """ This represents poin"""

    def Print_names(naming):
        First = ("%s") % (naming.First)
        Last = ("%s") % (naming.Last)

        return (f'{First} {Last}')
#creating point
class point():
    """points"""
    def Print_nums(naming):
        First = ("%.2f") % (naming.x)
        Last = ("%.2f") % (naming.y)
        return (First, Last)
#creating Rectangle
class Rectangle():
    """Rectangle"""
    def center(cen):
        c = point()
        c.x = (cen.w/2) + r1.p.x
        c.y = (cen.h/2) + r1.p.y

        return (c.x,c.y)

    def showrec(rects):
        """dispay"""
        x = rects.w
        y = rects.h
        px = rects.p.x
        py = rects.p.y
        py = 3

        return (x, y, px, py)

names = Name()
names.First = "john"
names.Last = "Doe"


p1 = point()
p2 = point()
p3 = point()
p4 = point()
# point_1
p1.x=0
p1.y=0
# point_2
p2.x=2
p2.y=0
# point_3
p3.x=2
p3.y=2
# point_4
p4.x=0
p4.y=2
#show point



r1 = Rectangle()
#rect_1
r1.w = 100
r1.h = 200
r1.p = p3
#show center

print(r1.showrec())