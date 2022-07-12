import requests
from dotenv import load_dotenv
import os

load_dotenv()
ID = os.getenv('ID')


def API1(name,mode):    
        key = os.getenv('KEY')
        params = {
                'k' : key,
                'u' : name,
                'm' : mode,
                'type' : 'string'
        }
        OSU_API = "https://osu.ppy.sh/api"
        USER = "/get_user"
        PROFILE = "https://osu.ppy.sh/users/"
        IMGE = "https://a.ppy.sh/"
        ICON = "https://img.barks.jp/image/review/1000161129/01.jpg"
        req = requests.get(OSU_API+USER,params=params)
        data = req.json()[0]
        uname = data['username']
        id = data['user_id']
        level = float(data['level'])
        join = data['join_date']
        playcount = data['playcount']
        rank_total = data['pp_rank']
        rank = data['pp_country_rank']
        pp_total = data['pp_raw']
        acc  = float(data['accuracy'])
        country = data['country']
        profile  =  PROFILE+id
        IMGE_Profile = IMGE+id
        

        OSU = {
                "uname": uname,
                "level" : level,
                "join"  : join,
                "play"  : playcount,
                "rank"  : rank_total,
                "rankfrom" : rank,
                "pp"    : pp_total,
                "acc"   : acc,
                "From" : country,
                "Profile" : profile,
                "imge"  : IMGE_Profile,
                "icon"  : ICON
        }
        
        return OSU
print("Import\t"+__name__)
