import sys
import json
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import faiss
import torch
from torchvision import transforms

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

image_path = sys.argv[1]

model = torch.load("model_test_2_resnet.pt")
model.eval()

val_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
])

with open('im_indices.json') as json_file:
    im_indices = json.load(json_file)

faiss_index = faiss.read_index("faiss_index")

with torch.no_grad():
    im = Image.open(image_path)
    im = im.resize((224, 224))
    im = torch.tensor([val_transforms(im).numpy()]).cuda()

    test_embed = model(im).cpu().numpy()
    _, I = faiss_index.search(test_embed, 5)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    image_to_display = Image.open(im_indices[I[0][0]])
    image_to_display_array = np.array(image_to_display)

    ref_image = Image.open(image_path)
    ref_image_array = np.array(ref_image)

    ax1.imshow(ref_image_array)
    ax1.set_title("reference")

    ax2.imshow(image_to_display_array)
    ax2.set_title("predicted")

    plt.show()