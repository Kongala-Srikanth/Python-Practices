#########################################################
#               ERROR HANDLING
#########################################################

try:
    print(a)
except:
    print("first line error")
else:
    print("no error")
finally:
    print("always run")
print("________________________________")

#########################################################


try:
    print(2/0)

except Exception as ds:
    print(ds)
print("________________________________")
#########################################################


try:
    try:
        print(a)
    except Exception as kk:
        print(kk)

except:
    print("error found")
else:
    print("no errors")
