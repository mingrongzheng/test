import requests


if __name__ == "__main__":
    #ua伪装 user-agent()身份标识
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.208.400 QQBrowser/12.0.5440.400'
    }
    url = "https://www.sogou.com/web?"
    #处理url参数；封装字典

    
    kw = input("enter a word:")

    param = {
        'query':kw
    }
    #对指定url发起请求，并在请求过程中处理参数
    response=requests.get(url=url,params=param,headers=headers)
    #获取请求信息
    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！')
