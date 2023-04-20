import logging   #getting logging module into current file

'''
 ======< logging MODULE >=======
    -----------------------
        *  logging module in Python is a ready-to-use and powerful module
           that is designed to meet the needs of beginners as well as enterprise teams.
        *  It is used by most of the third-party Python libraries,
           so you can integrate your log messages with the ones from those
           libraries to produce a homogeneous log for your application.

       GETTING logging MODULE INTO FILE

          >>>import logging
          
          *   With the logging module imported,
              you can use something called a “logger”
              to log messages that you want to see.
          *   By default, there are 5 standard levels
              indicating the severity of events.
              Each has a corresponding method that can be
              used to log events at that level of severity.
          *   The defined levels, in order of increasing severity,
              are the following:

                1) DEBUG
                2) INFO
                3) WARNING
                4) ERROR
                5) CRITICAL

        *   The logging module provides you with a default logger
            that allows you to get started without needing to do much
            configuration.
        *   The corresponding methods for each level can be called as
            shown in the following example:

Note:
      [***] debug() and info() messages didn’t get logged.
            This is because, by default, the logging module
            logs the messages with a severity level of WARNING or above.
            You can change that by configuring the logging module
            to log events of all levels if you want. You can also
            define your own severity levels by changing configurations,
            but it is generally not recommended.


===============< BASIC CONFIGURATIONS >==================
         -------------------------------------
         
        (*)  We can use the basicConfig(**kwargs) method to configure the logging

        " The logging module breaks PEP8 styleguide and uses camelCase naming conventions.
          This is because it was adopted from Log4j, a logging utility in Java.
          It is a known issue in the package but by the time it was decided
          to add it to the standard library, it had already been adopted
          by users and changing it to meet PEP8 requirements would
          cause backward compatibility issues.”
          
        ------------------------------------
        parameters for basicConfig() method :
        ------------------------------------

        level       : The root logger will be set to the specified severity level.
        filename    : This specifies the file.
        filemode    : If filename is given, the file is opened in this mode. The default is a, which means append.
        format      : This is the format of the log message.

        By using the level parameter, you can set what level of
        log messages you want to record. This can be done by passing
        one of the constants available in the class, and this would
        enable all logging calls at or above that level to be logged.

        =========================
         example :  go-to EG : 2
        =========================

'''



# EG : 1
'''
logging.debug("     This is DEBUG level information")
logging.info("    This is INFO level information")
logging.warning("    This is WARNING level information")
logging.error("      This is ERROR level information")
logging.critical("   This is CRITICAL level information")
'''

# EG : 2

logging.basicConfig(level=logging.DEBUG,filename=r"C:\Users\patha\OneDrive\Desktop\PYTHON3\LOGGERS\loggingFiles\firstLoggingFile.txt",filemode="a",format='%(process)d-%(levelname)s-%(message)s')
logging.debug('Logging message')


















