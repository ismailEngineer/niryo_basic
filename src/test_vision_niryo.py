from pyniryo import NiryoRobot, ObjectShape, ObjectColor
import time
import yaml

fichier_config = '..\config\config.yaml'
print("Le fichier config se trouve ici : ",fichier_config)

with open(fichier_config,'r+') as file:
    object_file = yaml.safe_load(file)

IP_robot = object_file['IP_ROBOT']

robot = NiryoRobot(IP_robot)
robot.calibrate_auto()

#----------------- HELP CALIBRATING WORKSPACE : MOVING CAMERA TO OBSERVATION POSITION ------------------------
# move to camera observation position
print("la caméra se positionne en hauteur (MODE OBSERVATION)")
#robot.move_pose([0.193, 0.005, 0.283, 0, 1.287, 2.897])
time.sleep(2)
#robot.close_connection()
#-------------------------------------------------------------------------------------------------------------


print("Start Vision")
# gStep = 0.060
# gcX = 0.250  # 0.2454
# gcY = 0.0    # 0.0059
# gcZ = 0.1043  # 0.1043
pZ = 0.095  # pZ : coordonnée Z du plateau de jeu (<=> hauteur du plateau par rapport au sol)
protectZ = 0.05 # pour mettre la pince en position sécurisée (un peu plus haut que nécessaire)
shiftTargetEdge = 40
#robot.move_pose([0.310, -0.060, pZ+protectZ, 2.774, 1.387, 2.573])
#robot.close_connection()
# ----------------------- CREATION WORKSPACE --------------------------------------
# HELP AGO : Ned2 en mode "angle droit" (les bras à la verticale et à l'horizontale)
#robot.move_joints([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])                 # en joints (degrés ou radians) : c'est plus facile à programmer ...
#robot.move_pose([256.364, 0.208, 371.643, 0.693, 1.571, 0.695])   # en mm

# TRES IMPORTANT : les points doivent $etre définis en (X, Y, Z) et donc SANS roll, pitch et yaw !!!!!!
point1 = (0.335, -0.120, pZ)   # , 1.57, 0, 0)
point2 = (0.165, -0.120, pZ)   # , 1.57, 0, 0)
point3 = (0.165,  0.120, pZ)   # , 1.57, 0, 0)
point4 = (0.335,  0.120, pZ)   # , 1.57, 0, 0)

#vrobot.save_workspace_from_points("wp_test_save4", point1, point2, point3,point4)
#list_workspaces = robot.get_workspace_ratio('wp_test_save')
#list_workspaces = robot.get_workspace_list()
#print(list_workspaces)

# robot.move_pose([0.310, -0.060, pZ+protectZ, 2.774, 1.387, 2.573])
# robot.open_gripper(500, 100, 20)
# robot.move_pose([0.310, -0.060, pZ, 2.774, 1.387, 2.573])
# robot.close_gripper()

# time.sleep(2)
# robot.move_pose([0.190, -0.060, pZ, 2.774, 1.387, 2.573])
# time.sleep(2)
# robot.move_pose([0.190,  0.060, pZ, 2.774, 1.387, 2.573])
# time.sleep(2)
# robot.move_pose([0.310,  0.060, pZ, 2.774, 1.387, 2.573]) # 2.774, 1.387, 2.573])
# time.sleep(2)

my_workspace = "wp_manual_test"    # "wp_TicTacToe"

#----------------- MOVING CAMERA TO OBSERVATION POSITION ------------------------
# move to camera observation position
print("la caméra se positionne en hauteur (MODE OBSERVATION)")
#robot.move_pose([0.193, 0.005, 0.283, 2.889, 1.287, 2.897])
robot.move_pose([0.15, 0.0, 0.35, 0.0, 1.57, 0.0])


# NB AGO : si le plateau est au niveau du sol (<=> Z = 0) alors le Z de la pince, pour qu'elle ne touche pas le plateau, doit être à 0.95469 (approximativement)

#----------------- PICK & PLACE -------------------------------------------------
#for i in range(6) :
isFinded = True
while isFinded :
    # move to camera observation position
    robot.move_pose([0.15, 0.0, 0.35, 0.0, 1.57, 0.0])

    (isFinded,position,shape,color) = robot.detect_object(my_workspace,shape=ObjectShape.CIRCLE,color=ObjectColor.ANY)
    #if isFinded :
    robot.vision_pick(my_workspace, 0/1000.0, ObjectShape.CIRCLE, ObjectColor.ANY)
    # If an object has been taken, do:
    print("je prends le jeton")
    robot.place_from_pose([0.15, -0.17, 0.20, 0.2, 1.57, 0])
    #robot.move_pose([0.15, -0.1, 0.25, 0.2, 1.57, 0.0])

    print('isFinded = ',isFinded)
    print('position = ',position)
    print('shape = ',shape)
    print('color = ',color)

    time.sleep(2)
    #isFinded = True


robot.close_connection()