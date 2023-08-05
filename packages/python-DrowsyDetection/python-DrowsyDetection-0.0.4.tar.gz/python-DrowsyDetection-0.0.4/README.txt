This library uses deep learning to detect drowsiness of a person

To use it just follow the steps(install tf-nightly also , pip install tf-nightly)

1.  import it in your project
     from DrowsinessDetection.DrowsinessDetector import  drowsiness_detector

2.   initializing the detector
     d = drowsiness_detector()

3.   starting the detector in separate thread
     d.start()

     # your other code .........

