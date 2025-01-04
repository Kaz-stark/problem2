#!/bin/bash -xv
# -xvオプション: 実行したコマンドと結果を表示

# ROS 2の環境をソース
source /opt/ros/humble/setup.bash
source /root/ros2_ws/install/setup.bash

# ビルド
cd /root/ros2_ws
colcon build --packages-select mypkg

# パッケージのセットアップファイルをソース
source /root/ros2_ws/install/setup.bash

# humidity.pyを実行（バックグラウンドで）
ros2 run mypkg humidity > /tmp/humidity_output.txt &
pid=$!  # プロセスIDを保存

# 少し待って出力を確認できるようにする
sleep 3

# 出力ファイルの内容を確認
cat /tmp/humidity_output.txt

# テスト: 出力に"湿度:"という文字列が含まれているか確認
grep "湿度:" /tmp/humidity_output.txt
if [ $? -eq 0 ]; then
    echo "Test passed: 湿度の出力を確認"
else
    echo "Test failed: 湿度の出力が見つかりません"
    kill $pid
    exit 1
fi

# プロセスを終了
kill $pid

echo "All tests passed successfully!"
exit 0
