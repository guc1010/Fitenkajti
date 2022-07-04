import re
import yaml
f = open('D:/ProgramData/Lexique Pro Data/Seniva/Seniva.db', 'r', encoding='utf-8')
zyen = f.readlines()
f.close()

khoh = []
i = -1

for ghang in zyen:
    #print(ghang)
    phuaih = re.search(r'^\\(\S*)\s(.*?)$', ghang)
    #print(phuaih)
    if phuaih == None:
        continue
    if i == -1 and phuaih.group(1) != 'lx':
        continue
    if phuaih.group(1) == 'lx':
        i += 1
        khoh.append({'lx': [phuaih.group(2)]})
    elif phuaih.group(1) == 'nt':
        ftnkp = re.search(r'^\\nt\sFtnk:\s(.*?)$', ghang)
        if ftnkp == None:
            ety = re.search(r'^\\nt\s词源:\s(.*?)$', ghang)
            if ety == None:
                khoh[i][phuaih.group(1)] = [phuaih.group(2)]
            else:
                khoh[i]['et'] = [ety.group(1)]
        else:
            ftnk = ftnkp.group(1)
            dokcjengh = []
            ftnkn = ftnk.split('/')
            for ftnkj in ftnkn:
                kuatghauh = re.search(r'([^\(]*?)\(([^\)]*?)\)(.*?)', ftnkj)
                if kuatghauh == None:
                    dokcjengh.append(ftnkj)
                else:
                    dokcjengh.append(kuatghauh.group(1)+kuatghauh.group(3))
                    dokcjengh.append(kuatghauh.group(1)+kuatghauh.group(2)+kuatghauh.group(3))
            khoh[i]['Ftnk'] = dokcjengh
    elif phuaih.group(1) in khoh[i]:
        khoh[i][phuaih.group(1)].append(phuaih.group(2))
    else:
        khoh[i][phuaih.group(1)] = [phuaih.group(2)]

#print(khoh)
g = open('khoh.yaml', 'w', encoding='utf-8')
#g.write(khoh)
g.write(yaml.dump(khoh,allow_unicode=True))
g.close()