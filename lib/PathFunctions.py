class PathFunction:
    ''' Functions useful for dealing with URLs '''
    def merge(self, xpath: str, ypath: str) -> str:
        ''' Merges two parts of url '''
        if not xpath or not ypath:
            return ""
        xpath = self.urlerslasher(xpath)
        ypath = self.unstarter(ypath, '/')
        return xpath + ypath
  
    def urlerslasher(self, xpath: str) -> str:
        ''' Converts a subdomain into a url '''
        if not xpath:
            return xpath
        ypath = self.ender(self.urler(xpath), '/')
        return ypath
    
    def starter(self, xpath:str, ypath: str) -> str:
        ''' Appends text to start if not found '''
        if not xpath or not ypath:
            return ""
        if xpath[0] != ypath:
            return ypath + xpath
        else:
            return xpath

    def unstarter(self, xpath:str, ypath: str) -> str:
        ''' Removes text from start if found '''
        if not xpath or not ypath:
            return ""
        if xpath[0] == ypath:
            return xpath[1:]
        else:
            return xpath

    def ender(self, xpath: str, ypath: str) -> str:
        ''' Appends text to end if not found '''
        if not xpath or not ypath:
            return ""
        if xpath[-1] != ypath:
            return xpath + ypath
        else:
            return xpath

    def unender(self, xpath: str, ypath: str) -> str:
        ''' Removes text from end if found '''
        if not xpath or not ypath:
            return ""
        if xpath[-1] == ypath:
            return xpath[:-1]
        return xpath
   
    def urler(self, xpath: str) -> str:
        ''' Appends http:// to subdomain/domain '''
        if not xpath:
            return xpath
        if not xpath.startswith('http://') and not xpath.startswith('https://'):
            ypath = "http://" + xpath
        else:
            ypath = xpath
        return ypath

    def unurler(self, xpath: str) -> str:
        ''' Removes scheme from url '''
        if not xpath:
            return xpath
        if not '://' in xpath:
            ypath = xpath
        else:
            ypath = xpath.split('://')[-1]
        return ypath
