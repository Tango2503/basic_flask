from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'ErrorLogs'}
    return ''' 
<noscript>

<a href="https://servedby.flashtalking.com/click/1/120094;4687913;0;209;0/?ft_width=120&ft_height=600&url=27923356" target="_blank">

<img border="0" src="https://servedby.flashtalking.com/imp/1/120094;4687913;205;gif;MediaIQ;BreakingDadS1120x600/?"></a>

</noscript>

<script language="Javascript1.1" type="text/javascript">

var ftClick = "";

var ftExpTrack_4687913 = "";

var ftX = "";

var ftY = "";

var ftZ = "";

var ftOBA = 1;

var ftContent = "";

var ftCustom = "";

var ft120x600_OOBclickTrack = "";

var ftRandom = Math.random()*1000000;

var ftBuildTag1 = "<scr";

var ftBuildTag2 = "</";

var ftClick_4687913 = ftClick;

if(typeof(ft_referrer)=="undefined"){var ft_referrer=(function(){var r="";if(window==top){r=window.location.href;}else{try{r=window.parent.location.href;}catch(e){}r=(r)?r:document.referrer;}while(encodeURIComponent(r).length>1000){r=r.substring(0,r.length-1);}return r;}());}

var ftDomain = (window==top)?"":(function(){var d=document.referrer,h=(d)?d.match("(?::q/q/)+([qw-]+(q.[qw-]+)+)(q/)?".replace(/q/g,decodeURIComponent("%"+"5C")))[1]:"";return (h&&h!=location.host)?"&ft_ifb=1&ft_domain="+encodeURIComponent(h):"";}());

var ftTag = ftBuildTag1 + 'ipt language="javascript1.1" type="text/javascript" ';

ftTag += 'src="https://servedby.flashtalking.com/imp/1/120094;4687913;201;js;MediaIQ;BreakingDadS1120x600/?ftx='+ftX+'&fty='+ftY+'&ftadz='+ftZ+'&ftscw='+ftContent+'&ft_custom='+ftCustom+'&ftOBA='+ftOBA+ftDomain+'&ft_agentEnv='+(window.mraid||window.ormma?'1':'0')+'&ft_referrer='+encodeURIComponent(ft_referrer)+'&cachebuster='+ftRandom+'" id="ftscript_120x600" name="ftscript_120x600"';

ftTag += '>' + ftBuildTag2 + 'script>';

document.write(ftTag);

</script>
'''

''' ASSUMING HERE THAT PAGE ISN'T LOADING CAUSE iframe src = "about:blank" '''
#<ins class='dcmads' style='display:inline-block;width:970px;height:250px'
#    data-dcm-placement='N8913.285985MEDIAIQ/B23899303.269608586'
#    data-dcm-rendering-mode='iframe'
#    data-dcm-https-only
#    data-dcm-resettable-device-id=''
#    data-dcm-app-id=''>
#  <script src='https://fw.adsafeprotected.com/rjss/www.googletagservices.com/423088/44223315/dcm/dcmads.js'></script>
#</ins>


#<ins class='dcmads' style='display:inline-block;width:728px;height:90px'
#    data-dcm-placement='N3643.3325855MIQ/B23580787.262966451'
#    data-dcm-rendering-mode='script'
#    data-dcm-https-only
#    data-dcm-resettable-device-id=''
#    data-dcm-app-id=''>
#  <script src='https://www.googletagservices.com/dcm/dcmads.js'></script>
#</ins>

#'''
#<html>
#    <head>
#        <title>Home Page - Microblog</title>
#    </head>
#    <body>
#        <h1>Hello, ''' + user['username'] + '''!</h1>
#    </body>
#</html>'''



if __name__ == '__main__':
    app.run()