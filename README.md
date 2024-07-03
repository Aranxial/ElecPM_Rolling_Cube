# Rolling_Cube
Contains **.sdf file** and a **demonstration video** of the cube model in gazebo.
Download the files to a folder and open this folder in terminal and run: 
``bash
ign gazebo robot_v2.sdf``. Gazebo will open up and you can see the cube. Now click on the three dots on the top-right corner and select **Key Publisher**. This plugin allows gazebo to use keyboard signals for cube movements. Press the **playbutton** and press "w" and "s" for rotating the wheel forward and backward, press one of them, wait a little and press the key for **opposite direction** which causes the cube to topple.

(Optional): Open another terminal and use the code ``bash ign topic -e -t /keyboard/keypress`` to get **ASCII** values of the keys you press in Gazebo.
