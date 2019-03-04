# ntlm-username-jsonp
Decode the NTLM authentication header and return the username as JSONP.

**This is not a method of authentication!!**

This is a simple Python 2.7 script that runs Flask with a web service that will return JSONP with the username of the current logged in user.

After you run the script *python ntlm-username-jsonp.py* you can use the below example HTML to call the JSONP and show the username.

```html
<!DOCTYPE html "-//w3c//dtd xhtml 1.0 transitional //en" "http://www.w3.org/tr/xhtml1/dtd/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <script>
    function setUsername(j) {
      alert("hi " + j["username"]);
    } 
  </script>
  <script src="http://localhost:8080/js?callback=setUsername"></script>
</head>
<body>
  <p></p>
</body>
</html>
```

This is script is based on https://www.rgagnon.com/javadetails/java-0441.html .
