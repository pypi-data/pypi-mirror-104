This library uses deep learning to detect drowsiness of a person

Before using this library make sure you have installed following libraries which are needed

1. Tensorflow ( pip install tensorflow )
2. keras ( pip install keras )
3. pyaudio
4. pyttsx3







To use it just follow the steps

initialize detector inside __name__ == "__main__"  (as for processing frames library will create a new process
so if code will be outside this if condition then in some os like windows script may get stuck in infinite loop) :

1.  import it in your project
     from DrowsinessDetection.DrowsinessDetector import  getDetector

2.   initializing the detector
     d = getDetector()(Audio="path to audio file, completely optional",UseAssistant=True)

3.   starting the detector in separate thread
     d.start()

     # your other code .........

4.   d.join()





 
if you want to listen for  changing state of person then set a callback function 
which will take boolean as argument and this function will get fired every time person drowsy state changes
it will trigger true for sleeping and false for awake

def My_Callback(sleep):
        print("recieved ______________________________________________________"+str(sleep))

d = getDetector()(UseAssistant=True)
d.setCallbackForStateChange(My_Callback)
    



If you programatically want to control the behaviour then there are few apis 

1. for setting sensitivity
     detector.setSensitivity(any integer ) 
2. for closing the detector 
    detector.quit()
3. for observing state changes
   detector.setCallbackForStateChange(My_Callback)
    







 Use Voice Assistant  to control the sensitivity of detector and for quiting

 voice commands are ----->>>
 1.  sensitivity low
 2. sensitivity medium
 3. sensitivity high
 4. quit