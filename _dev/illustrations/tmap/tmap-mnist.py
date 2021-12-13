""" TMAP Illustration: Visualization of MNIST image data using tmap.
    -------------------------------------------------------------------------------------------------

    Creator: Data Science for Managers - EPFL Program - https://www.dsfm.ch
    Source:  https://github.com/dsfm-org/code-bank.git
    License: MIT License (https://opensource.org/licenses/MIT) - see LICENSE in Code Bank repository. 
    
    Sections of code adapted from: http://tmap.gdb.tools/index.html#ex-mnist 
      under a GNU General Public License v3.0
      
    OVERVIEW:
    
    This illustration is in development. Intended to show a spatial representation of 

"""

import base64
from io import BytesIO

import numpy as np
from faerun import Faerun
from mnist import MNIST
from PIL import Image
from tqdm import tqdm
import os

import tmap as tm

# Load the data
MN = MNIST("./data/mnist-data")
IMAGES_TRAIN, LABELS_TRAIN = MN.load_training()
IMAGES_TEST, LABELS_TEST = MN.load_testing()

IMAGES = np.concatenate((IMAGES_TRAIN, IMAGES_TEST))
LABELS = np.concatenate((LABELS_TRAIN, LABELS_TEST))
IMAGE_LABELS = []

# Coniguration for the tmap layout
CFG = tm.LayoutConfiguration()
CFG.node_size = 1 / 50


def main():
    """ Main function """

    # Initialize and configure tmap
    dims = 1024
    enc = tm.Minhash(dims)
    lf = tm.LSHForest(dims, 128)

    print("Converting images ...")
    for image in tqdm(IMAGES):
        img = Image.fromarray(np.uint8(np.split(np.array(image), 28)))
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        IMAGE_LABELS.append(
            "data:image/bmp;base64," + str(img_str).replace("b'", "").replace("'", "")
        )
    tmp = []
    for _, image in enumerate(IMAGES):
        avg = sum(image) / sum([1 if x > 0 else 0 for x in image])
        tmp.append(tm.VectorUchar([1 if x >= avg else 0 for x in image]))
        # tmp.append(tm.VectorUint(image))

    print("Running tmap ...")
    lf.batch_add(enc.batch_from_binary_array(tmp))
    # LF.batch_add(ENC.batch_from_int_weight_array(tmp))
    lf.index()

    x, y, s, t, _ = tm.layout_from_lsh_forest(lf, CFG)

    faerun = Faerun(clear_color="#111111", view="front", coords=False)
    faerun.add_scatter(
        "MNIST",
        {"x": x, "y": y, "c": LABELS, "labels": IMAGE_LABELS},
        colormap="tab10",
        shader="smoothCircle",
        point_scale=2.5,
        max_point_size=10,
        has_legend=True,
        categorical=True,
    )
    faerun.add_tree(
        "MNIST_tree", {"from": s, "to": t}, point_helper="MNIST", color="#666666"
    )
    faerun.plot("i3d-tmap-mnist", path="outputs", template="url_image")


if __name__ == "__main__":

    if "i3d-tmap-mnist.html" in os.listdir("./outputs"):
        print('MESSAGE: TMAP MNIST output already generated. Go to "outputs" directory.')
    else:
        main()
