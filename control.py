
"""
Demo the direct flying for the python interface

Author: Amy McGovern
"""

from pyparrot.Minidrone import Mambo

# you will need to change this to the address of YOUR mambo
mamboAddr =  "d0:3a:52:0b:e6:22"
#def print_status():

def shutdown_land(mambo):
	mambo.safe_land(5)
	mambo.smart_sleep(5)
	print("disconnect")
	mambo.disconnect()


# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambo = Mambo(mamboAddr, use_wifi=False)
#mambo.set_user_sensor_callback(print_status,args)
print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
	print("taking off!")
	mambo.safe_takeoff(5)
	mambo.smart_sleep(5)
	try:
		while True:
			direction = input("Please Enter Direction")
			if direction == 'w':
				print("movinig up")
				mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=8, duration=1)
			elif direction == 's':
				print("moving down")
				mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-8, duration=1)
			elif direction == 'a':
				print("moving left")
				mambo.fly_direct(roll=0, pitch=0, yaw=-8, vertical_movement=0, duration=1)
			elif direction == 'd':
				print("moving right")
				mambo.fly_direct(roll=0, pitch=0, yaw=8, vertical_movement=0, duration=1)
			elif direction == 'r':
				print("rotating")
				mambo.move_relative(0,0,0,math.radians(30))
			elif direction == 'p':
				mambo.fly_direct(roll=0, pitch=10, yaw=0, vertical_movement=0, duration=1)
			elif direction == 'n':
				shutdown_land(mambo)
			
	except Exception as e:
		print(e)
		shutdown_land(mambo)
		print("done")
