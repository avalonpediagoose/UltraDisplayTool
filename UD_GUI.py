####################################################################################################
#
#
# Note: Any version of python 3.10
# Release Date: 2024/04/03
####################################################################################################
import wx    
####################################################################################################
class BasePage(wx.Panel):
    """ Panel class that Page_0"""
    #-----------------------------------------------------------------------------------------------
    def __init__(self, title):       
        wx.Panel.__init__(self, title)
        font = wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft Sans Serif")
        
        self.MutiCmdSBox = wx.StaticBox(self, wx.ID_ANY, label = 'Cmd to Driver IC', pos = (8, 8), size = (752, 289))
        
        self.MutiCmdST = wx.StaticText(self, wx.ID_ANY, label = 'CMD', pos = (89, 25), size = (31, 12))
        self.MutiParaST = wx.StaticText(self, wx.ID_ANY, label = 'Parameter', pos = (130, 25), size = (64, 12))
        self.MutiP1ST = wx.StaticText(self, wx.ID_ANY, label = '1', pos = (211, 25), size = (16, 12))
        self.MutiP2ST = wx.StaticText(self, wx.ID_ANY, label = '2', pos = (259, 25), size = (16, 12))
        self.MutiP3ST = wx.StaticText(self, wx.ID_ANY, label = '3', pos = (307, 25), size = (16, 12))
        self.MutiP4ST = wx.StaticText(self, wx.ID_ANY, label = '4', pos = (355, 25), size = (16, 12))
        self.MutiP5ST = wx.StaticText(self, wx.ID_ANY, label = '5', pos = (403, 25), size = (16, 12))
        self.MutiP6ST = wx.StaticText(self, wx.ID_ANY, label = '6', pos = (451, 25), size = (16, 12))
        self.MutiP7ST = wx.StaticText(self, wx.ID_ANY, label = '7', pos = (499, 25), size = (16, 12))
        self.MutiP8ST = wx.StaticText(self, wx.ID_ANY, label = '8', pos = (547, 25), size = (16, 12))
        self.MutiP9ST = wx.StaticText(self, wx.ID_ANY, label = '9', pos = (595, 25), size = (16, 12))
        self.MutiP10ST = wx.StaticText(self, wx.ID_ANY, label = '10', pos = (641, 25), size = (16, 12))      
        #-----------------------------------------------------------------------------------------------            
        self.MulitWr1 = wx.Button(self, label = 'CMD1', pos = (14, 40), size = (60, 33))
        
        self.Data0TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (80, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data0TC1.SetMaxLength(2)
        self.Data0TC1.SetFont(font)
        self.Data0TC1.SetForegroundColour((139,0,0))
        
        self.Parabox1 = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (135, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Parabox1.SetMaxLength(2)
        self.Parabox1.SetFont(font)
        self.Parabox1.SetForegroundColour((139,0,0))
        self.Parabox1.SetBackgroundColour((255,255,225))                

        self.Data1TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (191, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data1TC1.SetMaxLength(2)
        self.Data1TC1.SetFont(font)
        self.Data1TC1.SetForegroundColour((139,0,0)) 
        
        self.Data2TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (239, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data2TC1.SetMaxLength(2)
        self.Data2TC1.SetFont(font)
        self.Data2TC1.SetForegroundColour((139,0,0)) 
        
        self.Data3TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (287, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data3TC1.SetMaxLength(2)
        self.Data3TC1.SetFont(font)
        self.Data3TC1.SetForegroundColour((139,0,0)) 
        
        self.Data4TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (335, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data4TC1.SetMaxLength(2)
        self.Data4TC1.SetFont(font)
        self.Data4TC1.SetForegroundColour((139,0,0)) 
        
        self.Data5TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (383, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data5TC1.SetMaxLength(2)
        self.Data5TC1.SetFont(font)
        self.Data5TC1.SetForegroundColour((139,0,0)) 
        
        self.Data6TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (431, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data6TC1.SetMaxLength(2)
        self.Data6TC1.SetFont(font)
        self.Data6TC1.SetForegroundColour((139,0,0)) 
        
        self.Data7TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (479, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data7TC1.SetMaxLength(2)
        self.Data7TC1.SetFont(font)
        self.Data7TC1.SetForegroundColour((139,0,0)) 
        
        self.Data8TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (527, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data8TC1.SetMaxLength(2)
        self.Data8TC1.SetFont(font)
        self.Data8TC1.SetForegroundColour((139,0,0)) 
        
        self.Data9TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (575, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data9TC1.SetMaxLength(2)
        self.Data9TC1.SetFont(font)
        self.Data9TC1.SetForegroundColour((139,0,0)) 
        
        self.Data10TC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (623, 40), size = (48, 33), style = wx.TE_CENTER)
        self.Data10TC1.SetMaxLength(2)
        self.Data10TC1.SetFont(font)
        self.Data10TC1.SetForegroundColour((139,0,0)) 
        
        self.CBox1 = wx.CheckBox(self, wx.ID_ANY, label="", pos = (674, 58))
        self.CBox1.SetValue(True)
        self.MulitRd1 = wx.Button(self, label = 'Read', pos = (693, 40), size = (60, 33))       
        #-----------------------------------------------------------------------------------------------       
        self.MulitWr2 = wx.Button(self, label = 'CMD2', pos = (14, 76), size = (60, 33))        
        
        self.Data0TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (80, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data0TC2.SetMaxLength(2)
        self.Data0TC2.SetFont(font)
        self.Data0TC2.SetForegroundColour((139,0,0)) 
        
        self.Parabox2 = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (135, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Parabox2.SetMaxLength(2)
        self.Parabox2.SetFont(font)
        self.Parabox2.SetForegroundColour((139,0,0))
        self.Parabox2.SetBackgroundColour((255,255,225))                 

        self.Data1TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (191, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data1TC2.SetMaxLength(2)
        self.Data1TC2.SetFont(font)
        self.Data1TC2.SetForegroundColour((139,0,0)) 
        
        self.Data2TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (239, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data2TC2.SetMaxLength(2)
        self.Data2TC2.SetFont(font)
        self.Data2TC2.SetForegroundColour((139,0,0)) 
        
        self.Data3TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (287, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data3TC2.SetMaxLength(2)
        self.Data3TC2.SetFont(font)
        self.Data3TC2.SetForegroundColour((139,0,0)) 
        
        self.Data4TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (335, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data4TC2.SetMaxLength(2)
        self.Data4TC2.SetFont(font)
        self.Data4TC2.SetForegroundColour((139,0,0)) 
        
        self.Data5TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (383, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data5TC2.SetMaxLength(2)
        self.Data5TC2.SetFont(font)
        self.Data5TC2.SetForegroundColour((139,0,0)) 
        
        self.Data6TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (431, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data6TC2.SetMaxLength(2)
        self.Data6TC2.SetFont(font)
        self.Data6TC2.SetForegroundColour((139,0,0)) 
        
        self.Data7TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (479, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data7TC2.SetMaxLength(2)
        self.Data7TC2.SetFont(font)
        self.Data7TC2.SetForegroundColour((139,0,0)) 
        
        self.Data8TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (527, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data8TC2.SetMaxLength(2)
        self.Data8TC2.SetFont(font)
        self.Data8TC2.SetForegroundColour((139,0,0)) 
        
        self.Data9TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (575, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data9TC2.SetMaxLength(2)
        self.Data9TC2.SetFont(font)
        self.Data9TC2.SetForegroundColour((139,0,0)) 
        
        self.Data10TC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (623, 76), size = (48, 33), style = wx.TE_CENTER)
        self.Data10TC2.SetMaxLength(2)
        self.Data10TC2.SetFont(font)
        self.Data10TC2.SetForegroundColour((139,0,0)) 
        
        self.CBox2 = wx.CheckBox(self, wx.ID_ANY, label="", pos = (674, 94))
        self.CBox2.SetValue(True)
        self.MulitRd2 = wx.Button(self, label = 'Read', pos = (693, 76), size = (60, 33))                
        #-----------------------------------------------------------------------------------------------
        self.MulitWr3 = wx.Button(self, label = 'CMD3', pos = (14, 112), size = (60, 33))       
        
        self.Data0TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (80, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data0TC3.SetMaxLength(2)
        self.Data0TC3.SetFont(font)
        self.Data0TC3.SetForegroundColour((139,0,0)) 
        
        self.Parabox3 = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (135, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Parabox3.SetMaxLength(2)
        self.Parabox3.SetFont(font)
        self.Parabox3.SetForegroundColour((139,0,0))                 
        self.Parabox3.SetBackgroundColour((255,255,225))
        
        self.Data1TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (191, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data1TC3.SetMaxLength(2)
        self.Data1TC3.SetFont(font)
        self.Data1TC3.SetForegroundColour((139,0,0)) 
        
        self.Data2TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (239, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data2TC3.SetMaxLength(2)
        self.Data2TC3.SetFont(font)
        self.Data2TC3.SetForegroundColour((139,0,0)) 
        
        self.Data3TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (287, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data3TC3.SetMaxLength(2)
        self.Data3TC3.SetFont(font)
        self.Data3TC3.SetForegroundColour((139,0,0)) 
        
        self.Data4TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (335, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data4TC3.SetMaxLength(2)
        self.Data4TC3.SetFont(font)
        self.Data4TC3.SetForegroundColour((139,0,0)) 
        
        self.Data5TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (383, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data5TC3.SetMaxLength(2)
        self.Data5TC3.SetFont(font)
        self.Data5TC3.SetForegroundColour((139,0,0)) 
        
        self.Data6TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (431, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data6TC3.SetMaxLength(2)
        self.Data6TC3.SetFont(font)
        self.Data6TC3.SetForegroundColour((139,0,0)) 
        
        self.Data7TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (479, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data7TC3.SetMaxLength(2)
        self.Data7TC3.SetFont(font)
        self.Data7TC3.SetForegroundColour((139,0,0)) 
        
        self.Data8TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (527, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data8TC3.SetMaxLength(2)
        self.Data8TC3.SetFont(font)
        self.Data8TC3.SetForegroundColour((139,0,0)) 
        
        self.Data9TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (575, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data9TC3.SetMaxLength(2)
        self.Data9TC3.SetFont(font)
        self.Data9TC3.SetForegroundColour((139,0,0)) 
        
        self.Data10TC3 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (623, 112), size = (48, 33), style = wx.TE_CENTER)
        self.Data10TC3.SetMaxLength(2)
        self.Data10TC3.SetFont(font)
        self.Data10TC3.SetForegroundColour((139,0,0)) 
        
        self.CBox3 = wx.CheckBox(self, wx.ID_ANY, label="", pos = (674, 130))
        self.CBox3.SetValue(True)
        self.MulitRd3 = wx.Button(self, label = 'Read', pos = (693, 112), size = (60, 33))        
        #-----------------------------------------------------------------------------------------------
        self.MulitWr4 = wx.Button(self, label = 'CMD4', pos = (14, 148), size = (60, 33))        
        
        self.Data0TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (80, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data0TC4.SetMaxLength(2)
        self.Data0TC4.SetFont(font)
        self.Data0TC4.SetForegroundColour((139,0,0)) 
        
        self.Parabox4 = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (135, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Parabox4.SetMaxLength(2)
        self.Parabox4.SetFont(font)
        self.Parabox4.SetForegroundColour((139,0,0))                 
        self.Parabox4.SetBackgroundColour((255,255,225))
        
        self.Data1TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (191, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data1TC4.SetMaxLength(2)
        self.Data1TC4.SetFont(font)
        self.Data1TC4.SetForegroundColour((139,0,0)) 
        
        self.Data2TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (239, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data2TC4.SetMaxLength(2)
        self.Data2TC4.SetFont(font)
        self.Data2TC4.SetForegroundColour((139,0,0)) 
        
        self.Data3TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (287, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data3TC4.SetMaxLength(2)
        self.Data3TC4.SetFont(font)
        self.Data3TC4.SetForegroundColour((139,0,0)) 
        
        self.Data4TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (335, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data4TC4.SetMaxLength(2)
        self.Data4TC4.SetFont(font)
        self.Data4TC4.SetForegroundColour((139,0,0)) 
        
        self.Data5TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (383, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data5TC4.SetMaxLength(2)
        self.Data5TC4.SetFont(font)
        self.Data5TC4.SetForegroundColour((139,0,0)) 
        
        self.Data6TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (431, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data6TC4.SetMaxLength(2)
        self.Data6TC4.SetFont(font)
        self.Data6TC4.SetForegroundColour((139,0,0)) 
        
        self.Data7TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (479, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data7TC4.SetMaxLength(2)
        self.Data7TC4.SetFont(font)
        self.Data7TC4.SetForegroundColour((139,0,0)) 
        
        self.Data8TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (527, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data8TC4.SetMaxLength(2)
        self.Data8TC4.SetFont(font)
        self.Data8TC4.SetForegroundColour((139,0,0)) 
        
        self.Data9TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (575, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data9TC4.SetMaxLength(2)
        self.Data9TC4.SetFont(font)
        self.Data9TC4.SetForegroundColour((139,0,0)) 
        
        self.Data10TC4 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (623, 148), size = (48, 33), style = wx.TE_CENTER)
        self.Data10TC4.SetMaxLength(2)
        self.Data10TC4.SetFont(font)
        self.Data10TC4.SetForegroundColour((139,0,0)) 
        
        self.CBox4 = wx.CheckBox(self, wx.ID_ANY, label="", pos = (674, 166))
        self.CBox4.SetValue(True)
        self.MulitRd4 = wx.Button(self, label = 'Read', pos = (693, 148), size = (60, 33))       
        #-----------------------------------------------------------------------------------------------
        self.MulitWr5 = wx.Button(self, label = 'CMD5', pos = (14, 184), size = (60, 33))        
        
        self.Data0TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (80, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data0TC5.SetMaxLength(2)
        self.Data0TC5.SetFont(font)
        self.Data0TC5.SetForegroundColour((139,0,0)) 
        
        self.Parabox5 = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (135, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Parabox5.SetMaxLength(2)
        self.Parabox5.SetFont(font)
        self.Parabox5.SetForegroundColour((139,0,0))                 
        self.Parabox5.SetBackgroundColour((255,255,225))
        
        self.Data1TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (191, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data1TC5.SetMaxLength(2)
        self.Data1TC5.SetFont(font)
        self.Data1TC5.SetForegroundColour((139,0,0)) 
        
        self.Data2TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (239, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data2TC5.SetMaxLength(2)
        self.Data2TC5.SetFont(font)
        self.Data2TC5.SetForegroundColour((139,0,0)) 
        
        self.Data3TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (287, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data3TC5.SetMaxLength(2)
        self.Data3TC5.SetFont(font)
        self.Data3TC5.SetForegroundColour((139,0,0)) 
        
        self.Data4TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (335, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data4TC5.SetMaxLength(2)
        self.Data4TC5.SetFont(font)
        self.Data4TC5.SetForegroundColour((139,0,0)) 
        
        self.Data5TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (383, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data5TC5.SetMaxLength(2)
        self.Data5TC5.SetFont(font)
        self.Data5TC5.SetForegroundColour((139,0,0)) 
        
        self.Data6TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (431, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data6TC5.SetMaxLength(2)
        self.Data6TC5.SetFont(font)
        self.Data6TC5.SetForegroundColour((139,0,0)) 
        
        self.Data7TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (479, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data7TC5.SetMaxLength(2)
        self.Data7TC5.SetFont(font)
        self.Data7TC5.SetForegroundColour((139,0,0)) 
        
        self.Data8TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (527, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data8TC5.SetMaxLength(2)
        self.Data8TC5.SetFont(font)
        self.Data8TC5.SetForegroundColour((139,0,0)) 
        
        self.Data9TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (575, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data9TC5.SetMaxLength(2)
        self.Data9TC5.SetFont(font)
        self.Data9TC5.SetForegroundColour((139,0,0)) 
        
        self.Data10TC5 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (623, 184), size = (48, 33), style = wx.TE_CENTER)
        self.Data10TC5.SetMaxLength(2)
        self.Data10TC5.SetFont(font)
        self.Data10TC5.SetForegroundColour((139,0,0))
       
        self.CBox5 = wx.CheckBox(self, wx.ID_ANY, label="", pos = (674, 202))
        self.CBox5.SetValue(True)
        self.MulitRd5 = wx.Button(self, label = 'Read', pos = (693, 184), size = (60, 33))        
        #-----------------------------------------------------------------------------------------------
        self.MulitWr6 = wx.Button(self, label = 'CMD6', pos = (14, 220), size = (60, 33))        
        
        self.Data0TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (80, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data0TC6.SetMaxLength(2)
        self.Data0TC6.SetFont(font)
        self.Data0TC6.SetForegroundColour((139,0,0)) 
        
        self.Parabox6 = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (135, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Parabox6.SetMaxLength(2)
        self.Parabox6.SetFont(font)
        self.Parabox6.SetForegroundColour((139,0,0))                 
        self.Parabox6.SetBackgroundColour((255,255,225))
        
        self.Data1TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (191, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data1TC6.SetMaxLength(2)
        self.Data1TC6.SetFont(font)
        self.Data1TC6.SetForegroundColour((139,0,0)) 
        
        self.Data2TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (239, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data2TC6.SetMaxLength(2)
        self.Data2TC6.SetFont(font)
        self.Data2TC6.SetForegroundColour((139,0,0)) 
        
        self.Data3TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (287, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data3TC6.SetMaxLength(2)
        self.Data3TC6.SetFont(font)
        self.Data3TC6.SetForegroundColour((139,0,0)) 
        
        self.Data4TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (335, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data4TC6.SetMaxLength(2)
        self.Data4TC6.SetFont(font)
        self.Data4TC6.SetForegroundColour((139,0,0)) 
        
        self.Data5TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (383, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data5TC6.SetMaxLength(2)
        self.Data5TC6.SetFont(font)
        self.Data5TC6.SetForegroundColour((139,0,0)) 
        
        self.Data6TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (431, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data6TC6.SetMaxLength(2)
        self.Data6TC6.SetFont(font)
        self.Data6TC6.SetForegroundColour((139,0,0)) 
        
        self.Data7TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (479, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data7TC6.SetMaxLength(2)
        self.Data7TC6.SetFont(font)
        self.Data7TC6.SetForegroundColour((139,0,0)) 
        
        self.Data8TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (527, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data8TC6.SetMaxLength(2)
        self.Data8TC6.SetFont(font)
        self.Data8TC6.SetForegroundColour((139,0,0)) 
        
        self.Data9TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (575, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data9TC6.SetMaxLength(2)
        self.Data9TC6.SetFont(font)
        self.Data9TC6.SetForegroundColour((139,0,0)) 
        
        self.Data10TC6 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (623, 220), size = (48, 33), style = wx.TE_CENTER)
        self.Data10TC6.SetMaxLength(2)
        self.Data10TC6.SetFont(font)
        self.Data10TC6.SetForegroundColour((139,0,0))
       
        self.CBox6 = wx.CheckBox(self, wx.ID_ANY, label="", pos = (674, 238))
        self.CBox6.SetValue(True)
        self.MulitRd6 = wx.Button(self, label = 'Read', pos = (693, 220), size = (60, 33))        
        #-----------------------------------------------------------------------------------------------
        self.MulitWr7 = wx.Button(self, label = 'CMD7', pos = (14, 256), size = (60, 33))        
        
        self.Data0TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (80, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data0TC7.SetMaxLength(2)
        self.Data0TC7.SetFont(font)
        self.Data0TC7.SetForegroundColour((139,0,0)) 
        
        self.Parabox7 = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (135, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Parabox7.SetMaxLength(2)
        self.Parabox7.SetFont(font)
        self.Parabox7.SetForegroundColour((139,0,0))                 
        self.Parabox7.SetBackgroundColour((255,255,225))
        
        self.Data1TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (191, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data1TC7.SetMaxLength(2)
        self.Data1TC7.SetFont(font)
        self.Data1TC7.SetForegroundColour((139,0,0)) 
        
        self.Data2TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (239, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data2TC7.SetMaxLength(2)
        self.Data2TC7.SetFont(font)
        self.Data2TC7.SetForegroundColour((139,0,0)) 
        
        self.Data3TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (287, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data3TC7.SetMaxLength(2)
        self.Data3TC7.SetFont(font)
        self.Data3TC7.SetForegroundColour((139,0,0)) 
        
        self.Data4TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (335, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data4TC7.SetMaxLength(2)
        self.Data4TC7.SetFont(font)
        self.Data4TC7.SetForegroundColour((139,0,0)) 
        
        self.Data5TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (383, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data5TC7.SetMaxLength(2)
        self.Data5TC7.SetFont(font)
        self.Data5TC7.SetForegroundColour((139,0,0)) 
        
        self.Data6TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (431, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data6TC7.SetMaxLength(2)
        self.Data6TC7.SetFont(font)
        self.Data6TC7.SetForegroundColour((139,0,0)) 
        
        self.Data7TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (479, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data7TC7.SetMaxLength(2)
        self.Data7TC7.SetFont(font)
        self.Data7TC7.SetForegroundColour((139,0,0)) 
        
        self.Data8TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (527, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data8TC7.SetMaxLength(2)
        self.Data8TC7.SetFont(font)
        self.Data8TC7.SetForegroundColour((139,0,0)) 
        
        self.Data9TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (575, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data9TC7.SetMaxLength(2)
        self.Data9TC7.SetFont(font)
        self.Data9TC7.SetForegroundColour((139,0,0)) 
        
        self.Data10TC7 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (623, 256), size = (48, 33), style = wx.TE_CENTER)
        self.Data10TC7.SetMaxLength(2)
        self.Data10TC7.SetFont(font)
        self.Data10TC7.SetForegroundColour((139,0,0))
       
        self.CBox7 = wx.CheckBox(self, wx.ID_ANY, label="", pos = (674, 274))
        self.CBox7.SetValue(True)
        self.MulitRd7 = wx.Button(self, label = 'Read', pos = (693, 256), size = (60, 33))                      
        #-----------------------------------------------------------------------------------------------          
        HiLoList = ['Low', 'High']
        self.GPIO_0RBox = wx.RadioBox(self, label = 'GPIO_0', pos = (777, 8), size = (104, 46), 
                        choices = HiLoList, majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        self.GPIO_0RBox.SetSelection(0)
        self.GPIO_1RBox = wx.RadioBox(self, label = 'GPIO_1', pos = (777, 58), size = (104, 46), 
                        choices = HiLoList, majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        self.GPIO_1RBox.SetSelection(1)
        self.GPIO_2RBox = wx.RadioBox(self, label = 'GPIO_2', pos = (777, 108), size = (104, 46), 
                        choices = HiLoList, majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        self.GPIO_2RBox.SetSelection(1)
        self.GPIO_3RBox = wx.RadioBox(self, label = 'GPIO_3', pos = (777, 158), size = (104, 46), 
                        choices = HiLoList, majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        self.GPIO_3RBox.SetSelection(0)
        #-----------------------------------------------------------------------------------------------
        self.ScriptSBox = wx.StaticBox(self, wx.ID_ANY, label = 'Load Script', pos = (8, 307), size = (730, 72))          
        self.PathST = wx.StaticText(self, wx.ID_ANY, label = '', pos = (18, 334), size = (500, 30))      
        self.OpenIniBtn = wx.Button(self, label = 'Open Ini', pos = (588, 336), size = (67, 25))        
        self.LoadIniBtn = wx.Button(self, label = 'Load Ini', pos = (659, 336), size = (67, 25))
        #self.LoadIniBtn.Enable(False)
        self.ScriptLoopST = wx.StaticText(self, wx.ID_ANY, label = 'Loop：', pos = (750, 323), size = (47, 20))
        self.ScriptLoopTC = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (797, 321), size = (48, 23), style = wx.TE_CENTER)
        self.ScriptCMD = wx.StaticText(self, wx.ID_ANY, label = 'CMD', pos = (750, 348), size = (31, 12))
        self.ScriptCMD.SetForegroundColour((0,0,255))
####################################################################################################
class TestPage(wx.Panel):
    """ Panel class that Page_1"""
    #-----------------------------------------------------------------------------------------------
    def __init__(self, title):        
        wx.Panel.__init__(self, title)
        
        PosX = 16
        PosY = 16
        self.LoopTotalST = wx.StaticText(self, wx.ID_ANY, label = 'Loop：', pos = (PosX, PosY), size = (47, 20))
        self.LoopExeST = wx.StaticText(self, wx.ID_ANY, label = '0', pos = (PosX+60, PosY), size = (47, 20))
        self.ThreadBtn = wx.Button(self, label = 'Thread', pos = (PosX+120, PosY-6), size = (67, 25))
        
        self.GenScriptST = wx.StaticText(self, wx.ID_ANY, label = 'Parameter：', pos = (PosX, PosY+60), size = (107, 20))
        self.IndexTC = wx.TextCtrl(self, wx.ID_ANY, value = '', pos = (PosX+110, PosY+60), size = (40, 28), style = wx.TE_CENTER)
        self.ParameterTC = wx.TextCtrl(self, wx.ID_ANY, value = '', pos = (PosX+110, PosY+104), size = (400, 28), style = wx.TE_CENTER)
        self.InputBtn = wx.Button(self, label = 'input', pos = (PosX+164, PosY+60), size = (50, 28))
####################################################################################################
class SRAMPage(wx.Panel):
    """ Panel class that Page_2"""
    #-----------------------------------------------------------------------------------------------
    def __init__(self, title):        
        wx.Panel.__init__(self, title)
        font = wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft Sans Serif")
        
        PosX = 8
        PosY = 8       
        self.SARMWriteSBox = wx.StaticBox(self, wx.ID_ANY, label = 'SARM', pos = (PosX, PosY), size = (320, 244))
        self.SARMWr = wx.Button(self, label = 'Write', pos = (PosX+10, PosY+19), size = (60, 33))        
        
        self.E1data0TC = wx.TextCtrl(self, wx.ID_ANY, value = 'E1', pos = (PosX+10, PosY+58), size = (48, 33), style = wx.TE_CENTER)
        self.E1data0TC.SetMaxLength(2)
        self.E1data0TC.SetFont(font)
        self.E1data0TC.SetForegroundColour((139,0,0))
        self.E1data0TC.SetEditable(False)
        self.E1para0TC = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (PosX+64, PosY+58), size = (48, 33), style = wx.TE_CENTER)
        self.E1para0TC.SetMaxLength(1)
        self.E1para0TC.SetFont(font)
        self.E1para0TC.SetForegroundColour((139,0,0))
        self.E1para0TC.SetBackgroundColour((255,255,225))
        self.E1para0TC.SetEditable(False)
        self.E1data1TC = wx.TextCtrl(self, wx.ID_ANY, value = '03', pos = (PosX+118, PosY+58), size = (48, 33), style = wx.TE_CENTER)
        self.E1data1TC.SetMaxLength(2)
        self.E1data1TC.SetFont(font)
        self.E1data1TC.SetForegroundColour((139,0,0))
        
        self.E2data0TC = wx.TextCtrl(self, wx.ID_ANY, value = 'E2', pos = (PosX+10, PosY+94), size = (48, 33), style = wx.TE_CENTER)
        self.E2data0TC.SetMaxLength(2)
        self.E2data0TC.SetFont(font)
        self.E2data0TC.SetForegroundColour((139,0,0))
        self.E2data0TC.SetEditable(False)
        self.E2para0TC = wx.TextCtrl(self, wx.ID_ANY, value = '4', pos = (PosX+64, PosY+94), size = (48, 33), style = wx.TE_CENTER)
        self.E2para0TC.SetMaxLength(1)
        self.E2para0TC.SetFont(font)
        self.E2para0TC.SetForegroundColour((139,0,0))
        self.E2para0TC.SetBackgroundColour((255,255,225))
        self.E2data1TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+118, PosY+94), size = (48, 33), style = wx.TE_CENTER)
        self.E2data1TC.SetMaxLength(2)
        self.E2data1TC.SetFont(font)
        self.E2data1TC.SetForegroundColour((139,0,0))       
        self.E2data2TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+166, PosY+94), size = (48, 33), style = wx.TE_CENTER)
        self.E2data2TC.SetMaxLength(2)
        self.E2data2TC.SetFont(font)
        self.E2data2TC.SetForegroundColour((139,0,0))        
        self.E2data3TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+214, PosY+94), size = (48, 33), style = wx.TE_CENTER)
        self.E2data3TC.SetMaxLength(2)
        self.E2data3TC.SetFont(font)
        self.E2data3TC.SetForegroundColour((139,0,0))
        self.E2data4TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+262, PosY+94), size = (48, 33), style = wx.TE_CENTER)
        self.E2data4TC.SetMaxLength(2)
        self.E2data4TC.SetFont(font)
        self.E2data4TC.SetForegroundColour((139,0,0))
        
        self.E3data0TC = wx.TextCtrl(self, wx.ID_ANY, value = 'E3', pos = (PosX+10, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.E3data0TC.SetMaxLength(2)
        self.E3data0TC.SetFont(font)
        self.E3data0TC.SetForegroundColour((139,0,0))
        self.E3data0TC.SetEditable(False)
        self.E3para0TC = wx.TextCtrl(self, wx.ID_ANY, value = '4', pos = (PosX+64, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.E3para0TC.SetMaxLength(1)
        self.E3para0TC.SetFont(font)
        self.E3para0TC.SetForegroundColour((139,0,0))
        self.E3para0TC.SetBackgroundColour((255,255,225))
        self.E3data1TC = wx.TextCtrl(self, wx.ID_ANY, value = '25', pos = (PosX+118, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.E3data1TC.SetMaxLength(2)
        self.E3data1TC.SetFont(font)
        self.E3data1TC.SetForegroundColour((139,0,0))
        self.E3data2TC = wx.TextCtrl(self, wx.ID_ANY, value = 'BE', pos = (PosX+166, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.E3data2TC.SetMaxLength(2)
        self.E3data2TC.SetFont(font)
        self.E3data2TC.SetForegroundColour((139,0,0))  
        self.E3data3TC = wx.TextCtrl(self, wx.ID_ANY, value = 'A3', pos = (PosX+214, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.E3data3TC.SetMaxLength(2)
        self.E3data3TC.SetFont(font)
        self.E3data3TC.SetForegroundColour((139,0,0))
        self.E3data4TC = wx.TextCtrl(self, wx.ID_ANY, value = '0B', pos = (PosX+262, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.E3data4TC.SetMaxLength(2)
        self.E3data4TC.SetFont(font)
        self.E3data4TC.SetForegroundColour((139,0,0))
        
        self.E5data0TC = wx.TextCtrl(self, wx.ID_ANY, value = 'E5', pos = (PosX+10, PosY+166), size = (48, 33), style = wx.TE_CENTER)
        self.E5data0TC.SetMaxLength(2)
        self.E5data0TC.SetFont(font)
        self.E5data0TC.SetForegroundColour((139,0,0))
        self.E5data0TC.SetEditable(False)
        self.E5para0TC = wx.TextCtrl(self, wx.ID_ANY, value = '3', pos = (PosX+64, PosY+166), size = (48, 33), style = wx.TE_CENTER)
        self.E5para0TC.SetMaxLength(1)
        self.E5para0TC.SetFont(font)
        self.E5para0TC.SetForegroundColour((139,0,0))
        self.E5para0TC.SetBackgroundColour((255,255,225))
        self.E5data1TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+118, PosY+166), size = (48, 33), style = wx.TE_CENTER)
        self.E5data1TC.SetMaxLength(2)
        self.E5data1TC.SetFont(font)
        self.E5data1TC.SetForegroundColour((139,0,0)) 
        self.E5data2TC = wx.TextCtrl(self, wx.ID_ANY, value = 'D0', pos = (PosX+166, PosY+166), size = (48, 33), style = wx.TE_CENTER)
        self.E5data2TC.SetMaxLength(2)
        self.E5data2TC.SetFont(font)
        self.E5data2TC.SetForegroundColour((139,0,0))     
        self.E5data3TC = wx.TextCtrl(self, wx.ID_ANY, value = '07', pos = (PosX+214, PosY+166), size = (48, 33), style = wx.TE_CENTER)
        self.E5data3TC.SetMaxLength(2)
        self.E5data3TC.SetFont(font)
        self.E5data3TC.SetForegroundColour((139,0,0))
        
        self.E6data0TC = wx.TextCtrl(self, wx.ID_ANY, value = 'E6', pos = (PosX+10, PosY+202), size = (48, 33), style = wx.TE_CENTER)
        self.E6data0TC.SetMaxLength(2)
        self.E6data0TC.SetFont(font)
        self.E6data0TC.SetForegroundColour((139,0,0))
        self.E6data0TC.SetEditable(False)
        self.E6para0TC = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (PosX+64, PosY+202), size = (48, 33), style = wx.TE_CENTER)
        self.E6para0TC.SetMaxLength(1)
        self.E6para0TC.SetFont(font)
        self.E6para0TC.SetForegroundColour((139,0,0))
        self.E6para0TC.SetBackgroundColour((255,255,225))
        self.E6para0TC.SetEditable(False)
        self.E6data1TC = wx.TextCtrl(self, wx.ID_ANY, value = '09', pos = (PosX+118, PosY+202), size = (48, 33), style = wx.TE_CENTER)
        self.E6data1TC.SetMaxLength(2)
        self.E6data1TC.SetFont(font)
        self.E6data1TC.SetForegroundColour((139,0,0))
        #-----------------------------------------------------------------------------------------------
        self.SARMReadSBox = wx.StaticBox(self, wx.ID_ANY, label = 'Read Line Buffer', pos = (PosX+330, PosY), size = (417, 174))
        self.SARMRd = wx.Button(self, label = 'R loop', pos = (PosX+340, PosY+19), size = (60, 33))
        self.SARMloopST = wx.StaticText(self, wx.ID_ANY, label = 'Loop：', pos = (PosX+444, PosY+27), size = (47, 20))
        self.SARMloopTC = wx.TextCtrl(self, wx.ID_ANY, value = '512', pos = (PosX+496, PosY+25), size = (48, 23), style = wx.TE_CENTER)
        
        self.F1data0TC = wx.TextCtrl(self, wx.ID_ANY, value = 'F1', pos = (PosX+340, PosY+58), size = (48, 33), style = wx.TE_CENTER)
        self.F1data0TC.SetMaxLength(2)
        self.F1data0TC.SetFont(font)
        self.F1data0TC.SetForegroundColour((139,0,0))
        self.F1data0TC.SetEditable(False)
        self.F1para0TC = wx.TextCtrl(self, wx.ID_ANY, value = '2', pos = (PosX+394, PosY+58), size = (48, 33), style = wx.TE_CENTER)
        self.F1para0TC.SetMaxLength(1)
        self.F1para0TC.SetFont(font)
        self.F1para0TC.SetForegroundColour((139,0,0))
        self.F1para0TC.SetBackgroundColour((255,255,225))
        self.F1data1TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+448, PosY+58), size = (48, 33), style = wx.TE_CENTER)
        self.F1data1TC.SetMaxLength(2)
        self.F1data1TC.SetFont(font)
        self.F1data1TC.SetForegroundColour((139,0,0))        
        self.F1data2TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+496, PosY+58), size = (48, 33), style = wx.TE_CENTER)
        self.F1data2TC.SetMaxLength(2)
        self.F1data2TC.SetFont(font)
        self.F1data2TC.SetForegroundColour((139,0,0))
        
        self.F3data0TC = wx.TextCtrl(self, wx.ID_ANY, value = 'F3', pos = (PosX+340, PosY+94), size = (48, 33), style = wx.TE_CENTER)
        self.F3data0TC.SetMaxLength(2)
        self.F3data0TC.SetFont(font)
        self.F3data0TC.SetForegroundColour((139,0,0))
        self.F3data0TC.SetEditable(False)
        self.F3para0TC = wx.TextCtrl(self, wx.ID_ANY, value = '2', pos = (PosX+394, PosY+94), size = (48, 33), style = wx.TE_CENTER)
        self.F3para0TC.SetMaxLength(1)
        self.F3para0TC.SetFont(font)
        self.F3para0TC.SetForegroundColour((139,0,0))
        self.F3para0TC.SetBackgroundColour((255,255,225))
        self.F3data1TC = wx.TextCtrl(self, wx.ID_ANY, value = '41', pos = (PosX+448, PosY+94), size = (48, 33), style = wx.TE_CENTER)
        self.F3data1TC.SetMaxLength(2)
        self.F3data1TC.SetFont(font)
        self.F3data1TC.SetForegroundColour((139,0,0))        
        self.F3data2TC = wx.TextCtrl(self, wx.ID_ANY, value = '02', pos = (PosX+496, PosY+94), size = (48, 33), style = wx.TE_CENTER)
        self.F3data2TC.SetMaxLength(2)
        self.F3data2TC.SetFont(font)
        self.F3data2TC.SetForegroundColour((139,0,0))

        self.F2data0TC = wx.TextCtrl(self, wx.ID_ANY, value = 'F2', pos = (PosX+340, PosY+130), size = (48, 33), style = wx.TE_CENTER)        
        self.F2data0TC.SetMaxLength(2)
        self.F2data0TC.SetFont(font)
        self.F2data0TC.SetForegroundColour((139,0,0))
        self.F2data0TC.SetEditable(False)
        self.F2para0TC = wx.TextCtrl(self, wx.ID_ANY, value = '6', pos = (PosX+394, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.F2para0TC.SetMaxLength(1)
        self.F2para0TC.SetFont(font)
        self.F2para0TC.SetForegroundColour((139,0,0))
        self.F2para0TC.SetBackgroundColour((255,255,225))
        self.F2data1TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+448, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.F2data1TC.SetMaxLength(2)
        self.F2data1TC.SetFont(font)
        self.F2data1TC.SetForegroundColour((139,0,0))        
        self.F2data2TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+496, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.F2data2TC.SetMaxLength(2)
        self.F2data2TC.SetFont(font)
        self.F2data2TC.SetForegroundColour((139,0,0))
        self.F2data3TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+544, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.F2data3TC.SetMaxLength(2)
        self.F2data3TC.SetFont(font)
        self.F2data3TC.SetForegroundColour((139,0,0))        
        self.F2data4TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+592, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.F2data4TC.SetMaxLength(2)
        self.F2data4TC.SetFont(font)
        self.F2data4TC.SetForegroundColour((139,0,0))
        self.F2data5TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+640, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.F2data5TC.SetMaxLength(2)
        self.F2data5TC.SetFont(font)
        self.F2data5TC.SetForegroundColour((139,0,0))        
        self.F2data6TC = wx.TextCtrl(self, wx.ID_ANY, value = '00', pos = (PosX+688, PosY+130), size = (48, 33), style = wx.TE_CENTER)
        self.F2data6TC.SetMaxLength(2)
        self.F2data6TC.SetFont(font)
        self.F2data6TC.SetForegroundColour((139,0,0))
####################################################################################################
class FlashPage(wx.Panel):
    """ Panel class that Page_3"""
    #-----------------------------------------------------------------------------------------------
    def __init__(self, title):        
        wx.Panel.__init__(self, title)          
        font = wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft Sans Serif")
        flash = wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft Sans Serif")
        
        PosX = 16
        PosY = 16
        self.FlashIDSBox = wx.StaticBox(self, wx.ID_ANY, label = 'Flash ID (9Fh)', pos = (PosX, PosY), size = (230, 66))
        self.FlashID1TC = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosX+10, PosY+22), size = (48, 33), style = wx.TE_CENTER)
        self.FlashID1TC.SetMaxLength(2)
        self.FlashID1TC.SetFont(font)
        self.FlashID1TC.SetForegroundColour((139,0,0)) 
        self.FlashID2TC = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosX+58, PosY+22), size = (48, 33), style = wx.TE_CENTER)
        self.FlashID2TC.SetMaxLength(2)
        self.FlashID2TC.SetFont(font)
        self.FlashID2TC.SetForegroundColour((139,0,0))      
        self.FlashID3TC = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosX+106, PosY+22), size = (48, 33), style = wx.TE_CENTER)
        self.FlashID3TC.SetMaxLength(2)
        self.FlashID3TC.SetFont(font)
        self.FlashID3TC.SetForegroundColour((139,0,0))     
        self.FlashIDRd = wx.Button(self, label = 'Read', pos = (PosX+160, PosY+22), size = (60, 33))                 
        self.FlashErase = wx.Button(self, label = 'Erase', pos = (PosX+242, PosY+22), size = (60, 33))                        
        
        self.WriteSBox = wx.StaticBox(self, wx.ID_ANY, label = 'Write Flash', pos = (PosX, PosY+76), size = (456, 64))
        self.WritePathST = wx.StaticText(self, wx.ID_ANY, label = '', pos = (PosX+8, PosY+98), size = (300, 32))
        self.WritePathST.SetBackgroundColour((195,195,195))
        self.OpenFileBtn = wx.Button(self, label = 'Open', pos = (PosX+320, PosY+102), size = (60, 25))      
        self.WriteFileBtn = wx.Button(self, label = 'Write', pos = (PosX+386, PosY+102), size = (60, 25))
        self.WriteFileCMD = wx.StaticText(self, wx.ID_ANY, label = 'CMD', pos = (PosX+468, PosY+107), size = (31, 12))
        self.WriteFileCMD.SetForegroundColour((0,0,255))
        
        PosXr = 16
        PosYr = 16+82
        self.ReadSBox = wx.StaticBox(self, wx.ID_ANY, label = 'Read Flash', pos = (PosXr, PosYr+68), size = (350, 72))
        self.AddressST = wx.StaticText(self, wx.ID_ANY, label = 'Address', pos = (PosXr+28, PosYr+86), size = (50, 16))
        self.SizeST = wx.StaticText(self, wx.ID_ANY, label = 'Size(byte)', pos = (PosXr+112, PosYr+86), size = (64, 16))
        self.CompareST = wx.StaticText(self, wx.ID_ANY, label = 'Compare', pos = (PosXr+200, PosYr+86), size = (64, 16))
        self.AddressTC = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXr+10, PosYr+104), size = (78, 27), style = wx.TE_CENTER)
        self.AddressTC.SetFont(flash)  
        self.SizeTC = wx.TextCtrl(self, wx.ID_ANY, value = '512000', pos = (PosXr+100, PosYr+104), size = (78, 27), style = wx.TE_CENTER)
        self.SizeTC.SetFont(flash)
        self.CompareTC = wx.TextCtrl(self, wx.ID_ANY, value = 'False', pos = (PosXr+190, PosYr+104), size = (78, 27), style = wx.TE_CENTER)
        self.CompareTC.SetFont(flash)
        self.CompareTC.SetEditable(False)
        self.ReadFileBtn = wx.Button(self, label = 'Read', pos = (PosXr+280, PosYr+106), size = (60, 25))
        self.ReadFileCMD = wx.StaticText(self, wx.ID_ANY, label = 'CMD', pos = (PosXr+378, PosYr+111), size = (31, 12))
        self.ReadFileCMD.SetForegroundColour((0,0,255))
        
        PosXs = 16+380
        PosYs = 16-165
        self.StasusSBox = wx.StaticBox(self, wx.ID_ANY, label = 'Status Register', pos = (PosXs+222, PosYs+165), size = (243, 278))        
        self.ReadStatusBtn = wx.Button(self, label = 'Read', pos = (PosXs+350, PosYs+187), size = (60, 25))
        self.Stasus_07_00 = wx.StaticText(self, wx.ID_ANY, label = 'S07~S00', pos = (PosXs+230, PosYs+213), size = (60, 16))
        self.Stasus_07_00TC = wx.TextCtrl(self, wx.ID_ANY, value = '00000000', pos = (PosXs+230, PosYs+229), size = (93, 27), style = wx.TE_CENTER)
        self.Stasus_07_00TC.SetMaxLength(8)
        self.Stasus_07_00TC.SetFont(flash)
        self.Status07 = wx.TextCtrl(self, wx.ID_ANY, value = 'SRP0', pos = (PosXs+230, PosYs+259), size = (75, 22), style = wx.TE_CENTER)
        self.Status06 = wx.TextCtrl(self, wx.ID_ANY, value = 'BP4', pos = (PosXs+230, PosYs+281), size = (75, 22), style = wx.TE_CENTER)
        self.Status05 = wx.TextCtrl(self, wx.ID_ANY, value = 'BP3', pos = (PosXs+230, PosYs+303), size = (75, 22), style = wx.TE_CENTER)
        self.Status04 = wx.TextCtrl(self, wx.ID_ANY, value = 'BP2', pos = (PosXs+230, PosYs+325), size = (75, 22), style = wx.TE_CENTER)
        self.Status03 = wx.TextCtrl(self, wx.ID_ANY, value = 'BP1', pos = (PosXs+230, PosYs+347), size = (75, 22), style = wx.TE_CENTER)
        self.Status02 = wx.TextCtrl(self, wx.ID_ANY, value = 'BP0', pos = (PosXs+230, PosYs+369), size = (75, 22), style = wx.TE_CENTER)
        self.Status01 = wx.TextCtrl(self, wx.ID_ANY, value = 'WEL', pos = (PosXs+230, PosYs+391), size = (75, 22), style = wx.TE_CENTER)
        self.Status00 = wx.TextCtrl(self, wx.ID_ANY, value = 'WIP', pos = (PosXs+230, PosYs+413), size = (75, 22), style = wx.TE_CENTER)
        self.S07 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+307, PosYs+259), size = (30, 22), style = wx.TE_CENTER)
        self.S06 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+307, PosYs+281), size = (30, 22), style = wx.TE_CENTER)
        self.S05 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+307, PosYs+303), size = (30, 22), style = wx.TE_CENTER)
        self.S04 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+307, PosYs+325), size = (30, 22), style = wx.TE_CENTER)
        self.S03 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+307, PosYs+347), size = (30, 22), style = wx.TE_CENTER)
        self.S02 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+307, PosYs+369), size = (30, 22), style = wx.TE_CENTER)
        self.S01 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+307, PosYs+391), size = (30, 22), style = wx.TE_CENTER)
        self.S00 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+307, PosYs+413), size = (30, 22), style = wx.TE_CENTER)
        self.Stasus_15_08 = wx.StaticText(self, wx.ID_ANY, label = 'S15~S08', pos = (PosXs+350, PosYs+213), size = (60, 16))
        self.Stasus_15_08TC = wx.TextCtrl(self, wx.ID_ANY, value = '00000000', pos = (PosXs+350, PosYs+229), size = (93, 27), style = wx.TE_CENTER)
        self.Stasus_15_08TC.SetMaxLength(8)
        self.Stasus_15_08TC.SetFont(flash)
        self.Status15 = wx.TextCtrl(self, wx.ID_ANY, value = 'SUS', pos = (PosXs+350, PosYs+259), size = (75, 22), style = wx.TE_CENTER)
        self.Status14 = wx.TextCtrl(self, wx.ID_ANY, value = 'CMP', pos = (PosXs+350, PosYs+281), size = (75, 22), style = wx.TE_CENTER)
        self.Status13 = wx.TextCtrl(self, wx.ID_ANY, value = 'HPF', pos = (PosXs+350, PosYs+303), size = (75, 22), style = wx.TE_CENTER)
        self.Status12 = wx.TextCtrl(self, wx.ID_ANY, value = 'Reserved1', pos = (PosXs+350, PosYs+325), size = (75, 22), style = wx.TE_CENTER)
        self.Status11 = wx.TextCtrl(self, wx.ID_ANY, value = 'Reserved2', pos = (PosXs+350, PosYs+347), size = (75, 22), style = wx.TE_CENTER)
        self.Status10 = wx.TextCtrl(self, wx.ID_ANY, value = 'LB', pos = (PosXs+350, PosYs+369), size = (75, 22), style = wx.TE_CENTER)
        self.Status09 = wx.TextCtrl(self, wx.ID_ANY, value = 'QE', pos = (PosXs+350, PosYs+391), size = (75, 22), style = wx.TE_CENTER)
        self.Status08 = wx.TextCtrl(self, wx.ID_ANY, value = 'SRP1', pos = (PosXs+350, PosYs+413), size = (75, 22), style = wx.TE_CENTER)
        self.S15 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+427, PosYs+259), size = (30, 22), style = wx.TE_CENTER)
        self.S14 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+427, PosYs+281), size = (30, 22), style = wx.TE_CENTER)
        self.S13 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+427, PosYs+303), size = (30, 22), style = wx.TE_CENTER)
        self.S12 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+427, PosYs+325), size = (30, 22), style = wx.TE_CENTER)
        self.S11 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+427, PosYs+347), size = (30, 22), style = wx.TE_CENTER)
        self.S10 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+427, PosYs+369), size = (30, 22), style = wx.TE_CENTER)
        self.S09 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+427, PosYs+391), size = (30, 22), style = wx.TE_CENTER)
        self.S08 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosXs+427, PosYs+413), size = (30, 22), style = wx.TE_CENTER)        
####################################################################################################
class DMMPage(wx.Panel):
    """ Panel class that Page_4"""
    #-----------------------------------------------------------------------------------------------
    def __init__(self, title):        
        wx.Panel.__init__(self, title)
        #-----------------------------------------------------------------------------------------------
        PosX0 = 20
        PosY0 = 20
        
        SerialPortList0 = ['Choose a port']
        self.DACompareSBox0 = wx.StaticBox(self, wx.ID_ANY, label = 'DMM', pos = (PosX0, PosY0), size = (298, 247))

        self.SerialPortComboBox0 = wx.ComboBox(self, value = SerialPortList0[0], pos = (PosX0+11, PosY0+27), 
                        size = (200, 24), choices = SerialPortList0)
        
        self.OpenPort0 = wx.Button(self, label = 'Connect', pos = (PosX0+218, PosY0+27), size = (71, 23))
        self.dmmStartST0 = wx.StaticText(self, wx.ID_ANY, label = 'Voltage Get Value(V)', pos = (PosX0+15, PosY0+57), size = (161, 16))
        self.dmmStartTC0 = wx.TextCtrl(self, wx.ID_ANY, value = '0.0', pos = (PosX0+11, PosY0+75), size = (150, 23), style = wx.TE_CENTER)       
        self.dmmStepST0 = wx.StaticText(self, wx.ID_ANY, label = 'Voltage Step(mV)', pos = (PosX0+15, PosY0+149), size = (161, 16))
        self.dmmStepSC0 = wx.SpinCtrl(self, wx.ID_ANY, pos = (PosX0+11, PosY0+167), size = (153, 23), style = wx.TE_CENTER, min = 0, max = 1000000, initial = 2)
        self.dmmDelyTimeST0 = wx.StaticText(self, wx.ID_ANY, label = 'Delay Time(ms)', pos = (PosX0+15, PosY0+195), size = (161, 16))
        self.dmmDelyTimeTC0 = wx.TextCtrl(self, wx.ID_ANY, value = '500', pos = (PosX0+11, PosY0+213), size = (150, 23), style = wx.TE_CENTER)
        
        self.dmmAutoMeasureBtn0 = wx.Button(self, label = 'Auto Measure', pos = (PosX0+183, PosY0+75), size = (100, 23))
        self.dmmCMD0 = wx.StaticText(self, wx.ID_ANY, label = 'CMD', pos = (PosX0+183, PosY0+125), size = (31, 12))
        self.dmmCMD0.SetForegroundColour((0,0,255))
        self.dmmStopCB0 = wx.CheckBox(self, label = 'Stop', pos = (PosX0+183, PosY0+213), size = (58, 23))
        
        self.dmmThreadBtn0 = wx.Button(self, label = 'Run', pos = (PosX0+103, PosY0+290), size = (60, 23))
        self.dmmThreadTC0 = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosX0+183, PosY0+290), size = (100, 23), style = wx.TE_CENTER)
        self.dmmLoopST0 = wx.StaticText(self, wx.ID_ANY, label = 'Loop：', pos = (PosX0+123, PosY0+330), size = (47, 20))
        self.dmmLoopTC0 = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (PosX0+183, PosY0+330), size = (100, 23), style = wx.TE_CENTER)
        #-----------------------------------------------------------------------------------------------
        PosX1 = 20+310
        PosY1 = 20
        
        SerialPortList1 = ['Choose a port']   
        self.DACompareSBox1 = wx.StaticBox(self, wx.ID_ANY, label = 'Load', pos = (PosX1, PosY1), size = (298, 247))

        self.SerialPortComboBox1 = wx.ComboBox(self, value = SerialPortList1[0], pos = (PosX1+11, PosY1+27), 
                        size = (200, 24), choices = SerialPortList1)
        
        self.OpenPort1 = wx.Button(self, label = 'Connect', pos = (PosX1+218, PosY1+27), size = (71, 23))       
        self.dmmStartST1 = wx.StaticText(self, wx.ID_ANY, label = 'Voltage Start Value', pos = (PosX1+15, PosY1+57), size = (161, 16))
        self.dmmStartTC1 = wx.TextCtrl(self, wx.ID_ANY, value = '0.9', pos = (PosX1+11, PosY1+75), size = (150, 23), style = wx.TE_CENTER)
        self.dmmEndST1 = wx.StaticText(self, wx.ID_ANY, label = 'Voltage End Value', pos = (PosX1+15, PosY1+103), size = (161, 16))
        self.dmmEndTC1 = wx.TextCtrl(self, wx.ID_ANY, value = '5.1', pos = (PosX1+11, PosY1+121), size = (150, 23), style = wx.TE_CENTER)
        self.dmmStepST1 = wx.StaticText(self, wx.ID_ANY, label = 'Voltage Step(mV)', pos = (PosX1+15, PosY1+149), size = (161, 16))
        self.dmmStepSC1 = wx.SpinCtrl(self, wx.ID_ANY, pos = (PosX1+11, PosY1+167), size = (153, 23), style = wx.TE_CENTER, min = 0, max = 1000000, initial = 2)
        self.dmmDelyTimeST1 = wx.StaticText(self, wx.ID_ANY, label = 'Delay Time(ms)', pos = (PosX1+15, PosY1+195), size = (161, 16))
        self.dmmDelyTimeTC1 = wx.TextCtrl(self, wx.ID_ANY, value = '500', pos = (PosX1+11, PosY1+213), size = (150, 23), style = wx.TE_CENTER)
        
        self.dmmAutoMeasureBtn1 = wx.Button(self, label = 'Auto Measure', pos = (PosX1+183, PosY1+75), size = (100, 23))
        self.dmmCMD1 = wx.StaticText(self, wx.ID_ANY, label = 'CMD', pos = (PosX1+183, PosY1+125), size = (31, 12))
        self.dmmCMD1.SetForegroundColour((0,0,255))
        self.dmmStopCB1 = wx.CheckBox(self, label = 'Stop', pos = (PosX1+183, PosY1+213), size = (58, 23))
        
        self.dmmLoopST1 = wx.StaticText(self, wx.ID_ANY, label = 'Loop：', pos = (PosX1+123, PosY1+330), size = (47, 20))
        self.dmmLoopTC1 = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (PosX1+183, PosY1+330), size = (100, 23), style = wx.TE_CENTER)
        #-----------------------------------------------------------------------------------------------
        PosX2 = 20+270
        PosY2 = 20
        
        SerialPortList2 = ['Choose a port'] 
        self.DACompareSBox2 = wx.StaticBox(self, wx.ID_ANY, label = 'Power Supply', pos = (PosX2+350, PosY2), size = (298, 247))
        
        self.SerialPortComboBox2 = wx.ComboBox(self, value = SerialPortList2[0], pos = (PosX2+361, PosY2+27), 
                        size = (200, 24), choices = SerialPortList2)
        
        self.OpenPort2 = wx.Button(self, label = 'Connect', pos = (PosX2+568, PosY2+27), size = (71, 23))
        self.dmmStartST2 = wx.StaticText(self, wx.ID_ANY, label = 'Voltage Start Value', pos = (PosX2+365, PosY2+57), size = (161, 16))
        self.dmmStartTC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0.0', pos = (PosX2+361, PosY2+75), size = (150, 23), style = wx.TE_CENTER)
        self.dmmEndST2 = wx.StaticText(self, wx.ID_ANY, label = 'Voltage End Value', pos = (PosX2+365, PosY2+103), size = (161, 16))
        self.dmmEndTC2 = wx.TextCtrl(self, wx.ID_ANY, value = '0.0', pos = (PosX2+361, PosY2+121), size = (150, 23), style = wx.TE_CENTER)
        self.dmmStepST2 = wx.StaticText(self, wx.ID_ANY, label = 'Voltage Step(mV)', pos = (PosX2+365, PosY2+149), size = (161, 16))
        self.dmmStepSC2 = wx.SpinCtrl(self, wx.ID_ANY, pos = (PosX2+361, PosY2+167), size = (153, 23), style = wx.TE_CENTER, min = 0, max = 1000000, initial = 1)
        self.dmmDelyTimeST2 = wx.StaticText(self, wx.ID_ANY, label = 'Delay Time(ms)', pos = (PosX2+365, PosY2+195), size = (161, 16))
        self.dmmDelyTimeTC2 = wx.TextCtrl(self, wx.ID_ANY, value = '500', pos = (PosX2+361, PosY2+213), size = (150, 23), style = wx.TE_CENTER)
        
        self.dmmAutoMeasureBtn2 = wx.Button(self, label = 'Auto Measure', pos = (PosX2+533, PosY2+75), size = (100, 23))
        self.dmmCMD2 = wx.StaticText(self, wx.ID_ANY, label = 'CMD', pos = (PosX2+533, PosY2+125), size = (31, 12))
        self.dmmCMD2.SetForegroundColour((0,0,255))
        self.dmmOutputBtn2 = wx.Button(self, label = 'OUTPUT', pos = (PosX2+533, PosY2+167), size = (100, 23))
        self.dmmStopCB2 = wx.CheckBox(self, label = 'Stop', pos = (PosX2+533, PosY2+213), size = (58, 23))
        
        self.dmmLoopST2 = wx.StaticText(self, wx.ID_ANY, label = 'Loop：', pos = (PosX2+473, PosY2+330), size = (47, 20))
        self.dmmLoopTC2 = wx.TextCtrl(self, wx.ID_ANY, value = '1', pos = (PosX2+533, PosY2+330), size = (100, 23), style = wx.TE_CENTER)
####################################################################################################
class WebCamPage(wx.Panel):
    """ Panel class that Page_5"""
    #-----------------------------------------------------------------------------------------------
    def __init__(self, title):       
        wx.Panel.__init__(self, title)
        PosX = 20
        PosY = 20
        BtnSize = (75, 23)
        BigBtnSize = (75, 46)
        STSize = (161, 16)
        TCSize = (150, 23)
        TunningTCSize = (45, 23)
        ScrollBarSize = (180, 23)
        
        self.WebCamSBox = wx.StaticBox(self, wx.ID_ANY, label = 'Camera', pos = (PosX, PosY), size = (520, 312))
        # Choose Camera and Open
        self.OpenWebCamBtn = wx.Button(self, wx.ID_ANY, label='Open', pos = (PosX+171, PosY+40), size = BtnSize)
        self.CamChooseST = wx.StaticText(self, wx.ID_ANY, label = 'Camera Choose(0~3)', pos = (PosX+11, PosY+20), size = STSize)
        self.CamChooseTC = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosX+11, PosY+40), size = TCSize, style = wx.TE_CENTER) 
        # Close Camera
        self.CloseWebCamBtn = wx.Button(self, wx.ID_ANY, label='Close', pos = (PosX+171, PosY+66), size = BtnSize)
        self.CloseWebCamBtn.Enable(False)
        # Mass Shooting
        self.PictureNameST = wx.StaticText(self, wx.ID_ANY, label = 'Pictrue Name', pos = (PosX+11, PosY+95), size = STSize)
        self.PictureNameTC = wx.TextCtrl(self, wx.ID_ANY, value = 'EV9', pos = (PosX+11, PosY+115), size = TCSize, style = wx.TE_CENTER)
        self.PictureQntST = wx.StaticText(self, wx.ID_ANY, label = 'Pictrue Quantity', pos = (PosX+11, PosY+140), size = STSize)
        self.PictureQntTC = wx.TextCtrl(self, wx.ID_ANY, value = '16', pos = (PosX+11, PosY+160), size = TCSize, style = wx.TE_CENTER)
        self.IntervalST = wx.StaticText(self, wx.ID_ANY, label = 'Shooting Interval(seconds)', pos = (PosX+11, PosY+185), size = STSize)
        self.IntervalTC = wx.TextCtrl(self, wx.ID_ANY, value = '0.5', pos = (PosX+11, PosY+205), size = TCSize, style = wx.TE_CENTER)        
        self.MassShotBtn = wx.Button(self, wx.ID_ANY, label= 'Mass\n Shooting', pos = (PosX+171, PosY+115), size = BigBtnSize)
        self.MassShotBtn.Enable(False)
        self.MassShotStopCB = wx.CheckBox(self, label = 'Stop', pos = (PosX+171, PosY+172), size = (58, 23))
        self.MassShotCMD = wx.StaticText(self, wx.ID_ANY, label = 'CMD', pos = (PosX+171, PosY+208), size = (31, 12))
        self.MassShotCMD.SetForegroundColour((0,0,255))
        # Single Shooting
        self.SingleShotST = wx.StaticText(self, wx.ID_ANY, label = 'Single Shooting', pos = (PosX+11, PosY+255), size = STSize)
        self.SingleShotTC = wx.TextCtrl(self, wx.ID_ANY, value = 'photo.jpg', pos = (PosX+11, PosY+275), size = TCSize, style = wx.TE_CENTER)
        self.SingleShotBtn = wx.Button(self, wx.ID_ANY, label= 'Single\n Shooting', pos = (PosX+171, PosY+255), size = BigBtnSize)
        self.SingleShotBtn.Enable(False)
        # Tunning Exposure 
        self.SetExposureTC = wx.TextCtrl(self, wx.ID_ANY, value = '-6', pos = (PosX+301, PosY+40), size = TunningTCSize, style = wx.TE_CENTER)
        self.SetExposureST = wx.StaticText(self, wx.ID_ANY, label = 'Exposure Value', pos = (PosX+351, PosY+43), size = STSize)
        self.SetExposureBar = wx.ScrollBar(self, wx.ID_ANY, pos = (PosX+301, PosY+70), size = ScrollBarSize,
                        style = wx.SB_HORIZONTAL)
        self.SetExposureBar.SetScrollbar(0, 0, 27, 1)
        self.SetExposureBar.Enable(False)
        # Tunning Contrast
        self.SetContrastTC = wx.TextCtrl(self, wx.ID_ANY, value = '0.0', pos = (PosX+301, PosY+100), size = TunningTCSize, style = wx.TE_CENTER)
        self.SetContrastST = wx.StaticText(self, wx.ID_ANY, label = 'Contrast Value', pos = (PosX+351, PosY+103), size = STSize)
        self.SetContrastBar = wx.ScrollBar(self, wx.ID_ANY, pos = (PosX+301, PosY+130), size = ScrollBarSize,
                        style = wx.SB_HORIZONTAL)
        self.SetContrastBar.SetScrollbar(0, 0, 10, 1)
        self.SetContrastBar.Enable(False)
        # Tunning Saturation
        self.SetSatTC = wx.TextCtrl(self, wx.ID_ANY, value = '0', pos = (PosX+301, PosY+160), size = TunningTCSize, style = wx.TE_CENTER)
        self.SetSatST = wx.StaticText(self, wx.ID_ANY, label = 'Saturation Value', pos = (PosX+351, PosY+163), size = STSize)
        self.SetSatBar = wx.ScrollBar(self, wx.ID_ANY, pos = (PosX+301, PosY+190), size = ScrollBarSize,
                        style = wx.SB_HORIZONTAL)
        self.SetSatBar.SetScrollbar(0, 0, 100, 1)
        self.SetSatBar.Enable(False)
        # Setting Default Value
        self.ReturnDefaultBtn = wx.Button(self, wx.ID_ANY, label='Default', pos = (PosX+301, PosY+220), size = BtnSize)
        self.ReturnDefaultBtn.Enable(False)
        # Get Default Value
        self.GetDefaultBtn = wx.Button(self, wx.ID_ANY, label='Get Default', pos = (PosX+406, PosY+220), size = BtnSize)
        self.GetDefaultBtn.Enable(False)
####################################################################################################
class PatternPage(wx.Panel):
    """ Panel class that Page_6"""
    #-----------------------------------------------------------------------------------------------
    def __init__(self, title):        
        wx.Panel.__init__(self, title)
        ST = wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft Sans Serif")
        TC = wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft Sans Serif")
        PosXp = 12
        PosYp = 12
        FileList = ['png', 'bmp']
        self.FileFormatRBox = wx.RadioBox(self, label = 'Format', pos = (PosXp, PosYp), size = (64, 74), 
                        choices = FileList, majorDimension = 1, style = wx.RA_SPECIFY_COLS)
        self.FileFormatRBox.SetSelection(0)
        #-----------------------------------------------------------------------------------------------
        PosXx = 12+80
        PosYx = 12       
        self.XtalkSBox = wx.StaticBox(self, wx.ID_ANY, label = 'Cross-talk', pos = (PosXx, PosYx), size = (202, 330))  
        self.XtalkBtn = wx.Button(self, wx.ID_ANY, label= 'Build', pos = (PosXx+114, PosYx+20), size = (75, 32))
        
        self.XtalkWST = wx.StaticText(self, wx.ID_ANY, label = 'Width：', pos = (PosXx+48, PosYx+64), size = (47, 20))
        self.XtalkWST.SetFont(ST)
        self.XtalkWTC = wx.TextCtrl(self, wx.ID_ANY, value = '1920', pos = (PosXx+108, PosYx+60), size = (81, 30), style = wx.TE_CENTER)
        self.XtalkWTC.SetFont(TC)
        
        self.XtalkHST = wx.StaticText(self, wx.ID_ANY, label = 'Height：', pos = (PosXx+41, PosYx+104), size = (47, 20))
        self.XtalkHST.SetFont(ST)       
        self.XtalkHTC = wx.TextCtrl(self, wx.ID_ANY, value = '1080', pos = (PosXx+108, PosYx+100), size = (81, 30), style = wx.TE_CENTER)
        self.XtalkHTC.SetFont(TC)
        
        self.XtalkRST = wx.StaticText(self, wx.ID_ANY, label = 'R', pos = (PosXx+70, PosYx+138), size = (27, 20))
        self.XtalkRST.SetForegroundColour((255,0,0))
        self.XtalkRTC = wx.TextCtrl(self, wx.ID_ANY, value = '127', pos = (PosXx+60, PosYx+158), size = (32, 23), style = wx.TE_CENTER)
        
        self.XtalkGST = wx.StaticText(self, wx.ID_ANY, label = 'G', pos = (PosXx+102, PosYx+138), size = (27, 20))
        self.XtalkGST.SetForegroundColour((0,255,0))
        self.XtalkGTC = wx.TextCtrl(self, wx.ID_ANY, value = '127', pos = (PosXx+92, PosYx+158), size = (32, 23), style = wx.TE_CENTER)
        
        self.XtalkBST = wx.StaticText(self, wx.ID_ANY, label = 'B', pos = (PosXx+134, PosYx+138), size = (27, 20))
        self.XtalkBST.SetForegroundColour((0,0,255))
        self.XtalkBTC = wx.TextCtrl(self, wx.ID_ANY, value = '127', pos = (PosXx+124, PosYx+158), size = (32, 23), style = wx.TE_CENTER)
        
        self.XtalkAST = wx.StaticText(self, wx.ID_ANY, label = 'A', pos = (PosXx+166, PosYx+138), size = (27, 20))
        self.XtalkATC = wx.TextCtrl(self, wx.ID_ANY, value = '255', pos = (PosXx+156, PosYx+158), size = (32, 23), style = wx.TE_CENTER)
        
        self.WriteWST = wx.StaticText(self, wx.ID_ANY, label = 'Square W：', pos = (PosXx+16, PosYx+202), size = (47, 20))
        self.WriteWST.SetFont(ST)
        self.WriteWTC = wx.TextCtrl(self, wx.ID_ANY, value = '540', pos = (PosXx+108, PosYx+198), size = (81, 30), style = wx.TE_CENTER)
        self.WriteWTC.SetFont(TC)
        
        self.WriteHST = wx.StaticText(self, wx.ID_ANY, label = 'Square H：', pos = (PosXx+16, PosYx+242), size = (47, 20))
        self.WriteHST.SetFont(ST)
        self.WriteHTC = wx.TextCtrl(self, wx.ID_ANY, value = '540', pos = (PosXx+108, PosYx+238), size = (81, 30), style = wx.TE_CENTER)
        self.WriteHTC.SetFont(TC)
        
        self.WriteRST = wx.StaticText(self, wx.ID_ANY, label = 'R', pos = (PosXx+70, PosYx+276), size = (27, 20))
        self.WriteRST.SetForegroundColour((255,0,0))
        self.WriteRTC = wx.TextCtrl(self, wx.ID_ANY, value = '255', pos = (PosXx+60, PosYx+296), size = (32, 23), style = wx.TE_CENTER)
        
        self.WriteGST = wx.StaticText(self, wx.ID_ANY, label = 'G', pos = (PosXx+102, PosYx+276), size = (27, 20))
        self.WriteGST.SetForegroundColour((0,255,0))
        self.WriteGTC = wx.TextCtrl(self, wx.ID_ANY, value = '255', pos = (PosXx+92, PosYx+296), size = (32, 23), style = wx.TE_CENTER)
        
        self.WriteBST = wx.StaticText(self, wx.ID_ANY, label = 'B', pos = (PosXx+134, PosYx+276), size = (27, 20))
        self.WriteBST.SetForegroundColour((0,0,255))
        self.WriteBTC = wx.TextCtrl(self, wx.ID_ANY, value = '255', pos = (PosXx+124, PosYx+296), size = (32, 23), style = wx.TE_CENTER)
        
        self.WriteAST = wx.StaticText(self, wx.ID_ANY, label = 'A', pos = (PosXx+166, PosYx+276), size = (27, 20))
        self.WriteATC = wx.TextCtrl(self, wx.ID_ANY, value = '255', pos = (PosXx+156, PosYx+296), size = (32, 23), style = wx.TE_CENTER)
####################################################################################################
class MyLogView(wx.Frame):
    """
    Frame class that shows log message.
    """
    #-----------------------------------------------------------------------------------------------
    def __init__(self, title):
        super().__init__(parent = None, title = title, size = (342, 446))
        self.log = wx.Panel(self)
        
        self.textTC = wx.TextCtrl(self.log, wx.ID_ANY, style = wx.TE_MULTILINE, pos = (2, 24), size = (322, 381))
        self.textTC.SetEditable(False)
        
        save = wx.Bitmap('UD_Icon/save.png', wx.BITMAP_TYPE_PNG)
        self.LVSaveBtn = wx.BitmapButton(self.log, wx.ID_ANY, bitmap = save, pos = (4, 2), size = (20, 22))
        clear = wx.Bitmap('UD_Icon/clear.png', wx.BITMAP_TYPE_PNG)
        self.LVClearBtn = wx.BitmapButton(self.log, wx.ID_ANY, bitmap = clear, pos = (26, 2), size = (20, 22))       
####################################################################################################
class MyFrame(wx.Frame):
    """
    Frame class that holds all other widgets.
    """
    #-----------------------------------------------------------------------------------------------
    def __init__(self, title):
        super().__init__(parent = None, title = title, size = (986, 556)) 
        self.panel = wx.Panel(self)
        
        # Create the menu bar
        self.menubar = wx.MenuBar()
        # Create the Setting menu
        self.setting_menu = wx.Menu()
        self.menubar.Append(self.setting_menu, 'Setting')
        self.SetI2CItem = self.setting_menu.Append(wx.ID_ANY, 'I2C', kind = wx.ITEM_RADIO)
        self.SetSPIItem = self.setting_menu.Append(wx.ID_ANY, 'SPI', kind = wx.ITEM_RADIO)
        self.SetI2CItem.Check(True)
        # Create the Log menu
        #self.Log_menu = wx.Menu()
        #self.menubar.Append(self.Log_menu, 'Log')
        #self.LogShowItem = self.Log_menu.Append(wx.ID_ANY, 'Show', kind = wx.ITEM_CHECK)
        # Create the Help menu
        self.help_menu = wx.Menu()
        self.menubar.Append(self.help_menu, 'Help')
        self.HelpItem = self.help_menu.Append(wx.ID_HELP, 'About HotKey')
        # Set the menu bar for the frame
        self.SetMenuBar(self.menubar)
        
        # Create the status bar
        self.statusbar = self.CreateStatusBar()
        # Set text in the status bar        
        self.statusbar.SetStatusText('This is the status bar message', 0)
        # Create the progress bar
        self.progressbar = wx.Gauge(self.statusbar, wx.ID_ANY, range=100, size = (-1,-1), pos = (554, 4), style = wx.GA_HORIZONTAL)
        # Set the initial progress value
        self.progressbar.SetValue(0)
        # Set the number of fields and width of the status bar
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([-1, 200])
        #-----------------------------------------------------------------------------------------------
        self.SWConnectSBox = wx.StaticBox(self.panel, wx.ID_ANY, label = 'SW Connect', pos = (5, 5), size = (546, 51)) 
        
        self.SWOnRBtn = wx.RadioButton(self.panel, wx.ID_ANY, label = 'ON', pos = (14, 24), size = (50, 24), style = wx.RB_GROUP)
        self.SWOnRBtn.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft Sans Serif"))
        self.SWOnRBtn.SetValue(False)  
                
        self.SWOffRBtn = wx.RadioButton(self.panel, wx.ID_ANY, label = 'OFF', pos = (65, 24), size = (50, 24))
        self.SWOffRBtn.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft Sans Serif"))
        self.SWOffRBtn.SetForegroundColour((255,0,0))          
        self.SWOffRBtn.SetValue(True)                       
        
        self.RefreshButton = wx.Button(self.panel, label = 'Refresh', pos = (121, 23), size = (57, 24))       
        DeviceList = ['Choose a Usb Device'] 
        self.DeviceComboBox = wx.ComboBox(self.panel, value = DeviceList[0], pos = (182, 23), 
                        size = (355, 24), choices = DeviceList)                
               
        #self.ICResetButton = wx.Button(self.panel, label = 'IC Reset', pos = (567, 12), size = (111, 43))
        #self.ICResetButton.SetBackgroundColour((130, 208, 106))
        self.FPGAResetBtn = wx.Button(self.panel, label = 'FPGA Reset', pos = (567, 16), size = (90, 33))
        self.FPGAResetBtn.SetBackgroundColour((130, 208, 106))
        self.SPIBypassBtn = wx.Button(self.panel, label = 'SPI Bypass', pos = (667, 16), size = (90, 33))
        self.SPIBypassBtn.SetBackgroundColour((106, 130, 208))       
        
        self.nb = wx.Notebook(self.panel, pos = (1, 60), size = (970, 437))     
        self.TabPage = ['Base','Test','SRAM','Flash','DMM/Load/PS','WebCam','Pattern']
        pages = [BasePage(self.nb), TestPage(self.nb), SRAMPage(self.nb), FlashPage(self.nb), DMMPage(self.nb), WebCamPage(self.nb), PatternPage(self.nb)]
        for index, page in enumerate(pages):
            if page is not None:
                setattr(self, f"Page_{index}", page)
                self.nb.AddPage(page, self.TabPage[index])
        
        self.logframe = MyLogView('LogView')
        self.logframe.SetIcon(wx.Icon('UD_Icon/LogView.ico'))
        self.HK_LogView = wx.NewIdRef()
        self.HK_EnablePage = wx.NewIdRef()
        self.RegisterHotKey(self.HK_LogView, wx.MOD_ALT, ord('L'))
        self.RegisterHotKey(self.HK_EnablePage, wx.MOD_ALT, ord('E'))
        #-----------------------------------------------------------------------------------------------      
        self.Bind(wx.EVT_HOTKEY, self.HotkeyLogViewEvent, id = self.HK_LogView)
        self.Bind(wx.EVT_HOTKEY, self.HotkeyEnablePageEvent, id = self.HK_EnablePage)
        self.Bind(wx.EVT_MENU, self.SetI2CItemEvent, self.SetI2CItem)
        self.Bind(wx.EVT_MENU, self.SetSPIItemEvent, self.SetSPIItem)
        self.Bind(wx.EVT_MENU, self.HelpItemEvent, self.HelpItem)
        
        self.DeviceComboBox.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.FrameComboBoxDropdownEvent) 
        self.DeviceComboBox.Bind(wx.EVT_COMBOBOX, self.FrameComboBoxEvent) 
        self.RefreshButton.Bind(wx.EVT_BUTTON, self.RefreshButtonEvent)
        self.SWOnRBtn.Bind(wx.EVT_RADIOBUTTON, self.SWConnectEvent) 
        self.SWOffRBtn.Bind(wx.EVT_RADIOBUTTON, self.SWConnectEvent)
        #self.ICResetButton.Bind(wx.EVT_BUTTON, self.ICResetButtonEvent)
        self.FPGAResetBtn.Bind(wx.EVT_BUTTON, self.FPGAResetBtnEvent)
        self.SPIBypassBtn.Bind(wx.EVT_BUTTON, self.SPIBypassBtnEvent)        
        
        self.Page_0.MulitWr1.Bind(wx.EVT_BUTTON, self.MulitWr1Event)      
        self.Page_0.MulitWr2.Bind(wx.EVT_BUTTON, self.MulitWr2Event)
        self.Page_0.MulitWr3.Bind(wx.EVT_BUTTON, self.MulitWr3Event)
        self.Page_0.MulitWr4.Bind(wx.EVT_BUTTON, self.MulitWr4Event)
        self.Page_0.MulitWr5.Bind(wx.EVT_BUTTON, self.MulitWr5Event)
        self.Page_0.MulitWr6.Bind(wx.EVT_BUTTON, self.MulitWr6Event)
        self.Page_0.MulitWr7.Bind(wx.EVT_BUTTON, self.MulitWr7Event)
        self.Page_0.MulitRd1.Bind(wx.EVT_BUTTON, self.MulitRd1Event)
        self.Page_0.MulitRd2.Bind(wx.EVT_BUTTON, self.MulitRd2Event)
        self.Page_0.MulitRd3.Bind(wx.EVT_BUTTON, self.MulitRd3Event)
        self.Page_0.MulitRd4.Bind(wx.EVT_BUTTON, self.MulitRd4Event) 
        self.Page_0.MulitRd5.Bind(wx.EVT_BUTTON, self.MulitRd5Event)
        self.Page_0.MulitRd6.Bind(wx.EVT_BUTTON, self.MulitRd6Event) 
        self.Page_0.MulitRd7.Bind(wx.EVT_BUTTON, self.MulitRd7Event)
        
        text_controls = [self.Page_0.Data0TC1, 
        self.Page_0.Data1TC1, self.Page_0.Data2TC1, self.Page_0.Data3TC1, self.Page_0.Data4TC1, 
        self.Page_0.Data5TC1, self.Page_0.Data6TC1, self.Page_0.Data7TC1, self.Page_0.Data8TC1, 
        self.Page_0.Data9TC1, self.Page_0.Data10TC1, self.Page_0.Data0TC2, self.Page_0.Data1TC2, 
        self.Page_0.Data2TC2, self.Page_0.Data3TC2, self.Page_0.Data4TC2, self.Page_0.Data5TC2, 
        self.Page_0.Data6TC2, self.Page_0.Data7TC2, self.Page_0.Data8TC2, self.Page_0.Data9TC2, 
        self.Page_0.Data10TC2, self.Page_0.Data0TC3, self.Page_0.Data1TC3, self.Page_0.Data2TC3, 
        self.Page_0.Data3TC3, self.Page_0.Data4TC3, self.Page_0.Data5TC3, self.Page_0.Data6TC3, 
        self.Page_0.Data7TC3, self.Page_0.Data8TC3, self.Page_0.Data9TC3, self.Page_0.Data10TC3, 
        self.Page_0.Data0TC4, self.Page_0.Data1TC4, self.Page_0.Data2TC4, self.Page_0.Data3TC4, 
        self.Page_0.Data4TC4, self.Page_0.Data5TC4, self.Page_0.Data6TC4, self.Page_0.Data7TC4,
        self.Page_0.Data8TC4, self.Page_0.Data9TC4, self.Page_0.Data10TC4, self.Page_0.Data0TC5, 
        self.Page_0.Data1TC5, self.Page_0.Data2TC5, self.Page_0.Data3TC5, self.Page_0.Data4TC5,
        self.Page_0.Data5TC5, self.Page_0.Data6TC5, self.Page_0.Data7TC5, self.Page_0.Data8TC5, 
        self.Page_0.Data9TC5, self.Page_0.Data10TC5, self.Page_0.Data0TC6, self.Page_0.Data1TC6, 
        self.Page_0.Data2TC6, self.Page_0.Data3TC6, self.Page_0.Data4TC6, self.Page_0.Data5TC6, 
        self.Page_0.Data6TC6, self.Page_0.Data7TC6, self.Page_0.Data8TC6, self.Page_0.Data9TC6, 
        self.Page_0.Data10TC6, self.Page_0.Data0TC7, self.Page_0.Data1TC7, self.Page_0.Data2TC7,
        self.Page_0.Data3TC7, self.Page_0.Data4TC7, self.Page_0.Data5TC7, self.Page_0.Data6TC7, 
        self.Page_0.Data7TC7, self.Page_0.Data8TC7, self.Page_0.Data9TC7, self.Page_0.Data10TC7]    
        for control in text_controls:
            control.Bind(wx.EVT_TEXT, lambda event, ctrl=control: self.CMDparaGrop(event, ctrl))
            control.Bind(wx.EVT_LEFT_DCLICK, lambda event, ctrl=control: self.CMDparaGropDclick(event, ctrl))

        self.Page_0.GPIO_0RBox.Bind(wx.EVT_RADIOBOX, self.GPIO_0RBoxEvent)
        self.Page_0.GPIO_1RBox.Bind(wx.EVT_RADIOBOX, self.GPIO_1RBoxEvent)
        self.Page_0.GPIO_2RBox.Bind(wx.EVT_RADIOBOX, self.GPIO_2RBoxEvent)
        self.Page_0.GPIO_3RBox.Bind(wx.EVT_RADIOBOX, self.GPIO_3RBoxEvent)
        self.Page_0.OpenIniBtn.Bind(wx.EVT_BUTTON, self.OpenIniBtnEvent)
        self.Page_0.LoadIniBtn.Bind(wx.EVT_BUTTON, self.LoadIniBtnEvent)
        
        self.Page_1.ThreadBtn.Bind(wx.EVT_BUTTON, self.TestThreadBtnEvent)
        self.Page_1.InputBtn.Bind(wx.EVT_BUTTON, self.TestInputBtnEvent)
        self.Page_2.SARMWr.Bind(wx.EVT_BUTTON, self.SARMWrEvent)
        self.Page_2.SARMRd.Bind(wx.EVT_BUTTON, self.SARMRdEvent)
        
        self.Page_3.FlashIDRd.Bind(wx.EVT_BUTTON, self.FlashIDRdEvent)
        self.Page_3.FlashErase.Bind(wx.EVT_BUTTON, self.FlashEraseEvent)              
        self.Page_3.OpenFileBtn.Bind(wx.EVT_BUTTON, self.OpenFileBtnEvent)
        self.Page_3.WriteFileBtn.Bind(wx.EVT_BUTTON, self.WriteFileBtnEvent)
        self.Page_3.ReadFileBtn.Bind(wx.EVT_BUTTON, self.ReadFileBtnEvent)
        self.Page_3.ReadStatusBtn.Bind(wx.EVT_BUTTON, self.ReadStatusBtnEvent)
                       
        self.Page_4.SerialPortComboBox0.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.Page2ComboBox0DropdownEvent)
        self.Page_4.SerialPortComboBox0.Bind(wx.EVT_COMBOBOX, self.Page2ComboBox0Event)
        self.Page_4.OpenPort0.Bind(wx.EVT_BUTTON, self.OpenPort0Event)
        self.Page_4.dmmAutoMeasureBtn0.Bind(wx.EVT_BUTTON, self.dmmAutoMeasure0Event) 
        self.Page_4.dmmThreadBtn0.Bind(wx.EVT_BUTTON, self.dmmThread0Event)
        self.Page_4.SerialPortComboBox1.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.Page2ComboBox1DropdownEvent)
        self.Page_4.SerialPortComboBox1.Bind(wx.EVT_COMBOBOX, self.Page2ComboBox1Event)
        self.Page_4.OpenPort1.Bind(wx.EVT_BUTTON, self.OpenPort1Event)
        self.Page_4.dmmAutoMeasureBtn1.Bind(wx.EVT_BUTTON, self.dmmAutoMeasure1Event) 
        self.Page_4.SerialPortComboBox2.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.Page2ComboBox2DropdownEvent)
        self.Page_4.SerialPortComboBox2.Bind(wx.EVT_COMBOBOX, self.Page2ComboBox2Event)
        self.Page_4.OpenPort2.Bind(wx.EVT_BUTTON, self.OpenPort2Event)
        self.Page_4.dmmAutoMeasureBtn2.Bind(wx.EVT_BUTTON, self.dmmAutoMeasure2Event)
        self.Page_4.dmmOutputBtn2.Bind(wx.EVT_BUTTON, self.dmmOutput2Event) 
        
        self.Page_5.OpenWebCamBtn.Bind(wx.EVT_BUTTON, self.OpenWebCamEvent)
        self.Page_5.CloseWebCamBtn.Bind(wx.EVT_BUTTON, self.CloseWebCamEvent)
        self.Page_5.MassShotBtn.Bind(wx.EVT_BUTTON, self.MassShootingEvent)
        self.Page_5.MassShotStopCB.Bind(wx.EVT_CHECKBOX, self.MassShotStopEvent)
        self.Page_5.SingleShotBtn.Bind(wx.EVT_BUTTON, self.SingleShootingEvent)

        # Web Cam Tunning: Exposure Contrast Saturation
        self.Page_5.SetExposureBar.Bind(wx.EVT_SCROLL, self.SetExposureEvent)
        self.Page_5.SetContrastBar.Bind(wx.EVT_SCROLL, self.SetContrastEvent)
        self.Page_5.SetSatBar.Bind(wx.EVT_SCROLL, self.SetSatEvent)
        self.Page_5.ReturnDefaultBtn.Bind(wx.EVT_BUTTON, self.ReturnDefaultEvent)
        self.Page_5.GetDefaultBtn.Bind(wx.EVT_BUTTON, self.GetDefaultEvent)
        
        self.Page_6.XtalkBtn.Bind(wx.EVT_BUTTON, self.XtalkBuildEvent)
        
        self.logframe.LVSaveBtn.Bind(wx.EVT_BUTTON, self.ToolScriptSaveEvent)
        self.logframe.LVClearBtn.Bind(wx.EVT_BUTTON, self.ToolScriptClearEvent)
        self.logframe.textTC.Bind(wx.EVT_LEFT_DCLICK, self.ToolScriptClearEvent)
        self.logframe.Bind(wx.EVT_CLOSE, self.LogViewOnClose)
#------------------------------------------------------------------------------------------
#EOF             