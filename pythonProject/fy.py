import requests
import csv  
import json
if __name__ == "__main__":
    
    post_url = "https://fanyi.baidu.com/sug"
    word = input("enter a word:")
    data= {
        'kw':word
    }
    #ua伪装
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.208.400 QQBrowser/12.0.5440.400'
    }
    #请求发送
    response= requests.post(url=post_url,data=data,headers=headers)
    dic_obj=response.json()
    # with open(word+'.csv', 'w', newline='', encoding='utf-8') as csvfile:  
    #     fieldnames = ['k', 'v']  # 列名  
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
    #     writer.writeheader()  # 写入列名  
    #     for item in dic_obj['data']:  # 遍历每一项数据  
    #         writer.writerow(item)  # 将每一项数据写入CSV文件
    # fileName = word+'.json'
    # fp=open(fileName,'w',encoding='utf-8')
    # json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print(dic_obj)
    print("over!")