import random
import tqdm
import os
import cv2

dapth = "results/cub200_2/eval/solid"
keep = 0
imsi = 256

steps = os.listdir(dapth)

for step in steps:
	if not os.path.isdir(os.path.join(dapth, step)): continue
	print("Step %s" % step)
	ipth = os.path.join(dapth, step, "images")
	imgs = os.listdir(ipth)
	for img in tqdm.tqdm(imgs):
		impth = os.path.join(ipth, img)
		im = cv2.imread(impth)
		tim = im[:,imsi*keep:imsi*(keep+1)]
		cv2.imwrite(impth, tim)
