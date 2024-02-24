# Smart_Vision_Glasses_for_blind
The aim of this project is to develop a smart lens for visually impaired individuals that can
detect and announce the presence of objects along with their respective distances. The
proposed smart lens will leverage object detection techniques and a speaker to provide users
with real-time feedback about their surroundings, enabling them to navigate more effectively
and safely.
The smart lens will consist of a camera that captures images of the user's surroundings and
sends them to a machine learning model for object detection. The model will analyze the
images and identify any objects that are present, as well as their respective distances. Once an
object has been detected, a speaker will announce the object and its distance to the user in
real-time. The system will be designed to work in a range of environments, including indoors
and outdoors, and will be compact and easy to use. The project consists of one product that
acts as the eyes of the blind and much more. It takes orders and helps them fulfill their desired
tasks.
These features are dependent on each other to communicate and execute actions that suit the
user the best. This product is expected to achieve many tasks that help blind people. It is
expected to act as their eyes and help them in many ways.
The key features of this project include
Obstacle Detection: The smart glasses incorporate advanced computer vision algorithms to
detect obstacles in the user's path, providing real-time alerts and enhancing their mobility and
safety. These glasses will assist users in navigating their surroundings, recognizing objects, and
reading text in real time.
Virtual Assistant: A powerful virtual assistant is integrated into the glasses, enabling users to
ask questions and receive instant responses. From performing calculations and checking
weather forecasts to accessing news headlines, Google Maps locations, music playback,
Wikipedia information, and conducting online searches, the virtual assistant offers a wide
range of functionalities.
By combining these features, the Smart-Vision Glasses project aims to create a comprehensive
and empowering solution for individuals with visual impairments, enhancing their
accessibility, independence, and engagement in various aspects of their daily lives


List of Parts for AI-Based Smart Glasses:
1. Raspberry Pi 4 (4GB variant)
2. USB Camera
3. Microphone
4. LEDs for Night Vision
5. Ultrasonic Sensor
6. Power Bank
7. Push Buttons (3)
8. Various Circuits and Electronics
9. Connecting Wires
10. Headset or Earphones with a 3.5mm jack for audio output
11. Switch (for controlling LEDs)
12. Resistors and Capacitors (as required for pull-up configurations and circuitry)
13. Enclosure for Smart Glasses (3D printed case )
14. Additional Sensors or Components for Future Features


Hardware Connections and Working of the Project:
The project is smart ai based glasses for blind people with components is using a Raspberry Pi 4 4GB 
variant with a camera and microphone and LED's for the night and on the other hand its also using 
ultrasonic sensor and using a power bank to power it up and some push buttons and some circuits and 
other electronics..
So we talk about the connections the camera is connecting through the USB port of the Raspberry Pi 
same with the microphone for the ultrasonic sensor we are using the GPIO PINES of the Raspberry Pi 4 5 
volts for VCC pin. GND to gnd eacho to GPio pin 17 trigger to GPio22 and for the buttons we are using 
the GPio in the pull up configuration button one is connecting to 23gpio button 2 is connected to 
24gpio pin. 
Now let's talk about the working of the project. first we need to power up the glasses after powering up 
we will use the push buttons on the circuit for example when we press button one it will turn on the 
path finding algorithm it use the camera and the ultrasonic sensor to find the path and tell the distance 
between the object it will tell the user about the path and the distance through the audio for that we 
need to connect a earphone to Raspberry Pi from 3.5 mm jack on it. It use the Text to Speech which 
converted text output into speech and user will get to know the path where it need to go right or left 
and this distance from the front object and when we press the button two on the circuit it will it start the 
assistant algorithm which will help the user to tell anything


Hardware Screenshots:


![image](https://github.com/rahull2711/Smart_Vision_Glasses_for_blind/assets/108586386/3e8d7c25-bceb-4a9b-868d-9822d4e67795)

Software Screenshots:


![image](https://github.com/rahull2711/Smart_Vision_Glasses_for_blind/assets/108586386/cb8a8221-ae2c-4bbc-b8f1-fa6a6abe1642)


![image](https://github.com/rahull2711/Smart_Vision_Glasses_for_blind/assets/108586386/040e8dfb-04e6-4a64-84a2-ac5b194294fb)


![image](https://github.com/rahull2711/Smart_Vision_Glasses_for_blind/assets/108586386/32b30422-cff1-40dc-b031-495193abcb1f)


![image](https://github.com/rahull2711/Smart_Vision_Glasses_for_blind/assets/108586386/4841f396-0bbe-4418-90b1-db23b6d7f77b)



