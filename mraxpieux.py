import yaml
import unidecode
ya = open('khoh.yaml', 'r', encoding='utf-8')
yar = ya.read()
khoh = yaml.load(yar, yaml.FullLoader)
ya.close()
mp = {}
onp = '''# Rime dictionary
# vim: set ts=8 sw=8 noet:
# encoding: utf-8
#
# \\u7279\\u6b63\\u6587\\u5168\\u62fc
#
# Author:
#  - Kinboise	<zsimghuadsjing@163.com>
#
---
name: fitenkazp
version: "2022.05.30"
sort: by_weight
use_preset_vocabulary: false
...
'''
uni = 0xF0000
uni += 32

wq = 'IEAOUYW'
wq = list(wq)
bq = 'QHPBTDKGCJSZFVMNLR'
bq = list(bq) + ['Ʒ','X','Ž','Ŋ']

for i in wq:
  mp[i.lower()] = hex(uni)
  uni += 1
for i in bq:
  mp[i] = hex(uni)
  uni += 1
for i in bq:
  mp[i.lower()] = hex(uni)
  uni += 1
for i in bq:
  for j in wq:
    mp[i+j] = hex(uni)
    uni += 1

for deu in khoh:
  if 'Ftnk' in deu and '-' not in deu['ph'][0]:
    lat = unidecode.unidecode(deu['ph'][0].strip('˙')).lower()
    for f in deu['Ftnk']:
      f = f.strip('·')
      f = f.strip('˙')
      f = f.strip('.')
      for z in f.split('_'):
        if z not in mp:
          mp[z] = hex(uni)
          uni += 1
        onp += ('\\U' + '000' + mp[z][2:])
      onp += ('\t' + lat + '\r')

mpy = open('mraxpieux.yaml','w',encoding='utf-8')
mpy.write(yaml.dump(mp, allow_unicode=True))
mpy.close()

mpt =''
for z in mp:
  mpt += (mp[z] + ' ' + z + '\n')

na = open('namelist.txt','w',encoding='utf-8')
na.write(mpt)
na.close

onp = onp.encode().decode("unicode_escape")
onpy = open('fitenkazp.dict.yaml','w',encoding='utf-8')
onpy.write(onp)
onpy.close()