# meningfaylim=open("F:\Python\Projects\salom1.txt",'w')
# meningfaylim.write("assalomu alekum Onajonim")
# meningfaylim.close()
#
# di=open("salom.txt",'r')
# a=di.read()
# print(a)

    #istisnoli holatlarni oldini olish
try:
    somefile=open("salom.txt",'w')
    try:
        somefile.write("Salom dunyo")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)

