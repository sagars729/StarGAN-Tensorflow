import argparse
import os

parser = argparse.ArgumentParser(description='Generate Test Results While Training')
parser.add_argument("--models_dir", type=str, required=True)
parser.add_argument("--checkpoint_dir", type=str, required=True)
parser.add_argument("--dataset", type=str, required=True)
parser.add_argument("--selected_attrs", type=str, required=True)
parser.add_argument("--labels", type=str, required=True)
parser.add_argument("--img_size", type=int, default=256)
parser.add_argument("--results_dir", type=str)

parser.add_argument("--base_step", type=int, default=0)
parser.add_argument("--max_step", type=int, default=-1)

args = parser.parse_args()
steps = set()
while True:
	files = os.listdir(args.models_dir)
	files = [int(i[14:-5]) for i in files if i[-5:] == ".meta"]
	files = sorted([i for i in files if i not in steps])
	for s in files:
		if s < args.base_step: continue
		if args.max_step != -1 and s > args.max_step: continue
		steps.add(s)
		print("Step", s)
		os.system("python3 main.py --phase test --dataset %s --img_size %d --selected_attrs %s --checkpoint_dir %s --result_dir %s --custom_label %s --load_step %d" % (args.dataset, args.img_size, args.selected_attrs, args.checkpoint_dir, os.path.join(args.results_dir, str(s)), args.labels, s))
		imgs = os.path.join(args.results_dir, str(s))
		imgs = os.path.join(imgs, os.listdir(imgs)[0], "images")
		print(imgs)
		ims = os.listdir(imgs)
		for f in ims:
			if "real" in f or "fake" in f: os.system("rm %s" % (os.path.join(imgs,f),))
		os.system("mv %s %s" % (imgs, os.path.join(args.results_dir, str(s))))
