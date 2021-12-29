import StellarPlayer
import os
from .m3uParse import m3uParse


class weishiplugin(StellarPlayer.IStellarPlayerPlugin):
    def __init__(self,player:StellarPlayer.IStellarPlayer):
        super().__init__(player)
        print("init weishi plugin")
        self.list_weishi = []
        self.list_weishi_name = []

    def show(self):
        print('ui start')

        test = m3uParse()   
        newFilePath = os.path.join(os.path.dirname(__file__), "weishi.m3u")
        self.list_weishi = test.openFile(newFilePath)
        self.list_weishi_name = test.getListName()

        list_item_layout = [
            [
                {'type': 'space', 'width': 5},
                {
                    'group': [
                        {'type': 'button', 'name': 'weishi', 'textColor': '#FFFFFFE6', 'fontSize': 16,'matchParent':True}, 
                        {'type':'space','width':6},
                        {'type': 'button', 'name': 'weishi1', 'textColor': '#FFFFFFE6', 'fontSize': 16,'matchParent':True},
                        {'type':'space','width':6},
                        {'type': 'button', 'name': 'weishi2', 'textColor': '#FFFFFFE6', 'fontSize': 16,'matchParent':True},
                        {'type':'space','width':6},
                        {'type': 'button', 'name': 'weishi3', 'textColor': '#FFFFFFE6', 'fontSize': 16,'matchParent':True},
                        {'type':'space','width':6},
                        {'type': 'button', 'name': 'weishi4', 'textColor': '#FFFFFFE6', 'fontSize': 16,'matchParent':True},
                        {'type':'space','width':6}
                    ], 'dir': 'hertical'
                }
            ]
        ]

        controls = [
            {'type':'space','height':10}, 
            [
                {'type':'space','width':10},
                {'type':'list','name':'list1','itemheight':30,'itemlayout':list_item_layout,'value':self.list_weishi_name,'marginSize':3},
                {'type':'space','width':10}
            ],
             {'type':'space','height':10}
        ]

        result, controls = self.player.doModal('test', 740, 780, '我要看电视', controls)
        print(f'{result=},{controls=}')

    def onListItemClick(self, page, control, item):
        print(f'onListItemClick,{control=},{item=}')

    def onListItemControlClick(self, page, listControl, item, itemControl):
        keyName = self.list_weishi_name[item]
        key = ""
        index = 0
        print(f'onListItemControlClick,{item=}')
        if itemControl == 'weishi':
            key = keyName["weishi"]
            index = (item + 1) * 5 - 5
        elif itemControl == 'weishi1':
            key = keyName["weishi1"]
            index = (item + 1) * 5 - 4
        elif itemControl == 'weishi2': 
            key = keyName["weishi2"]
            index = (item + 1) * 5 - 3
        elif itemControl == 'weishi3': 
            key = keyName["weishi3"]
            index = (item + 1) * 5 - 2
        elif itemControl == 'weishi4': 
            key = keyName["weishi4"]
            index = (item + 1) * 5 - 1
        try:
            self.player.play(self.list_weishi[index]['link'],caption=self.list_weishi[index]['weishi'])
        except:
            self.player.play(self.list_weishi[index]['link'])
    def stop(self):
        super().stop()
        print("pugin stop")

def newPlugin(player:StellarPlayer.IStellarPlayer,*arg):
    plugin = weishiplugin(player)
    return plugin

def destroyPlugin(plugin:StellarPlayer.IStellarPlayerPlugin):
    plugin.stop()

