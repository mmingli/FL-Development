import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import numpy as np
from collections import OrderedDict

"""
We support the following models:
    - AlexNet model customized for CIFAR-10 (AlexCifarNet) with 1756426 parameters
    - LeNet model customized for MNIST with 61706 parameters
    - Further ResNet models
    - Further Vgg models
"""


# AlexNet model customized for CIFAR-10 with 1756426 parameters
class AlexCifarNet(nn.Module):
    supported_dims = {32}

    def __init__(self):
        super(AlexCifarNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=5, stride=1, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
            nn.LocalResponseNorm(4, alpha=0.001 / 9.0, beta=0.75, k=1),
            nn.Conv2d(64, 64, kernel_size=5, stride=1, padding=2),
            nn.ReLU(inplace=True),
            nn.LocalResponseNorm(4, alpha=0.001 / 9.0, beta=0.75, k=1),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
        )
        self.classifier = nn.Sequential(
            nn.Linear(4096, 384),
            nn.ReLU(inplace=True),
            nn.Linear(384, 192),
            nn.ReLU(inplace=True),
            nn.Linear(192, 10),
        )

    def forward(self, x):
        out = self.features(x)
        out = out.view(out.size(0), 4096)
        out = self.classifier(out)
        return out


# LeNet model customized for MNIST with 61706 parameters
class LeNet(nn.Module):
    supported_dims = {28}

    def __init__(self, num_classes=10, in_channels=1):
        super(LeNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, 6, 5, padding=2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, num_classes)

    def forward(self, x):
        out = F.relu(self.conv1(x), inplace=True)  # 6 x 28 x 28
        out = F.max_pool2d(out, 2)  # 6 x 14 x 14
        out = F.relu(self.conv2(out), inplace=True)  # 16 x 7 x 7
        out = F.max_pool2d(out, 2)   # 16 x 5 x 5
        out = out.view(out.size(0), -1)  # 16 x 5 x 5
        out = F.relu(self.fc1(out), inplace=True)
        out = F.relu(self.fc2(out), inplace=True)
        out = self.fc3(out)

        return out


# Further ResNet models
def generate_resnet(num_classes=10, in_channels=1, model_name="ResNet18"):
    if model_name == "ResNet18":
        model = models.resnet18(pretrained=True)
    elif model_name == "ResNet34":
        model = models.resnet34(pretrained=True)
    elif model_name == "ResNet50":
        model = models.resnet50(pretrained=True)
    elif model_name == "ResNet101":
        model = models.resnet101(pretrained=True)
    elif model_name == "ResNet152":
        model = models.resnet152(pretrained=True)
    model.conv1 = nn.Conv2d(in_channels, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
    fc_features = model.fc.in_features
    model.fc = nn.Linear(fc_features, num_classes)

    return model


# Further Vgg models
def generate_vgg(num_classes=10, in_channels=1, model_name="vgg11"):
    if model_name == "VGG11":
        model = models.vgg11(pretrained=False)
    elif model_name == "VGG11_bn":
        model = models.vgg11_bn(pretrained=True)
    elif model_name == "VGG13":
        model = models.vgg11(pretrained=False)
    elif model_name == "VGG13_bn":
        model = models.vgg11_bn(pretrained=True)
    elif model_name == "VGG16":
        model = models.vgg11(pretrained=False)
    elif model_name == "VGG16_bn":
        model = models.vgg11_bn(pretrained=True)
    elif model_name == "VGG19":
        model = models.vgg11(pretrained=False)
    elif model_name == "VGG19_bn":
        model = models.vgg11_bn(pretrained=True)

    # first_conv_layer = [nn.Conv2d(1, 3, kernel_size=3, stride=1, padding=1, dilation=1, groups=1, bias=True)]
    # first_conv_layer.extend(list(model.features))
    # model.features = nn.Sequential(*first_conv_layer)
    # model.conv1 = nn.Conv2d(num_classes, 64, 7, stride=2, padding=3, bias=False)

    fc_features = model.classifier[6].in_features
    model.classifier[6] = nn.Linear(fc_features, num_classes)

    return model


class CNN(nn.Module):
    def __init__(self, num_classes=10, in_channels=1):
        super(CNN, self).__init__()

        self.fp_con1 = nn.Sequential(OrderedDict([
            ('con0', nn.Conv2d(in_channels=in_channels, out_channels=32, kernel_size=3, padding=1)),
            ('relu0', nn.ReLU(inplace=True)),
            ]))

        self.ternary_con2 = nn.Sequential(OrderedDict([
            # Conv Layer block 1
            ('conv1', nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1, bias=False)),
            ('norm1', nn.BatchNorm2d(64)),
            ('relu1', nn.ReLU(inplace=True)),
            ('pool1', nn.MaxPool2d(kernel_size=2, stride=2)),

            # Conv Layer block 2
            ('conv2', nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1, bias=False)),
            ('norm2', nn.BatchNorm2d(128)),
            ('relu2', nn.ReLU(inplace=True)),
            ('conv3', nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1, bias=False)),
            ('norm3', nn.BatchNorm2d(128)),
            ('relu3', nn.ReLU(inplace=True)),
            ('pool2', nn.MaxPool2d(kernel_size=2, stride=2)),
            # nn.Dropout2d(p=0.05),

            # Conv Layer block 3
            ('conv3', nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1, bias=False)),
            ('norm3', nn.BatchNorm2d(256)),
            ('relu3', nn.ReLU(inplace=True)),
            ('conv4', nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1, bias=False)),
            ('norm4', nn.BatchNorm2d(256)),
            ('relu4', nn.ReLU(inplace=True)),
            ('pool4', nn.MaxPool2d(kernel_size=2, stride=2)),
        ]))

        self.fp_fc = nn.Linear(4096, num_classes, bias = False)

    def forward(self, x):
        x = self.fp_con1(x)
        x = self.ternary_con2(x)
        x = x.view(x.size(0), -1)
        x = self.fp_fc(x)
        output = F.log_softmax(x, dim=1)
        return output



