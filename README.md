# Rolling Cube
Contains **.sdf file** and a **demonstration video** of the cube model in gazebo.
Download the files **(only robot_v2.sdf is needed)** to a folder and open this folder in terminal and run: 
``bash
ign gazebo robot_v2.sdf``. Gazebo will open up and you can see the cube. Now click on the three dots on the top-right corner and select **Key Publisher**. This plugin allows gazebo to use keyboard signals for cube movements.

Press the **play button** and then use "w" or "s" to rotate the wheel forward or backward. Wait a little before pressing the **opposite direction** key, which will cause the cube to topple in the direction of the initial key press.

(Optional): Open another terminal and use the code ``bash ign topic -e -t /keyboard/keypress`` to get **ASCII** values of the keys you press in Gazebo.
