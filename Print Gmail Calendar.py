# Copyright 2010, Mark Kendrat
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

FileButton ="1264458174384.png"
CloseWindowButton = "1264458128527.png"
OkCancelButtons = "1264457738647.png"
OkButton = "1264457744310.png"
SystemStartButton = "1264453432087.png"
FirefoxStartButton = "1264453848346.png"
BookmarksButton = "1264454047986.png"
GmailBookmark = "1264454808693.png"
GmailLoadedImage = "1264454851923.png"
GmailCalendarButton = "1264454723262.png"
GmailPrintButton = "1264455178791.png"
BlackAndWhite = "1264455865056.png"
PrintSaveAsCancelButtons = "1264456519100.png"
CancelButton = "1264456528456.png"
PrintButton = "1264455258249.png"
GmailMonthButton = "1264455266391.png"
CheckBox = "1264455565026.png"
click (SystemStartButton)
click (FirefoxStartButton)
click (BookmarksButton)
click (GmailBookmark)
wait (GmailLoadedImage, timeout = 8000)
click (GmailCalendarButton)
click (GmailMonthButton)
click (GmailPrintButton)
#if find (BlackAndWhite):
#   popup ("Black and White")
#   find.region.inside ().click (CheckBox)
click (PrintButton)
click (OkButton)
sleep (5)
click (CancelButton)
click (FileButton)
click (CloseWindowButton)
