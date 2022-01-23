from HandController import run_server

# Ubuntu下请以管理员权限运行该程序，否则读取串口的时候会报错: Permission Denied
# 或者在运行程序前赋予串口权限： sudo chmod 777 /dev/ttyS3
if __name__ == '__main__':

    run_server(
        host='0.0.0.0',
        port=10086,
        user="admin",
        pwd="admin"
    )
