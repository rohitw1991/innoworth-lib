# coding: utf-8
from __future__ import unicode_literals
import webnotes
import webnotes.db
from webnotes.utils import cstr
import webnotes.utils
import webnotes.profile

class create_html:
	def __init_(self):
		pass

def html_data(data):
	webnotes.errprint(data['rounded_total'])	
	return ("""
				<!DOCTYPE html><html> <head>  <meta charset="utf-8" />  <title>"""+cstr(data['doctype_no'])+"""</title>
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
</style> </head>
 <body><div class="page-settings">
<div style="max-width: 100%">
<div style="text-align:left">
</div>
</div>
<div class="form-layout-row">
<div>
</div>
<div>
<div style="padding: 0px;">
<h1 style="font-size: 22px; margin-bottom: 8px;">"""+cstr(data['doctype'])+"""</h1>
<div style="font-size: 16px; color: rgb(136, 136, 136); margin-bottom: 8px; padding-bottom: 8px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(0, 0, 0);">"""+cstr(data['doctype_no'])+"""</div>
</div>
<div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr></tr>
</tbody>
</table>
</div>
</div>
</div>
<div class="form-layout-row">
<div>
</div>
<div><div style="padding: 0px;"></div><div>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody><tr><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;">
<table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">Name</td><td class="datainputcell">"""+cstr(data['customer_name'])+"""</td></tr></tbody></table>
<table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">"""+cstr(data['addr_name'])+"""</td><td class="datainputcell">"""+cstr(data['address'])+"""</td></tr></tbody></table>
<table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">Company</td><td class="datainputcell">"""+cstr(data['company'])+"""</td></tr></tbody></table>
</div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"><table style="width: 100%;"><tbody><tr><td class="datalabelcell" style="width: 38%;">"""+cstr(data['date_1'])+"""</td>
<td class="datainputcell">"""+cstr(data['posting_date'])+"""</td></tr></tbody></table><table style="width: 100%;"><tbody><tr>
<td class="datalabelcell" style="width: 38%;">"""+cstr(data['date_2'])+"""</td><td class="datainputcell">"""+cstr(data['due_date'])+"""</td></tr></tbody></table></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div>
<div style="padding: 0px;"></div><div>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
<td style="vertical-align: top; width: 100%;">
<div style="padding: 0px;">
</div>
<div style="padding: 0px;">
<div>
<table style="width: 100%; border-collapse: collapse; margin-bottom: 10px; margin-top: 10px; table-layout: fixed;">
<tbody>
<tr>
<td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 5%;">Sr</td>
<td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 13%;">Item</td>
<td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 32%;">Description</td>
<td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 13%; text-align: right;">Quantity</td>
<td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 13%;">UOM</td>
<td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 13%; text-align: right;">Basic Rate</td>
<td style="border: 1px solid rgb(153, 153, 153); padding: 3px; vertical-align: top; background-color: rgb(221, 221, 221); font-weight: bold; word-wrap: break-word; width: 13%; text-align: right;">Amount</td>
</tr>
"""+cstr(data['table_data'])+"""
</tbody>
</table>
</div>
</div>
</td>
</tr>
</tbody>
</table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"><div></div></div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div>
<div>
<div style="padding: 0px;"></div><div>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody><tr>
<td style="vertical-align: top; width: 100%;">
<div style="padding: 0px;"></div>
<div style="padding: 0px;"><div><div>
<table class="noborder" style="width:100%"><tbody><tr><td style="width: 60%"></td>
<td>
<table class="noborder" style="width:100%"><tbody><tr><td style="width:50%;">
<b>Net Total</b></td>
<td style="width:50%;text-align:right;">₹ """+cstr(data['net_total'])+"""</td></tr>
"""+cstr(data['tax_detail'])+"""
<tr><td style="width:50%;">
<b>Grand Total</b></td><td style="width:50%;text-align:right;">₹ """+cstr(data['grand_total'])+"""</td></tr><tr><td style="width:50%;">
<b>Rounded Total</b></td><td style="width:50%;text-align:right;">₹ """+cstr(data['rounded_total'])+""" </td>
</tr></tbody></table></td></tr><tr>
<td colspan="2">
</td>
</tr></tbody></table></div></div></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"><div></div><div></div><div></div></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 100%;"><div style="padding: 0px;"></div><div style="padding: 0px;"><div></div></div></td></tr></tbody></table></div></div></div>
<div class="form-layout-row"><div></div><div><div style="padding: 0px;"></div><div><table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td><td style="vertical-align: top; width: 50%;"><div style="padding: 0px;"></div><div style="padding: 0px;"></div></td></tr></tbody></table></div></div></div></div> </body></html> 
""")
	