class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()

        def conv_block(in_channels, out_channels):
            return nn.Sequential(
                nn.Conv2d(in_channels, out_channels, 3, padding=1),
                nn.ReLU(inplace=True),
                nn.Conv2d(out_channels, out_channels, 3, padding=1),
                nn.ReLU(inplace=True)
            )

        self.encoder1 = conv_block(1, 64)
        self.encoder2 = conv_block(64, 128)
        self.encoder3 = conv_block(128, 256)
        self.encoder4 = conv_block(256, 512)

        self.pool = nn.MaxPool2d(2)
        self.up = nn.ConvTranspose2d(512, 512, kernel_size=2, stride=2)

        self.decoder3 = conv_block(256 + 512, 256)
        self.decoder2 = conv_block(128 + 256, 128)
        self.decoder1 = conv_block(128 + 64, 64)
        
        self.final_conv = nn.Conv2d(64, 1, 1)

    def forward(self, x):
        enc1 = self.encoder1(x)
        enc2 = self.encoder2(self.pool(enc1))
        enc3 = self.encoder3(self.pool(enc2))
        enc4 = self.encoder4(self.pool(enc3))

        dec3 = self.decoder3(torch.cat([self.up(enc4), enc3], dim=1))
        dec2 = self.decoder2(torch.cat([self.up(dec3), enc2], dim=1))
        dec1 = self.decoder1(torch.cat([self.up(dec2), enc1], dim=1))

        return self.final_conv(dec1)



if __name__ == "__main__":
    model_name_list = ["ResNet18", "ResNet34", "ResNet50", "ResNet101", "ResNet152"]
    for model_name in model_name_list:
        model = generate_resnet(num_classes=10, in_channels=1, model_name=model_name)
        # model_parameters = filter(lambda p: p.requires_grad, model.parameters())
        # param_len = sum([np.prod(p.size()) for p in model_parameters])
        param_len = sum(p.numel() for p in model.parameters() if p.requires_grad)
        print('Number of model parameters of %s :' % model_name, ' %d ' % param_len)
        
        # another way to calculate the model size
        size = sum(p.numel() for p in model.parameters() if p.requires_grad) / 1_024**2
        print(f"Model size: {size:.3f} MB")

    # model = UNet()
    # size = sum(p.numel() for p in model.parameters() if p.requires_grad) / 1_024**2
    # logits_size = sum(p.numel() for name, p in model.named_parameters() if name.startswith('final_conv') and p.requires_grad) / 1_024**2
    # print(f"Model size: {size:.3f} MB")
    # print(f"logits size: {size:.3f} MB")
