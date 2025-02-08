from pyjop import *
import cv2
import numpy as np

SimEnv.connect()
env = SimEnvManager.first()
env.reset()
drone = ServiceDrone.first()
lower_green = np.array([25, 100, 100])
upper_green = np.array([75, 255, 255])
lower_red = np.array([170, 100, 100])
upper_red = np.array([180, 255, 255])


while SimEnv.run_main():
    drone.set_thruster_force_right(120)
    drone.set_thruster_force_left(120)

    img = drone.get_camera_frame()

    # Convert the image to HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    # Create masks for green and red colors
    mask_green = cv2.inRange(hsv_img, lower_green, upper_green)
    mask_red = cv2.inRange(hsv_img, lower_red, upper_red)

    # Combine the masks
    mask = cv2.bitwise_or(mask_green, mask_red)

    # Find contours in the combined mask
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Initialize variables to store the largest green contour and its properties
    largest_green_contour = None
    largest_green_contour_area = 0

    # Iterate over the contours and find the largest green contour
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > largest_green_contour_area and cv2.mean(
            mask_green, mask=mask
        )[0] > 0:
            largest_green_contour_area = area
            largest_green_contour = contour

    # If a green contour is found, calculate its centroid and navigate the drone towards the orb
    if largest_green_contour is not None:
        M = cv2.moments(largest_green_contour)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        # Calculate the error in the drone's position relative to the centroid of the green orb
        error_x = cx - img.shape[1] / 2
        error_y = cy - img.shape[0] / 2

        # Adjust the drone's thrusters based on the error in its position
        drone.set_thruster_force_right(120 + error_x)
        drone.set_thruster_force_left(120 - error_x)

    # If no green contour is found, check for red contours
    else:
        largest_red_contour = None
        largest_red_contour_area = 0

        # Iterate over the contours and find the largest red contour
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > largest_red_contour_area and cv2.mean(
                mask_red, mask=mask
            )[0] > 0:
                largest_red_contour_area = area
                largest_red_contour = contour

        # If a red contour is found, avoid it by adjusting the drone's direction
        if largest_red_contour is not None:
            # Calculate the centroid of the red contour
            M = cv2.moments(largest_red_contour)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            # Calculate the error in the drone's position relative to the centroid of the red obstacle
            error_x = cx - img.shape[1] / 2
            error_y = cy - img.shape[0] / 2

            # Adjust the drone's thrusters based on the error in its position to avoid the red obstacle
            drone.set_thruster_force_right(120 - error_x)
            drone.set_thruster_force_left(120 + error_x)

    # Display the original image, the green mask, and the red mask for visualization
    cv2.imshow('Original Image', img)
    cv2.imshow('Green Mask', mask_green)
    cv2.imshow('Red Mask', mask_red)
    cv2.waitKey(1)

SimEnv.disconnect()
