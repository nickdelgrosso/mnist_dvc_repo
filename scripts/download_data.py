from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from tqdm import tqdm
from itertools import islice

N = 200

# Download the Data
(trainX, trainy), (testX, testy) = mnist.load_data()


# Merge Training and Test Data (the distinction isn't relevant in this particular demo)
X = np.concatenate((trainX, testX), axis=0)
y = np.concatenate((trainy, testy), axis=0)
X.shape, y.shape

# Convert the Data to individual PNGs and save in the "data/raw" folder
data_dir = Path("./data/raw")
data_dir.mkdir(parents=True, exist_ok=True)
for idx, (img, num) in tqdm(islice(enumerate(zip(X, y)), N)):
    plt.imsave(data_dir.joinpath(f"{idx}_{num}.png"), img)
    