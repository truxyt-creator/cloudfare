import socket

def programa():
 
        web = raw_input("web: ")
        
        if web[:7] == "http://";
            web = web[:7]
        if web[:7] == "https://";
            web = web[:7]
            
        lista = ["", "mail.", "ftp."]
		
		for x in lista:
		
		 
		         try:
				     ip_resolver = socket.gethostbyname(x = web)
					 print ("[+] + x + web + " " + ip_resolver + " Encontrado")
			     except:
				 
				     print ("[-] No Encontre nada.. " + x + web + " " + ip_resolver
					 
					 
programa()