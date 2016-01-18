import urllib2
import re

def Based_on_user_choice(choice):
    if choice == 'A':
        Download_latest_one(),
    elif choice == "B":
        Download_the_one(),
    elif choice == "C":
        Show_total_number()
    else:
        print "undefind input"
    return

def Download_latest_one():
    total_number = Show_total_number()
    format_total_number= int(total_number)
    image_url="http://www.gunnerkrigg.com/comics/" + total_number + ".jpg";
    Download_image(image_url, total_number)
    print "The latest comic image is saved as " + str(format_total_number) + ".jpg in your local device"
    return

def Download_the_one():
    format_image_id = raw_input("please input which image you need! (a number is required)")
    image_id = format_image_id.zfill(8)
    image_url="http://www.gunnerkrigg.com/comics/" + image_id + ".jpg";
    Download_image(image_url, format_image_id)
    print "The latest comic image is saved as " + format_image_id + ".jpg in your local device"
    return

def Download_image(image_url, format_image_id):
    image = urllib2.urlopen(image_url)
    output = open(format_image_id + ".jpg", "wb")
    output.write(image.read())
    output.close()

def Show_total_number():
    response=page.read()
    pattern=re.compile(r'img class="comic_image" src="/comics/(.*).jpg">')
    total_number= pattern.search(response).group(1)
    format_total_number= total_number[total_number.rfind('0')+1:]
    print "there are " + format_total_number + " comic images in this site!"
    return total_number

page=urllib2.urlopen("http://www.gunnerkrigg.com/")
argument =raw_input("What can I do for you?(CASE SENSITIVE) A: Show me the latest comic image! B: Show me the comic image I prefer! C: How many comic images exist here?")
Based_on_user_choice(argument)
