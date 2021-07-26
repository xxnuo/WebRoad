# [url=home.php?mod=space&uid=267492]@file[/url]   : bing_lym.py
# [url=home.php?mod=space&uid=238618]@Time[/url]   : 2021/6/4 8:53
 
import re
import os
import win32api
import win32con
import win32gui
import requests
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}
''
 
 
def downloads_img(time_info, img_d_url, img_text):
    path = os.getcwd() + f'/{time_info}.jpg'
    with open(path, 'wb') as f:
        f.write(requests.get(img_d_url, headers=headers).content)
 
    path_ = os.getcwd() + f'/{time_info}.txt'
    with open(path_, 'w', encoding='utf-8') as f_:
        f_.write(img_text + '\n' + img_d_url)
 
    print("*-> 文件链接", img_d_url)
    print(f"*-> 文件  {time_info}.jpg --> 下载成功！")
 
 
def get_res_html():
    aspx_url = 'http://cn.bing.com/HPImageArchive.aspx?idx=0&n=1'
    img_html = requests.get(url=aspx_url, headers=headers).text
    # print(img_html)
 
    date_info = re.findall('<fullstartdate>(.*?)</fullstartdate>', img_html)[0]
    img_info = re.findall('<url>(.*?)</url>', img_html)[0]
 
    # 07_06 加入关于图片说明
    img_text = re.findall('<copyright>(.*?)</copyright>', img_html)[0]
    print(' date_info -> %s\n img_info  -> %s\n img_text  -> %s' % (date_info, img_info, img_text))
 
    return date_info, img_info, img_text
 
 
def setWallPaper(pic):
    # open register
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regKey, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # refresh screen
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic, win32con.SPIF_SENDWININICHANGE)
 
 
def img_main():
    bing_url = 'https://cn.bing.com'
    date_info, img_info, img_text = get_res_html()
    # 下载函数
    downloads_img(time_info=date_info, img_d_url=bing_url + img_info, img_text=img_text)
    # 绝对路径储存
    path = os.getcwd() + f'/{date_info}.jpg'
    # print(type(path), path)
 
    pd = input('> 更换壁纸？ y/n :')
    if pd == "y":
        setWallPaper(pic=path)
    else:
        pass
 
 
if __name__ == '__main__':
    img_main()