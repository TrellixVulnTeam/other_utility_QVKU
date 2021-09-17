import http_util
import argparse
import yaml
import json


URL = "http://sz-name-jingwei.huya.com/nacos/v1/cs/configs?tenant=2068b85d-33a1-4c2d-a0b8-cc0977826a08&dataId={0}&group={1}"
WUXI_URL = "http://wx-name-jingwei.huya.com/nacos/v1/cs/configs?tenant=2068b85d-33a1-4c2d-a0b8-cc0977826a08&dataId={0}&group={1}"
TEST_URL = "http://dev-name-jingwei.huya.com/nacos/v1/cs/configs?tenant=b753b5ac-0c71-4577-88c7-92d9550f11b5&dataId={0}&group={1}"

USERDATA = "game_userdata"
CONF = "game_conf"
DEFAULT = "DEFAULT_GROUP"
MACHINE_T4 = "T4_ws2019"
MACHINE_SLICE2 = "T4_tencent_slice_2"
MACHINE_SLICE4 = "T4_tencent_slice_4"
GLOBAL_GAMES = "global_games"

def parser_commandline():
    parser = argparse.ArgumentParser(description="get user last archive of gameid")
    parser.add_argument('-c', '--conf',action='store_true')
    parser.add_argument('-u', '--userdata', action='store_true')
    parser.add_argument('-t','--test', action='store_true')
    parser.add_argument('--wuxi', action='store_true')
    parser.add_argument('--compare',action='store_true')
    parser.add_argument('-g','--global_games')
    parser.add_argument('name', nargs='?')
    return parser.parse_args()

class UrlArg:
    def __init__(self,name,group,test,wuxi) -> None:
        self.name = name
        self.group = group
        self.test = test
        self.wuxi = wuxi
    
    def get_url(self):
        if self.test:
            base_url = TEST_URL
        elif self.wuxi:
            base_url = WUXI_URL
        else:
            base_url = URL

        return base_url.format(self.name,self.group)


def get_url(args):
    name = args.name

    machine_type = args.global_games
    if machine_type:
        name = GLOBAL_GAMES
        if machine_type == '1':
            group = MACHINE_T4
        elif machine_type == '2':
            group = MACHINE_SLICE2
        elif machine_type == '4':
            group = MACHINE_SLICE4
        else:
            group = machine_type
    else:
        if args.conf:
            group = CONF
        elif args.userdata:
            group = USERDATA
        else:
            group = DEFAULT


    urlarg = UrlArg(name,group,args.test,args.wuxi)
    return urlarg.get_url()

def get_global_games(machine):
    games = []
    ua = UrlArg("global_games",machine,False,False)
    configs = http_util.request_get_yaml(ua.get_url())
    game_list = configs['GameList']
    for item in game_list:
        games.append(item['gameId'])
    return games


def compare_game(game):
    a = compare_game_group(game,CONF)
    b = compare_game_group(game,USERDATA)
    if a and b:
        print('same for ',game)

def compare_game_group(game,group):
    ua = UrlArg(game,group,False,False)
    exist = http_util.request_get_exist(ua.get_url())

    ua = UrlArg(game,group,False,True)
    exist2 = http_util.request_get_exist(ua.get_url())

    if exist2 != exist:
        print("Warnning is not same ", game, group)
        return False
    elif not exist2:
        print("both 404 ",game,group)
    return True



def compare_two_service():
    games = []
    machine_types = ['T4_ws2019','T4_tencent_slice_2','T4_tencent_slice_4']
    for machine in machine_types:
        games += get_global_games(machine)

    #games = ['pes21']
    for game in games:
        compare_game(game)




def main():
    args = parser_commandline()
    if args.compare:
        compare_two_service()
        return 

    url = get_url(args)
    
    #url = URL.format('3','DEFAULT_GROUP')
    print(url,"\n")

    result = http_util.request_get_text(url)
    print(result)


    try:
        json.loads(result)
        print("\n--valid json--")
    except:
        aa = yaml.load(result, Loader=yaml.FullLoader)
        print("\n--valid yaml--")





if __name__ == '__main__':
    main()
