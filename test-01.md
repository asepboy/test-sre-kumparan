The GET method means to retrieve any information (in the form of entities) identified by the Request-URI. If the Request-URI refers to the data production process, it is the resulting data that will be returned as an entity in the response. Example :
    
    GET /index.html?report_id=31312321 HTTP/1.1
     Host: www.asep.com
     User-Agent: Chrome/6.2
   

 As for HEAD, this method can be used to obtain metainformation about the entity implied by the request without transferring the entity-body itself. This method is often used to test hypertext links for validity, accessibility, and recent modifications. Example :
 
    
     HEAD /de HTTP/1.1[CRLF]
     Host: www.google.com[CRLF]
     Connection: close[CRLF]
     User-Agent: Web-sniffer/1.0.37 [CRLF]
     Accept-Encoding: gzip[CRLF]
     Accept-Charset: ISO-8859-1,UTF-8;q=0.7,*;q=0.7[CRLF]
     Cache-Control: no-cache[CRLF]
     Accept-Language: de,en;q=0.7,en-us;q=0.3[CRLF]
     Referer: http://web-sniffer.net/[CRLF]
    
