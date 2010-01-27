# Copyright 2010, Mark Kendrat
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

NumberOfMonthsToPrint = 3

class PrintDialog:
   ReadyImage = "1264569817966.png"
   OkButton = "1264569589937.png"
class StartMenu:
   Button = "1264453432087.png"
   FirefoxStartButton = "1264453848346.png"
class Firefox:
   FileButton ="1264458174384.png"
   CloseWindowButton = "1264458128527.png"
   UrlBox = "1264568783832.png"
   BookmarksButton = "1264454047986.png"
   def Open ():
#      openApp ("firefox")
      click (StartMenu.Button)
      click (StartMenu.FirefoxStartButton)
   Open = staticmethod (Open)
   def CloseWindow ():
      click (Firefox.FileButton)
      click (Firefox.CloseWindowButton)
   CloseWindow = staticmethod (CloseWindow)
class Gmail:
   ReadyImage = "1264454851923.png"
   CalendarReadyImage = "1264536171212.png"
   CalendarButton = "1264454723262.png"
   NextPageButton = "1264570033916.png"
   MonthButton = "1264455266391.png"
   PrintButton = "1264455178791.png"
   PrintDialogBlackAndWhiteButton = "1264568374364.png"
   PrintDialogPrintButton = "1264455258249.png"
   PrintDialogCancelButton = "1264456528456.png"
   def Open ():
      Firefox.Open ()
      type (Firefox.UrlBox, "gmail.com\n")
      wait (Gmail.ReadyImage, timeout = 8000)
   Open = staticmethod (Open)
   def OpenCalendar ():
      Firefox.Open ()
      type (Firefox.UrlBox, "google.com/calendar\n")
      wait (Gmail.CalendarReadyImage, 8000)
   OpenCalendar = staticmethod (OpenCalendar)
   def GotoCalendar ():
      click (Gmail.CalendarButton)
   GotoCalendar = staticmethod (GotoCalendar)

Gmail.OpenCalendar ()
click (Gmail.MonthButton)
for I in range (NumberOfMonthsToPrint):
   click (Gmail.PrintButton)
   click (Gmail.PrintDialogBlackAndWhiteButton)
   click (Gmail.PrintDialogPrintButton)
   wait (PrintDialog.ReadyImage, 8000)
   click (PrintDialog.OkButton)
   sleep (5)
   click (Gmail.PrintDialogCancelButton)
   click (Gmail.NextPageButton)
Firefox.CloseWindow( )
