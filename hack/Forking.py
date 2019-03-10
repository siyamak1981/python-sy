import os
print (os.getpid())
# out:
# 888
########################################
import os
# import fork
# print (type(os.getpid()))
def child_proc():
    print ("child proces is exit")
    print ("child proces exit %d pid " % os.getpid())

def parent_proc():
    print ("parent_proc is started %d pid"%os.getpid())
    fork_proc = os.fork()
    if (fork_proc == 0):
        child_proc()
    else :
        print ("child proc forked %d pid"%fork_pros)



parent_proc()

##############################################333
print (os.execvp('ping',['ping','223.12.110.16']))
# out
# $ Reply from 192.168.1.4: Destination host unreachable.
# Reply from 192.168.1.4: Destination host unreachable.
# Reply from 192.168.1.4: Destination host unreachable.
# Reply from 192.168.1.4: Destination host unreachable.

# Ping statistics for 223.12.110.16:
#     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),

print (os.execvp('ls',['ls','-la']))
# out

# drwxr-xr-x 1 PC 197121    0 Feb 13 13:18  .
# drwxr-xr-x 1 PC 197121    0 Nov 15 14:09  ..
# drwxr-xr-x 1 PC 197121    0 Jan 21 12:37  .git
# drwxr-xr-x 1 PC 197121    0 Nov 15 14:20  .vscode
# drwxr-xr-x 1 PC 197121    0 Dec 14 12:38  __doc__
# drwxr-xr-x 1 PC 197121    0 Feb 13 06:27  __pycache__
# -rw-r--r-- 1 PC 197121  360 Dec  7 10:30  api.py
# drwxr-xr-x 1 PC 197121    0 Dec 14 12:31  args-kwargs-packages
# drwxr-xr-x 1 PC 197121    0 Dec 29 11:04  assert
# -rw-r--r-- 1 PC 197121  845 Dec 15 10:53  carrying.py
# drwxr-xr-x 1 PC 197121    0 Dec 29 12:39 'class[].{}'
# -rw-r--r-- 1 PC 197121 3725 Dec  3 10:46  comprehension.py
# drwxr-xr-x 1 PC 197121    0 Dec  8 09:53  connection
# drwxr-xr-x 1 PC 197121    0 Feb 11 13:59  csv
# -rw-r--r-- 1 PC 197121  425 Feb 13 13:17  cwd.py
# -rw-r--r-- 1 PC 197121 2953 Feb 13 06:27  datetime.py
# -rw-r--r-- 1 PC 197121 2903 Dec 14 08:41  dictionary.py
# drwxr-xr-x 1 PC 197121    0 Dec 11 05:45  exception
# drwxr-xr-x 1 PC 197121    0 Feb  5 13:12  exercise
# -rw-r--r-- 1 PC 197121  130 Dec 10 08:15  for.py
# -rw-r--r-- 1 PC 197121  463 Feb 13 13:38  Forking.py
# drwxr-xr-x 1 PC 197121    0 Dec 15 09:26  function
# -rw-r--r-- 1 PC 197121 1311 Feb  5 12:55  hack.py
# drwxr-xr-x 1 PC 197121    0 Dec  5 12:27  Images
# drwxr-xr-x 1 PC 197121    0 Dec 29 12:36  letter_game
# -rw-r--r-- 1 PC 197121  976 Jan  7 02:22  liks.txt
# drwxr-xr-x 1 PC 197121    0 Dec 29 07:39  list
# -rw-r--r-- 1 PC 197121 1623 Dec 14 09:24  logic.py
# -rw-r--r-- 1 PC 197121 1117 Nov 18 13:24  numbergame.py
# -rw-r--r-- 1 PC 197121  152 Dec  5 07:33 'pdb.set_trace().py'
# drwxr-xr-x 1 PC 197121    0 Dec  8 10:45  regex-findfile
# -rw-r--r-- 1 PC 197121  362 Dec  9 03:26  request.py
# -rw-r--r-- 1 PC 197121 1443 Feb 11 14:10  requirement.txt
# -rw-r--r-- 1 PC 197121 1557 Dec 12 09:41  reversedstr.py
# drwxr-xr-x 1 PC 197121    0 Dec 29 07:38  rpg
# -rw-r--r-- 1 PC 197121 2189 Dec 14 08:01  set.py
# -rw-r--r-- 1 PC 197121  891 Nov 17 13:51  shopinglist.py
# -rw-r--r-- 1 PC 197121  807 Dec  7 03:45 'splite().py'
# drwxr-xr-x 1 PC 197121    0 Feb 13 06:29  tamrin
# -rw-r--r-- 1 PC 197121 1367 Dec 14 09:06  tuples.py
# drwxr-xr-x 1 PC 197121    0 Nov 15 14:12  venv
# -rw-r--r-- 1 PC 197121 1427 Dec 14 11:14  wiki.py
# -rw-r--r-- 1 PC 197121 3390 Dec 28 13:34  yeild.py