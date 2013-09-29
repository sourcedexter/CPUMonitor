import psutil
import sys
import time
import curses
print("CPU Utilisation!!!")
print("1.CPU utilisation in percent  2.CPU utilisation corewise")
choice = input()
if choice == '1':
    print (chr(27) + "[2J")
    while True:
        sys.stdout.write("\r")
        sys.stdout.write("(utilisation:"+ str(psutil.cpu_percent())+'%' + ')')
        time.sleep(1)
        sys.stdout.flush()
elif choice == '2':
    print (chr(27) + "[2J")
    while True:
        cores = psutil.cpu_percent(interval=1, percpu=True)
        no_cores= len(cores)
        if  no_cores == 8:
            def core_report():
                stdscr.addstr(0,0,"core 1: "+str(cores[0])+"%"+"     core 2: "+str(cores[1])+"%"+
                "     core 3: "+str(cores[2])+"%"+ "     core 4: "+str(cores[3])+"%")
                stdscr.addstr(1,0,"core 5: "+str(cores[0])+"%"+"     core 6: "+str(cores[1])+"%"+
                "     core 7: "+str(cores[2])+"%"+ "     core 8: "+str(cores[3])+"%")
            stdscr = curses.initscr()
            core_report()
            time.sleep(1)
        elif no_cores == 4:
            sys.stdout.write("core 1: "+str(cores[0])+"%"+"     core 2: "+str(cores[1])+"%"+
            "     core 3: "+str(cores[2])+"%"+ "     core 4: "+str(cores[3])+"%")
            time.sleep(1)
            sys.stdout.flush()
        elif no_cores == 2:
            sys.stdout.write("core 1: "+str(cores[0])+"%"+"     core 2: "+str(cores[1])+"%")
            time.sleep(1)
            sys.stdout.flush()
        elif no_cores == 1:
            sys.stdout.write("core 1: "+str(cores[0]))
            time.sleep(1)
            sys.stdout.flush()
