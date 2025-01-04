# humidityコマンド

## 概要
- humidityは課題2のために作成されたコマンドです。  
- humidity.pyを実行して、別のターミナルでその実行結果を受け取ることでその日の東京の湿度が〇%と認識することができる。

## 使い方
- 以下を実行します。  
```
  $ git clone https://github.com/Kaz-stark/problem2.git  

  $ cd problem2  

  $  ros2 run mypkg humidity  
```  
- 次に別のターミナルを開いて以下を実行します。  
```  
$ ros2 topic echo /tokyo_humidity --field data | awk '{print "本日の東京の湿度は " $1 "%"}'
``` 

## 必要なソフトウェア  
- Python
  - テスト済みのバージョン: 3.7~3.10  

## テスト環境  
- Ubuntu 24.04 LTS

## 権利関係    
### 権利  
- © 2024 Kazuya Ochiai  
- このソフトウェアパッケージは、3条項BSDライセンスのもと、再配布および利用が許可されています。  
- このパッケージのコードは、Ryuichi Ueda氏本人の許可を得て、下記のスライド(© 2024 Ryuichi Ueda) (CC-BY-SA4.0 by Ryuichi Ueda)のものを一部参考にし、自身の著作として作成されたものです。  
    - [ryuichiueda/my_slides robosys_2022] (https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)  

### 参考記事
- [著作権とライセンス|上田隆一](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson5.html#1)  
- [ソフトウェアのテスト|上田隆一](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson6.html)  
- [GitHubでのテスト|上田隆一](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson7.html#1)
- [Robot Operating System(ROS 2)|上田隆一](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html#24)  
- [ROSシステムのテスト|上田隆一](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html#4)  
- [ROS2 publisher/subscriber node(+topic)の作成|@Dorebom(dorebom b)](https://qiita.com/Dorebom/items/47fb67e5e47a205f1395)  
- [Pythonで学ぶROS2ノード開発：パブリッシャーとサブスクライバーの基本ROS2で通信する|Murasan Lab](https://murasan-net.com/2024/09/23/ros2-publisher-subscriber-python/)  
  


