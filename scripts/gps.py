#!/usr/bin/env python
import rospy

pose = rospy.get_param("/gps/pose")
path = rospy.get_param("/gps/path")

def GpsExecution():
    rospy.loginfo("Still updating")

if __name__ == '__main__':
    try:
        GpsExecution()
    except rospy.ROSInterruptException:
        pass