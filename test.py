import time

count = 1


def time_out():
    time.sleep(1)
    print("stop")




while count < 5:
    print ("Hello World!")
    count+=1
    time_out()
    



    
