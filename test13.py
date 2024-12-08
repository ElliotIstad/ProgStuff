import time
import subprocess
import os
import time
filedir = "/home/jacob"
curr = "Workplan "+time.strftime("%d-%m-%Y"); out = curr+".txt"
file = os.path.join(filedir, out)
if not os.path.exists(file):
    open(file, "wt").write("curl ascii.live/rick")
    subprocess.Popen(["gedit", file])
    t = 0
    while t < 20:
        t += 1; time.sleep(1)
        wlist = subprocess.check_output(["wmctrl", "-l"]).decode("utf-8")
        if out in wlist:
            w = [l.split()[0] for l in wlist.splitlines() if out in l][0]
            for cmd in [["xdotool", "windowmove", w, "0", "0"],
                        ["xdotool", "windowsize", w, "47%", "100%"]]:
                subprocess.call(cmd)
            break