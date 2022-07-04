wq = 'IEAOUYW'
wq = list(wq)
bq = 'QHPBTDKGCJSZFVMNLRX'
bq = list(bq) + ['Dc','Xz','Nq']

mp = ''

for i in wq:
  mp += (i + ' ' + i.lower() + '\n')
  mp += (i.lower() + ' ' + i.lower() + '\n')
for i in bq:
  mp += (i + ' ' + i + '\n')
  mp += (i.lower() + ' ' + i + '\n')
for i in bq:
  for j in wq:
    mp += (i + j + ' ' + i + j + '\n')
    mp += (i.lower() + j.lower() + ' ' + i + j + '\n')

print(mp)