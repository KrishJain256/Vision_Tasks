#!/usr/bin/env python
import rospy

# Getting the AckermannDriveStamped msg type
from ackermann_msgs.msg import AckermannDriveStamped

msg_recieved = None

def relay(data):
    global msg_recieved,pub,rate
    msg_recieved = data
    rospy.loginfo(rospy.get_caller_id() + " Recieived message \n" + str(data))
    msg = msg_recieved
    msg.drive.speed *= 3
    msg.drive.steering_angle *= 3
    rospy.loginfo("Publishing updated message to drive_relay at " + str(rospy.Time.now()))
    pub.publish(msg)
    rate.sleep()

# def publisher():
#     global msg_recieved,pub,rate
#     msg_recieved.drive.speed *= 3
#     msg_recieved.drive.steering_angle *= 3
#     rospy.loginfo("Publishing updated message to drive_relay at " + str(rospy.Time.now()))
#     pub.publish(msg_recieved)
#     rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('relay', anonymous=True)
        rospy.Subscriber('drive', AckermannDriveStamped, relay)
        pub = rospy.Publisher('drive_relay',AckermannDriveStamped,queue_size=100)
        rate=rospy.Rate(100)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass