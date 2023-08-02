#!/usr/bin/env python

# 导入必要的库
import rospy
from KCF_Tracker import ImageConverter  # 假设 KCF_Tracker 功能在 ImageConverter 类中实现

# 定义主函数
def main():
    # 初始化 ROS 节点，给节点指定名称为 "KCF_Tracker"，anonymous=True 确保节点具有唯一标识符以防止命名冲突
    rospy.init_node("KCF_Tracker", anonymous=True)

    # 创建一个 NodeHandle，类似于 C++ 中的 ros::NodeHandle
    n = rospy.NodeHandle()

    # 创建一个 ImageConverter 类的对象，传递 NodeHandle n 作为构造函数的参数
    image_converter = ImageConverter(n)

    # 进入 ROS 事件循环，开始处理回调函数，类似于 C++ 中的 ros::spin()
    rospy.spin()

# 如果当前文件是主文件（而不是被其他文件导入的模块），则执行下面的代码
if __name__ == "__main__":
    try:
        # 调用主函数 main()
        main()
    except rospy.ROSInterruptException:
        # 如果出现 ROSInterruptException 异常，忽略该异常
        pass
