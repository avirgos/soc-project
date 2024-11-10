# Some refactoring to get the exception handling for sendmail with UTF8 option
# centralized and also to get ability to unit test. This file should eventually move
# to py/splunk library as we move out additional duplicate work from sendemail.py and
# sendemail_handler.py into this file for better encapsulation, and maintenance.

from smtplib import SMTPNotSupportedError, SMTPSenderRefused

#########################################################################
# Send email with utf8 option.
#
# Returns error if SMTP server returned any of the following exceptions:
# 1. SMTPNotSupportedError
#      SMTP server does not support utf8.
# 2. SMTPSenderRefused with 502 error code
#     SMTP server returned command not implemented.
#
# Returns None if neither of above two errors found
#########################################################################
def sendEmailWithUTF8(smtp, sender, recipients, message):
    error = None
    try:
        # mail_options SMTPUTF8 allows UTF8 message serialization
        smtp.sendmail(sender, recipients, message, mail_options=["SMTPUTF8"])
    except SMTPNotSupportedError as smtpNotSupportedEx:
        # sendmail failed with SMTPUTP8 option as not supported
        error =  smtpNotSupportedEx
    except SMTPSenderRefused as smtpSenderRefusedEx:
        # sendmail failed with SMTPUTP8 option as sender refused
        if (smtpSenderRefusedEx.smtp_code == 502):
            error =  smtpSenderRefusedEx

    return error

