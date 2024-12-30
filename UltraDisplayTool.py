####################################################################################################
#
#
# Note: Any version of python 3.10
# Release Date: 2024/04/03
####################################################################################################
""" UltraDisplay Library Import """
import UD_Package.UD_FT4222_I2C
import UD_Package.UD_FT4222_SPI
import UD_Package.UD_Instrument
import UD_Package.WebCam
import UD_GUI
#---------------------------------------------------------------------------------------------------
""" Library Import """
import csv
import datetime
from decimal import Decimal
from PIL import Image
import pyvisa
import threading
import time
import random
import re
import wx
#---------------------------------------------------------------------------------------------------
""" Global variables """
UD_ToolName = 'UltraDisplayTool_V0'
write_data_list = []
####################################################################################################
""" Class Definition """ 
class UDFrame(UD_GUI.MyFrame):    
    #""" Frame Event """----------------------------------------------------------------------------            
    def __init__(self,title):       
        UD_GUI.MyFrame.__init__(self, title)
        print(UD_ToolName+'.exe Loaded.')
        # GUI Loaded function
        UDFrame.Page_Disable(self)
        UDFrame.SettingINI(self) 
        # Update the progress bar.
        self.UpdateProgress(0)
        # GUI Close event
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        
        # Create wxConfig instance
        self.config = wx.Config()
        # Load the setting
        setting = self.config.ReadInt('SETTING', -1)
        if setting == wx.ID_NONE:
            self.SetI2CItem.Check(True)
        elif setting == wx.ID_ANY:
            self.SetSPIItem.Check(True)
            
    def OnClose(self, event):
        if self.SetI2CItem.IsChecked():
            try:
                UD_Package.UD_FT4222_I2C.i2c_Close()
                print('Interface: I2C Closed.')
            except Exception:
                pass                
        elif self.SetSPIItem.IsChecked():
            try:                
                UD_Package.UD_FT4222_SPI.spi_Close()
                print('Interface: SPI Closed.')
            except Exception:
                pass                        
        else:
            print('Nothing to do.')
        print(UD_ToolName+'.exe Closed.')
        KillThread()
        UDFrame.SaveAPSetting(self)
        self.UnregisterHotKey(self.HK_LogView)
        self.UnregisterHotKey(self.HK_EnablePage)
        self.Destroy()
        app.ExitMainLoop() # Exit the main event loop                 
        
    def SWConnectEvent(self, event):       
        if event.GetEventObject() == self.SWOnRBtn:
            if 'FT' in self.DeviceComboBox.GetValue():
                if self.SetI2CItem.IsChecked():
                    try:                       
                        UD_Package.UD_FT4222_I2C.i2c_Init(0)
                        self.statusbar.SetStatusText(' Interface: I2C', 0)
                        print('[SW On] Interface: I2C Initial.')
                        UDFrame.LogP(self, 'Interface: I2C Initial.')
                    except Exception as e:
                        self.statusbar.SetStatusText('I2C open fail.', 0)
                        print(f'[Error] {str(e)}')
                        UDFrame.LogP(self, '[Error] I2C open fail.')
                elif self.SetSPIItem.IsChecked():
                    try:                       
                        UD_Package.UD_FT4222_SPI.spi_Init(0)
                        self.statusbar.SetStatusText(' Interface: SPI', 0)
                        print('[SW On] Interface: SPI Initial.')
                        UDFrame.LogP(self, 'Interface: SPI Initial.')
                    except Exception as e:
                        self.statusbar.SetStatusText('SPI open fail.', 0)
                        print(f'[Error] {str(e)}')
                        UDFrame.LogP(self, '[Error] SPI open fail.')
                else:
                    print('[SW On]')
                UDFrame.Page_Enable(self)
                self.SWOnRBtn.SetForegroundColour((255,0,0))
                self.SWOffRBtn.SetForegroundColour((0,0,0))
                #UD_Thread.FT4222_GPIO_Thread()
            else:
                self.SWOffRBtn.SetValue(True)                
                wx.MessageBox('No Connect HW , Refresh device', 
                                'Message Box', wx.OK| wx.ICON_INFORMATION)
            
        elif event.GetEventObject() == self.SWOffRBtn:          
            if self.SetI2CItem.IsChecked():
                try:
                    UD_Package.UD_FT4222_I2C.i2c_Close()
                    self.statusbar.SetStatusText(' Interface Closed.', 0)
                    print('[SW Off] Interface: I2C Closed.')
                    UDFrame.LogP(self, 'Interface: I2C Closed.')
                except Exception as e:
                    self.statusbar.SetStatusText(' Interface closed fail.', 0)
                    print(f'[Error] {str(e)}')
                    UDFrame.LogP(self, '[Error] I2C closed fail.')
            elif self.SetSPIItem.IsChecked():
                try:
                    UD_Package.UD_FT4222_SPI.spi_Close()
                    self.statusbar.SetStatusText(' Interface Closed.', 0)
                    print('[SW Off] Interface: SPI Closed.')
                    UDFrame.LogP(self, 'Interface: SPI Closed.')
                except Exception as e:
                    self.statusbar.SetStatusText(' Interface closed fail.', 0)
                    print(f'[Error] {str(e)}') 
                    UDFrame.LogP(self, '[Error] SPI closed fail.')                       
            else:
                print('[SW Off]')           
            UDFrame.Page_Disable(self)
            self.SWOffRBtn.SetForegroundColour((255,0,0))
            self.SWOnRBtn.SetForegroundColour((0,0,0))
            #UD_Package.UD_FT4222_I2C.FT4222_GPIO_Stop()
                
    def RefreshButtonEvent(self, event):
        try:
            self.DeviceComboBox.Clear()
            PortList = UD_Package.UD_FT4222_I2C.FT4222_USB()
            self.DeviceComboBox.Append(PortList)
            self.DeviceComboBox.SetSelection(0)
            print(self.DeviceComboBox.GetValue())
        except ValueError:
            print('The device has no langid.')
        
    def FrameComboBoxDropdownEvent(self, event):
        try:
            self.DeviceComboBox.Clear()
            PortList = UD_Package.UD_FT4222_I2C.FT4222_USB()
            self.DeviceComboBox.Append(PortList) 
        except ValueError:
            print('The device has no langid.')                  
        
    def FrameComboBoxEvent(self, event):
        print(self.DeviceComboBox.GetValue())
        
    def ICResetButtonEvent(self, event):
        self.ICResetButton.Enable(False)
        #try:
        print('Nothing to do.')
        #except Exception as e:
            #print('[Error]', e)
        self.ICResetButton.Enable(True)
 
    def FPGAResetBtnEvent(self, event):
        self.FPGAResetBtn.Enable(False)
        try:
            UD_Package.UD_FT4222_I2C.fpga_Reset()
            print('FPGA Reset Finish.')
            UDFrame.LogP(self, 'FPGA Reset Finish.')
        except Exception as e:
            print(f'[Error] {str(e)}')
            UDFrame.LogP(self, f'[Error] {str(e)}')
        self.FPGAResetBtn.Enable(True)
        
    def SPIBypassBtnEvent(self, event):
        self.SPIBypassBtn.Enable(False)
        try:
            status = UD_Package.UD_FT4222_I2C.spi_ByPass()
            if status == 1:
                print('SPI By Pass is High.')
                UDFrame.LogP(self, 'SPI By Pass is High.')
            else:
                print('SPI By Pass is Low.')
                UDFrame.LogP(self, 'SPI By Pass is Low.')
        except Exception as e:
            print(f'[Error] {str(e)}')
            UDFrame.LogP(self, f'[Error] {str(e)}')
        self.SPIBypassBtn.Enable(True)        
        
    def SetI2CItemEvent(self, event):
        if self.SWOffRBtn.GetValue() == True:
            self.config.WriteInt('SETTING', wx.ID_NONE)
            self.SetI2CItem.Check(True)
            print('Switch Interface: I2C')
        else:
            self.SetSPIItem.Check(True)
            print('Click the SW Connect Off and try again.')
               
    def SetSPIItemEvent(self, event):
        if self.SWOffRBtn.GetValue() == True:
            self.config.WriteInt('SETTING', wx.ID_ANY)
            self.SetSPIItem.Check(True)
            print('Switch Interface: SPI')
        else:
            self.SetI2CItem.Check(True)
            print('Click the SW Connect Off and try again.')
               
    def HelpItemEvent(self, event):
        wx.MessageBox('Alt + E = Enable Page\nAlt + L = LogView Show',
                                'Help', wx.OK|wx.ICON_INFORMATION)   
        
    def HotkeyLogViewEvent(self, event):
        try:
            if self.logframe.IsShown():
                print('Alt + L: LogView hide.')
                self.logframe.Hide()
            else:
                print('Alt + L: LogView show.')
                self.logframe.Show()
        except Exception as e:
            print(f'[Error] {str(e)}')
            
    def HotkeyEnablePageEvent(self, event):
        print('Alt + E: Enable Page.')
        UDFrame.Page_Enable(self)
        self.SWOnRBtn.SetValue(True)
        self.SWOffRBtn.SetValue(False)
    
    def Page_Enable(self):
        self.Page_0.Enable(True)
        self.Page_2.Enable(True)
        self.Page_3.Enable(True)
        self.Page_4.Enable(True)
        self.Page_5.Enable(True)
        self.Page_6.Enable(True)
        
    def Page_Disable(self):
        self.Page_0.Enable(False)
        self.Page_2.Enable(False)
        self.Page_3.Enable(False)
        self.Page_4.Enable(False)
        self.Page_5.Enable(False)
        self.Page_6.Enable(False)            
        
    def SettingINI(self):
        IniBuf = {}
        PosIndex = 0
        path = 'Setting.ini'
        try:
            with open(path, 'r') as f:
                for line in f:
                    PosIndex+=1                                                      
                    if line != None: 
                        IniBuf[PosIndex] = line 
              
            for IndexExe in range(1,PosIndex+1):
                if IniBuf != None:
                    SplitExe = re.split(' |,', IniBuf[IndexExe])
                    
                    match SplitExe[0]:
                        case 'CONFIG':                            
                            if SplitExe[7] !='1':
                                self.nb.RemovePage(6)
                                del self.TabPage[6]
                            if SplitExe[6] !='1':
                                self.nb.RemovePage(5)
                                del self.TabPage[5]                            
                            if SplitExe[5] !='1':
                                self.nb.RemovePage(4)
                                del self.TabPage[4]                           
                            if SplitExe[4] !='1':
                                self.nb.RemovePage(3)
                                del self.TabPage[3]
                            if SplitExe[3] !='1':
                                self.nb.RemovePage(2)
                                del self.TabPage[2]
                            if SplitExe[2] !='1':
                                self.nb.RemovePage(1)
                                del self.TabPage[1]
                            if SplitExe[1] !='1':
                                self.nb.RemovePage(0)
                                del self.TabPage[0]
                                                                                    
                        case 'P1DATA0':
                            self.Page_0.Data0TC1.SetValue(SplitExe[1])
                            self.Page_0.Parabox1.SetValue(SplitExe[2])
                            self.Page_0.Data1TC1.SetValue(SplitExe[3])
                            self.Page_0.Data2TC1.SetValue(SplitExe[4])
                            self.Page_0.Data3TC1.SetValue(SplitExe[5])
                            self.Page_0.Data4TC1.SetValue(SplitExe[6])
                            self.Page_0.Data5TC1.SetValue(SplitExe[7])
                            self.Page_0.Data6TC1.SetValue(SplitExe[8])
                            self.Page_0.Data7TC1.SetValue(SplitExe[9])
                            self.Page_0.Data8TC1.SetValue(SplitExe[10])
                            self.Page_0.Data9TC1.SetValue(SplitExe[11])
                            self.Page_0.Data10TC1.SetValue(SplitExe[12])
                        case 'P2DATA0':
                            self.Page_0.Data0TC2.SetValue(SplitExe[1])
                            self.Page_0.Parabox2.SetValue(SplitExe[2])
                            self.Page_0.Data1TC2.SetValue(SplitExe[3])
                            self.Page_0.Data2TC2.SetValue(SplitExe[4])
                            self.Page_0.Data3TC2.SetValue(SplitExe[5])
                            self.Page_0.Data4TC2.SetValue(SplitExe[6])
                            self.Page_0.Data5TC2.SetValue(SplitExe[7])
                            self.Page_0.Data6TC2.SetValue(SplitExe[8])
                            self.Page_0.Data7TC2.SetValue(SplitExe[9])
                            self.Page_0.Data8TC2.SetValue(SplitExe[10])
                            self.Page_0.Data9TC2.SetValue(SplitExe[11])
                            self.Page_0.Data10TC2.SetValue(SplitExe[12])
                        case 'P3DATA0':
                            self.Page_0.Data0TC3.SetValue(SplitExe[1])
                            self.Page_0.Parabox3.SetValue(SplitExe[2])
                            self.Page_0.Data1TC3.SetValue(SplitExe[3])
                            self.Page_0.Data2TC3.SetValue(SplitExe[4])
                            self.Page_0.Data3TC3.SetValue(SplitExe[5])
                            self.Page_0.Data4TC3.SetValue(SplitExe[6])
                            self.Page_0.Data5TC3.SetValue(SplitExe[7])
                            self.Page_0.Data6TC3.SetValue(SplitExe[8])
                            self.Page_0.Data7TC3.SetValue(SplitExe[9])
                            self.Page_0.Data8TC3.SetValue(SplitExe[10])
                            self.Page_0.Data9TC3.SetValue(SplitExe[11])
                            self.Page_0.Data10TC3.SetValue(SplitExe[12])
                        case 'P4DATA0':
                            self.Page_0.Data0TC4.SetValue(SplitExe[1])
                            self.Page_0.Parabox4.SetValue(SplitExe[2])
                            self.Page_0.Data1TC4.SetValue(SplitExe[3])
                            self.Page_0.Data2TC4.SetValue(SplitExe[4])
                            self.Page_0.Data3TC4.SetValue(SplitExe[5])
                            self.Page_0.Data4TC4.SetValue(SplitExe[6])
                            self.Page_0.Data5TC4.SetValue(SplitExe[7])
                            self.Page_0.Data6TC4.SetValue(SplitExe[8])
                            self.Page_0.Data7TC4.SetValue(SplitExe[9])
                            self.Page_0.Data8TC4.SetValue(SplitExe[10])
                            self.Page_0.Data9TC4.SetValue(SplitExe[11])
                            self.Page_0.Data10TC4.SetValue(SplitExe[12])
                        case 'P5DATA0':
                            self.Page_0.Data0TC5.SetValue(SplitExe[1])
                            self.Page_0.Parabox5.SetValue(SplitExe[2])
                            self.Page_0.Data1TC5.SetValue(SplitExe[3])
                            self.Page_0.Data2TC5.SetValue(SplitExe[4])
                            self.Page_0.Data3TC5.SetValue(SplitExe[5])
                            self.Page_0.Data4TC5.SetValue(SplitExe[6])
                            self.Page_0.Data5TC5.SetValue(SplitExe[7])
                            self.Page_0.Data6TC5.SetValue(SplitExe[8])
                            self.Page_0.Data7TC5.SetValue(SplitExe[9])
                            self.Page_0.Data8TC5.SetValue(SplitExe[10])
                            self.Page_0.Data9TC5.SetValue(SplitExe[11])
                            self.Page_0.Data10TC5.SetValue(SplitExe[12])
                        case 'P6DATA0':
                            self.Page_0.Data0TC6.SetValue(SplitExe[1])
                            self.Page_0.Parabox6.SetValue(SplitExe[2])
                            self.Page_0.Data1TC6.SetValue(SplitExe[3])
                            self.Page_0.Data2TC6.SetValue(SplitExe[4])
                            self.Page_0.Data3TC6.SetValue(SplitExe[5])
                            self.Page_0.Data4TC6.SetValue(SplitExe[6])
                            self.Page_0.Data5TC6.SetValue(SplitExe[7])
                            self.Page_0.Data6TC6.SetValue(SplitExe[8])
                            self.Page_0.Data7TC6.SetValue(SplitExe[9])
                            self.Page_0.Data8TC6.SetValue(SplitExe[10])
                            self.Page_0.Data9TC6.SetValue(SplitExe[11])
                            self.Page_0.Data10TC6.SetValue(SplitExe[12])
                        case 'P7DATA0':
                            self.Page_0.Data0TC7.SetValue(SplitExe[1])
                            self.Page_0.Parabox7.SetValue(SplitExe[2])
                            self.Page_0.Data1TC7.SetValue(SplitExe[3])
                            self.Page_0.Data2TC7.SetValue(SplitExe[4])
                            self.Page_0.Data3TC7.SetValue(SplitExe[5])
                            self.Page_0.Data4TC7.SetValue(SplitExe[6])
                            self.Page_0.Data5TC7.SetValue(SplitExe[7])
                            self.Page_0.Data6TC7.SetValue(SplitExe[8])
                            self.Page_0.Data7TC7.SetValue(SplitExe[9])
                            self.Page_0.Data8TC7.SetValue(SplitExe[10])
                            self.Page_0.Data9TC7.SetValue(SplitExe[11])
                            self.Page_0.Data10TC7.SetValue(SplitExe[12])
                        case 'SCRIPT':
                            self.Page_0.PathST.SetLabel(WrapStr(SplitExe[1],82))
                            self.Page_0.ScriptLoopTC.SetValue(SplitExe[2])
                        case 'SRAMEX':                            
                            self.Page_2.E1data1TC.SetValue(SplitExe[1])
                            self.Page_2.E2para0TC.SetValue(SplitExe[2])
                            self.Page_2.E2data1TC.SetValue(SplitExe[3])
                            self.Page_2.E2data2TC.SetValue(SplitExe[4])
                            self.Page_2.E2data3TC.SetValue(SplitExe[5])
                            self.Page_2.E2data4TC.SetValue(SplitExe[6])
                            self.Page_2.E3para0TC.SetValue(SplitExe[7])
                            self.Page_2.E3data1TC.SetValue(SplitExe[8])
                            self.Page_2.E3data2TC.SetValue(SplitExe[9])
                            self.Page_2.E3data3TC.SetValue(SplitExe[10])
                            self.Page_2.E3data4TC.SetValue(SplitExe[11])
                            self.Page_2.E5para0TC.SetValue(SplitExe[12])
                            self.Page_2.E5data1TC.SetValue(SplitExe[13])
                            self.Page_2.E5data2TC.SetValue(SplitExe[14])
                            self.Page_2.E5data3TC.SetValue(SplitExe[15])
                            self.Page_2.E6data1TC.SetValue(SplitExe[16])                           
                        case 'SRAMFX':
                            self.Page_2.F1para0TC.SetValue(SplitExe[1])
                            self.Page_2.F1data1TC.SetValue(SplitExe[2])
                            self.Page_2.F1data2TC.SetValue(SplitExe[3])
                            self.Page_2.F3para0TC.SetValue(SplitExe[4])
                            self.Page_2.F3data1TC.SetValue(SplitExe[5])
                            self.Page_2.F3data2TC.SetValue(SplitExe[6])
                            self.Page_2.F2para0TC.SetValue(SplitExe[7])
                            self.Page_2.F2data1TC.SetValue(SplitExe[8])
                            self.Page_2.F2data2TC.SetValue(SplitExe[9])
                            self.Page_2.F2data3TC.SetValue(SplitExe[10])
                            self.Page_2.F2data4TC.SetValue(SplitExe[11])
                            self.Page_2.F2data5TC.SetValue(SplitExe[12])
                            self.Page_2.F2data6TC.SetValue(SplitExe[13])
                            self.Page_2.SARMloopTC.SetValue(SplitExe[14])
                        case 'FLASH':
                            self.Page_3.WritePathST.SetLabel(WrapStr(SplitExe[1],52))
                        case 'CAMERA':
                            self.Page_5.CamChooseTC.SetValue(SplitExe[1])
                            self.Page_5.PictureNameTC.SetValue(SplitExe[2])
                            self.Page_5.PictureQntTC.SetValue(SplitExe[3])
                            self.Page_5.IntervalTC.SetValue(SplitExe[4])
                            self.Page_5.SingleShotTC.SetValue(SplitExe[5])
                            self.Page_5.SetExposureTC.SetValue(SplitExe[6])
                            self.Page_5.SetContrastTC.SetValue(SplitExe[7])
                            self.Page_5.SetSatTC.SetValue(SplitExe[8])
                        case 'XTALK':
                            self.Page_6.XtalkWTC.SetValue(SplitExe[1])
                            self.Page_6.XtalkHTC.SetValue(SplitExe[2])
                            self.Page_6.XtalkRTC.SetValue(SplitExe[3])
                            self.Page_6.XtalkGTC.SetValue(SplitExe[4])
                            self.Page_6.XtalkBTC.SetValue(SplitExe[5])
                            self.Page_6.XtalkATC.SetValue(SplitExe[6])
                            self.Page_6.WriteWTC.SetValue(SplitExe[7])
                            self.Page_6.WriteHTC.SetValue(SplitExe[8])                            
                            self.Page_6.WriteRTC.SetValue(SplitExe[9]) 
                            self.Page_6.WriteGTC.SetValue(SplitExe[10]) 
                            self.Page_6.WriteBTC.SetValue(SplitExe[11]) 
                            self.Page_6.WriteATC.SetValue(SplitExe[12]) 
                        #case _:
                            #print('Default')           
        except FileNotFoundError:
            UDFrame.SaveAPSetting(self)

    def SaveAPSetting(self):
        IniBuf = {}
        path = 'Setting.ini'
        
        IniBuf[0]='CONFIG,1,1,1,1,1,1,1,1'
        IniBuf[1]='P1DATA0,'\
            +self.Page_0.Data0TC1.GetValue()+','+self.Page_0.Parabox1.GetValue()+','\
            +self.Page_0.Data1TC1.GetValue()+','+self.Page_0.Data2TC1.GetValue()+','\
            +self.Page_0.Data3TC1.GetValue()+','+self.Page_0.Data4TC1.GetValue()+','\
            +self.Page_0.Data5TC1.GetValue()+','+self.Page_0.Data6TC1.GetValue()+','\
            +self.Page_0.Data7TC1.GetValue()+','+self.Page_0.Data8TC1.GetValue()+','\
            +self.Page_0.Data9TC1.GetValue()+','+self.Page_0.Data10TC1.GetValue()
        IniBuf[2]='P2DATA0,'\
            +self.Page_0.Data0TC2.GetValue()+','+self.Page_0.Parabox2.GetValue()+','\
            +self.Page_0.Data1TC2.GetValue()+','+self.Page_0.Data2TC2.GetValue()+','\
            +self.Page_0.Data3TC2.GetValue()+','+self.Page_0.Data4TC2.GetValue()+','\
            +self.Page_0.Data5TC2.GetValue()+','+self.Page_0.Data6TC2.GetValue()+','\
            +self.Page_0.Data7TC2.GetValue()+','+self.Page_0.Data8TC2.GetValue()+','\
            +self.Page_0.Data9TC2.GetValue()+','+self.Page_0.Data10TC2.GetValue()      
        IniBuf[3]='P3DATA0,'\
            +self.Page_0.Data0TC3.GetValue()+','+self.Page_0.Parabox3.GetValue()+','\
            +self.Page_0.Data1TC3.GetValue()+','+self.Page_0.Data2TC3.GetValue()+','\
            +self.Page_0.Data3TC3.GetValue()+','+self.Page_0.Data4TC3.GetValue()+','\
            +self.Page_0.Data5TC3.GetValue()+','+self.Page_0.Data6TC3.GetValue()+','\
            +self.Page_0.Data7TC3.GetValue()+','+self.Page_0.Data8TC3.GetValue()+','\
            +self.Page_0.Data9TC3.GetValue()+','+self.Page_0.Data10TC3.GetValue()
        IniBuf[4]='P4DATA0,'\
            +self.Page_0.Data0TC4.GetValue()+','+self.Page_0.Parabox4.GetValue()+','\
            +self.Page_0.Data1TC4.GetValue()+','+self.Page_0.Data2TC4.GetValue()+','\
            +self.Page_0.Data3TC4.GetValue()+','+self.Page_0.Data4TC4.GetValue()+','\
            +self.Page_0.Data5TC4.GetValue()+','+self.Page_0.Data6TC4.GetValue()+','\
            +self.Page_0.Data7TC4.GetValue()+','+self.Page_0.Data8TC4.GetValue()+','\
            +self.Page_0.Data9TC4.GetValue()+','+self.Page_0.Data10TC4.GetValue()
        IniBuf[5]='P5DATA0,'\
            +self.Page_0.Data0TC5.GetValue()+','+self.Page_0.Parabox5.GetValue()+','\
            +self.Page_0.Data1TC5.GetValue()+','+self.Page_0.Data2TC5.GetValue()+','\
            +self.Page_0.Data3TC5.GetValue()+','+self.Page_0.Data4TC5.GetValue()+','\
            +self.Page_0.Data5TC5.GetValue()+','+self.Page_0.Data6TC5.GetValue()+','\
            +self.Page_0.Data7TC5.GetValue()+','+self.Page_0.Data8TC5.GetValue()+','\
            +self.Page_0.Data9TC5.GetValue()+','+self.Page_0.Data10TC5.GetValue()
        IniBuf[6]='P6DATA0,'\
            +self.Page_0.Data0TC6.GetValue()+','+self.Page_0.Parabox6.GetValue()+','\
            +self.Page_0.Data1TC6.GetValue()+','+self.Page_0.Data2TC6.GetValue()+','\
            +self.Page_0.Data3TC6.GetValue()+','+self.Page_0.Data4TC6.GetValue()+','\
            +self.Page_0.Data5TC6.GetValue()+','+self.Page_0.Data6TC6.GetValue()+','\
            +self.Page_0.Data7TC6.GetValue()+','+self.Page_0.Data8TC6.GetValue()+','\
            +self.Page_0.Data9TC6.GetValue()+','+self.Page_0.Data10TC6.GetValue()
        IniBuf[7]='P7DATA0,'\
            +self.Page_0.Data0TC7.GetValue()+','+self.Page_0.Parabox7.GetValue()+','\
            +self.Page_0.Data1TC7.GetValue()+','+self.Page_0.Data2TC7.GetValue()+','\
            +self.Page_0.Data3TC7.GetValue()+','+self.Page_0.Data4TC7.GetValue()+','\
            +self.Page_0.Data5TC7.GetValue()+','+self.Page_0.Data6TC7.GetValue()+','\
            +self.Page_0.Data7TC7.GetValue()+','+self.Page_0.Data8TC7.GetValue()+','\
            +self.Page_0.Data9TC7.GetValue()+','+self.Page_0.Data10TC7.GetValue()
        IniBuf[8]='SCRIPT,'\
            +self.Page_0.PathST.GetLabel().replace("\n", "")+','\
            +self.Page_0.ScriptLoopTC.GetValue()
        IniBuf[9]='SRAMEX,'\
            +self.Page_2.E1data1TC.GetValue()+','+self.Page_2.E2para0TC.GetValue()+','\
            +self.Page_2.E2data1TC.GetValue()+','+self.Page_2.E2data2TC.GetValue()+','\
            +self.Page_2.E2data3TC.GetValue()+','+self.Page_2.E2data4TC.GetValue()+','\
            +self.Page_2.E3para0TC.GetValue()+','+self.Page_2.E3data1TC.GetValue()+','\
            +self.Page_2.E3data2TC.GetValue()+','+self.Page_2.E3data3TC.GetValue()+','\
            +self.Page_2.E3data4TC.GetValue()+','+self.Page_2.E5para0TC.GetValue()+','\
            +self.Page_2.E5data1TC.GetValue()+','+self.Page_2.E5data2TC.GetValue()+','\
            +self.Page_2.E5data3TC.GetValue()+','+self.Page_2.E6data1TC.GetValue()                
        IniBuf[10]='SRAMFX,'\
            +self.Page_2.F1para0TC.GetValue()+','+self.Page_2.F1data1TC.GetValue()+','\
            +self.Page_2.F1data2TC.GetValue()+','+self.Page_2.F3para0TC.GetValue()+','\
            +self.Page_2.F3data1TC.GetValue()+','+self.Page_2.F3data2TC.GetValue()+','\
            +self.Page_2.F2para0TC.GetValue()+','+self.Page_2.F2data1TC.GetValue()+','\
            +self.Page_2.F2data2TC.GetValue()+','+self.Page_2.F2data3TC.GetValue()+','\
            +self.Page_2.F2data4TC.GetValue()+','+self.Page_2.F2data5TC.GetValue()+','\
            +self.Page_2.F2data6TC.GetValue()+','+self.Page_2.SARMloopTC.GetValue()               
        IniBuf[11]='FLASH,'+self.Page_3.WritePathST.GetLabel().replace("\n", "")
        IniBuf[12]='CAMERA,'\
            +self.Page_5.CamChooseTC.GetValue()+','\
            +self.Page_5.PictureNameTC.GetValue()+','\
            +self.Page_5.PictureQntTC.GetValue()+','\
            +self.Page_5.IntervalTC.GetValue()+','\
            +self.Page_5.SingleShotTC.GetValue()+','\
            +self.Page_5.SetExposureTC.GetValue()+','\
            +self.Page_5.SetContrastTC.GetValue()+','\
            +self.Page_5.SetSatTC.GetValue()
        IniBuf[13]='XTALK,'\
            +self.Page_6.XtalkWTC.GetValue()+','\
            +self.Page_6.XtalkHTC.GetValue()+','\
            +self.Page_6.XtalkRTC.GetValue()+','\
            +self.Page_6.XtalkGTC.GetValue()+','\
            +self.Page_6.XtalkBTC.GetValue()+','\
            +self.Page_6.XtalkATC.GetValue()+','\
            +self.Page_6.WriteWTC.GetValue()+','\
            +self.Page_6.WriteHTC.GetValue()+','\
            +self.Page_6.WriteRTC.GetValue()+','\
            +self.Page_6.WriteGTC.GetValue()+','\
            +self.Page_6.WriteBTC.GetValue()+','\
            +self.Page_6.WriteATC.GetValue()
        try:
            file = open(path, "w")  
            for x in range(14):
                print(IniBuf[x], end="\n", file=file)
            file.close()            
        except IOError:
            print("[Error] Unable to write file.")
            
    def UpdateProgress(self, value):
        self.progressbar.SetValue(value)
        self.statusbar.SetStatusText(f'Progress: {value}%', 1)             
    #""" Page_0 Event """----------------------------------------------------------------------------  
    def MulitWr1Event(self, event):        
        self.Page_0.MulitWr1.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []            
            cmd = int(self.Page_0.Data0TC1.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox1.GetValue())
            OutData = [
            int(self.Page_0.Data1TC1.GetValue(), 16),
            int(self.Page_0.Data2TC1.GetValue(), 16),
            int(self.Page_0.Data3TC1.GetValue(), 16),
            int(self.Page_0.Data4TC1.GetValue(), 16),
            int(self.Page_0.Data5TC1.GetValue(), 16),
            int(self.Page_0.Data6TC1.GetValue(), 16),
            int(self.Page_0.Data7TC1.GetValue(), 16),
            int(self.Page_0.Data8TC1.GetValue(), 16),
            int(self.Page_0.Data9TC1.GetValue(), 16),
            int(self.Page_0.Data10TC1.GetValue(), 16)]

            if self.SetI2CItem.IsChecked():
                TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                for x in range(DataCount):
                    TempIoBuf.append(OutData[x])
                    TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            elif self.SetSPIItem.IsChecked():
                if self.Page_0.CBox1.GetValue():
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                    for x in range(DataCount):
                        TempIoBuf.append(OutData[x])
                        TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, TempIoBuf)
                else:
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, [])
            else:
                print('Nothing to do.')
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')           
        self.Page_0.MulitWr1.Enable(True)
        
    def MulitWr2Event(self, event):
        self.Page_0.MulitWr2.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            cmd = int(self.Page_0.Data0TC2.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox2.GetValue())
            OutData = [
            int(self.Page_0.Data1TC2.GetValue(), 16),
            int(self.Page_0.Data2TC2.GetValue(), 16),
            int(self.Page_0.Data3TC2.GetValue(), 16),
            int(self.Page_0.Data4TC2.GetValue(), 16),
            int(self.Page_0.Data5TC2.GetValue(), 16),
            int(self.Page_0.Data6TC2.GetValue(), 16),
            int(self.Page_0.Data7TC2.GetValue(), 16),
            int(self.Page_0.Data8TC2.GetValue(), 16),
            int(self.Page_0.Data9TC2.GetValue(), 16),
            int(self.Page_0.Data10TC2.GetValue(), 16)]

            if self.SetI2CItem.IsChecked():
                TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                for x in range(DataCount):
                    TempIoBuf.append(OutData[x])
                    TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            elif self.SetSPIItem.IsChecked():
                if self.Page_0.CBox2.GetValue():
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                    for x in range(DataCount):
                        TempIoBuf.append(OutData[x])
                        TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, TempIoBuf)
                else:
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, [])
            else:
                print('Nothing to do.')       
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitWr2.Enable(True)
        
    def MulitWr3Event(self, event):
        self.Page_0.MulitWr3.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            cmd = int(self.Page_0.Data0TC3.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox3.GetValue())
            OutData = [
            int(self.Page_0.Data1TC3.GetValue(), 16),
            int(self.Page_0.Data2TC3.GetValue(), 16),
            int(self.Page_0.Data3TC3.GetValue(), 16),
            int(self.Page_0.Data4TC3.GetValue(), 16),
            int(self.Page_0.Data5TC3.GetValue(), 16),
            int(self.Page_0.Data6TC3.GetValue(), 16),
            int(self.Page_0.Data7TC3.GetValue(), 16),
            int(self.Page_0.Data8TC3.GetValue(), 16),
            int(self.Page_0.Data9TC3.GetValue(), 16),
            int(self.Page_0.Data10TC3.GetValue(), 16)]

            if self.SetI2CItem.IsChecked():
                TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                for x in range(DataCount):
                    TempIoBuf.append(OutData[x])
                    TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            elif self.SetSPIItem.IsChecked():
                if self.Page_0.CBox3.GetValue():
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                    for x in range(DataCount):
                        TempIoBuf.append(OutData[x])
                        TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, TempIoBuf)
                else:
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, [])
            else:
                print('Nothing to do.')      
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitWr3.Enable(True)
        
    def MulitWr4Event(self, event):
        self.Page_0.MulitWr4.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            cmd = int(self.Page_0.Data0TC4.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox4.GetValue())
            OutData = [
            int(self.Page_0.Data1TC4.GetValue(), 16),
            int(self.Page_0.Data2TC4.GetValue(), 16),
            int(self.Page_0.Data3TC4.GetValue(), 16),
            int(self.Page_0.Data4TC4.GetValue(), 16),
            int(self.Page_0.Data5TC4.GetValue(), 16),
            int(self.Page_0.Data6TC4.GetValue(), 16),
            int(self.Page_0.Data7TC4.GetValue(), 16),
            int(self.Page_0.Data8TC4.GetValue(), 16),
            int(self.Page_0.Data9TC4.GetValue(), 16),
            int(self.Page_0.Data10TC4.GetValue(), 16)]

            if self.SetI2CItem.IsChecked():
                TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                for x in range(DataCount):
                    TempIoBuf.append(OutData[x])
                    TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            elif self.SetSPIItem.IsChecked():
                if self.Page_0.CBox4.GetValue():
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                    for x in range(DataCount):
                        TempIoBuf.append(OutData[x])
                        TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, TempIoBuf)
                else:
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, [])
            else:
                print('Nothing to do.')     
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitWr4.Enable(True)
        
    def MulitWr5Event(self, event):
        self.Page_0.MulitWr5.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            cmd = int(self.Page_0.Data0TC5.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox5.GetValue())
            OutData = [
            int(self.Page_0.Data1TC5.GetValue(), 16),
            int(self.Page_0.Data2TC5.GetValue(), 16),
            int(self.Page_0.Data3TC5.GetValue(), 16),
            int(self.Page_0.Data4TC5.GetValue(), 16),
            int(self.Page_0.Data5TC5.GetValue(), 16),
            int(self.Page_0.Data6TC5.GetValue(), 16),
            int(self.Page_0.Data7TC5.GetValue(), 16),
            int(self.Page_0.Data8TC5.GetValue(), 16),
            int(self.Page_0.Data9TC5.GetValue(), 16),
            int(self.Page_0.Data10TC5.GetValue(), 16)]

            if self.SetI2CItem.IsChecked():
                TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                for x in range(DataCount):
                    TempIoBuf.append(OutData[x])
                    TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            elif self.SetSPIItem.IsChecked():
                if self.Page_0.CBox5.GetValue():
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                    for x in range(DataCount):
                        TempIoBuf.append(OutData[x])
                        TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, TempIoBuf)
                else:
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, [])
            else:
                print('Nothing to do.')       
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitWr5.Enable(True)
    
    def MulitWr6Event(self, event):
        self.Page_0.MulitWr6.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            cmd = int(self.Page_0.Data0TC6.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox6.GetValue())
            OutData = [
            int(self.Page_0.Data1TC6.GetValue(), 16),
            int(self.Page_0.Data2TC6.GetValue(), 16),
            int(self.Page_0.Data3TC6.GetValue(), 16),
            int(self.Page_0.Data4TC6.GetValue(), 16),
            int(self.Page_0.Data5TC6.GetValue(), 16),
            int(self.Page_0.Data6TC6.GetValue(), 16),
            int(self.Page_0.Data7TC6.GetValue(), 16),
            int(self.Page_0.Data8TC6.GetValue(), 16),
            int(self.Page_0.Data9TC6.GetValue(), 16),
            int(self.Page_0.Data10TC6.GetValue(), 16)]

            if self.SetI2CItem.IsChecked():
                TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                for x in range(DataCount):
                    TempIoBuf.append(OutData[x])
                    TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            elif self.SetSPIItem.IsChecked():
                if self.Page_0.CBox6.GetValue():
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                    for x in range(DataCount):
                        TempIoBuf.append(OutData[x])
                        TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, TempIoBuf)
                else:
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, [])
            else:
                print('Nothing to do.')       
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitWr6.Enable(True)
        
    def MulitWr7Event(self, event):
        self.Page_0.MulitWr7.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            cmd = int(self.Page_0.Data0TC7.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox7.GetValue())
            OutData = [
            int(self.Page_0.Data1TC7.GetValue(), 16),
            int(self.Page_0.Data2TC7.GetValue(), 16),
            int(self.Page_0.Data3TC7.GetValue(), 16),
            int(self.Page_0.Data4TC7.GetValue(), 16),
            int(self.Page_0.Data5TC7.GetValue(), 16),
            int(self.Page_0.Data6TC7.GetValue(), 16),
            int(self.Page_0.Data7TC7.GetValue(), 16),
            int(self.Page_0.Data8TC7.GetValue(), 16),
            int(self.Page_0.Data9TC7.GetValue(), 16),
            int(self.Page_0.Data10TC7.GetValue(), 16)]

            if self.SetI2CItem.IsChecked():
                TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                for x in range(DataCount):
                    TempIoBuf.append(OutData[x])
                    TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            elif self.SetSPIItem.IsChecked():
                if self.Page_0.CBox7.GetValue():
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '
                    for x in range(DataCount):
                        TempIoBuf.append(OutData[x])
                        TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, TempIoBuf)
                else:
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)
                    UD_Package.UD_FT4222_SPI.spi_Write(cmd, [])
            else:
                print('Nothing to do.')       
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitWr7.Enable(True)
   
    def MulitRd1Event(self, event):
        self.Page_0.MulitRd1.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            InData = ['00','00','00','00','00','00','00','00','00','00']
            cmd = int(self.Page_0.Data0TC1.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox1.GetValue())
            if self.SetI2CItem.IsChecked():
                cmd0 = [cmd]               
                TempIoBuf = UD_Package.UD_FT4222_I2C.i2c_R_Register(0x6B, cmd0, DataCount)
            elif self.SetSPIItem.IsChecked():
                TempIoBuf = UD_Package.UD_FT4222_SPI.spi_Read(cmd, DataCount)
            else:
                print('Nothing to do.')            
            TempString = 'Read Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '                         
            for x in range(DataCount):
                InData[x] = TempIoBuf[x]
                TempString += '0x'+TempIoBuf[x].upper()+'_'            
            self.Page_0.Data1TC1.SetValue(InData[0].upper())
            self.Page_0.Data2TC1.SetValue(InData[1].upper())
            self.Page_0.Data3TC1.SetValue(InData[2].upper())
            self.Page_0.Data4TC1.SetValue(InData[3].upper())
            self.Page_0.Data5TC1.SetValue(InData[4].upper())
            self.Page_0.Data6TC1.SetValue(InData[5].upper())
            self.Page_0.Data7TC1.SetValue(InData[6].upper())
            self.Page_0.Data8TC1.SetValue(InData[7].upper())
            self.Page_0.Data9TC1.SetValue(InData[8].upper())
            self.Page_0.Data10TC1.SetValue(InData[9].upper())                        
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitRd1.Enable(True)
    
    def MulitRd2Event(self, event):
        self.Page_0.MulitRd2.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            InData = ['00','00','00','00','00','00','00','00','00','00']
            cmd = int(self.Page_0.Data0TC2.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox2.GetValue())
            if self.SetI2CItem.IsChecked():
                cmd0 = [cmd]             
                TempIoBuf = UD_Package.UD_FT4222_I2C.i2c_R_Register(0x6B, cmd0, DataCount)
            elif self.SetSPIItem.IsChecked():
                TempIoBuf = UD_Package.UD_FT4222_SPI.spi_Read(cmd, DataCount)
            else:
                print('Nothing to do.')
            TempString = 'Read Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '                         
            for x in range(DataCount):
                InData[x] = TempIoBuf[x]
                TempString += '0x'+TempIoBuf[x].upper()+'_'            
            self.Page_0.Data1TC2.SetValue(InData[0].upper())
            self.Page_0.Data2TC2.SetValue(InData[1].upper())
            self.Page_0.Data3TC2.SetValue(InData[2].upper())
            self.Page_0.Data4TC2.SetValue(InData[3].upper())
            self.Page_0.Data5TC2.SetValue(InData[4].upper())
            self.Page_0.Data6TC2.SetValue(InData[5].upper())
            self.Page_0.Data7TC2.SetValue(InData[6].upper())
            self.Page_0.Data8TC2.SetValue(InData[7].upper())
            self.Page_0.Data9TC2.SetValue(InData[8].upper())
            self.Page_0.Data10TC2.SetValue(InData[9].upper())                        
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitRd2.Enable(True)
        
    def MulitRd3Event(self, event):
        self.Page_0.MulitRd3.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            InData = ['00','00','00','00','00','00','00','00','00','00']
            cmd = int(self.Page_0.Data0TC3.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox3.GetValue())
            if self.SetI2CItem.IsChecked():
                cmd0 = [cmd]
                TempIoBuf = UD_Package.UD_FT4222_I2C.i2c_R_Register(0x6B, cmd0, DataCount)
            elif self.SetSPIItem.IsChecked():           
                TempIoBuf = UD_Package.UD_FT4222_SPI.spi_Read(cmd, DataCount)
            else:
                print('Nothing to do.')
            TempString = 'Read Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '                         
            for x in range(DataCount):
                InData[x] = TempIoBuf[x]
                TempString += '0x'+TempIoBuf[x].upper()+'_'            
            self.Page_0.Data1TC3.SetValue(InData[0].upper())
            self.Page_0.Data2TC3.SetValue(InData[1].upper())
            self.Page_0.Data3TC3.SetValue(InData[2].upper())
            self.Page_0.Data4TC3.SetValue(InData[3].upper())
            self.Page_0.Data5TC3.SetValue(InData[4].upper())
            self.Page_0.Data6TC3.SetValue(InData[5].upper())
            self.Page_0.Data7TC3.SetValue(InData[6].upper())
            self.Page_0.Data8TC3.SetValue(InData[7].upper())
            self.Page_0.Data9TC3.SetValue(InData[8].upper())
            self.Page_0.Data10TC3.SetValue(InData[9].upper())                        
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitRd3.Enable(True)
    
    def MulitRd4Event(self, event):
        self.Page_0.MulitRd4.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            InData = ['00','00','00','00','00','00','00','00','00','00']
            cmd = int(self.Page_0.Data0TC4.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox4.GetValue())
            if self.SetI2CItem.IsChecked():
                cmd0 = [cmd]
                TempIoBuf = UD_Package.UD_FT4222_I2C.i2c_R_Register(0x6B, cmd0, DataCount)
            elif self.SetSPIItem.IsChecked():             
                TempIoBuf = UD_Package.UD_FT4222_SPI.spi_Read(cmd, DataCount)
            else:
                print('Nothing to do.')
            TempString = 'Read Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '                         
            for x in range(DataCount):
                InData[x] = TempIoBuf[x]
                TempString += '0x'+TempIoBuf[x].upper()+'_'            
            self.Page_0.Data1TC4.SetValue(InData[0].upper())
            self.Page_0.Data2TC4.SetValue(InData[1].upper())
            self.Page_0.Data3TC4.SetValue(InData[2].upper())
            self.Page_0.Data4TC4.SetValue(InData[3].upper())
            self.Page_0.Data5TC4.SetValue(InData[4].upper())
            self.Page_0.Data6TC4.SetValue(InData[5].upper())
            self.Page_0.Data7TC4.SetValue(InData[6].upper())
            self.Page_0.Data8TC4.SetValue(InData[7].upper())
            self.Page_0.Data9TC4.SetValue(InData[8].upper())
            self.Page_0.Data10TC4.SetValue(InData[9].upper())                        
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitRd4.Enable(True)
    
    def MulitRd5Event(self, event):
        self.Page_0.MulitRd5.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            InData = ['00','00','00','00','00','00','00','00','00','00']
            cmd = int(self.Page_0.Data0TC5.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox5.GetValue())
            if self.SetI2CItem.IsChecked():
                cmd0 = [cmd]                
                TempIoBuf = UD_Package.UD_FT4222_I2C.i2c_R_Register(0x6B, cmd0, DataCount)
            elif self.SetSPIItem.IsChecked():               
                TempIoBuf = UD_Package.UD_FT4222_SPI.spi_Read(cmd, DataCount)
            else:
                print('Nothing to do.')
            TempString = 'Read Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '                         
            for x in range(DataCount):
                InData[x] = TempIoBuf[x]
                TempString += '0x'+TempIoBuf[x].upper()+'_'            
            self.Page_0.Data1TC5.SetValue(InData[0].upper())
            self.Page_0.Data2TC5.SetValue(InData[1].upper())
            self.Page_0.Data3TC5.SetValue(InData[2].upper())
            self.Page_0.Data4TC5.SetValue(InData[3].upper())
            self.Page_0.Data5TC5.SetValue(InData[4].upper())
            self.Page_0.Data6TC5.SetValue(InData[5].upper())
            self.Page_0.Data7TC5.SetValue(InData[6].upper())
            self.Page_0.Data8TC5.SetValue(InData[7].upper())
            self.Page_0.Data9TC5.SetValue(InData[8].upper())
            self.Page_0.Data10TC5.SetValue(InData[9].upper())                       
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitRd5.Enable(True)
    
    def MulitRd6Event(self, event):
        self.Page_0.MulitRd6.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            InData = ['00','00','00','00','00','00','00','00','00','00']
            cmd = int(self.Page_0.Data0TC6.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox6.GetValue())
            if self.SetI2CItem.IsChecked():
                cmd0 = [cmd]
                TempIoBuf = UD_Package.UD_FT4222_I2C.i2c_R_Register(0x6B, cmd0, DataCount)
            elif self.SetSPIItem.IsChecked():                             
                TempIoBuf = UD_Package.UD_FT4222_SPI.spi_Read(cmd, DataCount)
            else:
                print('Nothing to do.')
            TempString = 'Read Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '                         
            for x in range(DataCount):
                InData[x] = TempIoBuf[x]
                TempString += '0x'+TempIoBuf[x].upper()+'_'            
            self.Page_0.Data1TC6.SetValue(InData[0].upper())
            self.Page_0.Data2TC6.SetValue(InData[1].upper())
            self.Page_0.Data3TC6.SetValue(InData[2].upper())
            self.Page_0.Data4TC6.SetValue(InData[3].upper())
            self.Page_0.Data5TC6.SetValue(InData[4].upper())
            self.Page_0.Data6TC6.SetValue(InData[5].upper())
            self.Page_0.Data7TC6.SetValue(InData[6].upper())
            self.Page_0.Data8TC6.SetValue(InData[7].upper())
            self.Page_0.Data9TC6.SetValue(InData[8].upper())
            self.Page_0.Data10TC6.SetValue(InData[9].upper())                        
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitRd6.Enable(True)
    
    def MulitRd7Event(self, event):
        self.Page_0.MulitRd7.Enable(False)
        try:
            TempString = ''
            TempIoBuf = []
            InData = ['00','00','00','00','00','00','00','00','00','00']
            cmd = int(self.Page_0.Data0TC7.GetValue(), 16)
            DataCount = int(self.Page_0.Parabox7.GetValue())
            if self.SetI2CItem.IsChecked():
                cmd0 = [cmd]
                TempIoBuf = UD_Package.UD_FT4222_I2C.i2c_R_Register(0x6B, cmd0, DataCount)
            elif self.SetSPIItem.IsChecked():                              
                TempIoBuf = UD_Package.UD_FT4222_SPI.spi_Read(cmd, DataCount)
            else:
                print('Nothing to do.')
            TempString = 'Read Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '                         
            for x in range(DataCount):
                InData[x] = TempIoBuf[x]
                TempString += '0x'+TempIoBuf[x].upper()+'_'            
            self.Page_0.Data1TC7.SetValue(InData[0].upper())
            self.Page_0.Data2TC7.SetValue(InData[1].upper())
            self.Page_0.Data3TC7.SetValue(InData[2].upper())
            self.Page_0.Data4TC7.SetValue(InData[3].upper())
            self.Page_0.Data5TC7.SetValue(InData[4].upper())
            self.Page_0.Data6TC7.SetValue(InData[5].upper())
            self.Page_0.Data7TC7.SetValue(InData[6].upper())
            self.Page_0.Data8TC7.SetValue(InData[7].upper())
            self.Page_0.Data9TC7.SetValue(InData[8].upper())
            self.Page_0.Data10TC7.SetValue(InData[9].upper())                       
            print(TempString)
            UDFrame.LogP(self, TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_0.MulitRd7.Enable(True)
        
    def CMDparaGrop(self, event, text_ctrl):
        text = text_ctrl.GetValue()
        text_ctrl.SetValue(HEXValueCheck(text))
    
    def CMDparaGropDclick(self, event, text_ctrl):
        text_ctrl.SetValue('00')
        
    def GPIO_0RBoxEvent(self, event):
        try:
            selected = self.Page_0.GPIO_0RBox.GetSelection()
            if selected == 0:
                UD_Package.UD_FT4222_I2C.gpio0_Low()
            elif selected == 1:
                UD_Package.UD_FT4222_I2C.gpio0_High()
            else:
                print('Nothing to do.')
        except Exception as e:
            print(f'[Error][gpio0] {str(e)}')
               
    def GPIO_1RBoxEvent(self, event): 
        try:
            selected = self.Page_0.GPIO_1RBox.GetSelection()
            if selected == 0:
                UD_Package.UD_FT4222_I2C.gpio1_Low()
            elif selected == 1:
                UD_Package.UD_FT4222_I2C.gpio1_High()
            else:
                print('Nothing to do.')
        except Exception as e:
            print(f'[Error][gpio1] {str(e)}')
        
    def GPIO_2RBoxEvent(self, event):    
        try:
            selected = self.Page_0.GPIO_2RBox.GetSelection()
            if selected == 0:
                UD_Package.UD_FT4222_I2C.gpio2_Low()
            elif selected == 1:
                UD_Package.UD_FT4222_I2C.gpio2_High()
            else:
                print('Nothing to do.')
        except Exception as e:
            print(f'[Error][gpio2] {str(e)}')
        
    def GPIO_3RBoxEvent(self, event): 
        try:
            selected = self.Page_0.GPIO_3RBox.GetSelection()
            if selected == 0:
                UD_Package.UD_FT4222_I2C.gpio3_Low()
            elif selected == 1:
                UD_Package.UD_FT4222_I2C.gpio3_High()
            else:
                print('Nothing to do.')
        except Exception as e:
            print(f'[Error][gpio3] {str(e)}')
        
    def OpenIniBtnEvent(self, event):                
        self.Page_0.OpenIniBtn.Enable(False)
        OpenFileDialog = wx.FileDialog(self, 'Open', '', '', 'Ini files (*.ini)|*.ini', wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)
        dialogResult = OpenFileDialog.ShowModal()     
        if dialogResult !=  wx.ID_OK:
            self.Page_0.OpenIniBtn.Enable(True)
            return
        path = OpenFileDialog.GetPath()        
        self.Page_0.PathST.SetLabel(WrapStr(path,82))
        if self.Page_0.PathST.GetLabel != '':
            self.Page_0.LoadIniBtn.Enable(True)
        self.Page_0.OpenIniBtn.Enable(True)
               
    def LoadIniBtnEvent(self, event):
        thread = threading.Thread(target=self.LoadIniBtnTask)
        thread.start()
        
    def LoadIniBtnTask(self):
        self.Page_0.LoadIniBtn.Enable(False)
        self.Page_0.ScriptCMD.SetLabel('Run...')
               
        try:
            ScriptRun = True            
            CopyBuf = {}
            ScriptBuf = {} 
            SplitTest = {} 
            SplitExe = {}            
            PosS = -1
            PosE = -1
            IndexExe = 0
            PosIndex = 0
            path = self.Page_0.PathST.GetLabel().replace("\n", "")

            with open(path, 'r') as f:
                for line in f:
                    CopyBuf = line
                    PosIndex+=1                                                      
                    if CopyBuf != None and '[START]' in CopyBuf:
                        PosS = PosIndex                                               
                    if CopyBuf != None and '[END]' in CopyBuf:
                        PosE = PosIndex
                    if CopyBuf != None: 
                        ScriptBuf[PosIndex] = CopyBuf
                                              
            if  (PosE < 0) or (PosS < 0) or (PosS > PosE):           
                ScriptRun = False
                print('PosS:'+ str(PosS))
                print('PosE:'+ str(PosE))
                
                self.Page_0.ScriptCMD.SetLabel('Stop')
                self.Page_0.ScriptCMD.SetForegroundColour((255,0,0))
                self.Page_0.LoadIniBtn.Enable(False)
                return
            
            SplitTest = re.split(' |,', ScriptBuf[PosS + 1])           
            if SplitTest[0] != '0':            
                ScriptRun = False
                wx.MessageBox('NO IC Name Detect Please Check [START] after  0,IC NAME', 
                                'Message Box', wx.OK| wx.ICON_INFORMATION)
                
                self.Page_0.ScriptCMD.SetLabel('Stop')
                self.Page_0.ScriptCMD.SetForegroundColour((255,0,0))
                self.Page_0.LoadIniBtn.Enable(False)
                return
                        
            ScriptLoop = int(self.Page_0.ScriptLoopTC.GetValue())
            self.UpdateProgress(0)
            for LoopExe in range(0, ScriptLoop):
                for IndexExe in range(PosS+1, PosE):
                    if ScriptRun == False: return
                    if ScriptBuf != None:
                        if ScriptBuf != None:
                            ScriptS = ScriptBuf[IndexExe].strip()
                
                            if ScriptS.startswith('//'):
                                continue  # Skip comment lines starting with "//".
                            # Split into comment section and instruction section. The number 1 is passed as 
                            # a parameter to the split() method to specify the maximum number of splits.
                            parts = ScriptS.split('//', 1)
                            instruction = parts[0].strip()
                            if not instruction:
                                continue  # Skip blank lines.
                            if instruction:
                                SplitExe = re.split(',', instruction.replace(" ", ""))
                                              
                        match SplitExe[0]:                    
                            case '0': # Start case '0'
                                TempString = SplitExe[1].replace("\n", "")
                                UDFrame.LogP(self, f'**** {TempString} ****')
                                # End case '0'                        
                            case '1': # Start case '1'
                                TempString=''
                                cmd = int(SplitExe[1], 16)
                                
                                if self.SetI2CItem.IsChecked():
                                    DataCount = int(SplitExe[2])
                                    TempIoBuf = []
                                    if DataCount != len(SplitExe) - 3:
                                        ScriptRun = False
                                        print('Line Index :' + str(IndexExe) + ', Data Count and Total Data Different')
                                        self.Page_0.ScriptCMD.SetLabel('Stop')
                                        self.Page_0.ScriptCMD.SetForegroundColour((255,0,0))
                                        self.Page_0.LoadIniBtn.Enable(False)
                                        return
                                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '  
                                    for x in range(3,DataCount+3):
                                        TempIoBuf.append(int(SplitExe[x], 16))
                                        TempString+='0x{:02X}'.format(TempIoBuf[x-3])+'_'
                                    UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
                                elif self.SetSPIItem.IsChecked():
                                    if len(SplitExe) > 5:
                                        DataCount = int(SplitExe[2])
                                        TempIoBuf = []
                                        if DataCount != len(SplitExe) - 3:
                                            ScriptRun = False
                                            print('Line Index :' + str(IndexExe) + ', Data Count and Total Data Different')
                                            self.Page_0.ScriptCMD.SetLabel('Stop')
                                            self.Page_0.ScriptCMD.SetForegroundColour((255,0,0))
                                            self.Page_0.LoadIniBtn.Enable(False)
                                            return
                                        TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '  
                                        for x in range(3,DataCount+3):
                                            TempIoBuf.append(int(SplitExe[x], 16))
                                            TempString+='0x{:02X}'.format(TempIoBuf[x-3])+'_'
                                        UD_Package.UD_FT4222_SPI.spi_Write(cmd, TempIoBuf)
                                    else:                                   
                                        TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd)
                                        UD_Package.UD_FT4222_SPI.spi_Write(cmd, [])
                                else:
                                    print('Nothing to do.')
                                                           
                                print(TempString)
                                UDFrame.LogP(self, TempString)                                                    
                                # End case '1'                       
                            case '2': # Start case '2'
                                TempString=''
                                cmd = int(SplitExe[1],16)
                                DataCount = int(SplitExe[2])
                                TempIoBuf = []
                                if self.SetI2CItem.IsChecked():
                                    cmd0 = [cmd]                       
                                    TempIoBuf = UD_Package.UD_FT4222_I2C.i2c_R_Register(0x6B, cmd0, DataCount)
                                elif self.SetSPIItem.IsChecked():
                                    TempIoBuf = UD_Package.UD_FT4222_SPI.spi_Read(cmd, DataCount)
                                else:
                                    print('Nothing to do.')                                                                                 
                                TempString = 'Read Cmd: ' + '0x{:02X}'.format(cmd)+', Data: '                           
                                for x in range(DataCount):
                                    TempString+='0x'+TempIoBuf[x].upper()+'_'                         
                                print(TempString)
                                UDFrame.LogP(self, TempString)
                                # End case '2'                     
                            case '3': # Start case '3'
                                SecondCount = int(SplitExe[1])                                
                                wx.MilliSleep(SecondCount)                            
                                # End case '3'
                            case '4': # Start case '4'
                                print('I am 4')
                                # End case '4'
                            case '5': # Start case '5'
                                print('I am 5')
                                # End case '5'
                            case '6': # Start case '6'
                                print('I am 6')
                                # End case '6'
                            case '7': # Start case '7'
                                print('I am 7')
                                # End case '7'
                            case '8': # Start case '8'                    
                                match SplitExe[1]:
                                    case '1': # Digital Multimeter
                                        now = datetime.datetime.now()
                                        timestamp = now.strftime('_%m%d_%H%M%S')
                                        path = timestamp+'_output.csv'
                                        with open(path, mode='a', newline='') as file:
                                            writer = csv.writer(file)         
                                            value = UD_Package.UD_Instrument.Get_Meter()
                                            data = Decimal(value)                                   
                                            writer.writerow([format(data, ".8f")])
                                    # End case '1'
                                    case '2': # Precision Measurement DC Supply                                     
                                        value = SplitExe[2]
                                        value_float = float(value)
                                        UD_Package.UD_Instrument.Set_PSupply(value_float)                   
                                    # End case '2'
                                    case '3': # DC Electronic Load
                                        value = SplitExe[2]
                                        value_float = float(value)
                                        UD_Package.UD_Instrument.Set_Load(value_float)
                                    # End case '3'
                                    case _:
                                        print(f'[{IndexExe}] Nothing to do.')
                                        UDFrame.LogP(self, f'[{IndexExe}] Nothing to do.')
                                # End case '8'
                            case '9': # Start case '9'
                                print('I am 9')
                                # End case '9'
                            case _: # Start case default 
                                print(f'[{IndexExe}] Nothing to do.')
                                UDFrame.LogP(self, f'[{IndexExe}] Nothing to do.')
                                # End case default
                LoopFinish = LoopExe + 1
                print(f'Finish Loop: {LoopFinish}')
                UDFrame.LogP(self, f'Finish Loop: {LoopFinish}')
                progress = int(((LoopExe+1) / ScriptLoop) * 100)
                self.UpdateProgress(progress)
            self.UpdateProgress(100)
            self.Page_0.ScriptCMD.SetLabel('Finish')
            self.Page_0.ScriptCMD.SetForegroundColour((0,128,0))
        except Exception as e:
            print(f'Line index: {IndexExe}')
            print(f'[Error] {str(e)}')
            self.Page_0.ScriptCMD.SetLabel('Stop')
            self.Page_0.ScriptCMD.SetForegroundColour((255,0,0))
            self.Page_0.LoadIniBtn.Enable(True)
            return                    
            
        self.Page_0.LoadIniBtn.Enable(True)                                   
    #""" Page_1 Event """----------------------------------------------------------------------------
    def TestThreadBtnEvent(self, event):        
        thread = threading.Thread(target=self.Test_Task)
        thread.start()
                
    def Test_Task(self):
        self.Page_1.ThreadBtn.Enable(False)
        _time = 0
        for x in range(0, 10):
            time.sleep(1)
            _time += 1
            wx.CallAfter(self.UpdateLoopExeST, _time)
        self.Page_1.ThreadBtn.Enable(True)
        
    def UpdateLoopExeST(self, value):
        self.Page_1.LoopExeST.SetLabel(str(value))
    
    def TestInputBtnEvent(self, event):
        input_str = self.Page_1.IndexTC.GetValue()  # 獲取輸入的字符串
        try:
            input_num = int(input_str)  # 將字符串轉換為整數
            if input_num <= 0:
                raise ValueError("Input must be a positive integer.")
            
            # 清空之前的結果
            self.Page_1.ParameterTC.Clear()
            self.Page_1.IndexTC.Clear()
    
            result = generate_unique_numbers(input_num)  # 生成不重複的數字序列
            result_str = ",".join("{:02X}".format(num) for num in result)  # 格式化輸出
            self.Page_1.ParameterTC.AppendText(result_str)  # 在文本控制項中添加結果
        except ValueError as e:
            print("Error:", e)
    #""" Page_2 Event """----------------------------------------------------------------------------    
    def SARMWrEvent(self, event):
        self.Page_2.SARMWr.Enable(False)
        try:
            # 0xE1
            TempString = ''
            TempIoBuf = []
            cmd = 0xE1
            DataCount = int(self.Page_2.E1para0TC.GetValue())
            OutData = [int(self.Page_2.E1data1TC.GetValue(), 16)]              
            TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd) + ', Data: '
            for x in range(DataCount):
                TempIoBuf.append(OutData[x])
                TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'            
            UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            print(TempString)
            UDFrame.LogP(self, TempString)
            # 0xE2
            TempString = ''
            TempIoBuf = []
            cmd = 0xE2
            DataCount = int(self.Page_2.E2para0TC.GetValue())
            OutData = [
            int(self.Page_2.E2data1TC.GetValue(), 16),
            int(self.Page_2.E2data2TC.GetValue(), 16),
            int(self.Page_2.E2data3TC.GetValue(), 16),
            int(self.Page_2.E2data4TC.GetValue(), 16)]            
            TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd) + ', Data: '
            for x in range(DataCount):
                TempIoBuf.append(OutData[x])
                TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'            
            UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            print(TempString)
            UDFrame.LogP(self, TempString)
            # 0xE3
            TempString = ''
            TempIoBuf = []
            cmd = 0xE3
            DataCount = int(self.Page_2.E3para0TC.GetValue())
            OutData = [
            int(self.Page_2.E3data1TC.GetValue(), 16),
            int(self.Page_2.E3data2TC.GetValue(), 16),
            int(self.Page_2.E3data3TC.GetValue(), 16),
            int(self.Page_2.E3data4TC.GetValue(), 16)]            
            TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd) + ', Data: '
            for x in range(DataCount):
                TempIoBuf.append(OutData[x])
                TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'            
            UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            print(TempString)
            UDFrame.LogP(self, TempString)
            # 0xE5
            TempString = ''
            TempIoBuf = []
            cmd = 0xE5
            DataCount = int(self.Page_2.E5para0TC.GetValue())
            OutData = [
            int(self.Page_2.E5data1TC.GetValue(), 16),
            int(self.Page_2.E5data2TC.GetValue(), 16),
            int(self.Page_2.E5data3TC.GetValue(), 16)]            
            TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd) + ', Data: '
            for x in range(DataCount):
                TempIoBuf.append(OutData[x])
                TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'            
            UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            print(TempString)
            UDFrame.LogP(self, TempString)
            # 0xE6
            TempString = ''
            TempIoBuf = []
            cmd = 0xE6
            DataCount = int(self.Page_2.E6para0TC.GetValue())
            OutData = [int(self.Page_2.E6data1TC.GetValue(), 16)]              
            TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd) + ', Data: '
            for x in range(DataCount):
                TempIoBuf.append(OutData[x])
                TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'            
            UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
            print(TempString)
            UDFrame.LogP(self, TempString)                        
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_2.SARMWr.Enable(True)
            
    def SARMRdEvent(self, event):
        self.Page_2.SARMRd.Enable(False)
        try:
            AddrCount = int(self.Page_2.SARMloopTC.GetValue())
            GetData = [
            int(self.Page_2.F1data1TC.GetValue(), 16),
            int(self.Page_2.F1data2TC.GetValue(), 16)]
            AddrS = (GetData[1]*256) + GetData[0]
            AddrE = AddrS + AddrCount                      
            if (AddrE - AddrS) > 1024:
                self.SWOffRBtn.SetValue(True)                
                wx.MessageBox('The value in the loop should be less than or equal to 1024.', 
                                'Message Box', wx.OK| wx.ICON_INFORMATION)
            else:               
                for AddrIndex in range(AddrS, AddrE):
                    # 0xF1
                    TempString = ''
                    TempIoBuf = []
                    cmd = 0xF1
                    DataCount = DataCount = int(self.Page_2.F1para0TC.GetValue())
                    SetData_0 = AddrIndex % 256
                    SetData_1 = AddrIndex // 256
                    OutData = [SetData_0, SetData_1]            
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd) + ', Data: '
                    for x in range(DataCount):
                        TempIoBuf.append(OutData[x])
                        TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'            
                    UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
                    print(TempString)
                    UDFrame.LogP(self, TempString)
                    # 0xF3
                    TempString = ''
                    TempIoBuf = []
                    cmd = 0xF3
                    DataCount = int(self.Page_2.F3para0TC.GetValue())
                    OutData = [
                    int(self.Page_2.F3data1TC.GetValue(), 16),
                    int(self.Page_2.F3data2TC.GetValue(), 16)]            
                    TempString = 'Write Cmd: ' + '0x{:02X}'.format(cmd) + ', Data: '
                    for x in range(DataCount):
                        TempIoBuf.append(OutData[x])
                        TempString += '0x{:02X}'.format(TempIoBuf[x])+'_'            
                    UD_Package.UD_FT4222_I2C.i2c_W_Register(0x6B, cmd, TempIoBuf)
                    print(TempString)
                    UDFrame.LogP(self, TempString)
                    # 0xF2
                    TempString = ''
                    TempIoBuf = []
                    InData = ['00','00','00','00','00','00']
                    cmd = 0xF2
                    DataCount = int(self.Page_2.F2para0TC.GetValue())
                    if self.SetI2CItem.IsChecked():
                        cmd0 = [cmd]              
                        TempIoBuf = UD_Package.UD_FT4222_I2C.i2c_R_Register(0x6B, cmd0, DataCount)           
                    TempString = 'Read Cmd: ' + '0x{:02X}'.format(cmd) + ', Data: '                         
                    for x in range(DataCount):
                        InData[x] = TempIoBuf[x]
                        TempString += '0x'+TempIoBuf[x].upper()+'_'            
                    self.Page_2.F2data1TC.SetValue(InData[0].upper())
                    self.Page_2.F2data2TC.SetValue(InData[1].upper())
                    self.Page_2.F2data3TC.SetValue(InData[2].upper())
                    self.Page_2.F2data4TC.SetValue(InData[3].upper())
                    self.Page_2.F2data5TC.SetValue(InData[4].upper())
                    self.Page_2.F2data6TC.SetValue(InData[5].upper())                       
                    print(TempString)
                    UDFrame.LogP(self, TempString)
                    progress = int(((AddrIndex+1) / (AddrE - AddrS)) * 100)
                    self.UpdateProgress(progress)
                self.UpdateProgress(100)
        except Exception as e:
            print(f'[Error] {str(e)}')
        self.Page_2.SARMRd.Enable(True)
    #""" Page_3 Event """----------------------------------------------------------------------------
    def FlashEraseEvent(self, event):
        thread = threading.Thread(target=self.FlashEraseTask)
        thread.start()
        
    def FlashEraseTask(self):        
        self.Page_3.FlashErase.Enable(False)
        self.Page_3.FlashIDRd.Enable(False)
        self.Page_3.ReadStatusBtn.Enable(False)
        self.Page_3.WriteFileBtn.Enable(False)        
        self.Page_3.ReadFileBtn.Enable(False)
        try:
            UD_Package.UD_FT4222_SPI.chip_Erase()
            TempString = 'Write Cmd: 0x06\nWrite Cmd: 0xC7'
            print(TempString)
            UDFrame.LogP(self, TempString)
            wx.MilliSleep(3900)
        except Exception as e:
            print(f'[Error] {str(e)}')
            UDFrame.LogP(self, f'[Error] {str(e)}')
        self.Page_3.FlashErase.Enable(True)
        self.Page_3.FlashIDRd.Enable(True)
        self.Page_3.ReadStatusBtn.Enable(True)
        self.Page_3.WriteFileBtn.Enable(True)        
        self.Page_3.ReadFileBtn.Enable(True)           
        
    def FlashIDRdEvent(self, event):
        try:
            Flash_ID = []
            Flash_ID = UD_Package.UD_FT4222_SPI.read_Flash()
            self.Page_3.FlashID1TC.SetValue(str(Flash_ID[0]))
            self.Page_3.FlashID2TC.SetValue(str(Flash_ID[1]))
            self.Page_3.FlashID3TC.SetValue(str(Flash_ID[2]))
            TempString = 'Read Cmd: 0x9F, Data: 0x' + str(Flash_ID[0]) + '_0x' + str(Flash_ID[1]) + '_0x' + str(Flash_ID[2])
            print('[Flash ID] ' + TempString)
        except Exception as e:
            print(f'[Error] {str(e)}')
            UDFrame.LogP(self, f'[Error] {str(e)}')               
            
    def OpenFileBtnEvent(self, event):
        self.Page_3.OpenFileBtn.Enable(False)
        OpenFileDialog = wx.FileDialog(self, 'Open', '', '', 'hex files (*.bin)|*.bin', wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)
        dialogResult = OpenFileDialog.ShowModal()     
        if dialogResult !=  wx.ID_OK:
            self.Page_3.OpenFileBtn.Enable(True)
            return
        path = OpenFileDialog.GetPath()        
        self.Page_3.WritePathST.SetLabel(WrapStr(path,52))
        if self.Page_3.WritePathST.GetLabel != '':
            self.Page_3.WriteFileBtn.Enable(True)
        self.Page_3.OpenFileBtn.Enable(True)
        
    def WriteFileBtnEvent(self, event):
        global write_data_list           
        self.Page_3.WriteFileBtn.Enable(False)
        self.Page_3.WriteFileCMD.SetLabel('Run...')
            
        try:            
            path = self.Page_3.WritePathST.GetLabel().replace("\n", "")
            write_data_list = ReadBinFile(path)
            self.Page_3.SizeTC.SetValue(str(len(write_data_list)))
            chunk_size = 256
            num_chunks = len(write_data_list) // chunk_size
            addr_exe = 0            
            for i in range(num_chunks):
                start = i * chunk_size
                end = start + chunk_size
                chunk = write_data_list[start:end]                                           
                UD_Package.UD_FT4222_SPI.spi_02H_Write(addr_exe, chunk)
                addr_exe += 256
                progress = int(((i+1) / num_chunks) * 100)
                self.UpdateProgress(progress)
            remaining = len(write_data_list) % chunk_size            
            if remaining > 0: 
                start = num_chunks * chunk_size
                end = start + remaining
                last_chunk = write_data_list[start:end]
                UD_Package.UD_FT4222_SPI.spi_02H_Write(addr_exe, last_chunk)
            self.UpdateProgress(100)
            if UD_Package.UD_FT4222_SPI.PageFlag == False:
                print('Status Register Error.')
                UDFrame.LogP(self, 'Status Register Error.')
                self.Page_3.WriteFileCMD.SetLabel('Stop')
                self.Page_3.WriteFileCMD.SetForegroundColour((255,0,0))
            else:
                print('Write Flash Finish.')
                UDFrame.LogP(self, 'Write Flash Finish.')
                self.Page_3.WriteFileCMD.SetLabel('Finish')
                self.Page_3.WriteFileCMD.SetForegroundColour((0,128,0))
        except Exception as e:
            print(f'[Error] {str(e)}')
            UDFrame.LogP(self, f'[Error] {str(e)}')
            self.Page_3.BurnFileCMD.SetLabel('Stop')
            self.Page_3.BurnFileCMD.SetForegroundColour((255,0,0))
                   
        self.Page_3.WriteFileBtn.Enable(True)
        
    def ReadFileBtnEvent(self, event):
        global write_data_list
        self.Page_3.ReadFileBtn.Enable(False)       
        self.Page_3.ReadFileCMD.SetLabel('Run...')
        
        try:            
            addr_exe = int(self.Page_3.AddressTC.GetValue(), 16)
            total_size = int(self.Page_3.SizeTC.GetValue())
            chunk_size = 256
            num_chunks = total_size // chunk_size
            read_data_list = []
            for i in range(num_chunks):
                read_data = UD_Package.UD_FT4222_SPI.spi_03H_Read(addr_exe, chunk_size)
                addr_exe += 256
                read_data_list.extend(read_data)
                progress = int(((i+1) / num_chunks) * 100)
                self.UpdateProgress(progress)
            remaining = total_size % chunk_size
            if remaining > 0:
                read_data = UD_Package.UD_FT4222_SPI.spi_03H_Read(addr_exe, remaining)
                read_data_list.extend(read_data) 
            self.UpdateProgress(100)                                
            binary_data = bytes([int(data, 16) for data in read_data_list])            
            now = datetime.datetime.now()
            timestamp = now.strftime('%m%d_%H%M%S')
            path = timestamp + '_read.bin'            
            with open(path, "wb") as file:
                file.write(binary_data) 
            print('Read Flash Finish')
            UDFrame.LogP(self, 'Read Flash Finish')
            W_list = write_data_list
            R_list = [int(data, 16) for data in read_data_list]
            result = AutoCompare(W_list, R_list)
            if result == True:
                self.Page_3.CompareTC.SetValue('True')
                print('[Auto Compare] True')
                UDFrame.LogP(self, '[Auto Compare] True')
            else:
                self.Page_3.CompareTC.SetValue('False')
                print('[Auto Compare] False')
                UDFrame.LogP(self, '[Auto Compare] False')
                                              
        except AttributeError:
            print('[Error] AttributeError')
            UDFrame.LogP(self, '[Error] AttributeError')
        except Exception as e:
            print(f'[Error] {str(e)}')
            UDFrame.LogP(self, f'[Error] {str(e)}')
            
        self.Page_3.ReadFileCMD.SetLabel('Finish')
        self.Page_3.ReadFileCMD.SetForegroundColour((0,128,0))
        self.Page_3.ReadFileBtn.Enable(True)       
        
    def ReadStatusBtnEvent(self, event):
        self.Page_3.ReadStatusBtn.Enable(False)
        try:
            status = UD_Package.UD_FT4222_SPI.status_Register()
            TempString = 'Read Cmd: 0x05, Data: 0x' + status[0] + '\nRead Cmd: 0x35, Data: 0x' + status[1]
            print(TempString)
            UDFrame.LogP(self, TempString)
            self.Page_3.Stasus_07_00TC.SetValue(status[0])
            self.Page_3.Stasus_15_08TC.SetValue(status[1])
            status_07_00 = status[0]
            status_15_08 = status[1]
            s_07 = status_07_00[0:1]
            s_06 = status_07_00[1:2]
            s_05 = status_07_00[2:3]
            s_04 = status_07_00[3:4]
            s_03 = status_07_00[4:5]
            s_02 = status_07_00[5:6]
            s_01 = status_07_00[6:7]
            s_00 = status_07_00[7:8]
            s_15 = status_15_08[0:1]
            s_14 = status_15_08[1:2]
            s_13 = status_15_08[2:3]
            s_12 = status_15_08[3:4]
            s_11 = status_15_08[4:5]
            s_10 = status_15_08[5:6]
            s_09 = status_15_08[6:7]
            s_08 = status_15_08[7:8]            
            self.Page_3.S07.SetValue(s_07)
            self.Page_3.S06.SetValue(s_06)
            self.Page_3.S05.SetValue(s_05)
            self.Page_3.S04.SetValue(s_04)
            self.Page_3.S03.SetValue(s_03)
            self.Page_3.S02.SetValue(s_02)
            self.Page_3.S01.SetValue(s_01)
            self.Page_3.S00.SetValue(s_00)
            self.Page_3.S15.SetValue(s_15)
            self.Page_3.S14.SetValue(s_14)
            self.Page_3.S13.SetValue(s_13)
            self.Page_3.S12.SetValue(s_12)
            self.Page_3.S11.SetValue(s_11)
            self.Page_3.S10.SetValue(s_10)
            self.Page_3.S09.SetValue(s_09)
            self.Page_3.S08.SetValue(s_08)
        except AttributeError:
            print('[Error] AttributeError')
            UDFrame.LogP(self, '[Error] AttributeError')
        except Exception as e:
            print(f'[Error] {str(e)}')
            UDFrame.LogP(self, f'[Error] {str(e)}')
        self.Page_3.ReadStatusBtn.Enable(True)
    #""" Page_4 Event """----------------------------------------------------------------------------
    def Page2ComboBox0DropdownEvent(self, event):                                   
        self.Page_4.SerialPortComboBox0.Clear()
        PortList = UD_Package.UD_Instrument.Scan_Instrument()
        for x in PortList :
            self.Page_4.SerialPortComboBox0.Append(x)             
        
    def Page2ComboBox0Event(self, event):
        print(self.Page_4.SerialPortComboBox0.GetValue())
        self.Page_4.OpenPort0.SetLabel('Connect')
        self.Page_4.OpenPort0.SetBackgroundColour(wx.NullColour)
        
    def OpenPort0Event(self, event):
        try:
            if 'ASRL' in self.Page_4.SerialPortComboBox0.GetValue():
                if self.Page_4.OpenPort0.GetLabel()=='Connect':
                    UD_Package.UD_Instrument.Open_Meter()
                    SplitStr = re.split('ASRL|::', self.Page_4.SerialPortComboBox0.GetValue())
                    print('COM'+SplitStr[1]+':Digital Multimeter connected.')
                    self.Page_4.OpenPort0.SetLabel('Disconnect')
                    self.Page_4.OpenPort0.SetBackgroundColour((0, 240, 0))
                elif self.Page_4.OpenPort0.GetLabel()=='Disconnect':
                    UD_Package.UD_Instrument.Close_Meter()
                    print('Disconnected.')
                    self.Page_4.OpenPort0.SetLabel('Connect')
                    self.Page_4.OpenPort0.SetBackgroundColour(wx.NullColour)
                    if self.Page_4.dmmThreadBtn0.GetLabel() == 'Stop':
                        UD_Package.UD_Instrument.Meter_Task_Stop()
                        self.Page_4.dmmThreadBtn0.SetLabel('Run')
                        self.Page_4.dmmThreadBtn0.SetBackgroundColour(wx.NullColour)                     
            elif self.Page_4.SerialPortComboBox0.GetValue() == '':
                self.Page_4.OpenPort0.SetLabel('Connect')
                self.Page_4.OpenPort0.SetBackgroundColour(wx.NullColour)
                print('Nothing has been selected.')
            else:
                print(self.Page_4.SerialPortComboBox0.GetValue()+' connected.')
        except pyvisa.errors.VisaIOError as e:
            if e.error_code == pyvisa.constants.VI_ERROR_RSRC_BUSY:
                print('Resource is busy, please try again later')
            else:
                print('An error occurred:', e) 
        except Exception as e:
           print('[Error]', e)

    def dmmAutoMeasure0Event(self, event):
        self.Page_4.dmmAutoMeasureBtn0.Enable(False)
        self.Page_4.dmmCMD0.SetLabel('Run...')
        LoopCount = int(self.Page_4.dmmLoopTC0.GetValue())        
        try:           
            if 'ASRL' in self.Page_4.SerialPortComboBox0.GetValue():              
                    now = datetime.datetime.now()
                    timestamp = now.strftime('_%m%d_%H%M%S')
                    path = timestamp+'_output.csv'
                    with open(path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        i = 0           
                        while i < LoopCount:
                            value = UD_Package.UD_Instrument.Get_Meter()
                            print(value)
                            data = Decimal(value)
                            self.Page_4.dmmStartTC0.SetValue(format(data, ".8f"))                           
                            writer.writerow([format(data, ".8f")])
                            i+=1                               
            else:
                print('Nothing to do.')                
        except Exception as e:
           print('[Error]', e)           
        self.Page_4.dmmCMD0.SetLabel('Finish')
        self.Page_4.dmmCMD0.SetForegroundColour((0,128,0))        
        self.Page_4.dmmAutoMeasureBtn0.Enable(True)
        
    def dmmThread0Event(self, event):
        try:
            if self.Page_4.dmmThreadBtn0.GetLabel()=='Run':
                self.Page_4.dmmThreadBtn0.SetLabel('Stop')                        
                self.Page_4.dmmThreadBtn0.SetBackgroundColour((0, 240, 0))
                UD_Package.UD_Instrument.Get_Meter_Thread()
                self.Page_4.dmmThreadTC0.SetLabel('0.0')
            elif self.Page_4.dmmThreadBtn0.GetLabel()=='Stop':
                self.Page_4.dmmThreadBtn0.SetLabel('Run')
                self.Page_4.dmmThreadBtn0.SetBackgroundColour(wx.NullColour)
                UD_Package.UD_Instrument.Meter_Task_Stop()
        except Exception as e:
           print('[Error]', e)
            
    def Page2ComboBox1DropdownEvent(self, event):                           
        self.Page_4.SerialPortComboBox1.Clear()
        PortList = UD_Package.UD_Instrument.Scan_Instrument()
        for x in PortList :
            self.Page_4.SerialPortComboBox1.Append(x)                   
        
    def Page2ComboBox1Event(self, event):
        print(self.Page_4.SerialPortComboBox1.GetValue())
        
    def OpenPort1Event(self, event):
        try:
            if '0x2380' in self.Page_4.SerialPortComboBox1.GetValue():
                if self.Page_4.OpenPort1.GetLabel()=='Connect':
                    UD_Package.UD_Instrument.Open_Load()
                    SplitStr = re.split('::', self.Page_4.SerialPortComboBox1.GetValue())
                    print(SplitStr[2]+':DC Electronic load connected.')
                    self.Page_4.OpenPort1.SetLabel('Disconnect')
                    self.Page_4.OpenPort1.SetBackgroundColour((0, 240, 0)) 
                elif self.Page_4.OpenPort1.GetLabel()=='Disconnect':
                    UD_Package.UD_Instrument.Close_Meter()
                    print('Disconnected.')
                    self.Page_4.OpenPort1.SetLabel('Connect')
                    self.Page_4.OpenPort1.SetBackgroundColour(wx.NullColour)                            
            elif 'ASRL' in self.Page_4.SerialPortComboBox1.GetValue():
                if self.Page_4.OpenPort1.GetLabel()=='Connect':
                    UD_Package.UD_Instrument.Open_Meter()
                    SplitStr = re.split('ASRL|::', self.Page_4.SerialPortComboBox1.GetValue())
                    print('COM'+SplitStr[1]+':Digital Multimeter connected.')
                    self.Page_4.OpenPort1.SetLabel('Disconnect')
                    self.Page_4.OpenPort1.SetBackgroundColour((0, 240, 0))
                elif self.Page_4.OpenPort1.GetLabel()=='Disconnect':
                    UD_Package.UD_Instrument.Close_Meter()
                    print('Disconnected.')
                    self.Page_4.OpenPort1.SetLabel('Connect')
                    self.Page_4.OpenPort1.SetBackgroundColour(wx.NullColour)
            else:
                print(self.Page_4.SerialPortComboBox1.GetValue()+' connected.')
        except pyvisa.errors.VisaIOError as e:
            if e.error_code == pyvisa.constants.VI_ERROR_RSRC_BUSY:
                print('Resource is busy, please try again later')
            else:
                print('An error occurred:', e) 
            
    def dmmAutoMeasure1Event(self, event):
        self.Page_4.dmmAutoMeasureBtn1.Enable(False)
        self.Page_4.dmmCMD1.SetLabel('Run...')
        LoopCount = int(self.Page_4.dmmLoopTC1.GetValue())        
        try:
            if '0x2380' in self.Page_4.SerialPortComboBox1.GetValue():
                value_str = self.Page_4.dmmStartTC1.GetValue()
                value_float = float(value_str)
                UD_Package.UD_Instrument.Set_Load(value_float)
            elif 'ASRL' in self.Page_4.SerialPortComboBox1.GetValue():              
                    now = datetime.datetime.now()
                    timestamp = now.strftime('_%m%d_%H%M%S')
                    path = timestamp+'_output.csv'
                    with open(path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        i = 0           
                        while i < LoopCount:
                            value = UD_Package.UD_Instrument.Get_Meter()
                            print(value)
                            data = Decimal(value)                              
                            writer.writerow([format(data, ".8f")])
                            i+=1                               
            else:
                print('Nothing to do.')                
        except Exception as e:
           print('[Error]', e)           
        self.Page_4.dmmCMD1.SetLabel('Finish')
        self.Page_4.dmmCMD1.SetForegroundColour((0,128,0))        
        self.Page_4.dmmAutoMeasureBtn1.Enable(True)
                
    def Page2ComboBox2DropdownEvent(self, event):                           
        self.Page_4.SerialPortComboBox2.Clear()
        PortList = UD_Package.UD_Instrument.Scan_Instrument()
        for x in PortList :
            self.Page_4.SerialPortComboBox2.Append(x)                 
        
    def Page2ComboBox2Event(self, event):
        print(self.Page_4.SerialPortComboBox2.GetValue())
        
    def OpenPort2Event(self, event):           
        if '0x2280' in self.Page_4.SerialPortComboBox2.GetValue():
            UD_Package.UD_Instrument.Open_PSupply()
            SplitStr = re.split('::', self.Page_4.SerialPortComboBox2.GetValue())
            print(SplitStr[2]+':Precision Measurement DC Supply connected.')     
        else:
            print(self.Page_4.SerialPortComboBox2.GetValue()+' connected.')
        
    def dmmAutoMeasure2Event(self, event):
        self.Page_4.dmmAutoMeasureBtn2.Enable(False)
        self.Page_4.dmmCMD2.SetLabel('Run...')
        try:    
            if '0x2280' in self.Page_4.SerialPortComboBox2.GetValue():
                Voltage_S = self.Page_4.dmmStartTC2.GetValue()            
                Voltage_E = self.Page_4.dmmEndTC2.GetValue()
                Voltage_step = self.Page_4.dmmStepSC2.GetValue()               
                Voltage_SF = float(Voltage_S)
                Voltage_EF = float(Voltage_E)
                Voltage_stepF = (float(Voltage_step))/1000
                if Voltage_EF >= Voltage_SF:
                    Voltage_f = Voltage_SF
                    path = '_output.csv'
                    with open(path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        while Voltage_f <= (Voltage_EF + Voltage_stepF):
                            UD_Package.UD_Instrument.Set_PSupply(Voltage_f)                             
                            value = UD_Package.UD_Instrument.Get_Meter()                                                             
                            data = Decimal(value)                                                   
                            writer.writerow([str(f"{Voltage_f:.3f}")+' '+format(data, ".8f")])                  
                            Voltage_f += Voltage_stepF
                else:
                    Voltage_f = Voltage_SF
                    path = '_output.csv'
                    with open(path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        while Voltage_f >= Voltage_EF:
                            UD_Package.UD_Instrument.Set_PSupply(Voltage_f)
                            value = UD_Package.UD_Instrument.Get_Meter()                                                         
                            data = Decimal(value)                                                   
                            writer.writerow([str(f"{Voltage_f:.3f}")+' '+format(data, ".8f")])                                             
                            Voltage_f -= Voltage_stepF
            else:
                print('Nothing to do.')
        except ValueError as e:
            print(e)
            
        self.Page_4.dmmCMD2.SetLabel('Finish')
        self.Page_4.dmmCMD2.SetForegroundColour((0,128,0))        
        self.Page_4.dmmAutoMeasureBtn2.Enable(True)
        
    def dmmOutput2Event(self, event):
        if '0x2280' in self.Page_4.SerialPortComboBox2.GetValue():
            UD_Package.UD_Instrument.Set_PSupply_OUTP()
        else:
            print('Nothing to do.')
    #""" Page_5 Event """----------------------------------------------------------------------------        
    def OpenWebCamEvent(self, event):
        try:
            UD_Package.WebCam.WebCam_Cap_Thread(int(self.Page_5.CamChooseTC.GetValue()))
            self.Page_5.OpenWebCamBtn.Enable(False)
            self.Page_5.CloseWebCamBtn.Enable(True)
            self.Page_5.MassShotBtn.Enable(True)
            self.Page_5.SingleShotBtn.Enable(True)
            self.Page_5.SetExposureBar.Enable(True)
            self.Page_5.SetContrastBar.Enable(True)
            self.Page_5.SetSatBar.Enable(True)
            self.Page_5.ReturnDefaultBtn.Enable(True)
            self.Page_5.GetDefaultBtn.Enable(True)
            print('Open the WebCam.')
        except:
            print('No Such WebCam Found!')
    
    def CloseWebCamEvent(self, event):
        UD_Package.WebCam.WebCam_Cap_Stop()
        self.Page_5.CloseWebCamBtn.Enable(False)
        self.Page_5.OpenWebCamBtn.Enable(True)
        self.Page_5.MassShotBtn.Enable(False)
        self.Page_5.SingleShotBtn.Enable(False)
        self.Page_5.SetExposureBar.Enable(False)
        self.Page_5.SetContrastBar.Enable(False)
        self.Page_5.SetSatBar.Enable(False)
        self.Page_5.ReturnDefaultBtn.Enable(False)
        self.Page_5.GetDefaultBtn.Enable(False)       

    def MassShootingEvent(self, event):        
        self.Page_5.MassShotBtn.Enable(False)
        RunFlag = False
        if self.Page_5.MassShotStopCB.IsChecked():
            RunFlag = False
            print('[No action] Uncheck the "Stop" option.')
        else:
            RunFlag = True
        if RunFlag == True:
            #self.Page_5.MassShotCMD.SetLabel('Run...')
            
            print('Execute Mass Shooting...Please Wait!')
            FileName = self.Page_5.PictureNameTC.GetValue()
            Pic_Qnt = int(self.Page_5.PictureQntTC.GetValue())
            Pic_Interval = float(self.Page_5.IntervalTC.GetValue()) 
            UD_Package.WebCam.Multi_Picture_Thread(FileName, Pic_Qnt, Pic_Interval)
            #print("Mass Shooting Done!")
            
            #self.Page_5.MassShotCMD.SetLabel('Finish')
            #self.Page_5.MassShotCMD.SetForegroundColour((0,128,0))
        self.Page_5.MassShotBtn.Enable(True)
       
    def MassShotStopEvent(self, event):
        if self.Page_5.MassShotStopCB.IsChecked():
            UD_Package.WebCam.Multi_Picture_Stop()
    
    def SingleShootingEvent(self, event):
        self.Page_5.SingleShotBtn.Enable(False)
        UD_Package.WebCam.WebCam_Picture(self.Page_5.SingleShotTC.GetValue())
        print('Single Shooting Done!')
        self.Page_5.SingleShotBtn.Enable(True)   
        
    def SetExposureEvent(self, event):
        SetEV = self.Page_5.SetExposureBar.GetThumbPosition()
        self.Page_5.SetExposureTC.SetValue(str(SetEV-6))
        UD_Package.WebCam.WebCam_Exposure(SetEV-6)

    def SetContrastEvent(self, event):
        SetContrast = self.Page_5.SetContrastBar.GetThumbPosition()
        self.Page_5.SetContrastTC.SetValue(str(SetContrast*10))
        UD_Package.WebCam.WebCam_Contrast(SetContrast*10)

    def SetSatEvent(self, event):
        SetSat = self.Page_5.SetSatBar.GetThumbPosition()
        self.Page_5.SetSatTC.SetValue(str(SetSat))
        UD_Package.WebCam.WebCam_Saturation(SetSat)

    def ReturnDefaultEvent(self, event):
        UD_Package.WebCam.WebCam_Set_Default()

    def GetDefaultEvent(self, event):
        Default = UD_Package.WebCam.WebCam_Get_Default()
        # 0:Exposure
        # 1:Contrast
        # 2:Saturation
        Exp_Value = Default[0]
        Con_Value = Default[1]
        Sat_Value = Default[2]
        self.Page_5.SetExposureTC.SetValue(str(Exp_Value))
        self.Page_5.SetContrastTC.SetValue(str(Con_Value))
        self.Page_5.SetSatTC.SetValue(str(Sat_Value))    
    #""" Page_6 Event """--------------------------------------------------------------------------
    def XtalkBuildEvent(self, event):
        try:          
            now = datetime.datetime.now()
            timestamp = now.strftime('_%m%d_%H%M%S')              
            XtalkWid = int(self.Page_6.XtalkWTC.GetValue())
            XtalkHei = int(self.Page_6.XtalkHTC.GetValue())
            XtalkR = int(self.Page_6.XtalkRTC.GetValue())
            XtalkG = int(self.Page_6.XtalkGTC.GetValue())
            XtalkB = int(self.Page_6.XtalkBTC.GetValue())
            XtalkA = int(self.Page_6.XtalkATC.GetValue())
            squareW = int(self.Page_6.WriteWTC.GetValue())
            squareH = int(self.Page_6.WriteHTC.GetValue())
            squareR = int(self.Page_6.WriteRTC.GetValue())
            squareG = int(self.Page_6.WriteGTC.GetValue())
            squareB = int(self.Page_6.WriteBTC.GetValue())
            squareA = int(self.Page_6.WriteATC.GetValue())
            image = Image.new("RGBA", (XtalkWid, XtalkHei), (XtalkR, XtalkG, XtalkB, XtalkA))
            selected = self.Page_6.FileFormatRBox.GetSelection()
            
            if selected == 0:
                if squareW != 0 and squareH != 0:
                    left = (XtalkWid - squareW) // 2
                    top = (XtalkHei - squareH) // 2
                    right = left + squareW
                    bottom = top + squareH
                    square = (squareR, squareG, squareB, squareA)
                    image.paste(square, (left, top, right, bottom))
                    SaveFileName = f'{timestamp}_CrrossTalk_{XtalkWid}x{XtalkHei}.png'
                    image.save(SaveFileName, format="PNG")
                else:              
                    SaveFileName = f'{timestamp}_CrrossTalk_{XtalkWid}x{XtalkHei}.png'
                    image.save(SaveFileName, format="PNG")
                
            elif selected == 1:
                if squareW != 0 and squareH != 0:
                    left = (XtalkWid - squareW) // 2
                    top = (XtalkHei - squareH) // 2
                    right = left + squareW
                    bottom = top + squareH
                    square = (squareR, squareG, squareB, squareA)
                    image.paste(square, (left, top, right, bottom))
                    SaveFileName = f'{timestamp}_CrrossTalk_{XtalkWid}x{XtalkHei}.bmp'
                    image.save(SaveFileName, format="BMP")
                else:              
                    SaveFileName = f'{timestamp}_CrrossTalk_{XtalkWid}x{XtalkHei}.bmp'
                    image.save(SaveFileName, format="BMP")
                
            else:
                print('Nothing to do.')              
                
        except ValueError as e:
            print(e)
        print(SaveFileName)
        UDFrame.LogP(self, SaveFileName)
    #""" LogView Event """--------------------------------------------------------------------------
    def LogP(self, Slogging):
        self.logframe.textTC.AppendText(str(Slogging)+'\r\n')
        
    def ToolScriptSaveEvent(self, event):
        if self.logframe.textTC.GetValue() == '':
            pass
        else:
            self.logframe.LVSaveBtn.Enable(False)
            now = datetime.datetime.now()
            timestamp = now.strftime('_%m%d_%H%M%S')
            path = timestamp+'_log.txt'        
            with open(path, "w") as f:
                f.write(self.logframe.textTC.GetValue())
            self.logframe.LVSaveBtn.Enable(True)
        
    def ToolScriptClearEvent(self, event):        
        self.logframe.textTC.SetValue('')
        
    def LogViewOnClose(self, event):
        self.logframe.Hide()
        print('[Closed] LogView hide.')
####################################################################################################
""" Function Definition """ 
def generate_unique_numbers(n):
    if n > 256:
        print("Error: n should be less than or equal to 256.")
        return []

    numbers = set()
    while len(numbers) < n:
        num = random.randint(0, 255)
        numbers.add(num)

    return numbers  # 直接返回 set
     
def WrapStr(string, max_width):
    temp = [string[i:i+max_width] for i in range(0, len(string), max_width)]
    result = '\n'.join(temp)
    return result

def HEXValueCheck(HexData):
    try:
        hex(int(HexData, 16)).upper()
        return HexData
    except ValueError:
        return '0' 
    
def ReadBinFile(file_path):    
    with open(file_path, "rb") as file:
        binary_data = file.read()
    data_array = list(binary_data)
    return data_array

def AutoCompare(W_list, R_list):
    if W_list == R_list:
        return True
    else:
        return False        
        
def KillThread():   
    UD_Package.WebCam.Multi_Picture_Stop()
    UD_Package.WebCam.WebCam_Cap_Stop()
    UD_Package.UD_Instrument.Meter_Task_Stop()
####################################################################################################
# Run the program
if __name__ == "__main__":               
    app = wx.App() 
    frame = UDFrame(UD_ToolName)
    frame.SetIcon(wx.Icon('UD_Icon/UltraDisplayTool.ico')) 
    frame.Show()
    app.MainLoop() #start the applications
#------------------------------------------------------------------------------------------
#EOF