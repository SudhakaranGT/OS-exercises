import os
command_path =['/bin/ls','/bin/cat','/bin/cp','/bin/echo','/bin/ps','/bin/rm','/bin/mv','/usr/bin/man','/bin/chmod','/usr/bin/clear']
print('''
1.ls
2.cat
3.cp
4.echo
5.ps
6.rm
7.mv
8.man
9.chmod
10.clear
11.exit
'''
)
x=int(input("enter choice"))
while x!=11:
    i=x
    if i==11:
        break
    elif i==1:
        os.execl(command_path[0], 'ls', '-l')
    elif i==2:
        os.execl(command_path[1], 'cat', '1.txt')
    elif i==3:
        os.execl(command_path[2], 'cp ', '1.txt','2.txt')
    elif i==4:
        os.execl(command_path[3], 'echo', 'Hello World')
    elif i==5:
        os.execl(command_path[4], 'ps', '-aux')
    elif i==6:
        os.execl(command_path[5], 'rm', '2.txt')
    elif i==7:
        os.execl(command_path[6], 'mv', '1.txt','2.txt')
    elif i==8:
        os.execl(command_path[7], 'man', 'ls')
    elif i==9:
        os.execl(command_path[8], 'chmod', '755','2.txt')
    elif i==10:
        os.execl(command_path[9], 'clear')
    else:
        print("enter a valid choice")
