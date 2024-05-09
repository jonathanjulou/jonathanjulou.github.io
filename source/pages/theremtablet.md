[starttextbox]
[startgrid]
### Tablet Theremin
[startparagraph]

Input is handled using the x and y coordinates returned by the pyglet handle for the tablet. Pyglet is also used for display of the UI. Articulation is controlled using the keyboard. X axis controls pitch and y axis controls volume.


For audio generation the sounddevice library is used, with custom waveforms fed as binary sequences of intensities at sample rate. A custom sound generator was required as midi didn't allow properly continuous sound generation in real time.


The code can be found here : <a href=https://github.com/jonathanjulou/tablet-theremin>https://github.com/jonathanjulou/tablet-theremin</a>


[endparagraph]

[video](images/projects/ThereminTablet/outablette.mp4)


[startparagraph]







[endparagraph]

[endgrid]

[endtextbox]
