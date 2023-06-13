# -*- encoding=utf8 -*-
__author__ = "Anantha.k"
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
from poco.drivers.ios import iosPoco
from  airtest.core.device  import  Device
import sys
from datetime import datetime
from datetime import timedelta, date
from airtest.report.report import *
import re
import os
sys.path.append('/usr/local/bin/python3')
poco = iosPoco() 
class TicketMelonSanity:
    def __init__(self):
            return   
    def launchTmApp(self):
            self.closeTheExistingApp()
            log("Launch",desc="LAUNCH THE TEST FLIGHT APPLICATION")
            start_app("com.apple.TestFlight")
            installalert = poco(name="INSTALL")
            if  installalert.exists():
                    log("Launch",desc="INSTALL THE TICKETMELON APPLICATION")
                    poco(name="INSTALL").click()
                    poco(name="OPEN").wait_for_appearance()    
                    poco(name="OPEN").click()
                    poco(name="Next").wait_for_appearance()
                    poco(name="Next").click()
                    poco(name="Start Testing").wait_for_appearance()
                    poco(name="Start Testing").click()
                    poco(name="EN").wait_for_appearance()
                    poco(name="EN").click()
                    poco(name="DONE").click()
                    poco(name="Get Started →").wait_for_appearance()
                    poco(name="Get Started →").click()
                    self.trackActivity()
                    poco(name="Email Address").wait_for_appearance()
                    self.loginToApp()
            else:    
                    log("OPEN",desc="OPEN THE TICKETMELON APPLICATION")
                    poco(name="OPEN").wait_for_appearance()    
                    poco(name="OPEN").click()
            
    def searchEvent(self,args):
            log("SEARCH",desc="SEARCH THE EVENT NAME: "+args)
            poco(label="Search, tab, 2 of 4").click()
            poco(label="").wait_for_appearance()
            poco(label="").click()
            self.findEvents()
            poco(label="").click()
            text(args)
            if  poco(label="Hmm. No results!").exists():
                log("EVENT",desc="EVENT NOT FOUND")
            else:
                poco(type="ScrollView").child().click()
                poco(label="Get tickets").wait_for_appearance()
                poco(label="Get tickets").click()
            if  poco(label=args).exists():
                log("EVENT",desc="EVENT SEARCH SUCCESSFUL")
    def loginToApp(self):
            log("Login",desc="LOG INTO THE APPLICATION")  
            if  poco(name="Next").exists():
                poco(name="Next").click()
                poco(name="Start Testing").wait_for_appearance()
                poco(name="Start Testing").click()
                poco(name="EN").wait_for_appearance()
                poco(name="EN").click()
                poco(name="DONE").click()
                poco(name="Get Started →").wait_for_appearance()
                poco(name="Get Started →").click()
            poco(label="Email Address").wait_for_appearance()
            poco(label="Email Address").click()
            text("roan.l@rznet.com")
            poco(label="Password").click()
            text("Libelo05!")
            poco(name="Sign In").click()
            poco(label="Profile, tab, 4 of 4").wait_for_appearance()
    def bookTicket(self):
            log("Book",desc="PAYMENT FOR THE TICKET")
            if  poco(label="0").exists():
                (poco("Window").child("Other").child("Other").child("Other").offspring("Button")[1]).click()
                poco(label="Continue").click()
                sleep(5)
                itempaynow=poco(label="Pay Now")
                while not (itempaynow.exists()):
                    swipe((1000, 1000), (200, 200),duration=1, steps=10)
                log("PAYNOW",desc="PAY NOW IS ENABLED")
                poco(label="By checking out, I agree to Ticketmelon's Terms of Service and Event Organizer's Disclaimer. I accept that the items in this order cannot be canceled and payments are non-refundable.").click()
                assert_equal(str(poco(label="Pay Now").attr("isEnabled")), "1", "The pay now button is enabled")
                log("PAYNOW",desc="PAY NOW IS DISABLED")
                poco(label="By checking out, I agree to Ticketmelon's Terms of Service and Event Organizer's Disclaimer. I accept that the items in this order cannot be canceled and payments are non-refundable.").click()
                assert_equal(str(poco(label="Pay Now").attr("isEnabled")), "0", "The pay now button is disabled")
                poco(name="Button").click()
                sleep(2)
                poco(name="Button").click()
                sleep(2)
                poco(name="Button").click()
    def closeTheExistingApp(self):
        try:
            stop_app("com.ticketmelon.app.attendee")
            print("Ticketmelon app is closed")
            stop_app("com.apple.TestFlight")   
            print("Testflight app is closed")
        except:    
            print("An exception occurred in closing the opened apps")
    def trackActivity(self):
            trackalert = poco(label="Ask App Not to Track")
            if  trackalert.exists():
                    trackalert.click()
    def ticketHistory(self,ticket,args1,flag):
            log("HISTORY",desc="TICKET HISTORY")
            poco(label="Myticket, tab, 3 of 4").wait_for_appearance()
            poco(label="Myticket, tab, 3 of 4").click()
            poco(label="Upcoming").wait_for_appearance()
            evantlist=poco(name='ScrollView').sibling().attr("label")
            if flag=='yes':
                args2="Tracking View Ticket"
            else:
                args2="View Ticket"
            if ticket=="" or ticket=="0":
                ticket=="1"
            else:
                ticket=ticket
            print("{} {}".format(args1,flag))
            evant=evantlist.split("{} {}".format(args1,args2))
            print("Events Full list",evant)
            for i_event in evant:
                tickat = i_event.split(" ")
                tickat_count = tickat[-8]
                print(tickat_count)
                print(ticket)
                if ticket == tickat_count:
                    tickatstart = " ".join(tickat[-8:])
                    event_name="{} {} {}".format(tickatstart.strip(), args1, args2)
            print("Event search-",event_name)
            evantnew=poco(label=""+event_name+"")
            while not (evantnew.exists()):
                poco.scroll(direction="vertical", percent=0.3, duration=1)
                scrolpersentage=poco("ScrollView").offspring("ScrollView").child()[0].attr("value")
                scrolpersentage= str(scrolpersentage)
                if(scrolpersentage == "None"):
                    scrolpersentage=poco("ScrollView").offspring("ScrollView").child()[1].attr("value")
                print(scrolpersentage)
                if(scrolpersentage=="100%"):
                    break
            try:
                newposy=float("0.70")
                posx,posy=evantnew.attr("pos")
                print(posx,posy)
                if posy >= newposy:
                    poco.scroll(direction="vertical", percent=0.3, duration=1)
                    sleep(3)
                touch([0.5,0.67])
                sleep(5)
                assert_equal(str(poco(name=""+args1+"").attr("label")), ""+args1+"", "The Ticket details are displayed successfully")
                snapshot(msg="TicketDetails")
                poco(label="E-Tickets").child(name="Other").child(name="Other").click()
            except:    
                print("Event not displayed")
                sys.exit()
            
    def findEvents(self):
            trackalert = poco(label=" Find events by name, or location")
            if  trackalert.exists():
                    trackalert.click()
            else:
                poco(label="").click()
                poco(label="delete").click()
                poco(label="").click()
                poco(label="Select All").click()
                poco(label="Cut").click()
    def logout(self):
        poco(label="Profile, tab, 4 of 4").wait_for_appearance()
        poco(label="Profile, tab, 4 of 4").click()
        poco(label="Edit Profile").wait_for_appearance()
        itemlogout=poco(label="Log out")
        while not (itemlogout.exists()):
                swipe((1000, 1000), (200, 200),duration=1, steps=10)
        versionNumber=poco(label="Log out").sibling()[-4].attr("label")
        print(versionNumber)
        poco(label="Log out").click()
        poco(label="OK").wait_for_appearance()
        poco(label="OK").click()
        presentDay=datetime.now()
        presentDate = presentDay.strftime("%d%m%Y%H%M%S")
        fylename="TmIOS_"+versionNumber+"_"+presentDate
        fylename=fylename.replace(" ","")
        print(fylename)
        simple_report("/Users/rzqaimac/Desktop/Automation/TicketmelonIOS.air",logpath="/var/folders/qh/k7pz3pjn0hqcscl1vplw96rc0000gn/T/AirtestIDE/scripts/a407a3b5bd425774a7c1da9d6d36975e",logfile="/var/folders/qh/k7pz3pjn0hqcscl1vplw96rc0000gn/T/AirtestIDE/scripts/a407a3b5bd425774a7c1da9d6d36975e/log.txt",output="/var/folders/qh/k7pz3pjn0hqcscl1vplw96rc0000gn/T/AirtestIDE/scripts/a407a3b5bd425774a7c1da9d6d36975e/"+fylename+".html")
        
        self.closeTheExistingApp()
    def numbersToStrings(self,argument):
        if argument == "1":
            return "Jan"
        elif argument == "2":
                return "Feb"
        elif argument == "3":
                return "Mar"
        elif argument == "4":
                return "Apr"    
        elif argument == "5":
                return "May"    
        elif argument == "6":
                return "Jun"    
        elif argument == "7":
                return "Jul"
        elif argument == "8":
                return "Aug"
        elif argument == "9":
                return "Sep"
        elif argument == "10":
                return "Oct"
        elif argument == "11":
                return "Nov"
        elif argument == "12":
                return "Dec"    
    def scrollevant(self,args1):
            itemscroll=poco("Horizontal scroll bar, 1 page").sibling()[-3].attr("value")
            print(itemscroll)
            while not (args1.exists()):
                swipe((1000, 1000), (200, 200),duration=1, steps=10)
                scrolpersentage=poco("ScrollView").offspring("ScrollView").child()[0].attr("value")
                scrolpersentage= str(scrolpersentage)
                if(scrolpersentage == "None"):
                    scrolpersentage=poco("ScrollView").offspring("ScrollView").child()[1].attr("value")
                print(scrolpersentage)
                if(scrolpersentage=="100%"):
                    break
            try:
                args1.click()
            except:    
                print("Event not displayed")
    
                
Object = TicketMelonSanity()
Object.launchTmApp()
Object.loginToApp()
#Object.searchEvent("กิจกรรมดูแลช้าง ปางช้างแม่ริม")
#Object.bookTicket()
#Object.ticketHistory("1","Rz normal event - 11/05/2023","yes")
Object.logout()