#!/usr/bin/env python
import rospy

pose = rospy.get_param("/deadReckoning/pose")
path = rospy.get_param("/deadReckoning/path")

def DeadRecoExecution():
    rospy.loginfo("Still updating")

if __name__ == '__main__':
    try:
        DeadRecoExecution()
    except rospy.ROSInterruptException:
        pass