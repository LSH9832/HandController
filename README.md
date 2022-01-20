# UV Hand Controller
## Note
It is desighed only for bitcq unmanned vehicle hand controller
## Usage
### Install
```commandline
python3 setup.py install
```
### Use
if you want to control something with hand controller, you should first know the params of all buttons and joysticks.
```python
# from HandController import Data
from data import Data


controller = Data()
try:
    while True:
        controller.update()
        
        left_joystick_updown = controller.JOYSTICK.LEFT.UP_DOWN
        print("\rleft_joystick up_down value: %s" % left_joystick_updown)
        
        # controller.JOYSTICK.(LEFT/RIGHT).(LEFT_RIGHT/UP_DOWN)
        # controller.BUTTON.EMERGENCY_STOP
        # controller.BUTTON.(B1/B2/B3/B4)
        # controller.BUTTON.(F1/F2/F3/F4/F5/F6/F7/F8)
        
except KeyboardInterrupt:
    controller.close()
```