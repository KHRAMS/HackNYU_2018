import boto3
import json
import cv2
#
# # Camera 0 is the integrated web cam on my netbook
# camera_port = 0
#
# #Number of frames to throw away while the camera adjusts to light levels
# ramp_frames = 30
#
# # Now we can initialize the camera capture object with the cv2.VideoCapture class.
# # All it needs is the index to a camera port.
# camera = cv2.VideoCapture(camera_port)
#
# # Captures a single image from the camera and returns it in PIL format
# def get_image():
#  # read is the easiest way to get a full image out of a VideoCapture object.
#  retval, im = camera.read()
#  return im
#
# # Ramp the camera - these frames will be discarded and are only used to allow v4l2
# # to adjust light levels, if necessary
# for i in xrange(ramp_frames):
#  temp = get_image()
# # Take the actual image we want to keep
# camera_capture = get_image()
# file = "/home/katchu11/Pictures/user.jpg"
# # A nice feature of the imwrite method is that it will automatically choose the
# # correct format based on the file extension you provide. Convenient!
# cv2.imwrite(file, camera_capture)
#
# # You'll want to release the camera, otherwise you won't be able to create a new
# # capture object until your script exits
# del(camera)
import boto3
import json
if __name__ == "__main__":
	imageFile='/home/katchu11/MyPrograms/face.jpg'
	client=boto3.client('rekognition','us-east-1')
	with open(imageFile, 'rb') as image:
		response = client.detect_faces(Image={'Bytes': image.read()},Attributes=["ALL"])
	my_json = json.dumps(response)
	final_emotion = (str(response))
	print("You are %s" % final_emotion.lower())
	loaded_json = json.loads(my_json)
	print (json.dumps(loaded_json, indent=4, sort_keys=True))
	#print(loaded_json['FaceDetails'])
	#print(response)
