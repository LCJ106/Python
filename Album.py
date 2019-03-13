import wx
from PIL import Image
import matplotlib.pyplot as plt
import os
import tkinter
import re
import pygame

class wxGUI(wx.App):
    def OnInit(self):
        self.frame=wx.Frame(parent=None,title='x',size=(600,600))
        self.panel=wx.Panel(self.frame,-1)
        
        wx.StaticText(parent=self.panel,label='相册路径名',pos=(120,60))#静态文本控件
        self.inputN1=wx.TextCtrl(parent=self.panel,pos=(240,60))#文本框
        
        #添加按钮
        self.buttonCheck1=wx.Button(parent=self.panel,label='确定',pos=(400,60))
        self.Bind(wx.EVT_BUTTON,self.OnButtonCheck1,self.buttonCheck1)

        self.buttonCheck6=wx.Button(parent=self.panel,label='播放相册',pos=(140,400))#添加按钮
        self.Bind(wx.EVT_BUTTON,self.OnButtonCheck6,self.buttonCheck6)

        self.buttonCheck7=wx.Button(parent=self.panel,label='停止播放',pos=(300,400))#添加按钮
        self.Bind(wx.EVT_BUTTON,self.OnButtonCheck7,self.buttonCheck7)

        wx.StaticText(parent=self.panel,label='裁剪',pos=(120,140))#静态文本控件
        self.inputN2=wx.TextCtrl(parent=self.panel,pos=(240,140))#文本框
        self.buttonCheck2=wx.Button(parent=self.panel,label='确定',pos=(400,140))#添加按钮
        self.Bind(wx.EVT_BUTTON,self.OnButtonCheck2,self.buttonCheck2)

        wx.StaticText(parent=self.panel,label='缩放',pos=(120,190))#静态文本控件
        self.buttonCheck3=wx.Button(parent=self.panel,label='确定',pos=(400,190))#添加按钮
        self.inputN3=wx.TextCtrl(parent=self.panel,pos=(240,190))#文本框
        self.Bind(wx.EVT_BUTTON,self.OnButtonCheck3,self.buttonCheck3)

        wx.StaticText(parent=self.panel,label='旋转',pos=(120,240))#静态文本控件
        self.inputN4=wx.TextCtrl(parent=self.panel,pos=(240,240))#文本框
        self.buttonCheck4=wx.Button(parent=self.panel,label='确定',pos=(400,240))#添加按钮
        self.Bind(wx.EVT_BUTTON,self.OnButtonCheck4,self.buttonCheck4)



        #组合框
        self.comboBox1=wx.ComboBox(self.panel,value='click here',choices=[],pos=(100,100),size=(200,130))
        self.Bind(wx.EVT_COMBOBOX,self.OnCombo1,self.comboBox1)
        
        self.frame.Show()
        return True

    #按钮设置实时更新组合框
    def OnButtonCheck1(self,event):
        path=self.inputN1.GetValue()
        images=[f for f in os.listdir(path) if f.endswith('.jpg')]
        self.comboBox1.Set(images)

    #裁剪
    def OnButtonCheck2(self,event):
        path=self.inputN1.GetValue()
        name=self.comboBox1.GetValue()
        f=path+'\\'+name
        img=Image.open(f)
        x=self.inputN2.GetValue()
        pattern=re.compile(r',')
        y=pattern.split(x)
        print(y)
        left=int(y[0])
        upper=int(y[1])
        right=int(y[2])
        lower=int(y[3])
        box=(left,upper,right,lower)
        img1=img.crop(box)#该tuple中信息为(left, upper, right, lower)。系统的原点（0，0）为图片的左上角。坐标中的数字单位为像素点。
        plt.figure(2)
        plt.title('img1')
        plt.imshow(img1),plt.axis('off')
        plt.show()

    #缩放
    def OnButtonCheck3(self,event):
        path=self.inputN1.GetValue()
        name=self.comboBox1.GetValue() 
        f=path+'\\'+name
        img=Image.open(f)         
        m=self.inputN3.GetValue()
        pattern=re.compile(r',')
        n=pattern.split(m)
        width=int(n[0])
        height=int(n[1])
        img2=img.resize((width,height),Image.ANTIALIAS)
        plt.title('img2')
        plt.imshow(img2)
        plt.axis('off')
        plt.show()

    def OnButtonCheck4(self,event):
        plt.figure(4)
        path=self.inputN1.GetValue()
        name=self.comboBox1.GetValue()
        f=path+'\\'+name
        img=Image.open(f)         
        angle=int(self.inputN4.GetValue())
        img3=img.rotate(angle)
        plt.title('img3')
        plt.imshow(img3),plt.axis('off')
        plt.show()



    #相册播放   
    def OnButtonCheck6(self,event):
        global i
        i=1
        path=self.inputN1.GetValue()
        images=[f for f in os.listdir(path) if f.endswith('.jpg')]
        pygame.mixer.init()
        plt.figure(5)
        file=r'F:\QQ.music\刘瑞琦 - 歌路.mp3'
        file=file.encode('utf-8')
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        plt.ion()
        while 1:            
            for f in images:
                f=path+'\\'+f
                im=Image.open(f)
                plt.imshow(im)
                plt.axis('off')
                plt.pause(3)
                if(i==0):
                    break
            if(i==0):
                break
        plt.close()
        plt.ioff()
        
    #停止播放           
    def OnButtonCheck7(self,event):
        global i
        i=0
        pygame.mixer.music.stop()


    #组合框选定显示对应图片
    def OnCombo1(self,event):
        path=self.inputN1.GetValue()
        name=self.comboBox1.GetValue()
        plt.figure(1)
        f=path+'\\'+name
        im=Image.open(f)
        print(im.size)
        plt.imshow(im)
        plt.axis('off')
        plt.show()
app=wxGUI()
app.MainLoop()
