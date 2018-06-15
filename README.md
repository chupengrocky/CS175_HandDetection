# CS175_HandDetection and Gesture Classification
## File Description
Under the src/ is the two main implementation of this project:

## yad2k/ 
        the darknet implemention of hand detection
        the original imagine stored in yad2k/image
        the out put imagines stored in yad2k/images/out
        for more detail see -[Yad2k](https://github.com/allanzelener/YAD2K)

## Transfer-Learning-in-keras/ 
        the implementation of classification on hand gesture
        Start by runing the script transfer_learning_vgg16_custom_data.py
        data are stored in the directory data/
        This model also support transfer_learning in resnet50
        for more detail see -[Transfer_learning](https://github.com/anujshah1003/Transfer-Learning-in-keras---custom-data)

### Installation
```bash
git clone https://github.com/chupengrocky/CS175_HandDetection.git
```
## Requirements

- [Tensorflow](https://www.tensorflow.org/)
- [Numpy](http://www.numpy.org/)
- [h5py](http://www.h5py.org/) (For Keras model serialization.)
- [Pillow](https://pillow.readthedocs.io/) (For rendering test results.)
- [Python 3](https://www.python.org/)
- [pydot-ng](https://github.com/pydot/pydot-ng) (Optional for plotting model.)
