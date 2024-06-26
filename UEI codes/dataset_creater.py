import sqlite3
import cv2
import numpy as np

faceDetection=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

def insertUpdate(id,name,age):

    conn=sqlite3.connect("mydatabase.db")
    command="SELECT * FROM STUDENTS WHERE ID="+str(id)
    cursor=conn.execute(command)

    isRecordExist=0

    # for row in cursor:

