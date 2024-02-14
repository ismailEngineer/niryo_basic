from pyniryo import NiryoRobot

"""
    Initialization function 
    arg : ip_add --> the ip address of niryo robot 
    result : NiryoRobot object
"""
def init_robot(ip_add):
    try :
        print("Connecting to robot ... please wait")
        robot = NiryoRobot(ip_add)
        robot.calibrate_auto()
        # robot.move_joints(0.2, -0.3, 0.1, 0.0, 0.5, -0.8)
        robot.move_pose([0.16, 0.0, 0.35, 0.0, 1.57, 0.0])
        return robot
    except : 
        print("Unable to connect to robot")

"""
    Close robot connection 
    arg : NiryoRobot object
"""
def kill_robot(robot):
    try :
        robot.close_connection()
        print("Robot was desconnected successfully")
    except :
        print("Unable to disconnect the robot !!")

"""
    Go to a specific point function, the function accept joints or 3D points
    args :
        robot : NiryoRobot object
        goal : list of joints (j1,j2,j3,j4,j5,j6) if data_type ==1, 3D point (x,y,z) if data_type ==2
        data_type : 
            1 --> if goal is joints
            2 --> if goal is an euler points (x,y,z)
    result : void
"""
def goto(robot,goal,data_type):
    if data_type == 1 : # data_type = 1 is a joint data of 6 floats
        (j1,j2,j3,j4,j5,j6) = goal # (0.2, -0.3, 0.1, 0.0, 0.5, -0.8)
        print("GOTO is on execution ... ")
        print("Data type is joint --> "+ str((j1,j2,j3,j4,j5,j6)))
        try :
            robot.move_joints(j1,j2,j3,j4,j5,j6)
            print ("END Action ")
        except :
            print ("Unable to move robot !!")
    elif data_type == 2 : # data_type = 2 is a move (x, y, z, roll, pitch, yaw) data of 6 floats
        (x, y, z, roll, pitch, yaw) = goal    
    else : 
        print ("Unknown DATA TYPE !!")


"""
    pick and place oject from point 1 to point 2, the function accept joints or 3D points
    args :
        robot : NiryoRobot object
        point1 : list of joints (j1,j2,j3,j4,j5,j6) if data_type ==1, 3D point (x,y,z) if data_type ==2 
                    where object is located
        point1 : list of joints (j1,j2,j3,j4,j5,j6) if data_type ==1, 3D point (x,y,z) if data_type ==2
                    where you want to place the object
        data_type : 
            1 --> if goal is joints
            2 --> if goal is an euler points (x,y,z)
    result : void
"""
def pick_place(robot,point1,point2,data_type):
    if data_type == 1 : # data_type = 1 is a joint data of 6 floats
        (j1,j2,j3,j4,j5,j6) = point1
        print("PICK & PLACE is on execution ... ")

        print("Data type is joint --> Start joinst : "+ str((j1,j2,j3,j4,j5,j6)))
        try : 
            robot.move_joints(j1,j2,j3,j4,j5,j6)
            print("Catching Object ... ")
            robot.grasp_with_tool()
        except :
            print ("Unable to move & catch object !!")

        (j1,j2,j3,j4,j5,j6) = point2
        print("Data type is joint --> Goal joinst : "+ str((j1,j2,j3,j4,j5,j6)))
        try :
            robot.move_joints(j1,j2,j3,j4,j5,j6)
            print("Catching Object ... ")
            robot.release_with_tool()
        except :
            ("Unable to move & release object !!")

    else : 
        print ("Unknown DATA TYPE !!")

# -------------------  MAIN   ------------------------------------
mon_robot = init_robot("192.168.0.21")
goto(mon_robot,(0.16, 0, 0.35, 0, 1.57, 0),2)
kill_robot(mon_robot)