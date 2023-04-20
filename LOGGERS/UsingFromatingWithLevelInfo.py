import logging
# GETTING logging MODULE INTO CURRENT FILE
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO,filename=r"C:\Users\patha\OneDrive\Desktop\PYTHON3\LOGGERS\loggingFiles\secondLoggingFile.txt")
# LOGS WILLL BE LISTED INTO THE FILE ( ACCORDING DEVELOPER GIVEN PATH )
# HERE,  asctime IS COMPLETE FORMATING OF TIME. [ LIKE TODAY'S_DATE TIME_WITH_SECONDS TIME_ZONE_ID
# asctime IS STRING TYPE OF VARIABLE THAT'S WHY WE SHOULD MAKE USE OF %()S  SYNTAX. 
logging.info('Admin logged in')
