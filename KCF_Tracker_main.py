#!/usr/bin/env python

import rospy
from KCF_Tracker import ImageConverter  # Assuming the KCF_Tracker functionality is implemented in the ImageConverter class

def main():
    rospy.init_node("KCF_Tracker", anonymous=True)
    n = rospy.NodeHandle()
    image_converter = ImageConverter(n)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
