import rtos
import os
from datetime import datetime
from pathlib import Path

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FileMonitorNode(Node):
    def __init__(self, target_path: str):
        super().__init__('file_monitor_node')
        
        # パブリッシャーの設定
        self.publisher = self.create_publisher(
            String,
            'file_last_modified',
            10
        )
        
        # 監視対象のパスを設定
        self.target_path = Path(target_path)
        if not self.target_path.exists():
            self.get_logger().error(f'Path does not exist: {target_path}')
            return
            
        # タイマーの設定（1秒間隔でチェック）
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.last_modified = None
        
    def timer_callback(self):
        try:
            # 最終更新日時を取得
            current_modified = datetime.fromtimestamp(
                os.path.getmtime(self.target_path)
            )
            
            # 前回と異なる場合のみパブリッシュ
            if self.last_modified != current_modified:
                msg = String()
                msg.data = current_modified.isoformat()
                self.publisher.publish(msg)
                self.last_modified = current_modified
                
                self.get_logger().info(f'Published last modified: {msg.data}')
                
        except Exception as e:
            self.get_logger().error(f'Error checking file: {str(e)}')

def main(args=None):
    rclpy.init(args=args)
    
    # 監視対象のパスを指定してノードを作成
    node = FileMonitorNode('/path/to/your/target')
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
