hamza = input("Enter twittos with comma please :")
x=0
twittos = hamza.split(",")
originalstr="sourcetype:SOCIALMEDIA_TWITTER AND"
printer2 = ""

for member in twittos:
    if x == 0:
        printer1 = originalstr +' ((author:' + twittos[x] + ' OR mention:@' + twittos[x] + ' OR ("' + twittos[x] + '" AND is:retweet)) OR '
        x += 1
    elif x == (len(twittos)-1):
        printer2 += '(author:' + twittos[x] + ' OR mention:@' + twittos[x] + ' OR ("' + twittos[x] + '" AND is:retweet))) '   
    else:
        printer2 += '(author:' + twittos[x] + ' OR mention:@' + twittos[x] + ' OR ("' + twittos[x] + '" AND is:retweet)) OR '
        x += 1
        

parseform="""<h1 style="color: #5e9ca0;">Output Talkwalker</h1>
<h2 style="color: #2e6c80;">Copier-coller la requete sur Talkwalker sans ajouter d'espace :</h2>
<p>""" + printer1 + printer2 + "</p>"

with open("talkwalkeroutput.html", "w") as file:
    file.write(parseform)

input('File is saved as "talkwalkeroutput.html" yay ! Type ENTER to exit')




