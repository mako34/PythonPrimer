#escribir codigo asi

import sys
import requests
import base64
 
def main():
    # parse command line options
    print ("vacio")
    #r = requests.get("http://localhost:8080/AccountRight")
    
    userName = "administrator:"
    password = ""
    construida = "".join((userName, password))

    print (construida)
 
 	#tiene q ser encoded!
    encoded = base64.b64encode (bytes(construida, "utf-8"))


    print (encoded)

    #r = requests.get("http://localhost:8080/AccountRight/6680178c-1cb2-44b4-ab9f-8ca75155f9f5", 
    #	headers={"x-myobapi-cftoken":encoded});

    r = requests.get("http://localhost:8080/AccountRight/6680178c-1cb2-44b4-ab9f-8ca75155f9f5/Contact/Customer", 
  	headers={"x-myobapi-cftoken":encoded});

    #nota los headers! con usuario y contrasenia!

    print (r.content)

    print("------------")

    #parse to json!
    data = r.json()

    print (data)


if __name__ == "__main__":
    main()