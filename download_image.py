#"http://www.gunnerkrigg.com/"
import urllib2
import re

class website:
    pattern = re.compile(r'img class="comic_image" src="/comics/(.*).jpg">')
    def __init__(self, url):
        self.page = urllib2.urlopen(url)
        self.response = self.page.read()
        self.total_number= self.pattern.search(self.response).group(1)
        self.format_total_number= int(self.total_number)

    def Show_total_number(self):
        print "there are " + self.format_total_number + " comic images in this site!"
        return self.total_number

    def Based_on_user_choice(self, choice):
        if choice == 'A':
            self.Download_latest_one(self),
        elif choice == "B":
            self.Download_the_one(self),
        elif choice == "C":
            self.Show_total_number()
        else:
            print "undefind input"
        return

    def Download_latest_one(self):
        image_url = url + "comics/" + self.total_number + ".jpg";
        self.Download_image(image_url, self.total_number)
        print "The latest comic image is saved as " + str(self.format_total_number) + ".jpg in your local device"
        return

    def Download_the_one(self):
        format_image_id = raw_input("please input which image you need! (a number is required)")
        image_id = format_image_id.zfill(8)
        image_url = url + "comics/" + image_id + ".jpg";
        self.Download_image(image_url, format_image_id)
        print "The latest comic image is saved as " + format_image_id + ".jpg in your local device"
        return

    def Download_image(image_url, format_image_id):
        image = urllib2.urlopen(image_url)
        output = open(format_image_id + ".jpg", "wb")
        output.write(image.read())
        output.close()

url = raw_input("Please input the website url")
target = website(url)
argument =raw_input("What can I do for you?(CASE SENSITIVE) A: Show me the latest comic image! B: Show me the comic image I prefer! C: How many comic images exist here?")
target.Based_on_user_choice(argument)
