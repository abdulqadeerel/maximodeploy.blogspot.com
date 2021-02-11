#Imports
from java.util import Date 
from java.text import SimpleDateFormat
from psdi.mbo import MboConstants 
from psdi.server import MXServer
from java.util import Calendar
from psdi.app.common import DateUtility

#Milliseconds Constants
MILLISECONDS_DAY= 86400000 
MILLISECONDS_HOUR = 3600000
MILLISECONDS_MINUTE = 60000 

#Default hours and minutes values
days = 0
hours = 0
minutes = 0 

#If Actual Start and Actual Finish are not null, so calculate Estimated Duration
if not mbo.isNull('CHANGEDATE') and mbo.getString("STATUS") in ["RCAREVIEW"]  :

    FRACSet = MXServer.getMXServer().getMboSet("FRACSTATUS", mbo.getUserInfo())
    FRACSet.setWhere("FRACASNUM='"+ mbo.getString("FRACASNUM")+"' and STATUS='RCAINPROG' ")
    rcainprg = FRACSet.moveLast()
    rcainprgdate=rcainprg.getDate('FRACASETC')
    rcareviewdate=mbo.getDate('CHANGEDATE')
    if rcareviewdate >= rcainprgdate:
        cal2 = Calendar.getInstance();
        cal = Calendar.getInstance();
        cal2.setTime(rcareviewdate)
        etcdate=rcainprgdate.getTime() 
        cal.setTime(rcainprgdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.FRIDAY]:
            rcareviewdate = DateUtility.getDate(rcareviewdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.SATURDAY]:
            rcareviewdate = DateUtility.addDays(rcareviewdate,-1)
            rcareviewdate = DateUtility.getDate(rcareviewdate)
        cal = Calendar.getInstance();
        cal2.setTime(rcareviewdate)
        
        etcdate=rcainprgdate.getTime() 
        cal.setTime(rcainprgdate)
        
        diff = rcareviewdate.getTime() - rcainprgdate.getTime() 
        #Gets the days hours and minutes from the milliseconds difference
        days= long(diff)/MILLISECONDS_DAY
        hours = long(diff) / MILLISECONDS_HOUR
        minutes = (long(diff) / MILLISECONDS_MINUTE) - (long(hours) * 60) 
        loop=1
        days=abs(days)
        overdue=hours
    
        while (loop<=days):
                    cal.add(cal.DATE, +1)
                    if (cal.get(cal.DAY_OF_WEEK)) in [cal.FRIDAY,cal.SATURDAY] : 
                            
                            overdue=overdue-24
    #Sets Estimated Duration value as String without access check
    
                    loop=loop+1
    
        if  SimpleDateFormat("MM/dd/yyyy").format(rcareviewdate) ==SimpleDateFormat("MM/dd/yyyy").format(rcainprgdate):
                rcainprg.setValue("OVERDUEDURATION",str(hours) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
        else:  
            rcainprg.setValue("OVERDUEDURATION",str(overdue) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
            rcainprg.setValue("ISOVERDUE","1", MboConstants.NOACCESSCHECK)
        FRACSet.save()
    
if not mbo.isNull('CHANGEDATE') and mbo.getString("STATUS") in ["RCAAPPR","RCAREJECT"]  :
    FRACSet = MXServer.getMXServer().getMboSet("FRACSTATUS", mbo.getUserInfo())
    FRACSet.setWhere("FRACASNUM='"+ mbo.getString("FRACASNUM")+"' and STATUS='RCAREVIEW' ")
    rcareview = FRACSet.moveLast()
    rcareviewdate=rcareview.getDate('FRACASETC')
    rcaapprdate=mbo.getDate('CHANGEDATE')
    if rcaapprdate >= rcareviewdate:
        cal2 = Calendar.getInstance();
        cal = Calendar.getInstance();
        cal2.setTime(rcaapprdate)
        etcdate=rcareviewdate.getTime() 
        cal.setTime(rcareviewdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.FRIDAY]:
            rcaapprdate = DateUtility.getDate(rcaapprdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.SATURDAY]:
            rcaapprdate = DateUtility.addDays(rcaapprdate,-1)
            rcaapprdate = DateUtility.getDate(rcaapprdate)
        cal = Calendar.getInstance();
        cal2.setTime(rcaapprdate)
        
        etcdate=rcareviewdate.getTime() 
        cal.setTime(rcareviewdate)
        
        diff = rcaapprdate.getTime() - rcareviewdate.getTime() 
        #Gets the days hours and minutes from the milliseconds difference
        days= long(diff)/MILLISECONDS_DAY
        hours = long(diff) / MILLISECONDS_HOUR
        minutes = (long(diff) / MILLISECONDS_MINUTE) - (long(hours) * 60) 
        loop=1
        days=abs(days)
        overdue=hours
    
        while (loop<=days):
                    cal.add(cal.DATE, +1)
                    if (cal.get(cal.DAY_OF_WEEK)) in [cal.FRIDAY,cal.SATURDAY] : 
                            
                            overdue=overdue-24
    #Sets Estimated Duration value as String without access check
    
                    loop=loop+1
    
        if  SimpleDateFormat("MM/dd/yyyy").format(rcaapprdate) ==SimpleDateFormat("MM/dd/yyyy").format(rcareviewdate):
                rcareview.setValue("OVERDUEDURATION",str(hours) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
        else:  
            rcareview.setValue("OVERDUEDURATION",str(overdue) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
            rcareview.setValue("ISOVERDUE","1", MboConstants.NOACCESSCHECK)
        FRACSet.save()
    
#Sets Estimated Duration value as String without access check

if not mbo.isNull('CHANGEDATE') and mbo.getString("STATUS") in ["CAREVIEW"]  :
    FRACSet = MXServer.getMXServer().getMboSet("FRACSTATUS", mbo.getUserInfo())
    FRACSet.setWhere("FRACASNUM='"+ mbo.getString("FRACASNUM")+"' and STATUS='CAINPROG' ")
    carinprg = FRACSet.moveLast()
    carinprgdate=carinprg.getDate('FRACASETC')
    careviewdate=mbo.getDate('CHANGEDATE')
    if careviewdate >= carinprgdate:
        cal2 = Calendar.getInstance();
        cal = Calendar.getInstance();
        cal2.setTime(careviewdate)
        etcdate=carinprgdate.getTime() 
        cal.setTime(carinprgdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.FRIDAY]:
            careviewdate = DateUtility.getDate(careviewdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.SATURDAY]:
            careviewdate = DateUtility.addDays(careviewdate,-1)
            careviewdate = DateUtility.getDate(careviewdate)
        cal = Calendar.getInstance();
        cal2.setTime(careviewdate)
        
        etcdate=carinprgdate.getTime() 
        cal.setTime(carinprgdate)
        
        diff = careviewdate.getTime() - carinprgdate.getTime() 
        #Gets the days hours and minutes from the milliseconds difference
        days= long(diff)/MILLISECONDS_DAY
        hours = long(diff) / MILLISECONDS_HOUR
        minutes = (long(diff) / MILLISECONDS_MINUTE) - (long(hours) * 60) 
        loop=1
        days=abs(days)
        overdue=hours
    
        while (loop<=days):
                    cal.add(cal.DATE, +1)
                    if (cal.get(cal.DAY_OF_WEEK)) in [cal.FRIDAY,cal.SATURDAY] : 
                            
                            overdue=overdue-24
    #Sets Estimated Duration value as String without access check
    
                    loop=loop+1
    
        if  SimpleDateFormat("MM/dd/yyyy").format(careviewdate) ==SimpleDateFormat("MM/dd/yyyy").format(carinprgdate):
                carinprg.setValue("OVERDUEDURATION",str(hours) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
        else:  
            carinprg.setValue("OVERDUEDURATION",str(overdue) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
            carinprg.setValue("ISOVERDUE","1", MboConstants.NOACCESSCHECK)
        FRACSet.save()
#Sets Estimated Duration value as String without access check

    
if not mbo.isNull('CHANGEDATE') and mbo.getString("STATUS") in  ["CAAPPR","CAREJECT"]  :
    FRACSet = MXServer.getMXServer().getMboSet("FRACSTATUS", mbo.getUserInfo())
    FRACSet.setWhere("FRACASNUM='"+ mbo.getString("FRACASNUM")+"' and STATUS='CAREVIEW' ")
    careview = FRACSet.moveLast()
    careviewdate=careview.getDate('FRACASETC')
    caapprdate=mbo.getDate('CHANGEDATE')
    if caapprdate >= careviewdate:
        cal2 = Calendar.getInstance();
        cal = Calendar.getInstance();
        cal2.setTime(caapprdate)
        etcdate=careviewdate.getTime() 
        cal.setTime(careviewdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.FRIDAY]:
            caapprdate = DateUtility.getDate(caapprdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.SATURDAY]:
            caapprdate = DateUtility.addDays(caapprdate,-1)
            caapprdate = DateUtility.getDate(caapprdate)
        cal = Calendar.getInstance();
        cal2.setTime(caapprdate)
        
        etcdate=careviewdate.getTime() 
        cal.setTime(careviewdate)
        
        diff = caapprdate.getTime() - careviewdate.getTime() 
        #Gets the days hours and minutes from the milliseconds difference
        days= long(diff)/MILLISECONDS_DAY
        hours = long(diff) / MILLISECONDS_HOUR
        minutes = (long(diff) / MILLISECONDS_MINUTE) - (long(hours) * 60) 
        loop=1
        days=abs(days)
        overdue=hours
    
        while (loop<=days):
                    cal.add(cal.DATE, +1)
                    if (cal.get(cal.DAY_OF_WEEK)) in [cal.FRIDAY,cal.SATURDAY] : 
                            
                            overdue=overdue-24
    #Sets Estimated Duration value as String without access check
    
                    loop=loop+1
    
        if  SimpleDateFormat("MM/dd/yyyy").format(caapprdate) ==SimpleDateFormat("MM/dd/yyyy").format(careviewdate):
                careview.setValue("OVERDUEDURATION",str(hours) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
        else:  
            careview.setValue("OVERDUEDURATION",str(overdue) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
            careview.setValue("ISOVERDUE","1", MboConstants.NOACCESSCHECK)
        FRACSet.save()
#Sets Estimated Duration value as String without access check

    
if not mbo.isNull('CHANGEDATE') and mbo.getString("STATUS") in  ["IMPACCEPTED","IMPREJECT"]  :
    FRACSet = MXServer.getMXServer().getMboSet("FRACSTATUS", mbo.getUserInfo())
    FRACSet.setWhere("FRACASNUM='"+ mbo.getString("FRACASNUM")+"' and STATUS='IMPREVIEW' ")
    impreview = FRACSet.moveLast()
    impreviewdate=impreview.getDate('FRACASETC')
    impaccepteddate=mbo.getDate('CHANGEDATE')
    if impaccepteddate >= impreviewdate:
        cal2 = Calendar.getInstance();
        cal = Calendar.getInstance();
        cal2.setTime(impaccepteddate)
        etcdate=impreviewdate.getTime() 
        cal.setTime(impreviewdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.FRIDAY]:
            impaccepteddate = DateUtility.getDate(impaccepteddate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.SATURDAY]:
            impaccepteddate = DateUtility.addDays(impaccepteddate,-1)
            impaccepteddate = DateUtility.getDate(impaccepteddate)
        cal = Calendar.getInstance();
        cal2.setTime(impaccepteddate)
        
        etcdate=impreviewdate.getTime() 
        cal.setTime(impreviewdate)
        
        diff = impaccepteddate.getTime() - impreviewdate.getTime() 
        #Gets the days hours and minutes from the milliseconds difference
        days= long(diff)/MILLISECONDS_DAY
        hours = long(diff) / MILLISECONDS_HOUR
        minutes = (long(diff) / MILLISECONDS_MINUTE) - (long(hours) * 60) 
        loop=1
        days=abs(days)
        overdue=hours
    
        while (loop<=days):
                    cal.add(cal.DATE, +1)
                    if (cal.get(cal.DAY_OF_WEEK)) in [cal.FRIDAY,cal.SATURDAY] : 
                            
                            overdue=overdue-24
    #Sets Estimated Duration value as String without access check
    
                    loop=loop+1
    
        if  SimpleDateFormat("MM/dd/yyyy").format(impaccepteddate) ==SimpleDateFormat("MM/dd/yyyy").format(impreviewdate):
                impreview.setValue("OVERDUEDURATION",str(hours) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
        else:  
            impreview.setValue("OVERDUEDURATION",str(overdue) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
            impreview.setValue("ISOVERDUE","1", MboConstants.NOACCESSCHECK)
        FRACSet.save()
    
#Sets Estimated Duration value as String without access check

if not mbo.isNull('CHANGEDATE') and mbo.getString("STATUS") in  ["IMPREVIEW"]  :
    FRACSet = MXServer.getMXServer().getMboSet("FRACCORACTION", mbo.getUserInfo())
    FRACSet.setWhere("FRACASNUM='"+ mbo.getString("FRACASNUM")+"' and ACTIONETC=(SELECT MAX(ACTIONETC) FROM FRACCORACTION WHERE STATUS='COMP' and FRACASNUM='"+ mbo.getString("FRACASNUM")+"' ) ")
    impinprog = FRACSet.moveLast()
    FRACSet2 = MXServer.getMXServer().getMboSet("FRACSTATUS", mbo.getUserInfo())
    FRACSet2.setWhere("FRACASNUM='"+ mbo.getString("FRACASNUM")+"' and STATUS='IMPINPROG' ")
    impinprog2 = FRACSet2.moveLast()
    impinprogdate=impinprog.getDate('ACTIONETC')
    impreviewdate=mbo.getDate('CHANGEDATE')
    if impreviewdate >= impinprogdate:
        cal2 = Calendar.getInstance();
        cal = Calendar.getInstance();
        cal2.setTime(impreviewdate)
        etcdate=impinprogdate.getTime() 
        cal.setTime(impinprogdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.FRIDAY]:
            impreviewdate = DateUtility.getDate(impreviewdate)
        if (cal2.get(cal2.DAY_OF_WEEK)) in  [cal2.SATURDAY]:
            impreviewdate = DateUtility.addDays(impreviewdate,-1)
            impreviewdate = DateUtility.getDate(impreviewdate)
        cal = Calendar.getInstance();
        cal2.setTime(impreviewdate)
        
        etcdate=impinprogdate.getTime() 
        cal.setTime(impinprogdate)
        
        diff = impreviewdate.getTime() - impinprogdate.getTime() 
        #Gets the days hours and minutes from the milliseconds difference
        days= long(diff)/MILLISECONDS_DAY
        hours = long(diff) / MILLISECONDS_HOUR
        minutes = (long(diff) / MILLISECONDS_MINUTE) - (long(hours) * 60) 
        loop=1
        days=abs(days)
        overdue=hours
    
        while (loop<=days):
                    cal.add(cal.DATE, +1)
                    if (cal.get(cal.DAY_OF_WEEK)) in [cal.FRIDAY,cal.SATURDAY] : 
                            
                            overdue=overdue-24
    #Sets Estimated Duration value as String without access check
    
                    loop=loop+1
    
        if  SimpleDateFormat("MM/dd/yyyy").format(impreviewdate) ==SimpleDateFormat("MM/dd/yyyy").format(impinprogdate):

                impinprog2.setValue("OVERDUEDURATION",str(hours) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
        else:  
                impinprog2.setValue("OVERDUEDURATION",str(overdue) + ':' + str(minutes), MboConstants.NOACCESSCHECK)
                impinprog2.setValue("ISOVERDUE","1", MboConstants.NOACCESSCHECK)
                FRACSet2.save()