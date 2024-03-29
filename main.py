# -*- coding: utf-8 -*-
import string
import configparser
import time
import pickle
import sys
import multiprocessing
import os
from PIL import Image, ImageDraw, ImageFont
import face_recognition
from tqdm import tqdm

print("Initing...")
pbar = tqdm(total=100)
pbar.update(10)
pbar.update(10)
pbar.update(10)
pbar.update(10)
pbar.update(10)
pbar.update(10)
pbar.update(10)
pbar.update(10)
pbar.update(10)
T1 = time.time()
pbar.update(10)
pbar.close()
RunningPath = os.path.split(os.path.realpath(sys.argv[0]))[0]

print("LOADING config....", end="")
cf = configparser.ConfigParser()
cf.read(RunningPath+"\\config.ini")
RemoveThePicture = cf.get("Setting", "RemoveThePicture")
RectangleColour = cf.get("Setting", "RectangleColour")
FontLocation = cf.get("Setting", "FontLocation")
FontColour = cf.get("Setting", "FontColour")
FontSize = cf.get("Setting", "FontSize")
Max_Similarity = cf.get("Setting", "Max_Similarity")
print("[Complete]")


def StrToInt(self, s):
    if s == "":
        return 0
    flag = 1
    wei = 0
    num = 0
    if s[0] in "+-":
        if s[0] == "+":
            flag = flag
        else:
            flag *= -1
        s = s[1:]
    for i in range(len(s)-1, -1, -1):
        if s[i] not in "0123456789":
            return 0
        else:
            num += (ord(s[i]) - 48) * (10 ** wei)
            wei += 1
    return num * flag


def load_known_picture(fileloca):
    known_picture = face_recognition.load_image_file(
        RunningPath+"\\known-picture\\"+fileloca)
    known_encoding = face_recognition.face_encodings(known_picture)[0]
    x = fileloca.split('.', 1)
    name = x[0]
    fl = open(RunningPath+"\\data\\"+name+".dat", 'wb')
    pickle.dump(known_encoding, fl)
    fl.close()
    dirpath = RunningPath+"\\known-picture\\"+fileloca
    os.remove(dirpath)


def load_unknown_picture(known_work):
    image = face_recognition.load_image_file(
        RunningPath+"\\unknown-picture\\"+known_work)
    face_locations = face_recognition.face_locations(image)
    drawObj = Image.fromarray(image)
    d = ImageDraw.Draw(drawObj, 'RGBA')
    file_path = RunningPath+"\\data"
    known_list1 = os.listdir(file_path)
    for face_locations in face_locations:
        top, right, bottom, left = face_locations
        face_image = image[top-10:bottom+10, left-10:right+10]
        unknown_encoding = face_recognition.face_encodings(face_image)[0]
        pos = face_locations
        d.rectangle((pos[3], pos[0], pos[1], pos[2]), outline=RectangleColour)
        d.rectangle((pos[3], pos[0], pos[1], pos[2]), outline=RectangleColour)
        d.rectangle((pos[3], pos[0], pos[1], pos[2]), outline=RectangleColour)
        max = 100
        maxn = -1
        for j in range(len(known_list1)):
            fl = open(RunningPath+"\\data\\"+known_list1[j], "rb")
            known_encoding = pickle.load(fl)
            fl.close()
            face_similar = face_recognition.api.face_distance(
                [known_encoding], unknown_encoding)
            if face_similar < max:
                max = face_similar
                maxn = known_list1[j]
        if max > Max_Similarity:
            maxn = "unknown"
        x = maxn.split('.', 1)
        maxn = x[0]
        self = 0
        Fontsize1 = StrToInt(self, FontSize)
        myfont = ImageFont.truetype(FontLocation, size=Fontsize1)
        fillcolor = "#"+FontColour
        d.text((pos[3], pos[0]), maxn, font=myfont, fill=fillcolor)
    drawObj.save(RunningPath+"\\output\\"+known_work, 'jpeg')


print("LOADING new known pictures....", end="")
file_path = RunningPath+"\\known-picture"
known_list = os.listdir(file_path)
for i in range(len(known_list)):
    load_known_picture(known_list[i])
print("[Complete]")

print("LOADING unknown picture and find faces...")
file_path = RunningPath+"\\unknown-picture"
known_list = os.listdir(file_path)
for i in tqdm(range(len(known_list))):
    load_unknown_picture(known_list[i])
T2 = time.time()
print("[Complete]")

print("Complete in ", T2-T1, " Sec")
print("The final result is in the output floder")
