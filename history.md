```UniPAGe``` was first published on April 8 2017 as a demonstration of an adaptable graphic user interface between different platforms. It comprises two Python classes that create identical user interfaces in ```Kivy``` and the ```Pythonista UI``` without changes to the source code. This alongside custom scaling routines effectively allows a single script to run on all 5 major operating system environments (MS Windows, Apple OS X and iOS, Android and Linux) without any modification whatsoever. All updates to ```UniPAGe``` will be published under the name unipage_demo followed by a number corresponding to the chronological order of their creation but not a version number per se. This file will describe the evolution of UniPAGe through the modifications of its core classes in lieu of a formal ChangeLog.

unipage_demo.py

* Original release

unipage_demo1.py

* Promoted xratio and yratio to class level variables
* Added the tuple (0, 0) as a base resolution that will automatically compute an "optimal" viewing window for any device.

unipage_demo3.py

    Major release to address many inconsistancies,
    
    omissions and bugs discovered during intensive
    
    testing on multiple devices acrross all covered
    
    platforms (mainly on iOS and Android).
    
* Set the font size for the ```Kivy``` environment to adapt to the current window resolution
* Created Android windows within the full screen resolution in all orientations because the ```Kivy``` environment responded erratically when the window is set directly.
* Fixed font ratio for the textfields in ```Pythonista UI```
* Fixed the automated mode (0, 0) in the ```Pthonista UI``` for all iOS devices to present an "optimal" sheet (Tested on many iPhone and iPad models).
 * Note: I could not locate a reference for the height of the title bar in a sheet presentation in ```Pythonista```. A factor of 90 times the vertical ratios works on all tested devices although not quite optimal on higher resolution gears.
* Made the "closepage()" function independent of the global "mypage" variable so it could be used along with the UniPAGe classes in an external module if so desired.
