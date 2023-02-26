import schedule
import requests
import time
from MyCredential import phone_number

def sending_message():
    resp = requests.post('https://textbelt.com/text',{
    #it is best to use E.164 formate whenever possible:
    # E.164 has 3 formate: 1: prefix "+" 2: A 1-3 digit country code 3: User number
        'phone': phone_number,
        'message': 'Hope this message find you well',
        'key':'textbelt'
    })
    print(resp.json())


#after that we can schedule our message
schedule.every(10).seconds.do(sending_message)
# schedule.every(10).minute.do(sending_message)
# schedule.every().hour.do(schedule)
# schedule.every().day.at('06:30').do(schedule)
# schedule.every().monday.do(schedule)
# schedule.every().wednesday.at('11:30').do(schedule)
# schedule.every().minute.at('13.20').do(schedule)


while True:
    schedule.run_pending()
    time.sleep(1)
