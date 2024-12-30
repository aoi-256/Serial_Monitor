import serial
import csv
import pandas as pd
from matplotlib import pyplot as plt
import os

#user input (ここの値を調整してね)
data_range = 200 #表示範囲を設定

#params
index = 0
headers = ['index', 'data1', 'data2', 'data3']
data_1 = []
data_2 = []
data_3 = []

# シリアルポートの設定（ポート名とボーレートは適切に設定してください）
ser = serial.Serial('COM5', baudrate=1000000, timeout=1, stopbits=1)

fig, ax = plt.subplots()

os.remove("data.csv")

try:
    # CSVファイルを追記モードで開く
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(headers)

        csvfile.flush()  # ヘッダーを書き込んだ後にフラッシュ
        
        while True:
            # 1行分のデータを読み込む（'\n'まで）
            line = ser.readline()
            
            '''データが読めた時の処理'''
            if line:
                # 受信データをデコードして表示
                decoded_line = line.decode('utf-8').strip()
                
                parts = decoded_line.split(' ')

                parts_1, parts_2, parts_3 = parts[:3]

                # CSVに書き込む
                csvwriter.writerow([index, parts_1, parts_2, parts_3])
                csvfile.flush()  # データを即時に書き込む

            '''グラフの表示プログラム'''

            df = pd.read_csv('data.csv')

            if index >= data_range:

                df = df[df['index'] >= index - data_range]

            data1 = df["data1"] 
            data2 = df["data2"] 
            data3 = df["data3"] 

            plt.gca().clear()

            #プロット
            plt.plot(data1)
            plt.plot(data2)
            plt.plot(data3)

            index += 1

            plt.pause(0.001)

except KeyboardInterrupt:
    # Ctrl+Cが押された場合にループを抜ける
    print("終了します。")

finally:
    # シリアルポートを閉じる
    ser.close()
