#!/usr/bin/bash
#SPDX-FileCopyrightText: 2025 Kazuya Ochiai
#SPDX-License-Identifier: BSD-3-Clause


dr=~
[ "$1" != "" ] && dr="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# 正常なパスでのパブリッシュテスト
ros2 run problem2 LastUpdated / > test_publish.log 2>&1 & PUB_PID=$!
sleep 6
kill $PUB_PID

if grep -q "Published last modified:" test_publish.log; then
    : # テスト成功
else
    echo "failed publish"
    exit 1
fi

# 無効なパスでのテスト
ros2 run problem2 LastUpdated /dummy/path > test_invalid.log 2>&1 || true

if grep -q "Path does not exist" test_invalid.log; then
    : # テスト成功
else
    echo "failed invalid path test"
    exit 1
fi

# トピックの配信テスト
timeout 10 ros2 run problem2 LastUpdated / & NODE_PID=$!
sleep 6
timeout 10 ros2 topic echo /file_last_modified > test_topic.log & LISTEN_PID=$!
sleep 6

kill -SIGKILL $NODE_PID || true
kill -SIGKILL $LISTEN_PID || true

if grep -q "data:" test_topic.log; then
    : # テスト成功
    rm -rf test_topic.log
    exit 0
else
    rm -rf test_topic.log
    exit 1
fi
