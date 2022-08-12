# -*- coding: utf-8 -*-
import sys
import torchvision
import torchvision.transforms as transforms

def prepare_CIFAR(dataset,transform_train,transform_test):
  
  """Downloads and transforms CIFAR-10 and CIFAR-100 datasets. 

  Arguments:
    dataset : Speficies the dataset to be fetched and processed. Takes values 
    'cifar10' or 'cifar100'
    transform_train : A function/transform for training images that takes in an 
    PIL image and returns a transformed version.
    transform_test: A function/transform for testing images that takes in an 
    PIL image and returns a transformed version.

  Usage:

    trainset, testset, num_classes = fetch_CIFAR(dataset = 'cifar10' , ...
                                     transform_train = transforms.Compose(..), ...
                                     transform_test = transforms.Compose(..))
  """

  # Process CIFAR 10 data
  if(dataset == 'cifar10'):
    
    print("| Preparing CIFAR-10 dataset...")
    sys.stdout.write("| ")
    # Download and process train data. The dataset is downloaded at 'root' folder 
    # by default. 
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, 
                                            download=True, transform=transform_train)
    # Download and process test data. Since the dataset is alrady downloaded at 
    # 'root' during the previous step, no need to download it again. 
    testset = torchvision.datasets.CIFAR10(root='./data', train=False, 
                                           download=False, transform=transform_test)
    num_classes = 10
  
  # Process CIFAR 10 data
  elif(dataset == 'cifar100'):
    
    print("| Preparing CIFAR-100 dataset...")
    sys.stdout.write("| ")
    # Download and process train data. The dataset is downloaded at 'root' folder 
    # by default. 
    trainset = torchvision.datasets.CIFAR100(root='./data', train=True, 
                                             download=True, transform=transform_train)
    # Download and process test data. Since the dataset is alrady downloaded at 
    # 'root' during the previous step, no need to download it again. 
    testset = torchvision.datasets.CIFAR100(root='./data', train=False, 
                                            download=False, transform=transform_test)
    num_classes = 100

  else:
    print("ERROR: Incorrect 'dataset' value. Refer to the function help for more details.")  

  return trainset,testset,num_classes



if __name__ == '__main__':
  transform = transforms.Compose([transforms.RandomCrop(32, padding=4),
                                  transforms.RandomHorizontalFlip()])
  
  trainset, testset, num_classes = fetch_CIFAR(dataset = 'cifar10',
                                               transform_train = transform,
                                               transform_test = transform)
  
  print('--------------------------------------------------------------------')
  print('Train Data:', trainset)
