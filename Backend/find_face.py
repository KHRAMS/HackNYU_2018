
import dlib
from PIL import Image
from skimage import io
import matplotlib.pyplot as plt
import matplotlib.ticker as locator

def detect_faces(image):

    # Create a face detector
    face_detector = dlib.get_frontal_face_detector()

    # Run detector and get bounding boxes of the faces on image.
    detected_faces = face_detector(image, 1)
    face_frames = [(x.left(), x.top(),
                    x.right(), x.bottom()) for x in detected_faces]

    return face_frames

# Load image
img_path = '/home/katchu11/Pictures/murali.jpg'
image = io.imread(img_path)

# Detect faces
detected_faces = detect_faces(image)
#print(detected_faces)
# Crop faces and plot
for n, face_rect in enumerate(detected_faces):
    face = Image.fromarray(image).crop(face_rect)
    plt.subplot(1, len(detected_faces), n+1)
    plt.axis('off')
    ax=plt.gca()
    ax.xaxis.set_major_locator(locator.NullLocator())
    ax.yaxis.set_major_locator(locator.NullLocator())
    plt.imshow(face)
    plt.savefig("detected_face.png",bbox_inches='tight',pad_inches=-0.025)


# In[20]:


img = Image.open("detected_face.png")
basewidth = 48
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('final_user.png')
