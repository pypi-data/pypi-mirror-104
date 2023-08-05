This library uses deep learning to detect drowsiness of a person

Before using this library make sure you have installed following libraries which are needed

1. Tensorflow ( pip install tensorflow )
2. keras ( pip install keras )



To use it just follow the steps

1.  import it in your project
     from DrowsinessDetection.DrowsinessDetector import  drowsiness_detector

2.   initializing the detector
     d = drowsiness_detector()

3.   starting the detector in separate thread
     d.start()

     # your other code .........

