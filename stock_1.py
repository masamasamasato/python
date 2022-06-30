import pandas as pd #データ解析の支援を行うモジュール　データ集計やデータ加工など
import matplotlib.pyplot as plt
from pandas_datareader import data  #日経平均やナスダック、日本の個別銘柄の取得が可能となる
import numpy as np
import talib as ta  #テクニカル分析を算出するための、ライブラリ
import mplfinance as mpf  # ファイナンスに特化したライブラリ　mplfinanceの描画に必要とされる
from datetime import datetime
from datetime import timedelta

plt.rcParams["font.family"] = "Hiragino sans"   #labelなどに対して日本語対応のためのモジュール



#dataframeとは? 二次元以上のデータの扱いはデータフレームを用いる

#-----------株価の表示のための関数----------------------

def company_stock_price(company_stock_code,start_date,end_date):


    plt.figure(figsize=(50,10))
    df = data.DataReader(company_stock_code, 'stooq', start_date, end_date)    #証券コード　データソースはstooq　期間はいつからいつか
    date = pd.to_datetime(df.index) #データフレームのインデックス番号をdatetime64型に変換し格納
    df['weekday'] = date.weekday #曜日ごとで分類 曜日情報のカラムの追加を行う   月曜日を0として1,2,3,4,5,6でそれぞれの曜日を表す。ただし株取引を行わない土曜日と日曜日は存在しない。


    stock_price = df['Close']

    span_1 = 5  #移動平均における期間を表す。
    span_2 = 10 #移動平均における期間を表す。
    span_3 = 25 #移動平均における期間を表す。
    span_4 = 50 #移動平均における期間を表す。

    
    df['SMA_1'] = stock_price.rolling(window=span_1).mean() #株価に対して窓関数を用いる際にrollingが用いられる。窓関数とはspanごとに区切り、この場合はspan_1ごとに平均を求めている
    df['SMA_2'] = stock_price.rolling(window=span_2).mean() 
    df['SMA_3'] = stock_price.rolling(window=span_3).mean() 
    df['SMA_4'] = stock_price.rolling(window=span_4).mean()



#-----------線グラフ、ボリンジャーバンド(期間はspan_3(25日ごと))の描画部分----------------------

    plt.subplot(2,2,1) #subplotは棒グラフと線グラフを分割するための関数 (縦方向2分割,横方向1分割,位置)

    plt.plot(date,stock_price,label='企業平均株価') #線グラフの描画
    plt.plot(date,df['SMA_1'],label='単純移動平均(期間5日)')
    plt.plot(date,df['SMA_2'],label='単純移動平均(期間10日)')
    plt.plot(date,df['SMA_3'],label='単純移動平均(期間25日)')
    plt.plot(date,df['SMA_4'],label='単純移動平均(期間50日)')

    df['upper'],df['middle'],df['lower'] = ta.BBANDS(stock_price,timeperiod = span_3,nbdevup=2,nbdevdn=2,matype=0)
    plt.fill_between(date, df['upper'],df['lower'],color = "grey", alpha=0.5)
    plt.legend()    #分割した場合はどちらのグラフに対するラベルかを明示させる必要がある

#-----------棒グラフ描画部分----------------------
#出来高が株価のその後の価格に反映されることから出来高を表す棒グラフも表示させる

    plt.subplot(2,2,2)
    plt.bar(date,df['Volume'],label='出来高')
    plt.legend()


#-----------ヒストグラム描画部分----------------------
    df['macd'],df['macdsignal'],df['macdhist'] = ta.MACD(stock_price,fastperiod= 12,slowperiod= 26,signalperiod=9)
    plt.subplot(2,2,3)
    plt.fill_between(date,df['macdhist'], color= 'grey', alpha = 0.5, label = 'macdhist')
    plt.legend()

#-----------RSI描画部分----------------------

    df['RSI'] = ta.RSI(stock_price, timeperiod = span_1)    #期間をspan_1(5日)としてRSIを作成する
    plt.subplot(2,2,4)
    plt.plot(date,df['RSI'],label='RSI値')
    plt.hlines([30,50,70],date.min(),date.max(),"red",linestyles="dashed")
    plt.legend()


    plt.show()

    
company_stock_price('4751.JP','2021-06-25','2022-06-25') #サイバーエージェントの2021年06月25日から2022年06月25日の株価の推移
company_stock_price('2371.JP','2021-06-25','2022-06-25') #カカクコムの2021年06月25日から2022年06月25日の株価の推移
