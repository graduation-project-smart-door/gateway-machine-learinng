from datetime import datetime
import cv2
import os

# Resizes a image and maintains aspect ratio
def maintain_aspect_ratio_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # Grab the image size and initialize dimensions
    dim = None
    (h, w) = image.shape[:2]

    # Return original image if no need to resize
    if width is None and height is None:
        return image

    # We are resizing height if width is none
    if width is None:
        # Calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # We are resizing width if height is none
    else:
        # Calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # Return the resized image
    return cv2.resize(image, dim, interpolation=inter)

def video_to_frames(path):
     video_capture = cv2.VideoCapture()
     video_capture.open(path)
     fps = video_capture.get(cv2.CAP_PROP_FPS) 
     frames = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
     print("fps=", int(fps), "frames=", int(frames))

     for i in range(int(frames)):
          _, frame = video_capture.read()
          frame = maintain_aspect_ratio_resize(frame, width=224)
          if i % 2 == 0:
            cv2.imwrite("frames/%d.jpg"%(i), frame)


def start_make_frames(path: str):
    t1 = datetime.now()
    video_to_frames(path)
    t2 = datetime.now()
    print("Time cost = ", (t2 - t1))