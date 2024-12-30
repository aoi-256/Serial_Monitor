# 適当シリアルモニター

適当に作ったのでバグっても文句言わないでね

## 使い方

### データのフォーマット

- 基本のフォーマット
```
データ1 (スペース) データ2 （スペース) データ3 （改行コード)
```

- データの送信例(CPP)

```cpp
std::string str = std::to_string(count_1) + " " + std::to_string(count_2) + " " +std::to_string(count_3) + "\n";
```

### 表示数の調整

データの表示数はここで調節してね

```py
#user input (ここの値を調整してね)
data_range = 100 #表示範囲を設定
```

### 実際の表示例

データはCSVに保存したものを用いているので、線形じゃなくても大丈夫です！

新規実行すると保存したデータは消えてしまうので注意

Ctrl+Cで終了

![スクリーンショット (329)](https://github.com/user-attachments/assets/c8cec5a3-a51e-43d2-afcc-bafe3b17cc4b)
