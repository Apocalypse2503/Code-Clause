import pyshorteners
long = input("Enter the URL to shorten: ")
 
#TinyURL shortener service
tiny = pyshorteners.Shortener()
short = tiny.tinyurl.short(long)
 
print("The Shortened URL is: " + short)
