from pyniryo import NiryoRobot, ObjectShape, ObjectColor


robot = NiryoRobot("192.168.0.21")
robot.calibrate_auto()

print("Start Vision")

list_workspaces = robot.get_workspace_list()
print(list_workspaces)

my_workspace = "wp_square"

(isFinded,position,shape,color) = robot.detect_object(my_workspace,shape=ObjectShape.ANY,color=ObjectColor.ANY)

print('isFinded = ',isFinded)
print('position = ',position)
print('shape = ',shape)
print('color = ',color)
