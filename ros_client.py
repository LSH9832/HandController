#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
import time
import rospy
from geometry_msgs.msg import Twist,PointStamped,PoseStamped,Pose,Quaternion

from HandController import Data, WEB


class ROSCar(object):

    __cmd = Twist()
    __cmd_pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)

    def __init__(self):
        self.emergency_stop()
        
    def emergency_stop(self):
        self.__cmd.angular.z = 0.0
        self.__cmd.linear.x = 0.0                    
        self.__cmd_pub.publish(self.__cmd)

    def set_speed(self, value):
        self.__cmd.linear.x = value

    def set_rotation(self, value):
        self.__cmd.angular.z = value

    def update(self):
        self.__cmd_pub.publish(self.__cmd)



if __name__ == "__main__":

    ############################--初始化--############################

    rospy.init_node("car")      # 初始化car节点
    car = ROSCar()              # 创建小车控制实例

    # 初始化远端控制数据
    my_remote_data = Data(
        source=WEB,             # 表明数据来自网络而非本地， 需要填写后面的参数（本地只需 Data(),source默认LOCAL）
        host='10.31.203.6',     # 远端服务器IP地址
        port=10086,             # 远端服务器服务端口
        user="admin",           # 用户名， 要与远端服务端对应上
        pwd="password"          # 密码， 要与远端服务端对应上
    )

    assert not rospy.is_shutdown(), "ROS NOT LAUNCH!"
    print("Initialization Finished, Remote Control Start.")

    #################################################################

    while not rospy.is_shutdown():
        # 更新从网络中传来的控制数据
        my_remote_data.update()

        # 如果按下紧急制动按钮，则所有速度和转动控制量置零
        if my_remote_data.BUTTON.EMERGENCY_STOP:
            car.emergency_stop()

        # 否则使用摇杆进行控制
        else:
            # 左摇杆的上下控制小车前进和后退（控制量前正后负）
            car.set_speed(float(my_remote_data.STICK.LEFT.UP_DOWN) / 1000 * 5)  # 将控制值[-1000, 1000]转换到[-5, 5]

            # 右摇杆的左右控制小车转动（控制量左负右正）
            car.set_rotation(float(my_remote_data.STICK.RIGHT.LEFT_RIGHT) / 1000 * 5)
            
            """
            其他控制量：
            1.拨动开关, 从左到右命名为B1-B4,（上 True, 下 False)
            my_remote_data.BUTTON.(B1/B2/B3/B4)

            2.快捷按钮F1-F8 (按下为 True, 未按下为 False)
            my_remote_data.BUTTON.(F1/F2/F3/F4/F5/F6/F7/F8)
            """

        # 最后通过发布话题更新小车的控制量
        car.update()

