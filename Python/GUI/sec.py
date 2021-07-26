def get_weather(city, key):
    r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
    text = json.loads(r.text)
    dict = text['data']['forecast'][0]
    result = dict[str(key)]
    return result


if __name__ == '__main__':
    # 让所有文本居中
    sg.SetOptions(text_justification='center')

    # 整体的布局是从上而下，同一列表中为从左往右
    # 创建视图窗口，用二维列表 list 表示，用来存放组件
    # Text , Input 等是PySimpleGUI中的类
    layout = [
        # key 值代表了是这个输入框输入的值，以字典的 键 值来表示，这个用于找到输入框并跟新它的值
        [sg.Text('城市', size=(20, 1)), sg.Input(key='CITY')],
        [sg.Text('日期', size=(20, 1)), sg.Input(key='DATE')],
        [sg.Text('最高气温', size=(20, 1)), sg.Input(key='HIGH')],
        [sg.Text('风力', size=(20, 1)), sg.Input(key='FENGLI')],
        [sg.Text('最低气温', size=(20, 1)), sg.Input(key='LOW')],
        [sg.Text('风向', size=(20, 1)), sg.Input(key='FENGXIANG')],
        [sg.Text('天气', size=(20, 1)), sg.Input(key='TYPE')],
        [sg.Button('搜索')]
    ]
    # 创建窗口，将视窗放在窗口中 ‘天气小助手’为窗口的名字
    window = sg.Window('天气小助手', layout)
    # 获取输入框和按钮元素的值
    event, values = window.read()
    # 得到城市这个输入框的值
    city = values['CITY']
    # 以下六行代码均根据 key 值进行定位输入框
    date = get_weather(city, 'date')
    high = get_weather(city, 'high')
    fengli = get_weather(city, 'fengli')
    low = get_weather(city, 'low')
    fengxiang = get_weather(city, 'fengxiang')
    type = get_weather(city, 'type')
    # 更新输入框中的值
    weather_date = window['DATE'].update(date)
    weather_high = window['HIGH'].update(high)
    weather_fengli = window['FENGLI'].update(fengli)
    weather_low = window['LOW'].update(low)
    weather_fengxiang = window['FENGXIANG'].update(fengxiang)
    weather_type = window['TYPE'].update(type)

    # # 找到天气输入框
    # weather_wind = window['TYPE']
    # # 将天气更新到输入框
    # weather_wind.update(type)

    # 显示窗口
    window.read()

    window.close()
