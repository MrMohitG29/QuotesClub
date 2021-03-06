from django.shortcuts import render , HttpResponse , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import wikiquotes
import smtplib
import csv
import json





def index(request):
    return render(request , 'home.html')



def signupPage(request):
    return render(request , 'photo_register.html')



def signinPage(request):
    return render(request , 'photo_login.html')



def searchget(request):
    f = open(r'C:\Users\Mr.Mg\Documents\Python\Projects\quotesbook\Data\quotes/quotess.json', encoding="utf8")
    data = json.load(f)
    ans = []
    for row in data:
        ans.append([row['Quote'] , row['Author'] , row['Tags']])
    return render(request, 'search.html' , {'q' : ans})



def shayari(request):
    return render(request , 'shayari.html')


#Signup
def handlesignup(request):
    if request.method == 'POST':
        #getdata
        firstName = request.POST['firstName'].capitalize()
        lastName = request.POST['lastName'].capitalize()
        userName = request.POST['userName'].lower()
        emailId = request.POST['emailId']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        qemail = "mohitkosta26@gmail.com"
        qemail_pass = 'Radheradhe@2558'
        #msg = "Subject: Welcome \n\n Welcome to Quotesbook , the world of words and feelings."
        msg = MIMEMultipart('alternative')

        # check errors
        if password != confirmPassword:
            messages.error(request , 'Password does not match')
            return redirect('signupPage')

        if len(userName) < 5:
            messages.error(request , 'username should be greater than 5')
            return redirect('signupPage')

        if userName.isalnum() is not True:
            messages.error(request , 'username should contain only numbers and character')
            return redirect('signupPage')

        try:
            user = User.objects.get(username=userName)
            context = {'error': 'The username you entered has already been taken. Please try another username.'}
            return render(request, 'home.html', context)
        except User.DoesNotExist:
            myuser = User.objects.create_user(userName , emailId , password)
            myuser.first_name = firstName
            myuser.last_name = lastName
            myuser.save()
            messages.success(request , 'signed up')
            server = smtplib.SMTP('smtp.gmail.com' , 587)
            server.ehlo()
            server.starttls()
            html = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;"><head><meta charset="UTF-8"><meta content="width=device-width, initial-scale=1" name="viewport"><meta name="x-apple-disable-message-reformatting"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta content="telephone=no" name="format-detection"><title>New email</title> <!--[if (mso 16)]><style type="text/css">     a {text-decoration: none;}     </style><![endif]--> <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--><style type="text/css">
