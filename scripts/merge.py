from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


data_dir = Path("./data/raw")

image_files = list(data_dir.glob("*.png"))

images = []
nums = []
for image_file in image_files:
    num = int(str(image_file)[-5])
    image = plt.imread(image_file)
    im = image[:, :, 0]
    images.append(im)
    nums.append(num)


save_dir = Path("./data/processed")
save_dir.mkdir(exist_ok=True, parents=True)
np.save(save_dir.joinpath("images"), np.array(images))
np.save(save_dir.joinpath("values"), np.array(nums))    
