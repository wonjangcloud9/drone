from djitellopy import Tello
import time

drone = Tello()
drone.connect()

drone.takeoff()
time.sleep(5)
drone.land()

# Path: requirements.txt
djitellopy
