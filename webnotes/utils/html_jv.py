# coding: utf-8
from __future__ import unicode_literals
import webnotes
import webnotes.db
from webnotes.utils import cstr
import webnotes.utils
import webnotes.profile

class create_html_jv:
	def __init_(self):
		pass


def html_jv(data):
	return ("""
			<!DOCTYPE html><html> 
<head>  
<meta charset="utf-8" />   
<title></title> 
 <style>
html, body, div, span, td, p {   font-family: inherit;   font-size: inherit;  } 
.page-settings {  font-family: Arial, Helvetica Neue, Sans;  font-size: 9pt; } pre { margin:0; padding:0;}
.simpletable, .noborder {   border-collapse: collapse;  margin-bottom: 10px; } 
.simpletable td {  border: 1pt solid #777;  vertical-align: top;  padding: 4px; } 
.noborder td {  vertical-align: top; }  
.datalabelcell {    padding: 2px 0px;    width: 38%;    vertical-align: top;    }   
.datainputcell {    padding: 2px 0px;    width: 62%;    text-align: left;    }  
.sectionHeading {    font-size: 16px;    font-weight: bold;    margin: 8px 0px;    }   
.columnHeading {    font-size: 14px;    font-weight: bold;    margin: 8px 0px;    }
</style> 
</head> 
<body>
<div class="page-settings"><div style="max-width: 100%"></div>
<div class="form-layout-row"><div></div><div>
<div style="padding: 0px;"><h1 style="font-size: 22px; margin-bottom: 8px;">Journal Voucher</h1>
<div style="font-size: 16px; color: rgb(136, 136, 136); margin-bottom: 8px; padding-bottom: 8px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(0, 0, 0);">"""+cstr(data['name'])+"""</div>
</div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"><table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">Voucher Type</td><td class="datainputcell">"""+cstr(data['bank_voucher'])+"""</td>
</tr></tbody></table></div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"><table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">Posting Date</td><td class="datainputcell">"""+cstr(data['posting_date'])+"""</td>
</tr></tbody></table></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;">
</div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody><tr><td style="vertical-align: top; width: 100%;"><div style="padding: 0px;"></div>
<div style="padding: 0px;"><div><table style="width: 100%; border-collapse: collapse; margin-bottom: 10px; margin-top: 10px; table-layout: fixed;"><tbody><tr><td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 5%;">Sr</td><td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 32%;">Account</td>
<td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 23%;">Cost Center</td><td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 10%; text-align: right;">Debit</td><td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 10%; text-align: right;">Account Balance</td><td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 10%; text-align: right;">Credit</td>
</tr>"""+cstr(data['table'])+"""</tbody></table></div></div></td></tr>
</tbody></table></div></div></div><div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 50%;">
<div style="padding: 0px;"></div><div style="padding: 0px;"><table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">Total Debit</td><td class="datainputcell" style="text-align: left;"><div style="text-align: right">₹ """+cstr(data['total_debit'])+"""</div>
</td></tr></tbody></table><table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">Total Credit</td><td class="datainputcell" style="text-align: left;">
<div style="text-align: right">₹ """+cstr(data['total_credit'])+"""</div></td></tr></tbody></table></div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"><table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">Reference Number</td>
<td class="datainputcell">"""+cstr(data['reference_no'])+"""</td></tr></tbody></table><table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">Reference Date</td>
<td class="datainputcell">"""+cstr(data['reference_date'])+"""</td></tr></tbody></table></div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"><table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">Remark</td>
<td class="datainputcell">"""+cstr(data['remark'])+"""</td></tr></tbody></table></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td></tr></tbody></table></div></div></div></div> </body></html>
		
		""")
