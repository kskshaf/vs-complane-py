"""
    The original source code is from https://www.nmm-hd.org/newbbs/viewtopic.php?f=23&t=1813
    PSNR arguments are base on https://github.com/vcb-s/rp-checker
    rpc.vpy from https://github.com/AmusementClub/vapoursynth-script/blob/master/RpcTemplate.vpy
    usage: vspipe -p rpc.vpy . | python3 complane.py > rpc_result.txt
"""

import sys

d_y = {}
d_u = {}
d_v = {}

for l in sys.stdin:
    l = l.strip()
    if not l:
        continue

    parts = l.split(" ")
    if len(parts) != 5:
        continue

    frame, psnr_y , psnr_u, psnr_v = int(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])

    if psnr_y < 30:
        psnr_y = '%s' % (psnr_y)
        d_y.update({psnr_y: frame})

    elif psnr_u < 40:
        psnr_u = '%s' % (psnr_u)
        d_u.update({psnr_u: frame})

    elif psnr_v < 40:
        psnr_v = '%s' % (psnr_v)
        d_v.update({psnr_v: frame})

if d_y == {} and d_u == {} and d_v == {}:
    print("Every planes are OK!!!")

if d_y != {}:
    print("==============FUCKING_Y==============")
    [print("Frame:", fnm, "PSNR_Y:", list(d_y.keys())[list(d_y.values()).index(fnm)]) for fnm in sorted(d_y.values())]
    print("===================================")
else:
    print("Y plane is OK!")

if d_u != {}:
    print("==============FUCKING_U==============")
    [print("Frame:", fnm, "PSNR_U:", list(d_u.keys())[list(d_u.values()).index(fnm)]) for fnm in sorted(d_u.values())]
    print("===================================")
else:
    print("U plane is OK!")

if d_v != {}:
    print("==============FUCKING_V==============")
    [print("Frame:", fnm, "PSNR_V:", list(d_v.keys())[list(d_v.values()).index(fnm)]) for fnm in sorted(d_v.values())]
    print("===================================")
else:
    print("V plane is OK!")
