#!/usr/bin/env python3

import scrape_common as sc

print('SG')
d = sc.download("https://www.sg.ch/tools/informationen-coronavirus.html")
sc.timestamp()

d = d.replace('&nbsp;', ' ')

# 2020-03-20
""" 									<div class="col-xs-12"><p>20.03.2020:<br/>Bestätigte Fälle: 98<br/><br/></p></div>"""

# 2020-03-25
"""									<div class="col-xs-12"><p>25.03.2020:</p><p>Bestätigte Fälle: 228<br/>Todesfälle: 1</p><p>Die Fallzahlen können nicht nach Regionen oder Gemeinden selektioniert werden. Es treten in allen Regionen des Kantons Fälle auf.&nbsp;</p><p>&nbsp;</p></div>"""

# 2020-04-03
"""
		<h4>2. April 2020</h4>
		
			
			
				<table id="sgch_accordion_list__sgch_accordion_sgch_table" class="table small-padding table-bordered" style="width: 100%">
<thead><tr class="odd" ><th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>&nbsp; &nbsp;</b></th>
<th><b>Anzahl&nbsp;</b></th>
<th data-hide="phone"><b>Veränderungen gegenüber Vortag&nbsp;</b></th>
</tr></thead><tbody><tr class="even" ><td width="236" height="17">laborbestätigte Fälle (kumuliert)</td>
<td width="80">480</td>
<td>+25&nbsp;</td>
</tr><tr class="odd" ><td height="17">Hospitalisationen Isolation (aktueller Stand)</td>
<td>63</td>
<td>+10&nbsp;</td>
</tr><tr class="even" ><td height="17">Hospitalisationen Intensiv (aktueller Stand)</td>
<td>12</td>
<td>+1&nbsp;</td>
</tr><tr class="odd" ><td height="17">aus Spital entlassene (kumuliert)</td>
<td>50</td>
<td>+1&nbsp;</td>
</tr><tr class="even" ><td height="17">Verstorbene (kumuliert)</td>
<td>8</td>
<td>unverändert&nbsp;</td>
</tr></tbody></table>
"""

# 2020-04-05
"""
		<h4>5. April 2020</h4>
		
			
			
				<table id="sgch_accordion_list__sgch_accordion_sgch_table" class="table small-padding table-bordered" style="width: 100%">
<thead><tr class="odd" ><th>&nbsp;</th>
<th colspan="2">Anzahl&nbsp;</th>
<th data-hide="phone" colspan="2">Veränderung gegenüber dem Vortag</th>
</tr></thead><tbody><tr class="even" ><td height="20" width="263">laborbestätigte Fälle (kumuliert)</td>
<td colspan="2" width="160">515</td>
<td colspan="2" width="208">+11</td>
</tr><tr class="odd" ><td height="20">Hospitalisationen Isolation (akt. Stand)</td>
<td colspan="2">57</td>
<td colspan="2">-9</td>
</tr><tr class="even" ><td height="20">Hospitalisationen Intensiv (akt. Stand)</td>
<td colspan="2">13</td>
<td colspan="2">unverändert</td>
</tr><tr class="odd" ><td height="20">aus Spital entlassene (kumuliert)</td>
<td colspan="2">70</td>
<td colspan="2">+8</td>
</tr><tr class="even" ><td height="20">Verstorbene (kumuliert)</td>
<td colspan="2">9</td>
<td colspan="2">unverändert</td>
</tr></tbody></table>
"""

print('Date and time:', sc.find(r'<h4>([0-9]+\. [A-Za-z]* [0-9]{4})<\/h4>', d))
print('Confirmed cases:', sc.find(r'laborbestätigte\s*Fälle\s*\(kumuliert\)<\/t[hd]>\s*<t[hd][^>]*>([0-9]+)<\/t[hd]>', d.replace("\n", "")))
print('Deaths:', sc.find(r'>Verstorbene\s*\(kumuliert\)<\/td>\s*<td[^>]*>([0-9]+)<', d.replace("\n", "")))
print('Hospitalized:', sc.find(r'>Hospitalisationen Isolation\s*\((?:akt\.|aktueller)\s*Stand\)<\/td>\s*<td[^>]*>([0-9]+)<', d.replace("\n", "")))
print('ICU:', sc.find(r'>Hospitalisationen\s*Intensiv\s*\((?:akt\.|aktueller)\s*Stand\)<\/td>\s*<td[^>]*>([0-9]+)<', d.replace("\n", "")))
print('Recovered:', sc.find(r'>aus\s*Spital\s*entlassene\s*\(kumuliert\)<\/td>\s*<td[^>]*>([0-9]+)<', d.replace("\n", "")))
