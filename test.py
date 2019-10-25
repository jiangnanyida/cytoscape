# coding=utf-8
import csv
path = '/Users/huangyida/Desktop/大四上/row data/result_10.22/'
f = open(path+'infection.csv','r')
f_csv = csv.reader(f)
dic = []
w = open(path+'rinf.csv','w')
w_csv = csv.writer(w)
head = {'name','vendor','version','vul_id','vul_name','cve_number','cvss'}
for line in f_csv:
    name = line[0]
    vendor = line[1]
    version = line[2]
    print(version)
    vul_id = 'vul_'+line[3]
    vul_name = line[4]
    cve_number = line[5]
    cvss = line[6]
    dic.append({'name':name,'vendor':vendor,'version':version,'vul_id':vul_id,'vul_name':vul_name,'cve_number':cve_number,'cvss':cvss})

f.close()
w.close()

# with open(path+'infection.csv', mode='rb') as f:
#     reader = csv.reader(f)
#     # i 设置按行获取数据
#     for i, rows in enumerate(reader):
#         try:
#             # 解决读取csv文件中文格式乱码——gb2312只支持普通中文字符
#             row1 = [row1.decode('GB2312').encode('utf-8') for row1 in rows]
#         except:
#             #存在繁体时
#             #gbk支持繁体中文和日文假文
#             row1 = [row1.decode('GBK').encode('utf-8') for row1 in rows]











