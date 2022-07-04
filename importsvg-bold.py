import fontforge as ff
#import os
import shutil as sh

lohkengh = 'Fitenkajti.sfd'
sh.copyfile(lohkengh, 'FitenkajtiR.sfd')
regular = ff.open('FitenkajtiR.sfd')
regular.changeWeight(25, 'CJK', 0, 0, 'auto', 1)
regular.save('FitenkajtiR.sfd')

sh.copyfile(lohkengh, 'FitenkajtiB.sfd')
bold = ff.open('FitenkajtiB.sfd')
bold.changeWeight(50, 'CJK', 0, 0, 'auto', 1)
bold.save('FitenkajtiB.sfd')
