This file lists some randomness factors which could make the reproduced solution perform slightly different from the winning submission.
- Environments or hardware: should be negligible
- YOLOX training: I use [official YOLOX repository](https://github.com/Megvii-BaseDetection/YOLOX) to train breast ROI detection model. Unfortunately, the code is currently unreproducible between different experiments, even when using same config and `seed` used. The issue is mentioned [here](https://github.com/Megvii-BaseDetection/YOLOX/issues/1612). I did not notice this randomness until the competition ended. So, i think it's pretty hard to reproduce the exact YOLOX model used in the winning submission (we need to guess some random numbers?).
- Converting model from Torch to TensorRT would introduce small performance changes. But I expect these change to be also negligible