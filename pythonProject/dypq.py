import requests  
import json  
  
if __name__ == "__main__":  
    url = "https://movie.douban.com/j/chart/top_list" 
    start=input("从什么地方开始，例如第一输入0：")
    limit=input("多少部，例如一部输入1：")   
    param = {  
            'type':'24',
            'interval_id': '100:90',
            'action':'', 
            'start': start,
            'limit': limit
    }  
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    response = requests.get(url=url, params=param, headers=headers)   
    list_data = response.json()
    fp = open('./douban.json', 'w', encoding='utf-8')  
    json.dump(list_data, fp=fp, ensure_ascii=False)    
    print("over!")