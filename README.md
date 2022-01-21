# HandController: 手持地面站终端控制接口
## 注意
这是为特定型号的手持地面站终端写的控制接口，不通用。支持Linux 和 Windows系统
## 用法说明
### 安装
```commandline
python3 setup.py install
```
### 使用
#### demo
```python
from HandController import Data

controll_data = Data()
try:
    while True:
        control_data.update()
        
        left_joystick_updown = control_data.JOYSTICK.LEFT.UP_DOWN
        left_joystick_leftright = control_data.JOYSTICK.LEFT.LEFT_RIGHT
        print("\r左摇杆上下控制值: %s  左摇杆左右控制值:" % (left_joystick_updown.zfill(4), left_joystick_leftright.zfill(4)))
        
        # control_data.JOYSTICK.(LEFT/RIGHT).(LEFT_RIGHT/UP_DOWN)       # 左/右 摇杆 上下/左右 控制值(-1000, 1000)
        # control_data.BUTTON.EMERGENCY_STOP                            # 紧急制动按钮 (按下为True，松开为False)
        # control_data.BUTTON.(B1/B2/B3/B4)                             # 拨动开关（依次从左往右四个按钮，True为向上开启状态，False为向下关闭状态）
        # control_data.BUTTON.(F1/F2/F3/F4/F5/F6/F7/F8)                 # 快捷按钮F1-F8（按下为True, 松开为False）
        
except KeyboardInterrupt:
    control_data.close()
```
