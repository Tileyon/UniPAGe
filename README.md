# UniPAGe
A Universal Python Adaptable GUI extension

Copyright © 2017 Ti Leyon

## UniPAGe Tutorial
The Universal Python Adaptable GUI Extensions (UniPAGe) 

UniPAGe is a Python module primary designed to execute scripts under the five major computing platforms (MS Windows, OS X, Android, Linux and IOS) without modification to the source. It uses Kivy as a GUI frame in the first four Operating Systems mentioned earlier and Pythonista under IOS. Testing the demo under different OS will make you realize that the “look and feel” is quasi-identical across all targeted platforms. This is because UniPAGe is not just a bridge between Kivy and Pythonista but a fully adaptable GUI framework designed to feel and look the same under all screen resolutions and orientations.

To accomplish this feat UniPAGe had to take into consideration the fundamental differences between the two programming paradigms. First UniPAGe detects the working environment by “trying” to import a Kivy module. If it succeeds it sets a class level boolean variable named “kivy” to “True”. Otherwise it sets its value to “False” and use it to redirect the creation of GUI elements to specific functions and to activate the given instance. To adapt the GUI components to various screen and window resolutions and orientations the module defines a basic view ratio of 800x600 pixels which incidentally is the default resolution under Kivy. The user must be familiar with absolute positioning of the various constituent of the GUI in order to work with the extension. Every interface must be conceptualized at that level before placing the different parts on the main scenery. Each element must be conceived in the context of the 800 by 600 landscape. The extension will automatically adjust their size and that of their sub-components such as text and glyph according to variations in resolution or orientation. Try changing the original frame by modifying the first tuple parameter of the widget variable under the main section to experiment with the adaptability factor. Currently aspect ratios on most devices including desktops vary within a range of 1.33 to 1.88. Although the extension’s base ratio resides a the bottom of that range, surprisingly, it adapts with no excessive distortion to the full range.That is if you are not using basic drawings in the pictures. However, you can always adjust images ratios within the main framework. Test the demo on different devices and judge for yourself. You may also use a technic that reserves only a portion of the screen as the working area and fill the rest with a monotonic or artistic texture. The usable space is computed from the smaller size in perfect proportion to 800x600 resolution. On phones and tablets I often use that technic by forcing the device into portrait mode and use the smaller size as the horizontal definition while computing the vertical size from the first one base on the same 800x600 proportion. That way I can use the keyboard without covering any part of the working area.

To use UniPAGe you must put the functions that create screen elements (unitext, unibutton, unilabel, unimage, uniframe) into variables. Then create a list of tuples to hold the definitions of the screen elements. The first tuple in that list must contain two values that define the horizontal and vertical sizes of the main window. All the other tuples define various screen components. They contain two main elements: the variable holding the function that creates it and a tuple which contains the parameters for that function. These parameters are distributed in the following order: horizontal position, vertical position, width, height and a character string. That string will serve as the text for the component and in the case of an image it indicates the filename of that image. Buttons may contain a sixth optional parameter that refers to its targeted function. If it is omitted the button will be automatically assigned to a dummy function. At that point create an instance of the uniscreen class which itself is a descendent of unipage. That instance is initialized by using the list of tuples decribed above as its parameter. The window is then initialized by calling the setpage method. Use the showpage method to run the application.

Computers are molds that help create digital universes. Operating systems are the gatekeepers of these universes. Programming languages are the keys to open the gates. Python with its numerous free and open source modules and extensions is definitely a golden key. The five components implemented in this first release are used exclusively in 90% of all programs in all platforms excluding games. Other basic structures such as checkmarks, radio buttons, grids and even scroll views can be easily added to UniPAGe since their implementation in kivy and Pythonista are also quite similar. The main structure for games under Pythonista is the “Scene view”. Kivy also comprises a similar structure called scatter. Someone has also developed an entity-based game engine for Kivy called KivEnt. I hope this modest contribution is of use to the reader.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

