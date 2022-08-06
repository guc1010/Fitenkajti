import fontforge as ff
import os

print('自动导入svg至字体。')
mgk = input('请输入文件夹：')

#ff.loadNamelist('Fitenka.nam')
lohkengh = 'FitenkajtiR.sfd'

light = ff.open(lohkengh)

svgs = os.listdir('svg/' + mgk + '/')
for svg in svgs:
    glyph = light.createChar(int(svg[0:-4], 16))
    glyph.importOutlines('svg/' + mgk + '/' + svg)
    # glyph.left_side_bearing(0)
    # glyph.width(1000)
    glyph.removeOverlap()
    glyph.correctDirection()
    glyph.addExtrema('all')
light.save(lohkengh)

# import shutil as sh

# sh.copyfile(lohkengh, 'FitenkajtiR.sfd')
# regular = ff.open('FitenkajtiR.sfd')
# regular.changeWeight(25, 'CJK', 0, 0, 'auto', 1)
# regular.save('FitenkajtiR.sfd')

# sh.copyfile(lohkengh, 'FitenkajtiB.sfd')
# bold = ff.open('FitenkajtiB.sfd')
# bold.changeWeight(50, 'CJK', 0, 0, 'auto', 1)
# bold.save('FitenkajtiB.sfd')
