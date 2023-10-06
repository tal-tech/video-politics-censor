from algorithm.src.demo import Interface
import os
import cv2

def frame(input):
    cmd = "ffmpeg -i {} -vf fps=1 images/out%d.jpg".format(input)
    os.system(cmd)



if __name__ == "__main__":
    input = 'input.mp4'
    frame(input)

    gallery_dir = "algorithm/examples/multi_gallery"
    interface = Interface(gallery_dir)

    folder_path = 'images'
    image_extensions = ['jpg', 'png', 'jpeg']  # 可以添加更多扩展名

    for filename in os.listdir(folder_path):
        if any(filename.endswith(ext) for ext in image_extensions):
            img = cv2.imread(os.path.join(folder_path, filename))
            print(interface.query(img,0))
    