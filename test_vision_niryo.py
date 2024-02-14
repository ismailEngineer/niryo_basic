from pyniryo import NiryoRobot, ObjectShape, ObjectColor


robot = NiryoRobot("192.168.0.21")
robot.calibrate_auto()

print("Start Vision")
point1 = (0.29,-0.06,0.117)
point2 = (0.146,-0.06,0.119)
point3 = (0.147,0.074,0.118)
point4 = (0.289,0.076,0.115)

# robot.save_workspace_from_points("wp_test_save",point1,point2,point3,point4)
#list_workspaces = robot.get_workspace_ratio('wp_test_save')
list_workspaces = robot.get_workspace_list()
print(list_workspaces)

my_workspace = "wp_square"

(isFinded,position,shape,color) = robot.detect_object(my_workspace,shape=ObjectShape.ANY,color=ObjectColor.ANY)

print('isFinded = ',isFinded)
print('position = ',position)
print('shape = ',shape)
print('color = ',color)
