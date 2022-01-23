from HandController import Data, WEB

my_remote_data = Data(
    source=WEB,
    host="127.0.0.1",
    port=10086,
    user="admin",
    pwd="admin"
)

while True:
    my_remote_data.update()
    print(my_remote_data.BUTTON.EMERGENCY_STOP)
