import random
from vk_messages.vk_messages import requests, time, re, json, quote, BeautifulSoup, Exception_MessagesAPI, os, pickle
from vk_messages.utils import cleanhtml
from vk_messages import MessagesAPI
from difflib import SequenceMatcher

#Переопределяю класс, ибо вк присылает хрень. Здесь исправление
class MessagesAPI(MessagesAPI):

    def __init__(self, login, password, two_factor=False, cookies_save_path=''):
        self.login = login
        self.password = str(password.encode('UTF-8')).replace('\\x', '%')[2:-1]
        self.two_factor = two_factor

        if len(cookies_save_path) != 0 and cookies_save_path[-1] not in ["/", "\\", '']:
            raise Exception_MessagesAPI('Save path must end with one of this symbols: "/", "\\", or be empty',
                                        'InvalidPath')

        self.cookies_save_path = cookies_save_path
        self.main_session = requests.Session()

        if os.path.exists(f'{self.cookies_save_path}cookies_vk_auth_{self.login}.pickle'):
            with open(f'{self.cookies_save_path}cookies_vk_auth_{self.login}.pickle', 'rb') as handle:
                self.cookies_final = pickle.load(handle)
                response = self.main_session.get(f'https://vk.com/', cookies=self.cookies_final)
                if 'Войти через Facebook' not in response.text:
                    return None

        response = self.main_session.get(f'https://vk.com/')

        self.ip_h = re.findall(r'ip_h=(\S*)&lg', str(response.text))[0]
        self.lg_h = re.findall(r'lg_h=(\S*)&r', str(response.text))[0]

        if two_factor == True:
            self.two_factor_auth()
        else:
            self.single_factor_auth()

        with open(f'{self.cookies_save_path}cookies_vk_auth_{self.login}.pickle', 'wb') as handle:
            pickle.dump(self.cookies_final, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def method(self, name, **kwargs):
        if not hasattr(self, 'cookies_final'):
            raise Exception_MessagesAPI('No cookies found. Auth first.', 'AuthError')

        session = requests.Session()

        response = session.get(f'https://vk.com/dev/{name}', cookies=self.cookies_final)
        hash_data = re.findall(r'data-hash="(\S*)"', response.text)

        soup = BeautifulSoup(response.text, features="html.parser")
        params = soup.findAll("div", {"class": "dev_const_param_name"})
        params = [cleanhtml(str(i)) for i in params]

        if hash_data == []:
            raise Exception_MessagesAPI('Invalid method or not logined', 'Cannot_use_this_method')
        hash_data = hash_data[0]

        payload, checker = '', 0
        for param in params:
            if param in kwargs:
                checker += 1
                payload += '&{}={}'.format('param_' + \
                                           param, quote(
                    str(kwargs[param]) if type(kwargs[param]) != bool else str(int(kwargs[param]))))

        if checker != len(kwargs):
            raise Exception_MessagesAPI('Some of the parametrs invalid', 'InvalidParameters')

        response = session.post(f'https://vk.com/dev',
                                data=f'act=a_run_method&al=1&hash={quote(hash_data)}&method={name}{payload}&param_v=5.103',
                                cookies=self.cookies_final)

        response_json = json.loads(response.text[4:])['payload']

        # Исправленно(Заебись ответ от vk_api: ['3', ['"563a4f6752a2097bb1"', '"Pw--"']]. Как нибудь исправь это)
        if '3' in response_json:
            raise Bad_Respone(response_json)
        elif 'error' in json.loads(response_json[1][0]).keys():
            raise Exception_MessagesAPI(json.loads(response_json[1][0])['error']['error_msg'],
                                        json.loads(response_json[1][0])['error']['error_code'])

        return json.loads(response_json[1][0])['response']

class Bad_Respone(Exception):

    def __init__(self, value):
        super().__init__(value)
        self.value = value

class Longpool():

    def __init__(self, debug=False, ConnectionErrorMax=0, WaitTime=0.3):
        self.debug = debug
        self.ConnectionErrorMax = ConnectionErrorMax
        self.ConnectionErrorCount = 1
        self.WaitTime = WaitTime

    def get_start_pts(self, login, password):
        while True:
            time.sleep(self.WaitTime)
            try:
                vk_user = MessagesAPI(login=login, password=password)
                pts = vk_user.method('messages.getLongPollServer', need_pts=1)['pts']
                if self.debug == True:
                    print(r"Debug | Start Pts: ", pts)
                break

            except requests.exceptions.ConnectionError:
                if self.debug == True:
                    print(r"Debug | Start Pts: ConnectionError", self.ConnectionErrorCount)
                if self.ConnectionErrorCount >= self.ConnectionErrorMax:
                    if self.debug == True:
                        print(r"Debug | Start Pts: ConnectionError: Exceeded the number of connection errors when trying to get starting pts")
                    raise ConnectionError("Exceeded the number of connection errors when trying to get starting pts")
                else:
                    self.ConnectionErrorCount+=1
                    continue

        self.ConnectionErrorCount = 0
        return pts, vk_user

    def get_pool(self, pts, vk_user):

        while True:
            try:
                time.sleep(self.WaitTime)
                event = vk_user.method('messages.getLongPollHistory', pts=pts)
                if event['from_pts'] == event['new_pts']:
                    self.ConnectionErrorCount = 0
                    continue
                elif event['from_pts'] < event['new_pts']:
                    if self.debug == True:
                        print(r"Debug | Pool: ", event)
                    self.ConnectionErrorCount = 0
                    return event
                else:
                    self.ConnectionErrorCount = 0
                    continue


            except requests.exceptions.ConnectionError:
                if self.debug == True:
                    print(r"Debug | Pool: ConnectionError", self.ConnectionErrorCount, "/", self.ConnectionErrorMax)
                if self.ConnectionErrorCount >= self.ConnectionErrorMax:
                    if self.debug == True:
                        print(
                            r"Debug | Start Pts: ConnectionError: Exceeded the number of connection errors when trying to get pool")
                    raise ConnectionError("Exceeded the number of connection errors when trying to get pool")
                else:
                    self.ConnectionErrorCount += 1
                    continue

class Actions():

    def __init__(self, self_vk_id,  debug=False):
        self.debug = debug
        self.vk_id = self_vk_id

    def get_msgs(self, pool):
        events = []
        conversations = {}
        for items in pool['conversations']:
            admins = []
            if 'chat_settings' in items:
                admins.append(items['chat_settings']['owner_id'])
                items['chat_settings'].setdefault('admin_ids', [])
                admins.extend(items['chat_settings']['admin_ids'])
                conversations[items['peer']['id']] = admins
            else:
                conversations[items['peer']['id']] = [0]
        for items in pool['messages']['items']:
            items.setdefault('deleted', 0)
            if items['deleted'] == 0:
                if items['fwd_messages'] == []:
                    if items.setdefault("reply_message", []) == []:
                        fwd_rep_id = False
                    else:
                        fwd_rep_id = items["reply_message"]['from_id']
                else:
                    fwd_rep_id = items["fwd_messages"][0]['from_id']
                if self.vk_id in conversations[items['peer_id']]:
                    isHasPrim = True
                else:
                    isHasPrim = False
                if items['from_id'] in conversations[items['peer_id']]:
                    isAdmin = True
                else:
                    isAdmin = False
                events.append(
                    {'isHasPrim': isHasPrim, 'text': items['text'], 'peer_id': items['peer_id'], 'from_id': items['from_id'], 'id': items['id'], 'isAdmin': isAdmin,            'fwd_rep_id': fwd_rep_id})
        if self.debug == True:
            print(r"Debug | Msgs: ", events)
        return events

    def compare_text(self, text_1, text_2: list, accuracy=0.75):
        for items in text_2:
            precision = SequenceMatcher(lambda x: x == " ", text_1.lower(), items.lower()).ratio()
            if self.debug == True:
                print(r"Debug | СompareT: ", precision, "/", accuracy,'\t\t', text_1, ' |' , items, sep="")
            if precision >= accuracy:
                return True
        return False

    def compare_word(self, text_1, text_2: list, accuracy=0.75):
        for word in text_1.split():
            for items in text_2:
                precision = SequenceMatcher(lambda x: x == " ", word.lower(), items.lower()).ratio()
                if self.debug == True:
                    print(r"Debug | СompareW: ", precision, "/", accuracy,'\t\t', word, ' |' , items, sep="")
                if precision >= accuracy:
                    return True
        return False

    def compare_first_word(self, text_1, text_2: list, accuracy=0.75):
        if len(text_1) > 0:
            word = text_1.split()[0]
        else:
            if self.debug == True:
                print(r"Debug | СompareF: Haven't any word")
            return False
        for items in text_2:
            precision = SequenceMatcher(lambda x: x == " ", word.lower(), items.lower()).ratio()
            if self.debug == True:
                print(r"Debug | СompareF: ", precision, "/", accuracy,'\t\t', word, ' |' , items, sep="")
            if precision >= accuracy:
                return True
        return False

class Method():

    def __init__(self, vk_user, debug=False, ConnectionErrorMax=0, WaitTime=0.3, setActivity=True):
        self.vk_user = vk_user
        self.debug = debug
        self.ConnectionErrorMax = ConnectionErrorMax
        self.WaitTime = WaitTime
        self.setActivity = setActivity
        self.ConnectionErrorCount = 1

    def send_msg(self, text, peer_id):
        while True:
            try:
                if self.setActivity == True:
                    self.set_activity(peer_id=peer_id)
                time.sleep(self.WaitTime)
                return self.vk_user.method('messages.send', random_id=random.randint(1, 2147483647), peer_id=peer_id,
                               message=text)
            except requests.exceptions.ConnectionError:
                if self.debug == True:
                    print(r"Debug | Send: ConnectionError", self.ConnectionErrorCount, "/", self.ConnectionErrorMax)
                if self.ConnectionErrorCount >= self.ConnectionErrorMax:
                    if self.debug == True:
                        print(
                            r"Debug | Send: ConnectionError: Exceeded the number of connection errors when trying to get pool")
                    raise ConnectionError("Exceeded the number of connection errors when trying to get pool")
                else:
                    self.ConnectionErrorCount += 1
                    continue

    def delete_msg(self, message_ids, delete_for_all=True):
        while True:
            try:
                time.sleep(self.WaitTime)
                return self.vk_user.method('messages.delete',message_ids=",".join(str(x) for x in message_ids), delete_for_all=delete_for_all)
            except requests.exceptions.ConnectionError:
                if self.debug == True:
                    print(r"Debug | Delete: ConnectionError", self.ConnectionErrorCount, "/", self.ConnectionErrorMax)
                if self.ConnectionErrorCount >= self.ConnectionErrorMax:
                    if self.debug == True:
                        print(
                            r"Debug | Delete: ConnectionError: Exceeded the number of connection errors when trying to get pool")
                    raise ConnectionError("Exceeded the number of connection errors when trying to get pool")
                else:
                    self.ConnectionErrorCount += 1
                    continue

    def set_activity(self, peer_id, type='typing'):
        while True:
            try:
                time.sleep(self.WaitTime)
                return self.vk_user.method('messages.setActivity', type='typing', peer_id=peer_id)
            except requests.exceptions.ConnectionError:
                if self.debug == True:
                    print(r"Debug | Activity: ConnectionError", self.ConnectionErrorCount, "/", self.ConnectionErrorMax)
                if self.ConnectionErrorCount >= self.ConnectionErrorMax:
                    if self.debug == True:
                        print(
                            r"Debug | Activity: ConnectionError: Exceeded the number of connection errors when trying to get pool")
                    raise ConnectionError("Exceeded the number of connection errors when trying to get pool")
                else:
                    self.ConnectionErrorCount += 1
                    continue

    def get_comments(self, group_id, topic_id, count, offset):
        while True:
            try:
                time.sleep(self.WaitTime)
                return self.vk_user.method('board.getComments', group_id=group_id, topic_id=topic_id, count=count, offset=offset)
            except requests.exceptions.ConnectionError:
                if self.debug == True:
                    print(r"Debug | Comments: ConnectionError", self.ConnectionErrorCount, "/", self.ConnectionErrorMax)
                if self.ConnectionErrorCount >= self.ConnectionErrorMax:
                    if self.debug == True:
                        print(
                            r"Debug | Comments: ConnectionError: Exceeded the number of connection errors when trying to get pool")
                    raise ConnectionError("Exceeded the number of connection errors when trying to get pool")
                else:
                    self.ConnectionErrorCount += 1
                    continue

    def remove_user(self, user_id, peer_id):
        while True:
            try:
                time.sleep(self.WaitTime)
                return self.vk_user.method('messages.removeChatUser', user_id=user_id, chat_id=peer_id-2000000000)
            except requests.exceptions.ConnectionError:
                if self.debug == True:
                    print(r"Debug | Remove: ConnectionError", self.ConnectionErrorCount, "/", self.ConnectionErrorMax)
                if self.ConnectionErrorCount >= self.ConnectionErrorMax:
                    if self.debug == True:
                        print(
                            r"Debug | Remove: ConnectionError: Exceeded the number of connection errors when trying to get pool")
                    raise ConnectionError("Exceeded the number of connection errors when trying to get pool")
                else:
                    self.ConnectionErrorCount += 1
                    continue

class Bot():

    def __init__(self, vk_user, debug=False):
        self.debug = debug
        self.vk_user = vk_user

    def run(self, messeges: list, dict: dict, accuracy=0.95):
        del_msg=[]
        for msg in messeges:
            for key in dict:
                precision = SequenceMatcher(lambda x: x == " ", msg['text'].lower(), key.lower()).ratio()
                if self.debug == True:
                    print("Debug | Сompare: ", precision, "/", accuracy, '\t\t', msg['text'], '|', key, sep="")
                if precision >= accuracy:
                    if dict[key][0] == "send":
                        Method(self.vk_user, self.debug).send_msg(dict[key][1], msg['peer_id'])
                    elif dict[key][0] == "delete" and msg["isHasPrim"] == True and msg["isAdmin"] == False:
                        del_msg.append(msg["id"])
        if del_msg != []:
            Method(self.vk_user, self.debug).delete_msg(",".join(str(x) for x in del_msg))
        return False