def m(x1,y1,x2,y2):
    if x1 == x2:
        return None
    return (y1-y2)/(x1-x2)
def c(x1,y1,x2,y2):
    return (-x1) * m(x1,y1,x2,y2) + y1
def isInTriangle(xa,ya,xb,yb,xc,yc):
    xd = xa + (xc-xb)
    yd = ya + (yc-yb)
    xe = xa + (xb-xc)
    ye = ya + (yb-yc)
    
    dc = c(xd,yd,xc,yc)
    ab = c(xa,ya,xb,yb)
    ad = c(xa,ya,xd,yd)
    bc = c(xb,yb,xc,yc)

    eb = c(xe,ye,xb,yb)
    ac = c(xa,ya,xc,yc)
    ea = c(xe,ye,xa,ya)
    bc = c(xb,yb,xc,yc)
    if (dc <= 0 <= ab or ab <= 0 <= dc) and (ad <= 0 <= bc or bc <= 0 <= ad):
        if (eb <= 0 <= ac or ac <= 0 <= eb) and (ea <= 0 <= bc or bc <= 0 <= ea):
            return True
    return False
print(isInTriangle(-340,495,-153,-910,835,-947))
print(isInTriangle(-175,41,-421,-714,574,-645))
i = 0
with open("102_triangles.txt") as file:  
    data = file.read()
    for row in data.split("\n"):
        r = [int(x) for x in row.split(",")]
        if isInTriangle(r[0],r[1],r[2],r[3],r[4],r[5]):
            i += 1
print(i)
