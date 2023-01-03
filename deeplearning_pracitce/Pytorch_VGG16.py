#source: Pytorch Deeplearning. 만들면서 배우는 파이토치 딥러닝
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import torch
import torchvision
from torchvision import models, transforms

print(torch.__version__)

use_pretrained = True
net = models.vgg16(pretrained=use_pretrained)
net.eval()

class BaseTransform():
    def __init__(self,resize,mean,std):
        self.base_transform = transforms.Compose([
            transforms.Resize(resize),
            transforms.CenterCrop(resize),
            transforms.ToTensor(),
            transforms.Normalize(mean,std)
        ])

    def __call__(self,img):
        return self.base_transform(img)

#use image_file_path
img = Image.open(image_file_path)
plt.imshow(img)
plt.show()

resize = 224
mean = (0.485,0.456,0.406)
std = (0.229,0.224,0.225)
transform = BaseTransform(resize,mean,std)
img_transformed = transform(img)

img_transformed = img_transformed.numpy().transpose((1,2,0))
img_transformed = np.clip(img_transformed,0,1)

ILSVRC_class_index = json.load(open('path/imagenet_class_index.json','r'))

class ILSVRCPredictor():
    def __init__(self,class_index):
        self.class_index = class_index
    
    def predict_max(self,out):
        maxid = np.argmax(out.detach().numpy())
        predicted_label_name = self.class_index[str(maxid)][1]
        return predicted_label_name

predictor = ILSVRCPredictor(ILSVRC_class_index)

img = Image.open(image_file_path)
transform = BaseTransform(resize,mean,std)
img_transformed = transform(img)
inputs = img_transformed.unsqueeze_(0)

out = net(inputs)
result = predictor.predict_max(out)

#Transfer Learning

import glob 
import os.path as osp
import random
import numpy as np
import json
from PIL import Image
from tdqm import tdqm
import matplotlib.pyplot as plt

import pytorch
import torch.nn asnn
import torch.optim as optim
import torch.utils.data as data
import torchvision
from torchvision import models,transforms

torch.manual_seed(1234)
np.random.seed(1234)
random.seed(1234)

class ImageTransform():
    def __init__(self,resize,mean,std):
        self.data_transform = {
            'train':transforms.Compose([
                transforms.RandomResizedCrop(
                    resize,scale=(0.5,1.0)),
                    transforms.RandomHorizontalFlip(),
                    transforms.ToTensor(),
                    transforms.Normalize(mean,std)
            ]),
            'val':transforms.Compose([
                transforms.Resize(resize),
                transforms.CenterCrop(resize),
                transforms.ToTensor(),
                transforms.Normalize(mean,std)
            ])
        }

    def __call__(self,img,phase='train'):
        return self.data_transform[phase](img)

def make_datapath_list(phase='train'):
    path_list = []

    for path in glob.glob(target_path):
        path_list.append(path)
    return path_list

train_list = make_datapath_list(phase="train")
val_list = make_datapath_list(phase='val')

class HymenopterDataset(data.Dataset):
    def __init__(self,file_list,transform=None, phase='train'):
        self.file_list = file_list
        self.transform= transform
        self.phase = phase

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self.index):
        img_path = self.file_list[index]
        img = Image.open(img_path)

        img_transformed = self.transform(img,self.phase)

        if self.phase =='train':
            label = img_path[30:34]
        elif self.phase =='val':
            label = img_path[28:32]

        if label == 'ants':
            label = 0
        elif label =="bees":
            label = 1

        return img_transformed,label

train_dataset = HymenopteraDataset(file_list=train_list, transform=ImageTransform(size,mean,std),phase='train')
val_dataset = HymenopteraDataset(file_list=val_list, transform=ImageTransform(size,mean,std),phase='val')

index = 0
print(train_dataset.__getitem__(index)[0].size())
print(train_dataset.__getitem__(index)[1])


#Write a DataLoader

batch_size = 32

train_dataloader = torch.utils.data.DataLoader(
    train_dataset,batch_size = batch_size, shuffle=True)

val_dataloader = torch.utils.data.DataLoader(
    val_dataset,batch_size = batch_size, shuffle=False)

dataloaders_dict = {'train':train_dataloader,'val':val_dataloader}
batch_iterator = iter(dataloaders_dict['train'])
inputs, labels = next(batch_iterator)
print(input_size())
print(labels)

use_pretrained = True
net = models.vgg16(pretrained=use_pretrained)

net.classifier[6] = nn.Linear(in_features=4096, out_features=2)
net.train()

criterion = nn.CrossEntropyLoss()

params_to_update = []
update_param_names = ['classifier.6.weight','classifier.6.bias']

for name, param in net.named_parameters():
    if name in update_param_names:
        param.requires_grad = True
        params_to_update.append(param)
        print(name)
    else:
        param.requires_grad = False

optimizer = optim.SHD(params= params_to_update, lr= 0.01, momentum = 0.9)

def train_model(net, dataloaders_dict, criterion, optimizer,num_epochs):
    for epoch in range(num_epochs):
        print('Epoch{}/{}'.format(epoch+1,num_epochs))
        for phase in ['train','val']:
            if phase == 'train':
                net.train()
            else:
                net.eval()
            epoch_loss = 0.0
            epoch_corrects = 0

        if (epoch ==0) and (phase='train'):
            continue
        for inputs, labels in tdqm(dataloaders_dict[phase]):
            optimizer.zero_grad()
            with torch.set_grad_enabled(phase='train'):
                outputs = net(inputs)
                loss = criterion(outputs,labels)
                _, preds = torch.max(outputs,1)

                if phase == 'train':
                    loss.backward()
                    optimizer.step()

                epoch_loss += loss.item()*inputs.size(0)
                epoch_corrects += torch.sum(preds==labels.data)

                epoch_loss = epoch_loss/len(dataloaders_dict[phase].dataset)
                epoch_acc = epoch_corrects.double()/len(dataloaders_dict[phase].dataset)

                print('{} Loss : {:.4f} Acc: {:.4f}'.format(phase,epoch_loss,epoch_acc))

num_epochs=2
train_model(net, dataloaders_dict,criterion,optimizer, num_epochs=num_epochs)
