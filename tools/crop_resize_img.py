import os
import cv2

def center_crop(img_array, crop_size=-1, resize=-1, write_path=None):
	##从中心区域裁剪并调整正方形图像的大小。
	rows = img_array.shape[0]
	cols = img_array.shape[1]

	if crop_size==-1 or crop_size>max(rows,cols):
		crop_size = min(rows, cols)
	row_s = max(int((rows-crop_size)/2), 0)
	row_e = min(row_s+crop_size, rows) 
	col_s = max(int((cols-crop_size)/2), 0)
	col_e = min(col_s+crop_size, cols)

	img_crop = img_array[row_s:row_e,col_s:col_e,]

	if resize>0:
		img_crop = cv2.resize(img_crop, (resize, resize))

	if write_path is not None:
		cv2.imwrite(write_path, img_crop)
	return img_crop 


def crop_img_dir(img_dir,  save_dir, crop_method = "center"):
	##裁剪原始图像保存到img_dir中

	img_names = os.listdir(img_dir)
	img_names = [img_name for img_name in img_names if img_name.split(".")[-1]=="png"]
	index = 0
	for img_name in img_names:
		img = cv2.imread(os.path.join(img_dir, img_name))
		img_out_path = os.path.join(save_dir, img_name)
		if crop_method == "center":
			img_crop = center_crop(img, resize=640, write_path=img_out_path)
		if index%100 == 0:
			print ("total images number = ", len(img_names), "current image number = ", index)
		index += 1
		



if __name__ == "__main__":
	img_dir = "/home/xiao5/Desktop/Traffic_sign_recognition/data/train_images/PNGImages"
	save_dir = "/home/xiao5/Desktop/Traffic_sign_recognition/data/realTrain/PNGImages"
	crop_img_dir(img_dir, save_dir)
	

