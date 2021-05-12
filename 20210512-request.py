import requests

url = "https://www.sce.pccu.edu.tw"

try:
    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
                Safari/537.36', }
    url = 'https://www.ntu.edu.tw/'
    htmlfile = requests.get(url, headers=headers)
    print("偽裝瀏覽器擷取網路資料成功")
    print(htmlfile.text)

    fn = 'ntu.html'
    with open(fn, 'wb') as file_Obj:                        # 以二進位儲存
        for diskStorage in htmlfile.iter_content(10240): # Response物件處理
            size = file_Obj.write(diskStorage)           # Response物件寫入
            print(size)                                  # 列出每次寫入大小
        print("以 %s 儲存網頁HTML檔案成功" % fn)

except Exception as err:
    print("網頁下載失敗: ",err)
