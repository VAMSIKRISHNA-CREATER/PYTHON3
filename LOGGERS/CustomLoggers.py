'''
we have seen the default logger named root, which is used by the logging module
whenever its functions are called directly like this: logging.debug().
You can (and should) define your own logger by creating an object of the
Logger class, especially if your application has multiple modules. Let’s have a look
at some of the classes and functions in the module.

The most commonly used classes defined in the logging module are the following:

        Logger: This is the class whose objects will be used
                in the application code directly to call the functions.

        LogRecord: Loggers automatically create LogRecord objects that have
                   all the information related to the event being logged, like the name of the logger, the function, the line number, the message, and more.

        Handler: Handlers send the LogRecord to the required output destination,
                 like the console or a file. Handler is a base for subclasses
                 like StreamHandler, FileHandler, SMTPHandler, HTTPHandler,
                 and more. These subclasses send the logging outputs to corresponding
                 destinations, like sys.stdout or a disk file.

        Formatter: This is where you specify the format of the output by specifying
                   a string format that lists out the attributes that the output
                   should contain.
'''
import logging
logger = logging.getLogger("Custom_Logging")
logger.info("Hello This is info level information     (  1  )") # LowProority
logger.debug("Hello This is debug level information    (  2  )") # LowPriority\
logger.warning("Hello This is warning level information   (  3  )")
logger.error("Hello This is error level information     (  4  )")
logger.critical("Hello This is critical level information  (  5  )")

logging.getLogger(__name__)


