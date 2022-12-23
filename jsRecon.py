import os
import helper.findJSfiles as find
import helper.beautifyjs as beauty

from datetime import datetime
now = datetime.now() # current date and time

TARGET = 'twitter'

date_time = now.strftime("%Y%m%d-%H%M%S")
outputFolder = "beautified_" + date_time
downloadFolder = 'downloaded_' + date_time


find.extract_urls('targets/' + TARGET + '/source.js')
find.download_urls('out.txt','downloads/' + TARGET +'/prodjs/' + downloadFolder)

beauty.beautify_js_files('downloads/' + TARGET + '/prodjs/' + downloadFolder,'downloads/' + TARGET + '/beautified/' + outputFolder)