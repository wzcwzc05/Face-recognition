This is a project based on face_recognition
Please install face_recognition on python before using the project


0.4.0 BETA Upgrade LOG
Details


0.3.1 BETA Upgrade LOG
make the project more safe

0.3.0 BETA Upgrade LOG
We have Windows Edition and a start.exe and install.exe to make sure the program
is useful and we have a chinese using tips now


0.2.5 BETA Upgrade LOG
We have config.ini now!
RectangleColour代表框的颜色
FontLocation代表字体位置
FontColour代表字体颜色
FontSize代表字体大小

THE NEXT EDITION：Provide Windows edition and a install.exe to make the enviroment



0.2.0 BETA Upgrade LOG
Now,in the beginning of the programme, we change the picture into codings and save the in "data" ,
so the next time it don't need to recognize the known picture again.
Also we now provide users a way to enter the picture's filename but of course it should be in the "unknown-picture"

THE　NEXT EDITION:1.We think we should  process all the pictures in the "unknown-picture"
                  2.We may provide more ERROR information for the users


0.1.5 BETA Upgrade LOG
Compared with the last edition,now we can write the final result in the "output.jpg"
In the "output.jpg", you can see every face is on the ground. 
If the face also appear in the "known-picture" it will show its name or it will show "unknown"

ATTENTIONS:1.The unknown picture should be "jpg", I will fixed the problem in the next edition

THE NEXT EDITION:1.Write the face encoding in the files to get higher speed when spotting
                 2.I will provide a tools to change all the known picture into encodings and save in the files



0.1.0 BETA USING TIPS
First,please install python 3 and dlib
Then find face_recognition on github and install

put the known face picture in the "known picture" and pthe picture you want to recognition in the 
"unknown picture" 
then run main.py
the programme will return each value how similar they are.The value is smaller and the two pictures will be more similar.
At last it will print the most similar one in the "known picture"

WARNING:every picture should only have one face or it won't work.
