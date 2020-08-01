from requests_html import HTMLSession
import time
import sched
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

s = sched.scheduler(time.time, time.sleep)


def do_something(sc):

    # Google sheets authorizarion
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secret.json', scope)
    client = gspread.authorize(creds)

    # Opening sheets for different walls 
    document = client.open('Sheffield wall data')

    works = document.worksheet('works')
    depot = document.worksheet('depot')
    aw = document.worksheet('aw')
    foundry = document.worksheet('foundry')

    # Current time for record
    t = time.localtime()
    t = time.asctime(t)

    # Scraping data for walls
    sessionWorks = HTMLSession()
    r = sessionWorks.get(
        'https://gyms.vertical-life.info/en/the-climbing-works/counter')
    r.html.render(sleep=3)
    worksAttendance = r.html.find(".display-1")[0].text
    print(worksAttendance,'works',t)
    works.append_row([t, worksAttendance])

    sessionDepot = HTMLSession()
    r = sessionDepot .get(
        'https://portal.rockgympro.com/portal/public/4f7e4c65977f6cd9be6d61308c7d7cc2/occupancy?&iframeid=occupancyCounter&fId=1775')
    r.html.render(sleep=3)
    depotAttendance = r.html.find('#count')[0].text
    print(depotAttendance, 'depot', t)
    depot.append_row([t,depotAttendance])


    sessionFoundry = HTMLSession()
    r = sessionFoundry.get(
        'https://portal.rockgympro.com/portal/public/7489d57c01f2949270a79fe4287f25b4/occupancy?&iframeid=occupancyCounter&fId=')
    r.html.render(sleep=3)
    foundryAttendance = r.html.find('#count')[0].text
    print(foundryAttendance, 'foundry', t)
    foundry.append_row([t,foundryAttendance])

    sessionAw = HTMLSession()
    r = sessionAw.get(
        'https://portal.rockgympro.com/portal/public/92d94d22394b00c6d3f6f2c90c402db1/occupancy?&iframeid=occupancyCounter&fId=1352')
    r.html.render(sleep=3)
    awAttendance = r.html.find('#count')[0].text
    print(awAttendance, 'Awsomewalls', t)
    aw.append_row([t,awAttendance])

    # Rerun function after function complete
    s.enter(600, 1, do_something, (sc,))


s.enter(0, 1, do_something, (s,))
s.run()
