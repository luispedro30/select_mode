#!/usr/bin/env python
import rospy

pose = rospy.get_param("/slam/pose")
map = rospy.get_param("/slam/map")

def slamExecution():
    rospy.loginfo("Still updating")

if __name__ == '__main__':
    try:
        slamExecution()
    except rospy.ROSInterruptException:
        pass