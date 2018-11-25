
import tkinter
from tkinter import *
from tkinter import filedialog,messagebox


import cv2
import threading
import PIL.Image, PIL.ImageTk
import imutils
import multiprocessing
import numpy as np


from imutils import contours
class App():
    def __init__(self,):

        self.vs=cv2.VideoCapture(0)
        self.root=tkinter.Tk()
        self.panel = None
        self.panel2 = None
        self.panel3 = None
        self.panel4 = None

        self.var = IntVar()
        self.var1 = IntVar()
        self.var2 = IntVar()

        self.varMax = IntVar()
        self.varMax2 = IntVar()
        self.varMax3 = IntVar()
        self.varMax4 = IntVar()
        self.varMax5 = IntVar()

        self.rectY = IntVar()
        self.rectX = IntVar()
        self.sqY = IntVar()
        self.sqX = IntVar()
        self.treshImg = None
        self.ImgCap = None

        self.HeightBbox = None
        self.WeightBbox = None

        self.Detect_flag = 0
        self.frameShow = None
        self.ROI=None
        self.ROIFIX=None

        self.frame = None
        self.thread = None
        self.imgOrigin = None
        self.stopEvent = None
        self.ClickValue = 0
        self.stopEvent = threading.Event()

        self.page1_selectOption()
    def scale(self):

        scale = Scale(self.root, from_=0, to=255, variable=self.var,label="B")
        scale.set(0)
        scale1 = Scale(self.root, from_=0, to=255, variable=self.var1,label="G")
        scale1.set(0)
        scale2 = Scale(self.root, from_=0, to=255, variable=self.var2,label="R")
        scale2.set(80)
        scale.grid(row=0,column=4,)
        scale1.grid(row=0,column=5)
        scale2.grid(row=0,column=6)
    def scale2(self):

        scale = Scale(self.root, from_=0, to=255, variable=self.varMax)
        scale.set(255)
        scale1 = Scale(self.root, from_=0, to=255, variable=self.varMax2)
        scale1.set(255)
        scale2 = Scale(self.root, from_=0, to=255, variable=self.varMax3)
        scale2.set(255)
        scale3=Scale(self.root,from_=0, to=255,variable=self.varMax4,orient=tkinter.HORIZONTAL)
        scale3.set(90)
        scale4 = Scale(self.root, from_=0, to=255, variable=self.varMax5, orient=tkinter.HORIZONTAL)
        scale4.set(83)
        scale.grid(row=0, column=4)
        scale1.grid(row=0, column=5)
        scale2.grid(row=0, column=6)
        scale3.grid(row=0,column=7)
        scale4.grid(row=0,column=8)

    def scale2_1(self):
        scale4 = Scale(self.root, from_=0, to=255, variable=self.varMax5, orient=tkinter.HORIZONTAL)
        scale4.set(self.varMax5.get())
        scale4.grid(row=0, column=8)
    def scale3(self):
        #moregrap scale 20 10 18 10

        scale=Scale(self.root,from_=5,to=100,variable=self.rectY)
        scale.set(20)
        scale1=Scale(self.root,from_=5,to=100,variable=self.rectX)
        scale1.set(10)
        scale2=Scale(self.root,from_=5,to=100,variable=self.sqY)
        scale2.set(18)
        scale3=Scale(self.root,from_=5,to=100,variable=self.sqX)
        scale3.set(10)
        scale.grid(row=1, column=4)
        scale1.grid(row=1, column=5)
        scale2.grid(row=1, column=6)
        scale3.grid(row=1, column=7)
    def Show_panel01_0_0(self, img):
        try:
            img = imutils.resize(img, width=150, height=100)
        except:
            img = img
        img = PIL.Image.fromarray(img)
        img = PIL.ImageTk.PhotoImage(img)
        if self.panel is None:
            self.panel = tkinter.Label(image=img)
            self.panel.image = img
            self.panel.grid(row=0, column=0)
        else:
            self.panel.configure(image=img)
            self.panel.image = img
    def Show_panel02_0_1(self,img):
        try: img = imutils.resize(img, width=150, height=100)
        except: img=img
        img = PIL.Image.fromarray(img)
        img = PIL.ImageTk.PhotoImage(img)
        if self.panel2 is None:
            self.panel2 = tkinter.Label(image=img)
            self.panel2.image = img
            self.panel2.grid(row=0, column=1)
        else:
            self.panel2.configure(image=img)
            self.panel2.image = img
    def Show_panel03_1_0(self,img):
        try: img = imutils.resize(img, width=150, height=100)
        except: img=img
        img = PIL.Image.fromarray(img)
        img = PIL.ImageTk.PhotoImage(img)
        if self.panel3 is None:
            self.panel3 = tkinter.Label(image=img)
            self.panel3.image = img
            self.panel3.grid(row=1, column=0)
        else:
            self.panel3.configure(image=img)
            self.panel3.image = img
    def Show_panel04_1_1(self,img):
        try: img = imutils.resize(img, width=150, height=100)
        except: img=img
        img = PIL.Image.fromarray(img)
        img = PIL.ImageTk.PhotoImage(img)
        if self.panel4 is None:
            self.panel4 = tkinter.Label(image=img)
            self.panel4.image = img
            self.panel4.grid(row=1, column=1)
        else:
            self.panel4.configure(image=img)
            self.panel4.image = img
    def Save_Bbox(self,h,w):
        self.HeightBbox=h
        self.WeightBbox=w

    def Reset_Bbox(self):
        self.HeightBbox = None
        self.WeightBbox = None
    def Click_ValueBbox(self):
        self.ClickValue=5
    def save_ref(self):
        if not self.ROI is None:
            cv2.imwrite('./Ref/temp01.png', img=self.ROI[0])
            cv2.imwrite('./Ref/temp02.png', img=self.ROI[1])
            cv2.imwrite('./Ref/temp03.png', img=self.ROI[2])

    def load_ref(self):
        self.ROIFIX[0]=cv2.imread("./Ref/temp01.png",0)
        self.ROIFIX[1] = cv2.imread("./Ref/temp02.png", 0)
        self.ROIFIX[2] = cv2.imread("./Ref/temp03.png", 0)
    def page1_selectOption(self):
        self.root.geometry('800x480')
        self.root.title("Start page")
        defaultButton=Button(self.root,text='Default').grid(row=1,column=1,columnspan=2, rowspan=2,sticky=W+N+E+S)
        setingtButton = Button(self.root, text='Setting',command=self.setting_page).grid(row=1, column=3,columnspan=2, rowspan=2,sticky=W+N+E+S)
    def setting_page(self):
        self.ClickValue=1
        for ele in self.root.winfo_children():
            ele.destroy()
        self.root.title("Setting Video Capture")
        self.scale()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.daemon = True
        self.thread.start()
        BboxSaveButton = Button(self.root, text="Target Area", command=self.Click_ValueBbox).grid(row=1, column=2)
        ResetBboxSaveButton = Button(self.root, text="Reset", command=self.Reset_Bbox).grid(row=2, column=2)
        OkNextButton = Button(self.root, text="OK and Next", command=self.page2_to_page3).grid(row=3, column=3)
    def page2_to_page3(self):
        Msg = messagebox.askyesno("Save and Next", "Save target Area and Other setting")
        if Msg == True:
            self.panel = None
            Area_configre_H = open('./Configure/AreaH.txt', "w")
            Area_configre_H.write(str(self.HeightBbox))
            Area_configre_H.close()
            Area_configre_W = open('./Configure/AreaW.txt', "w")
            Area_configre_W.write(str(self.WeightBbox))
            Area_configre_W.close()
            B_scale = open('./Configure/B_scale.txt', "w")
            B_scale.write(str(self.var.get()))
            B_scale.close()
            G_scale = open('./Configure/G_scale.txt', "w")
            G_scale.write(str(self.var1.get()))
            G_scale.close()
            R_scale = open('./Configure/R_scale.txt', "w")
            R_scale.write(str(self.var2.get()))
            R_scale.close()
            self.ClickValue = 2
            self.page3_setting_roi()
    def page3_setting_roi(self):
        self.ClickValue = 2
        for ele in self.root.winfo_children():
            ele.destroy()
        self.panel = None
        self.panel2 = None
        self.panel3 = None
        self.panel4=None
        self.root.title("Setting ROI")
        if self.thread.isAlive() == True:
            print("thread Alive")
            self.scale2()
            self.scale3()
            # self.scale4()
            self.TextocrThread = threading.Thread(target=self.roi_setting, args=())
            self.TextocrThread.daemon = True
            self.TextocrThread.start()
            #savebutton=Button(self.root, text="Save roi", command=self.page3_to_page4).grid(row=3, column=3)
            OkNextButton = Button(self.root, text="OK and Next", command=self.page3_to_page4).grid(row=3, column=3)
    def page3_to_page4(self):
        Msg = messagebox.askyesno("Save and Next", "Save Value and Other setting")
        if Msg == True:
            self.ClickValue = 3
            B_scale2 = open('./Configure/B_scale2.txt', "w")
            B_scale2.write(str(self.varMax.get()))
            B_scale2.close()
            G_scale2 = open('./Configure/G_scale2.txt', "w")
            G_scale2.write(str(self.varMax2.get()))
            G_scale2.close()
            R_scale2 = open('./Configure/R_scale2.txt', "w")
            R_scale2.write(str(self.varMax3.get()))
            R_scale2.close()
            R_scale2_min_for_Imgtocrop = open('./Configure/R_scale2_for_Imgtocrop.txt', "w")
            R_scale2_min_for_Imgtocrop.write(str(self.varMax4.get()))
            R_scale2_min_for_Imgtocrop.close()
            R_scale2_min_for_ImgWarp = open('./Configure/R_scale2_for_ImgWarp.txt', "w")
            R_scale2_min_for_ImgWarp.write(str(self.varMax5.get()))
            R_scale2_min_for_ImgWarp.close()

            rectY = open('./Configure/rectY.txt', 'w')
            rectY.write(str(self.rectY.get()))
            rectY.close()
            rectX = open('./Configure/rectX.txt', 'w')
            rectX.write(str(self.rectX.get()))
            rectX.close()
            sqY = open('./Configure/sqY.txt', 'w')
            sqY.write(str(self.sqY.get()))
            sqY.close()
            sqX = open('./Configure/sqX.txt', 'w')
            sqX.write(str(self.sqX.get()))
            sqX.close()
            self.ClickValue = 3
            self.page4_save_roi()
    def page4_save_roi(self):
        self.ClickValue = 3
        for ele in self.root.winfo_children():
            ele.destroy()
        self.panel = None
        self.panel2 = None
        self.panel3 = None
        self.panel4=None
        self.scale2_1()
        savebutton=Button(self.root,text="Save").grid(row=1,column=3)
    def videoLoop(self):
        self.ret, self.frame = self.vs.read()
        self.detectThread = threading.Thread(target=self.detect, args=())
        self.detectThread.daemon = True
        self.detectThread.start()

        try:
            while not self.stopEvent.is_set():
                self.ret,self.frame=self.vs.read()
                image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                self.frameShow=image
                if self.ClickValue==1:

                    self.Show_panel01_0_0(self.frameShow)
        except RuntimeError as e:
            print("error runtime")
            self.vs.release()
    def detect(self):

        while not self.stopEvent.is_set():


                image = self.frame
                image_center = (image.shape[0] / 2, image.shape[1] / 2)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
                gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
                gradient = cv2.subtract(gradX, gradY)
                gradient = cv2.convertScaleAbs(gradient)

                Imin = np.array([self.var.get(), self.var1.get(),self.var2.get()], dtype='uint8')
                Imax = np.array([255,255, 255], dtype='uint8')
                hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                masks = cv2.inRange(hsv, Imin, Imax)
                blurred = cv2.blur(masks, (1, 1))



                (_, thresh) = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY_INV)

                rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))
                sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
                tophat = cv2.morphologyEx(thresh, cv2.MORPH_TOPHAT, rectKernel)
                np.seterr(divide='ignore', invalid='ignore')
                gradX = cv2.Sobel(tophat, ddepth=cv2.CV_64F, dx=1, dy=0,
                                  ksize=7)
                gradX = np.absolute(gradX)
                (minVal, maxVal) = (np.min(gradX), np.max(gradX))
                gradX = (255 * ((gradX - minVal) / (maxVal - minVal)))
                gradX = gradX.astype("uint8")

                gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
                thresh = cv2.threshold(gradX, 0, 255,
                                       cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
                thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)

                clone01 = np.dstack([thresh.copy()] * 3)
                self.treshImg=clone01

                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (55, 57))
                closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
                closed = cv2.erode(closed, None, iterations=4)
                closed = cv2.dilate(closed, None, iterations=4)



                _,cnts, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                _,cnts2,hierarchy2 = cv2.findContours(gradient.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                c2 = sorted(cnts2, key=cv2.contourArea, reverse=True)[0]
                rect2 = cv2.minAreaRect(c2)
                box2 = np.intp(cv2.boxPoints(rect2))
                if len(cnts) == 0:
                    box3 = box2
                    cnts=cnts2

                c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

                rect = cv2.minAreaRect(c)
                box = np.intp(cv2.boxPoints(rect))
                res = cv2.bitwise_and(image, image, mask=closed)
                if len(cnts) == 0:
                    box3 = box2
                if len(cnts) != 0: box3 = box
                d_min = 1000
                rect_min = [[0, 0], [0, 0]]
                rect3 = cv2.boundingRect(box3)
                pt1 = (rect3[0], rect3[1])
                c = (rect3[0] + rect3[2] * 1 / 2, rect3[1] + rect3[3] * 1 / 2)
                d = np.sqrt((c[0] - image_center[0]) ** 2 + (c[1] - image_center[1]) ** 2)
                if d < d_min:
                    d_min = d
                    rect_min = [pt1, (rect3[2], rect3[3])]


                pad = 30
                result = image[rect_min[0][1] - pad:rect_min[0][1] + rect_min[1][1] + pad,
                         rect_min[0][0] - pad:rect_min[0][0] + rect_min[1][0] + pad]
                h, w = result.shape[:2]
                if h <= 0 or w <= 0: #fixed box to tracking
                    result = image


                #print(result.shape[:2])
                if not self.HeightBbox is None or not  self.WeightBbox is None:
                    if self.HeightBbox >= h-40 and self.HeightBbox <= h+40:
                        if self.WeightBbox >= w-40 and self.WeightBbox <= w+40:
                            self.imgOrigin = result
                            self.Detect_flag=1
                        else:
                            self.Detect_flag=0
                            result = image
                    else:
                        #print("fu")
                        result = image
                        self.Detect_flag = 0

                if self.ClickValue==5:
                    h1, w1 = result.shape[:2]
                    self.Save_Bbox(h1,w1)
                    self.ClickValue=1

                self.imgOrigin=result
                self.ImgCap=result
                if self.ClickValue==1:
                    self.Show_panel02_0_1(self.treshImg)
                    self.Show_panel03_1_0(self.ImgCap)


    def roi_setting(self):
        while not self.stopEvent.is_set():
            if not self.imgOrigin is None:
                if self.Detect_flag == 1:
                    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (self.rectY.get(), self.rectX.get()))
                    sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (self.sqY.get(), self.sqX.get()))
                    imgOrigin = self.imgOrigin
                    gray = cv2.cvtColor(imgOrigin, cv2.COLOR_BGR2GRAY)
                    Imin = np.array([self.var.get(), self.var1.get(), self.varMax4.get()], dtype='uint8')
                    Imin2 = np.array([self.var.get(), self.var1.get(), self.varMax5.get()], dtype='uint8')
                    Imax = np.array([self.varMax.get(), self.varMax2.get(), self.varMax3.get()], dtype='uint8')
                    hsv = cv2.cvtColor(imgOrigin, cv2.COLOR_BGR2HSV)
                    masks = cv2.inRange(hsv, Imin, Imax)
                    masks2 = cv2.inRange(hsv, Imin2, Imax)
                    blurred = cv2.blur(masks, (1, 1))
                    blurred2 = cv2.blur(masks2, (1, 1))
                    img = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV)[1]
                    img2 = cv2.threshold(blurred2, 0, 255, cv2.THRESH_BINARY_INV)[1]
                    imgTocrop = img
                    imgWrap = img2
                    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, rectKernel)
                    img2 = img
                    np.seterr(divide='ignore', invalid='ignore')
                    gradX = cv2.Sobel(tophat, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=7)
                    gradX = np.absolute(gradX)
                    (minVal, maxVal) = (np.min(gradX), np.max(gradX))
                    gradX = (255 * ((gradX - minVal) / (maxVal - minVal)))
                    gradX = gradX.astype("uint8")

                    gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
                    thresh = cv2.threshold(gradX, 0, 255,
                                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
                    t2 = thresh
                    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
                    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_SIMPLE)
                    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
                    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
                    # cnts = contours.sort_contours(cnts, method="top-to-buttom")[0]
                    locs = []
                    tmpcnts = {}
                    clone01 = np.dstack([thresh.copy()] * 3)


                    font = cv2.FONT_HERSHEY_SIMPLEX
                    tmpcnts3 = {}
                    for (idx, c) in enumerate(cnts):
                        x, y, w, h = cv2.boundingRect(c)
                        x -= 15
                        y -= 8
                        w += 25
                        h += 10
                        # h=h+5
                        cv2.rectangle(clone01, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        tmpcnts[idx] = imgTocrop[y:y + h, x:x + w]
                        tmpcnts3[idx] = imgWrap[y:y + h, x:x + w]
                        #

                        locs.append((x, y, w, h))

                    locs = sorted(locs, key=lambda X: X[0])

                    self.ROI=tmpcnts3
                    img = clone01
                    try:
                        img = imutils.resize(img, width=300, height=200)
                    except:
                        img = img


                    text = []
                    tmpcnts2 = {}
                    for i in range(len(tmpcnts)):
                        # text = []
                        try:
                            img = tmpcnts[i]
                            h, w = img.shape[:2]
                            img = imutils.resize(img, width=int(w / 2), height=int(h / 2))
                            img = tmpcnts[i]
                        except:
                            img = imgTocrop
                        tmpcnts2[i] = img
                        text.append(i)
                    if len(tmpcnts) == 0:
                        tmpcnts2[0] = imgTocrop
                        tmpcnts3[0] = imgWrap
                    if self.ClickValue == 2:
                        self.Show_panel01_0_0(clone01)
                        self.Show_panel02_0_1(imgTocrop)
                        self.Show_panel03_1_0(imgWrap)
                        self.Show_panel04_1_1(tmpcnts3[0])
                    if self.ClickValue==3 :
                        if not self.ROI is None:
                            self.Show_panel01_0_0(self.ROI[0])
                            self.Show_panel02_0_1(self.ROI[1])
                            self.Show_panel03_1_0(self.ROI[2])

                else:
                    img = cv2.imread('no_detact.png')
                    if self.ClickValue == 2:
                        self.Show_panel01_0_0(img)
                        self.Show_panel02_0_1(img)
                        self.Show_panel03_1_0(img)
                        self.Show_panel04_1_1(img)
                    if self.ClickValue == 3:
                        self.Show_panel01_0_0(img)
                        self.Show_panel02_0_1(img)
                        self.Show_panel03_1_0(img)

                    if self.ClickValue == 10:
                        self.Show_panel01_0_0(self.ImgCap)
                        self.Show_panel03_1_0(img)

if __name__ == '__main__':

    t=App()
    t.root.mainloop()