'''
        __init__(level=NOTSET)
        
                Initializes the Handler instance by setting its level, setting the list of
                filters to the empty list and creating a lock (using createLock())
                for serializing access to an I/O mechanism.

        createLock()
        
                Initializes a thread lock which can be used to serialize access
                to underlying I/O functionality which may not be threadsafe.

        acquire()
        
                Acquires the thread lock created with createLock().

        release()
        
                Releases the thread lock acquired with acquire().

        setLevel(level)
        
                Sets the threshold for this handler to level. Logging
                messages which are less severe than level will be ignored.
                When a handler is created, the level is set to NOTSET
                which causes all messages to be processed).

                Changed in version 3.2: The level parameter
                now accepts a string representation of the level such
                as ‘INFO’ as an alternative to the integer constants such as INFO.



            setFormatter(fmt)
                Sets the Formatter for this handler to fmt.

            addFilter(filter)
                Adds the specified filter filter to this handler.

            removeFilter(filter)
                Removes the specified filter filter from this handler.

            filter(record)
                Apply this handler’s filters to the record and return
                True if the record is to be processed. The filters are
                consulted in turn, until one of them returns a false value.
                If none of them return a false value, the record will be emitted.
                If one returns a false value, the handler will not emit the record.

            flush()
                Ensure all logging output has been flushed. This version
                does nothing and is intended to be implemented by subclasses.

            close()
                Tidy up any resources used by the handler. This version does
                no output but removes the handler from an internal list of handlers
                which is closed when shutdown() is called. Subclasses should ensure
                that this gets called from overridden close() methods.

            handle(record)
                Conditionally emits the specified logging record,
                depending on filters which may have been added to
                the handler. Wraps the actual emission of the record
                with acquisition/release of the I/O thread lock.

            handleError(record)
                This method should be called from handlers when an
                exception is encountered during an emit() call. If
                the module-level attribute raiseExceptions is False,
                exceptions get silently ignored. This is what is mostly
                wanted for a logging system - most users will not care
                about errors in the logging system, they are more interested
                in application errors. You could, however, replace this with
                a custom handler if you wish. The specified record is the one
                which was being processed when the exception occurred.
                (The default value of raiseExceptions is True, as that
                is more useful during development).

            format(record)
                Do formatting for a record - if a formatter is set,
                use it. Otherwise, use the default formatter for the module.

            emit(record)
                Do whatever it takes to actually log the specified
                logging record. This version is intended to be implemented
                by subclasses and so raises a NotImplementedError.

            Warning
                This method is called after a handler-level
                lock is acquired, which is released after this method returns.
                When you override this method, note that you should be careful
                when calling anything that invokes other parts of the logging
                API which might do locking, because that might result in a deadlock.
                Specifically:
                Logging configuration APIs acquire the module-level lock, and then
                individual handler-level locks as those handlers are configured.

            Many logging APIs lock the module-level lock. If such an API is called
            from this method, it could cause a deadlock if a configuration call
            is made on another thread, because that thread will try to acquire the
            module-level lock before the handler-level lock, whereas this thread tries
            to acquire the module-level lock after the handler-level lock (because in
            this method, the handler-level lock has already been acquire



        LogRecord Objects
LogRecord instances are created automatically by the Logger every time something is logged, and can be created manually via makeLogRecord() (for example, from a pickled event received over the wire).

class logging.LogRecord(name, level, pathname, lineno, msg, args, exc_info, func=None, sinfo=None)
Contains all the information pertinent to the event being logged.

The primary information is passed in msg and args, which are combined using msg % args to create the message attribute of the record.

Parameters
name (str) – The name of the logger used to log the event represented by this LogRecord. Note that the logger name in the LogRecord will always have this value, even though it may be emitted by a handler attached to a different (ancestor) logger.

level (int) – The numeric level of the logging event (such as 10 for DEBUG, 20 for INFO, etc). Note that this is converted to two attributes of the LogRecord: levelno for the numeric value and levelname for the corresponding level name.

pathname (str) – The full string path of the source file where the logging call was made.

lineno (int) – The line number in the source file where the logging call was made.

msg (Any) – The event description message, which can be a %-format string with placeholders for variable data, or an arbitrary object (see Using arbitrary objects as messages).

args (tuple | dict[str, Any]) – Variable data to merge into the msg argument to obtain the event description.

exc_info (tuple[type[BaseException], BaseException, types.TracebackType] | None) – An exception tuple with the current exception information, as returned by sys.exc_info(), or None if no exception information is available.

func (str | None) – The name of the function or method from which the logging call was invoked.

sinfo (str | None) – A text string representing stack information from the base of the stack in the current thread, up to the logging call.

getMessage()
Returns the message for this LogRecord instance after merging any user-supplied arguments with the message. If the user-supplied message argument to the logging call is not a string, str() is called on it to convert it to a string. This allows use of user-defined classes as messages, whose __str__ method can return the actual format string to be used.

Changed in version 3.2: The creation of a LogRecord has been made more configurable by providing a factory which is used to create the record. The factory can be set using getLogRecordFactory() and setLogRecordFactory() (see this for the factory’s signature).

This functionality can be used to inject your own values into a LogRecord at creation time. You can use the following pattern:

old_factory = logging.getLogRecordFactory()

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.custom_attribute = 0xdecafbad
    return record

logging.setLogRecordFactory(record_factory)
With this pattern, multiple factories could be chained, and as long as they don’t overwrite each other’s attributes or unintentionally overwrite the standard attributes listed above, there should be no surprises.

LogRecord attributes
The LogRecord has a number of attributes, most of which are derived from the parameters to the constructor. (Note that the names do not always correspond exactly between the LogRecord constructor parameters and the LogRecord attributes.) These attributes can be used to merge data from the record into the format string. The following table lists (in alphabetical order) the attribute names, their meanings and the corresponding placeholder in a %-style format string.

If you are using {}-formatting (str.format()), you can use {attrname} as the placeholder in the format string. If you are using $-formatting (string.Template), use the form ${attrname}. In both cases, of course, replace attrname with the actual attribute name you want to use.

In the case of {}-formatting, you can specify formatting flags by placing them after the attribute name, separated from it with a colon. For example: a placeholder of {msecs:03d} would format a millisecond value of 4 as 004. Refer to the str.format() documentation for full details on the options available to you.

Attribute name

Format

Description

args

You shouldn’t need to format this yourself.

The tuple of arguments merged into msg to produce message, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary).

asctime

%(asctime)s

Human-readable time when the LogRecord was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time).

created

%(created)f

Time when the LogRecord was created (as returned by time.time()).

exc_info

You shouldn’t need to format this yourself.

Exception tuple (à la sys.exc_info) or, if no exception has occurred, None.

filename

%(filename)s

Filename portion of pathname.

funcName

%(funcName)s

Name of function containing the logging call.

levelname

%(levelname)s

Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').

levelno

%(levelno)s

Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).

lineno

%(lineno)d

Source line number where the logging call was issued (if available).

message

%(message)s

The logged message, computed as msg % args. This is set when Formatter.format() is invoked.

module

%(module)s

Module (name portion of filename).

msecs

%(msecs)d

Millisecond portion of the time when the LogRecord was created.

msg

You shouldn’t need to format this yourself.

The format string passed in the original logging call. Merged with args to produce message, or an arbitrary object (see Using arbitrary objects as messages).

name

%(name)s

Name of the logger used to log the call.

pathname

%(pathname)s

Full pathname of the source file where the logging call was issued (if available).

process

%(process)d

Process ID (if available).

processName

%(processName)s

Process name (if available).

relativeCreated

%(relativeCreated)d

Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.

stack_info

You shouldn’t need to format this yourself.

Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record.

thread

%(thread)d

Thread ID (if available).

threadName

%(threadName)s

Thread name (if available).








'''





logging.exception("Gaya Bye Bye Good Bye RestInPiece")
logging.log(msg="Using log() ",level=40)






