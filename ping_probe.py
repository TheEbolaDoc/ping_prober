import argparse
import time
import sys
import os

## TODO:
## + Argument Parser
## + Change os.system to subprocess.popen
## + implement GPIO interaction
## + while true?? 

def ping_host_bool(ip , print_ping, print_result):
    "function for testing wheter a host is up or not"
    
    # TODO: Change os.system to subprocess.popen
    if (print_ping):
        response = not (os.system("ping -c 1 " + ip)) #inverting bool because of misleading system exit codes
    else:
        response = not (os.system("ping -c 1 " + ip + "&> /dev/null"))
    
    if (print_result):
        if (response):
            print('The Host with the IP \"' + ip + '\" is up!')
        else:
            print('The Host with the IP \"' + ip + '\" is down!')
    
    return response
##
## end of ping_host_bool function

def ping_wrapper(ip , print_ping, print_result, max_tries):
    counter = 0
    for x in range(0,max_tries):
        time.sleep(1)
        if ping_host_bool(ip, print_ping, print_result):
            counter += 1
    if print_result: print("("+ str(counter) + "/" + str(max_tries) + ") pings were succssesfull!")
    return counter
##
## end of ping_wrapper function

def enable_gpio():
    pass        

if __name__ == "__main__":
    while True:
        pass:
        max_tries = 5
        if ((max_tries/2) >= ping_wrapper(sys.argv[1], False, True, max_tries)):
            print("Turn GPIO off!")
##
## end of main function