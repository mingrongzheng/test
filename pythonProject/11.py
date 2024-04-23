import requests
import csv
import datetime
# import hashlib
# import time
f = open('视频.csv',mode='w',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
    '标题',
    '播放量',
    '评论',
    '弹幕',
    '发布时间',
    
])
csv_writer.writeheader()
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Cookie":"buvid3=8AC50E1B-7CCE-4F8C-CDAF-EFB9B6F8BC4054417infoc; b_nut=1697195854; i-wanna-go-back=-1; b_ut=7; _uuid=79D23CDB-424F-F899-CC2D-71082B4AF5710254584infoc; buvid_fp=08e977886d24268e9cea7d44cd4b6bf9; buvid4=41D44DED-7397-E456-905F-C23A41C5278A55971-023101319-R442m6v4Q7HobtqRXdjKlQ%3D%3D; LIVE_BUVID=AUTO7716971958813708; CURRENT_FNVAL=4048; rpdid=|(mmkulkJml0J'uYm~um)~kk; hit-dyn-v2=1; enable_web_push=DISABLE; header_theme_version=CLOSE; is-2022-channel=1; DedeUserID=100804117; DedeUserID__ckMd5=728b1de205bbd974; fingerprint=48945eeafaf48b1a7013bd4751bbe56a; bp_video_offset_100804117=881940090812628996; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDQ5NzY4MTQsImlhdCI6MTcwNDcxNzU1NCwicGx0IjotMX0.duVFvvsNX34NFgcX-Y09zPDW8e7gT5j48h6RxnXv5OA; bili_ticket_expires=1704976754; SESSDATA=dcc81529%2C1720269616%2C03a9c%2A11CjAK6UEygwx6CU0Zk867qOgtGD-4sChPkQ3ZBH_CWWxqvnLgzTWfw07pR93XA32EoOsSVjkxX3Vta0kyOWFfU01PT00yb1hlMERFaXhyVVJ2bXpZdS1MZ1RCV0ZodzQ1NjNOZXFIcXFWbm1DODBybk14SWdJZXZDQmNQVHExcEFWem9JWVdZNzJ3IIEC; bili_jct=cf56b0433d969b1f003c310899eaea45; PVID=2; home_feed_column=5; innersign=0; b_lsid=FDEF8FD4_18CE985934E; browser_resolution=1528-602; sid=7ck2872r"
}
url = 'https://api.bilibili.com/x/space/wbi/arc/search'
response = requests.get(url=url,headers=headers)
json_data = response.json()

for index in json_data[b'data']['list']['vlist']: 
        try:
        #发布时间
            date = str(datetime.datetime.fromtimestamp(index['created']))
            dit={
                '标题':index['title'],
                '播放量':index['play'],
                '评论':index['comment'],
                '弹幕': index['video_review'],
                '发布时间':date,
            }
            csv_writer.writerow(dit)
            print(dit)
        except:
            print("wu")





# for index in info_list:
#     data_time = index['']
#     dit = {
#         '标题':index['title'],
#         'bv号':index['bvid'],
#         '播放量':index['play']
#     }
#     print(dit)
