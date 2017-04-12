import urllib
import base64
import optparse

print("""
      _.---.._             _.---...__
   .-'   /\   \          .'  /\     /
   `.   (  )   \        /   (  )   /
     `.  \/   .'\      /`.   \/  .'
       ``---''   )    (   ``---''
               .';.--.;`. 
             .' /_...._\ `.
           .'   `.a  a.'   `.
          (        \/        )
           `.___..-'`-..___.'
              \          /
               `-.____.-'
""")

while True:

        print ("[1] Text to URL Encoded Hex (Special Chars Only)")
        print ("[2] URL Encoded Hex to Plain Text")
        print ("[3] Text to URL Encoded Hex")
        print ("[4] Base64 to Text\n")
        try:        
            choice = raw_input("Enter your choice [1-4]: ")
            choice = int(choice)
        except ValueError:
                        print("Invalid Choice\n")

        def pix():
                if choice == 1:
                    try:
                        ch1 = raw_input("Enter Plain Text to Encode: ")
                        print(urllib.quote_plus(ch1 , safe="").encode("utf8"))
                        print("")
                    except UnicodeDecodeError:
                                            print("Error")
                                            print("")
                if choice == 2:
                    try:
                        ch2 = raw_input("Enter URL Encoded Hex to Decode: ")
                        print(urllib.unquote(ch2).decode("utf8"))
                        print("")
                    except UnicodeDecodeError:
                                            print("Error")
                                            print("")
                if choice == 3:    
                        ch3 = raw_input("Enter Plain Text to Convert: ")
                        url = (ch3.encode("hex"))
                        chunk = ([url[i:i+2] for i in range(0, len(url), 2)])
                        chunk = ("%".join(chunk))
                        print("%" + chunk).upper()
                        print("")

                if choice == 4:
                        try:
                            ch4 = raw_input("Enter Base64 to Decode: ")                        
                            print(base64.b64decode(ch4))
                            print("")
                        except TypeError:
                                        print("Error")
                                        print("")
                               
        pix()
