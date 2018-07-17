import requests
import re

con = "</td></tr></table><b>Database error:</b> Invalid SQL: update xy_img  set hits=hits+1 WHERE id =51'  <br>   Session halted."

html = requests.get('http://www.hzsrkj.com/allist.php?id=51'+"'")
err = re.search(r'error',con,re.I)
print(err)
print(html.content)
