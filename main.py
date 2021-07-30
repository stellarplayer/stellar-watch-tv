import StellarPlayer
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
        filePath = __file__
        pos = filePath.rindex('\\')
        filePath2 = filePath[0:pos]
        newFilePath = filePath2 +  "\\" + "weishi.m3u"
        self.list_weishi = test.openFile(newFilePath)
        self.list_weishi_name = test.getListName()

        list_item_layout = [
            [
                {'type': 'space', 'width': 10},
                {
                    'group': [
                        {'type': 'button', 'name': 'weishi', 'textColor': '#FFFFFFE6', 'fontSize': 20,'width': 0.5,'matchParent':True}, 
                        {'type':'space','width':10},
                        {'type': 'button', 'name': 'weishi1', 'textColor': '#FFFFFFE6', 'fontSize': 20,'width': 0.5,'matchParent':True},
                        {'type':'space','width':10}
                    ], 'dir': 'hertical'
                }
            ]
        ]

        controls = [
            {'type':'space','height':15}, 
            [
                {'type':'space','width':15},
                {'type':'list','name':'list1','itemheight':36,'itemlayout':list_item_layout,'value':self.list_weishi_name,'width':1,'marginSize':5}
            ]
        ]

        result, controls = self.player.doModal('test', 400, 600, 'ø¥µÁ ”', controls)
        print(f'{result=},{controls=}')

    def onListItemClick(self, page, control, item):
        print(f'onListItemClick,{control=},{item=}')

    def onListItemControlClick(self, page, listControl, item, itemControl):
        keyName = self.list_weishi_name[item]
        key = ""
        index = 0
        if itemControl == 'weishi':
            key = keyName["weishi"]
            index = (item + 1) * 2 - 2
        else:
            key = keyName["weishi1"]
            index = (item + 1) * 2 - 1
        self.player.play(self.list_weishi[index]['link'])
    def stop(self):
        super().stop()
        print("pugin stop")

def newPlugin(player:StellarPlayer.IStellarPlayer,*arg):
    plugin = weishiplugin(player)
    return plugin

def destroyPlugin(plugin:StellarPlayer.IStellarPlayerPlugin):
    plugin.stop()

