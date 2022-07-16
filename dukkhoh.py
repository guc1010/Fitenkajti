碼表路徑 = 'fep/Fitenka.nam'
詞庫路徑 = 'D:/ProgramData/rime/fitenkazp.dict.yaml'
新詞表路徑 = 'sinzsipieux.txt'
詞典路徑 = 'D:/ProgramData/Lexique Pro Data/Seniva/Seniva.db'
拉丁章路徑 = 'myoncjang.txt'
def 讀諸行(路徑):
  文件 = open(路徑, 'r', encoding='utf-8')
  諸行 = 文件.read().splitlines()
  文件.close()
  return 諸行

def 存文本(文本, 路徑):
  文件 = open(路徑, 'w', encoding='utf-8')
  文件.write(文本)
  文件.close()

# 特正文編碼與拉丁轉寫對應表：十六進制碼位 拉丁轉寫
def 讀碼表(碼表路徑):
  諸行 = 讀諸行(碼表路徑)
  碼表 = {}
  for 行 in 諸行:
    行 = 行.split(' ')
    碼表[行[1]] = int(行[0], 16)
    最大碼 = int(行[0], 16)
  return [碼表,最大碼]

# Rime輸入法碼表：特正文字符\t拉丁正字法
def 讀轉換庫(詞庫路徑):
  諸行 = 讀諸行(詞庫路徑)
  轉換庫 = {}
  for 行 in 諸行:
    行 = 行.split('\t')
    if len(行) == 2:
      if 行[1] not in 轉換庫:
        轉換庫[行[1]] = 行[0]
  return 轉換庫

# 新詞列表：拉丁正字法 拉丁轉寫
def 讀新詞(新詞路徑):
  諸行 = 讀諸行(新詞路徑)
  新詞表 = {}
  for 行 in 諸行:
    行 = 行.split(' ')
    行[1] = 行[1].split('_')
    新詞表[行[0]] = 行[1]
  return 新詞表

def 讀詞典(詞典路徑, 新詞表路徑):
  zyen = 讀諸行(詞典路徑)
  khoh = []
  i = -1

  import re
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
  新詞表 = ''
  import unidecode
  for deu in khoh:
    if 'Ftnk' in deu and '-' not in deu['ph'][0]:
      lat = unidecode.unidecode(deu['ph'][0].strip('˙')).lower()
      for f in deu['Ftnk']:
        f = re.sub('·','·_',f)
        f = re.sub('˙','˙_',f)
        f = re.sub(r'\.','_.',f)
        新詞表 += (lat + ' ' + f + '\n')
  存文本(新詞表, 新詞表路徑)

def 拉丁章分詞(拉丁章):
  import re
  # 拉丁章 = re.sub(r'([!?,])', r' \1', 拉丁章)
  # 拉丁章 = re.sub(r'\.', r' ,,', 拉丁章)

  # 拉丁章 = re.sub(r'^"', r'“', 拉丁章)
  # 拉丁章 = re.sub(r'(\s)"', r'\1“', 拉丁章)
  # 拉丁章 = re.sub(r'"', r'”', 拉丁章)

  # 拉丁章 = re.sub(r'(\S)([˙·\-\(\):\[\]“”《》])', r'\1 \2', 拉丁章)
  # 拉丁章 = re.sub(r'([˙·\-\(\):\[\]“”《》])(\S)', r'\1 \2', 拉丁章)
  拉丁章 = re.sub(r'X\.', 'XX\'', 拉丁章)
  拉丁章 = re.sub(r'X(\d)', r'XX \1', 拉丁章)
  拉丁章 = re.sub(r'0\.', 'Q\'', 拉丁章)
  拉丁章 = re.sub(r'1\.', 'J\'', 拉丁章)
  拉丁章 = re.sub(r'2\.', 'B\'', 拉丁章)
  拉丁章 = re.sub(r'3\.', 'K\'', 拉丁章)
  拉丁章 = re.sub(r'4\.', 'F\'', 拉丁章)
  拉丁章 = re.sub(r'5\.', 'P\'', 拉丁章)
  拉丁章 = re.sub(r'6\.', 'R\'', 拉丁章)
  拉丁章 = re.sub(r'7\.', 'C\'', 拉丁章)
  拉丁章 = re.sub(r'8\.', 'D\'', 拉丁章)
  拉丁章 = re.sub(r'9\.', 'Z\'', 拉丁章)
  拉丁章 = re.sub(r'^"', r'“', 拉丁章)
  拉丁章 = re.sub(r'(\s)"', r'\1“', 拉丁章)
  拉丁章 = re.sub(r'(\s)"', r'\1“', 拉丁章)
  拉丁章 = re.sub(r'"', r'”', 拉丁章)
  拉丁章 = re.sub(r'([^\w</>’])', r' \1 ', 拉丁章)
  拉丁章 = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹])', r' \1 ', 拉丁章)
  拉丁章 = re.sub(r'<', r' <', 拉丁章)
  拉丁章 = re.sub(r'>', r'> ', 拉丁章)
  拉丁章 = re.sub(r'\.', r' ,,', 拉丁章)
  拉丁章 = re.sub(r',,\s\s\s,,\s\s\s,,', r'...', 拉丁章)
  諸詞 = 拉丁章.split(' ')
  while '' in 諸詞:
    諸詞.remove('')
  return 諸詞