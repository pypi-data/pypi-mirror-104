This library uses deep learning to detect drowsiness of a person

Before using this library make sure you have installed following libraries which are needed

1. Tensorflow ( pip install tensorflow )
2. keras ( pip install keras )
3. pyaudio
4. pyttsx3







To use it just follow the steps

initialize detector inside __name__ == "__main__"  (as for processing frames library will fork a new process
so if code will be outside this if condition then in some os like windows script may get stuck in infinite loop) :

1.  import it in your project
     from DrowsinessDetection.DrowsinessDetector import  drowsiness_detector

2.   initializing the detector
     d = drowsiness_detector()

3.   starting the detector in separate thread
     d.start()

     # your other code .........

4.   d.join()


 Use Voice Assistant  to control the sensitivity of detector and for quiting

 voice commands are ----->>>
 1.  sensitivity low
 2. sensitivity medium
 3. sensitivity high
 4. quit