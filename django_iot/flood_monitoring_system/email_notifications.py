import smtplib
user = 'kentwaterupdates@gmail.com'
password = 'wghkerzlmhiwuhaj'

generic_flood_info = "For more information on the flood warning codes and what to do in a flood: https://flood-warning-information.service.gov.uk/what-to-do-in-a-flood.\n" \
                     "More information on what to do in the event of a flood from the fire service: https://www.fireservice.co.uk/safety/flood-advice/.\n" \
                     "For more information on how to make your home more secure against flooding: https://environmentagency.blog.gov.uk/2016/11/11/make-your-home-more-flood-resilient/.\n" \
                     "\nMark your notifications as read to avoid getting future emails about these floods alerts\n" \
                     "To unsubscribe simply unsubscribe from all stations in subscriptions\n" \
                     "\n- Kent Water Updates"

def send_email(recipient, message):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, recipient, message)
        server.close()
        print('Email to ' + recipient + " sent")

    except:
        print('Email to ' + recipient + " failed to send")

def build_and_send_email(recipient, alerts):
    message = ""
    send_email(recipient.email, message)
