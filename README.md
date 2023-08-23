# FL-Development

<h4 align="center"><i>This is a repo for implementing federated learning (FL) simulation studies in healthcare.</i></h4>



## SOTA FL Algorithms by Year 📚 (updating)

### 2017

- ***FedAvg*** -- [Communication-Efficient Learning of Deep Networks from Decentralized Data](https://arxiv.org/abs/1602.05629) (AISTATS'17)


### 2019

- ***FedMD*** -- [FedMD: Heterogenous Federated Learning via Model Distillation](http://arxiv.org/abs/1910.03581) (NIPS'19)

- ***FedAvgM*** -- [Measuring the Effects of Non-Identical Data Distribution for Federated Visual Classification](https://arxiv.org/abs/1909.06335) (ArXiv'19)

- ***CFL*** -- [Clustered Federated Learning: Model-Agnostic Distributed Multi-Task Optimization under Privacy Constraints](https://arxiv.org/abs/1910.01991) (ArXiv'19)


### 2020

- ***FedProx*** -- [Federated Optimization in Heterogeneous Networks](https://arxiv.org/abs/1812.06127) (MLSys'20)

- ***SCAFFOLD*** -- [SCAFFOLD: Stochastic Controlled Averaging for Federated Learning](https://arxiv.org/abs/1910.06378) (ICML'20)

- ***FedPer*** -- [Federated Learning with Personalization Layers](http://arxiv.org/abs/1912.00818) (AISTATS'20)

- ***Per-FedAvg*** -- [Personalized Federated Learning with Theoretical Guarantees: A Model-Agnostic Meta-Learning Approach](https://proceedings.neurips.cc/paper/2020/hash/24389bfe4fe2eba8bf9aa9203a44cdad-Abstract.html) (NIPS'20)


### 2021

- ***MOON*** -- [Model-Contrastive Federated Learning](http://arxiv.org/abs/2103.16257) (CVPR'21)

- ***FedBN*** -- [FedBN: Federated Learning On Non-IID Features Via Local Batch Normalization](http://arxiv.org/abs/2102.07623) (ICLR'21)

- ***FedGen*** -- [Data-Free Knowledge Distillation for Heterogeneous Federated Learning](https://arxiv.org/abs/2105.10056) (ICML'21)

- ***Ditto*** -- [Ditto: Fair and Robust Federated Learning Through Personalization](http://arxiv.org/abs/2012.04221) (ICML'21)

- ***pFedHN*** -- [Personalized Federated Learning using Hypernetworks](http://arxiv.org/abs/2103.04628) (ICML'21)


### 2022

- ***FedLC*** -- [Federated Learning with Label Distribution Skew via Logits Calibration](http://arxiv.org/abs/2209.00189) (ICML'22)

- ***pFedLA*** -- [Layer-Wised Model Aggregation for Personalized Federated Learning](https://openaccess.thecvf.com/content/CVPR2022/html/Ma_Layer-Wised_Model_Aggregation_for_Personalized_Federated_Learning_CVPR_2022_paper.html) (CVPR'22)

- ***FedAP*** -- [Personalized Federated Learning with Adaptive Batchnorm for Healthcare](https://arxiv.org/abs/2112.00734) (IEEE'22)

- ***kNN-Per*** -- [Personalized Federated Learning through Local Memorization](http://arxiv.org/abs/2111.09360) (ICML'22)

- ***MetaFed*** -- [MetaFed: Federated Learning among Federations with Cyclic Knowledge Distillation for Personalized Healthcare](http://arxiv.org/abs/2206.08516) (IJCAI'22)






## Environment Requirements 🛠

<!-- - `Python = 3.10`
- `PyToch = 1.13` -->

```
pip install -r requirements.txt
```


### Docker 🐳
Coming soon...



## Dataset Partition 📂
This part aims to divide the entire datasets into Non-IID datasets according to the number of clients and the partition scheme (Dirichlet distribution). 

```shell
# partition the MedMNIST dataset into 10 clients according to Dirichlet distribution with alpha=0.1
python generate_data.py -d medmnistS -a 0.1 -cn 10
```



## Run FL Simulation 🏃‍♂️

```shell
# run FedAvg simulation on MedMNIST dataset
python fedavg.py -d medmnistS
```

- `Note`: ALL the methods are inherited from `FedAvgServer` and `FedAvgClient`.
- please check [arguments_detail](arguments_detail.md) for more details. 





## Supported Tasks 📝

- [x] Classification
- [ ] Reconstruction (coming soon...)
- [ ] Segmentation (coming soon...)



## Supported Medical Datasets 🎨

- [*MedMNIST*](https://medmnist.com/) 

- [*COVID-19*](https://www.researchgate.net/publication/344295900_Curated_Dataset_for_COVID-19_Posterior-Anterior_Chest_Radiography_Images_X-Rays) 

- [*NIH Chest X-ray 14*](https://www.kaggle.com/nih-chest-xrays/data) 

- [*FeTS 2022*](https://www.synapse.org/#!Synapse:syn28546456/wiki/617246) (coming soon...)



## To-Do List 📝

- [ ] support more medical datasets
- [ ] support more SOTA FL methods
- [ ] support more tasks
- [ ] docker support
- [ ] pre-trained weights
- [ ] ...



<!-- ## Reference 📚 -->


