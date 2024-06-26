import os 
import pandas as pd
import torchvision.io as read_image

# UNFINISHED

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None,
        target_transform=None):
        self.img_labels = pd.read_csv("abalone.data")
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_label)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        
        if self.target_transform:
            label = self.target_transform(label)
        
        return image, label
    