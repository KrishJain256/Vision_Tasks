#!/usr/bin/env python
import rospy

# Getting the AckermannDriveStamped msg type
from ackermann_msgs.msg import AckermannDriveStamped


def talker(frm_num):
    frme_id = "frame_"+str(frm_num)

    v = float(rospy.get_param("/v"))
    d = float(rospy.get_param("/d"))

    # Forming the msg
    pub_msg = AckermannDriveStamped()
    pub_msg.header.stamp = rospy.Time.now()
    pub_msg.header.frame_id = frme_id
    pub_msg.drive.steering_angle = d
    pub_msg.drive.speed = v
        

    # Publishing the msg and logging data
    log = "Frame " + frme_id + " : Published message with steering angle = " + str(d) + " and speed = " + str(v) + " at timestamp " + str(rospy.Time.now())
    rospy.loginfo(log)
    return pub_msg


if __name__ == '__main__':
    try:
        pub = rospy.Publisher('drive',AckermannDriveStamped,queue_size=100)
        rospy.init_node('talker',anonymous=False)
        rate = rospy.Rate(100)
        frm_num = 0
        while not rospy.is_shutdown():
            msg = talker(frm_num)
            frm_num += 1
            pub.publish(msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
