import boto3

BUCKET = "amazon-rekognition"
KEY = "test.jpg"
FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence")

def detect_faces(bucket, key, attributes=['ALL'], region="eu-west-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_faces(
	    Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
	    Attributes=attributes,
	)
	return response['FaceDetails']

for face in detect_faces(BUCKET, KEY):
	print ("Face ({Confidence}%)".format(**face))
	# emotions
	for emotion in face['Emotions']:
		print( "  {Type} : {Confidence}%".format(**emotion))
	# quality
	for quality, value in face['Quality'].iteritems():
		print( "  {quality} : {value}".format(quality=quality, value=value))
	# facial features
	for feature, data in face.iteritems():
		if feature not in FEATURES_BLACKLIST:
			print ("  {feature}({data[Value]}) : {data[Confidence]}%".format(feature=feature, data=data))

"""
	Expected output:
	Face (99.945602417%)
	  SAD : 14.6038293839%
	  HAPPY : 12.3668470383%
	  DISGUSTED : 3.81404161453%
	  Sharpness : 10.0
	  Brightness : 31.4071826935
	  Eyeglasses(False) : 99.990234375%
	  Sunglasses(False) : 99.9500656128%
	  Gender(Male) : 99.9291687012%
	  EyesOpen(True) : 99.9609146118%
	  Smile(False) : 99.8329467773%
	  MouthOpen(False) : 98.3746566772%
	  Mustache(False) : 98.7549591064%
	  Beard(False) : 92.758682251%
"""
