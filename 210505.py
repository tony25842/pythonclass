def greting(Fname):
    """這是一個函數的說明"""
    print("%s 晚上好" % (Fname))

def gretingv2(Fname = "First",Lname = "Last"):
    """這是一個有兩個參數函數的說明"""
    print("%s %s 晚上好" % (Fname,Lname))

def gretingv3(Fname ,Lname):
    result = Fname + " " + Lname + " 晚上好"
    return result

def gretingv4(lists):
    for l in lists:
        print(l + " 晚上好")


Fname = "Tony"
Lname = "Lu"
help(greting)
greting(Fname)
gretingv2(Fname,Lname)

gretingv2(Fname = "Lu",Lname = "Tony") #具名呼叫
gretingv2(Lname = "Tony" ,Fname = "Lu")
gretingv2()#預設值
gretingv2("Tony")

print(gretingv3(Fname, Lname))

gretingv4(["Tony Lu","Jackie Chen","Eric Yu"])