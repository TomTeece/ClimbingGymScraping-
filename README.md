# Climbing Gym Scraping
Scraping the data from the occupancy trackers of the walls in sheffield and storing it in a google sheet. Will attempt to display soon.

## Documentation 
For storing in google sheets I used this video - [Google Sheets Twilio](https://www.youtube.com/watch?v=vISRn5qFrkM).  
The spreadsheets are viewed/edited using the [gspread](https://gspread.readthedocs.io/en/latest/index.html) library, which makes it super easy to edit sheets.  
To scrape requests-html was used. The `render()` method runs the javascript on the page allowing the counters to be scraped. The `render()` method has the parameter of `sleep = 3` to let the counters animation to finish before the count is scraped.  