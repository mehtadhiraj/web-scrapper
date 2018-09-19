import requests

try:
    resp = requests.get("https://www.bigbasket.com/pd/241600/tata-salt-salt-iodized-1-kg-pouch/")
    #print (resp.text)
    responseHtml = "(window,document,'script','dataLayer','GTM-5VBZ33');" \
                   "</script><!-- End Google Tag Manager --><!--headerfooter js end--></body></html>"
    #startDiv = "<div class=\"sc-bRBYWo iEAlBH\" style=\"align-self: flex-end; line-height: 20px;\">Rs"
    #endDiv = "</div>"
    startDiv = "</script>"
    endDiv = "</body>"
    start = responseHtml.index(startDiv)
    end = responseHtml.index(endDiv,start+len(startDiv))
    extractedText = responseHtml[start+len(startDiv):end]
    print (extractedText)
except ValueError:
    print ("Substring not found")
