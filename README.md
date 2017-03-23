# RTLS
This is a demo visualization software for indoor-location, the GUI was designed and achievw by pyqt.
In this project the loction data was provide by [EKV1000](http://www.decawave.com/products/evk1000-evaluation-kit)
The main location algorithm is geometric localization algorithm.
## Description
this is an demo for indoor-location, you can change the source and apply in your project.
The demo include four parts.
* algorithm
  * Myalgoruthm.py
  in this file there's two classes
  ~~~python
  class JiSuan()
  ~~~
  this class is used for get the final result for the location, you could change the algorithm for
  calculation.
  ~~~python
  class ReadCK()
  ~~~
  this class is used for get the data form equipment.the communication protocol could redesign 
  for your demand.
* uart
  * uart.py
   this file is design for search the equipment that have connect to computer.
* tabs
  * AnchCorrection.py
   this file is design for collect the node coordinates.
  * settingTab.py
   this file is for the basic settings design.
* draw
  * draw.py
   in this file you could define the way how to show the mobile node and define the way for coordinate transformation.
