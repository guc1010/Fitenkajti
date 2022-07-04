from easygui import fileopenbox, msgbox, enterbox
import PIL.Image as im
n = enterbox(msg='', title='输入起始编号')
n = int(n, 16)
print(n)
f = fileopenbox(title='选择要分割的图片')
print(f)
if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.tif'):
    end = -4
elif f.endswith('.webp') or f.endswith('.tiff'):
    end = -5
else:
    msgbox('格式错误！')
    end = 0
if end != 0:
    bs = im.open(f)
    import re
    fplm = re.sub(r'.*?\\([^\\]+?)\.png', r'\1', f) + '/'
    puto = 'D:/paine/Fitenka Kaiti/png/' + fplm
    print(fplm)
    w = bs.size[0] // 1000
    h = bs.size[1] // 1000
    print(w, h)
    k = 0
    l = 0
    import os
    os.mkdir(puto)
    for i in range(0,h):
        for j in range(0,w):
            if l == 20:
                l = 0
            if l == 0:
                os.mkdir(puto + str(k//20))
            plm = puto + str(k//20) + '/' + hex(n + k) + '.png'
            bs.crop((j*1000,i*1000,(j+1)*1000,(i+1)*1000)).save(plm)
            k += 1
            l += 1