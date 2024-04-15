# aligned-clip

CLIP is a multi-modal vision and language model. It can be used for image-text similarity and for zero-shot image classification. CLIP uses a ViT like transformer to get visual features and a causal language model to get the text features. In this project, CLIP has been aligned to be used as an Image Classifier. The "ViT-B/32" version of the model has been used.


The model has been trained on the following dataset:
.
The "Indian-Birds-Species-Image-Classification" consists of 25 bird species found in India, including Asian Green Bee-eater, Brown-Headed Barbet, Cattle Egret, Common Kingfisher, Common Myna, Common Rosefinch, Common Tailorbird, Coppersmith Barbet, Forest Wagtail, Gray Wagtail, Hoopoe, House Crow, Indian Grey Hornbill, Indian Peacock, Indian Pitta, Indian Roller, Jungle Babbler, Northern Lapwing, Red-Wattled Lapwing, Ruddy Shelduck, Rufous Treepie, Sarus Crane, White-Breasted Kingfisher, White-Breasted Waterhen, and White Wagtail.
The dataset contains a total of 37,000 images split into train and validation sets in an 80:20 ratio, with 30,000 images in the training set and 7,500 images in the validation set. Each species has 1,500 images in the dataset.

The trained model has then been used for Image classification on the test data of the Birds dataset.
