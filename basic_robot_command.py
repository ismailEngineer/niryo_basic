import pyniryo

class basic_command:
    def __init__(self):
        self.name_workspace = "GROUND PLATE"
        self.pose_initial = (0.1,0.2,0,0.0)
        
        # Variables begining with "_" are private
        self.x_offset = 0.0
        self.y_offset = 0.0
        self.z_offset = 0.0

    def getter_pose(self):
        return(self.x_offset,self.y_offset,self.z_offset)
    
    def setter_pose(self,x_of,y_of,z_of):
        if x_of != 0.0 :
            self.x_offset = x_of
        else :
            print('VALUE NOT CORRECT !!')
        self.y_offset = y_of
        self.z_offset = z_of
    

def navigate():
    print("****************")
    print("&&&&&&&&&&&&&&&&&&&&&&&")
    print("^^^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    print ("hello i am from external script")
    