@media only screen and (max-width:600px) {p, ul li, ol li, a { font-size:16px!important; line-height:150%!important } h1 { font-size:30px!important; text-align:center; line-height:120%!important } h2 { font-size:26px!important; text-align:center; line-height:120%!important } h3 { font-size:20px!important; text-align:center; line-height:120%!important } h1 a { font-size:30px!important } h2 a { font-size:26px!important } h3 a { font-size:20px!important } .es-menu td a { font-size:16px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:16px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:16px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 {
text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:block!important } a.es-button { font-size:20px!important; display:block!important; border-left-width:0px!important; border-right-width:0px!important } .es-btn-fw { border-width:10px 0px!important; text-align:center!important } .es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0px!important } .es-m-p0r
{ padding-right:0px!important } .es-m-p0l { padding-left:0px!important } .es-m-p0t { padding-top:0px!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } .es-desk-hidden { display:table-row!important; width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } .es-desk-menu-hidden { display:table-cell!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } }#outlook a {	padding:0;}.ExternalClass {	width:100%;}.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div {	line-height:100%;}.es-button
{	mso-style-priority:100!important;	text-decoration:none!important;}a[x-apple-data-detectors] {	color:inherit!important;	text-decoration:none!important;	font-size:inherit!important;	font-family:inherit!important;	font-weight:inherit!important;	line-height:inherit!important;}.es-desk-hidden {	display:none;	float:left;	overflow:hidden;	width:0;	max-height:0;	line-height:0;	mso-hide:all;}.es-button-border:hover a.es-button {	background:#2391ea!important;	border-color:#2391ea!important;}.es-button-border:hover {	background:#2391ea!important;	border-style:solid solid solid solid!important;	border-color:#1376c8 #1376c8 #1376c8 #1376c8!important;}</style></head><body style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;"><div class="es-wrapper-color" style="background-color:#F6F6F6;"> <!--[if gte mso 9]>
<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" color="#f6f6f6"></v:fill> </v:background><![endif]--><table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;"><tr style="border-collapse:collapse;"><td valign="top" style="padding:0;Margin:0;"><table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
<table class="es-header-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#040404;background-image:url(https://images.unsplash.com/photo-1551029506-0807df4e2031?ixlib=rb-1.2.1&auto=format&fit=crop&w=1791&q=80);background-position:center top;background-repeat:no-repeat;" width="600" cellspacing="0" cellpadding="0" bgcolor="#040404" align="center" background="https://ifhmpd.stripocdn.email/content/guids/CABINET_3cdb3bf19856ae2984edc8fe5b09bc3f/images/28261557925833174.jpg"><tr style="border-collapse:collapse;"><td style="Margin:0;padding-left:20px;padding-right:20px;padding-top:40px;padding-bottom:40px;background-position:center top;" align="left"><table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;">
<td width="560" valign="top" align="center" style="padding:0;Margin:0;"><table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;"><td align="left" style="padding:0;Margin:0;padding-bottom:10px;padding-top:40px;"><h2 style="Margin:0;line-height:46px;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;font-size:38px;font-style:normal;font-weight:bold;color:#FFFFFF;">WELCOME TO</h2><h2 style="Margin:0;line-height:46px;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;font-size:38px;font-style:normal;font-weight:bold;color:#FFFFFF;">QuotesClub</h2></td></tr><tr style="border-collapse:collapse;"><td align="left" style="padding:0;Margin:0;padding-bottom:40px;">
<h3 style="Margin:0;line-height:24px;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;font-size:20px;font-style:normal;font-weight:normal;color:#FFFFFF;">Your quotes introduce you before you even speak</h3></td></tr></table></td></tr></table></td></tr></table></td></tr></table><table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"><tr style="border-collapse:collapse;"><td align="center" style="padding:0;Margin:0;"><table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;"><tr style="border-collapse:collapse;">
<td style="padding:0;Margin:0;padding-top:20px;padding-left:20px;padding-right:20px;background-position:center center;" align="left"> <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="345" valign="top"><![endif]--><table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;"><tr style="border-collapse:collapse;"><td class="es-m-p20b" width="345" align="left" style="padding:0;Margin:0;"><table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-position:center center;" width="100%" cellspacing="0" cellpadding="0" role="presentation"><tr style="border-collapse:collapse;"><td align="center" style="padding:0;Margin:0;padding-top:10px;">
<h2 style="Margin:0;line-height:30px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:25px;font-style:normal;font-weight:bold;color:#333333;text-align:left;">ABOUT ME<br></h2></td></tr><tr style="border-collapse:collapse;"><td align="left" style="padding:0;Margin:0;padding-top:10px;"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;">QuotesClub is all about giving your words & thoughts a voice which can reach to milions of folks by our plaftform.QuotesClub encourages
    all type of thoughts which can help other people to think in broader way and enhance their thinking area.</p></td></tr></table></td></tr></table> <!--[if mso]></td><td width="10"></td><td width="205" valign="top"><![endif]-->
<table class="es-right" cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right;"><tr style="border-collapse:collapse;"><td width="205" align="left" style="padding:0;Margin:0;"><table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;"><td align="center" style="padding:0;Margin:0;font-size:0;"><a target="_blank" href="https://viewstripo.email/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:underline;color:#1376C8;">
<img class="adapt-img" src="https://images.unsplash.com/photo-1549122728-f519709caa9c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjF9&auto=format&fit=crop&w=925&q=80" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="205"></a></td></tr></table></td></tr></table> <!--[if mso]></td></tr></table><![endif]--></td></tr><tr style="border-collapse:collapse;"><td style="padding:0;Margin:0;padding-top:20px;padding-left:20px;padding-right:20px;background-position:center top;" align="left"><table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;"><td width="560" valign="top" align="center" style="padding:0;Margin:0;"><table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">

<table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;"><td align="center" style="padding:0;Margin:0;padding-top:10px;"><h2 style="Margin:0;line-height:30px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:25px;font-style:normal;font-weight:bold;color:#333333;text-align:center;">CONTACT US</h2></td></tr></table></td></tr></table></td></tr><tr style="border-collapse:collapse;"><td style="padding:0;Margin:0;padding-top:20px;padding-left:20px;padding-right:20px;background-position:center top;" align="left"><table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;">
<td width="560" valign="top" align="center" style="padding:0;Margin:0;"><table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-position:center top;" width="100%" cellspacing="0" cellpadding="0" role="presentation"><td align="center" style="padding:0;Margin:0;"><table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;"><tr style="border-collapse:collapse;"><td align="left" style="padding:20px;Margin:0;"> <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="356" valign="top"><![endif]--><table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;"><tr style="border-collapse:collapse;">
<td class="es-m-p20b" width="356" align="left" style="padding:0;Margin:0;"><table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;"><td class="es-m-txt-c" align="left" style="padding:0;Margin:0;"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;">© 2020. All rights reserved.</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;">You're receiving this email because you logged in our site.</p></td></tr></table></td></tr></table> <!--[if mso]></td><td width="20"></td>
<td width="184" valign="top"><![endif]--><table cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;"><td width="184" align="left" style="padding:0;Margin:0;"><table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;"><td class="es-m-txt-c" align="left" style="padding:0;Margin:0;padding-bottom:10px;"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;">Phone: +91 86027 18274</p>
<p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;">Address: Bangalore</p></td></tr><tr style="border-collapse:collapse;"><td class="es-m-txt-c" align="left" style="padding:0;Margin:0;padding-top:5px;font-size:0;"><table class="es-table-not-adapt es-social" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;"><td valign="top" align="center" style="padding:0;Margin:0;padding-right:10px;"><a href="https://viewstripo.email/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:underline;color:#1376C8;">
</td><td valign="top" align="center" style="padding:0;Margin:0;padding-right:10px;"><a href="https://viewstripo.email/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:underline;color:#1376C8;"></td><td valign="top" align="center" style="padding:0;Margin:0;"><a href="https://viewstripo.email/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:underline;color:#1376C8;">
</td></tr></table></td></tr></table></td></tr></table> <!--[if mso]></td></tr></table><![endif]--></td></tr></table></td></tr></table><table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"><tr style="border-collapse:collapse;"><td align="center" style="padding:0;Margin:0;"><table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;" width="600" cellspacing="0" cellpadding="0" align="center"><tr style="border-collapse:collapse;">
<td align="left" style="Margin:0;padding-left:20px;padding-right:20px;padding-top:30px;padding-bottom:30px;"><table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;"><td width="560" valign="top" align="center" style="padding:0;Margin:0;"><table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"><tr style="border-collapse:collapse;"><td class="es-infoblock made_with" align="center" style="padding:0;Margin:0;line-height:120%;font-size:0;color:#CCCCCC;">
</td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table></div></body>
</html>

"""
            part1 = MIMEText(html,'html')
            msg.attach(part1)
            server.login(qemail , qemail_pass)
            server.sendmail(qemail , emailId , msg.as_string())
            server.quit()
            messages.success(request , 'Registered succesfully ')
            return redirect('signupPage')

    else:
        return HttpResponse('Error')



#login
def handlesignin(request):
    if request.method == 'POST':
        loginUserName = request.POST['userName'].lower()
        loginPassword = request.POST['password']

        user = authenticate(username = loginUserName , password = loginPassword)

        if user is not None:
            login(request , user)
            return redirect('/')

        else:
            messages.error(request , 'Incorrect Username or Password')
            return redirect('signinPage')

    else:
        messages.error(request, 'Error')
        return redirect('signinPage')


#logout
def handlesignout(request):
    logout(request)
    return redirect('home')
