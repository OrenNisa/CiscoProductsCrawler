from urllib.parse import urlparse
import time


class Product:
    def __init__(self):
        self._vendor = ""
        self._url = ""
        self._series = ""
        self._category = ""
        self._model = ""
        self._path = ""
        self._release = ""
        self._endofsale = ""
        self._enfodsupport = ""
        self._downloads = ""

    def getvendor(self):
        return self.vendor

    def setvendor(self, value):
        value = '{uri.netloc}'.format(uri=urlparse(value)).removeprefix('www.')
        self.vendor = value

    def geturl(self):
        return self.url

    def seturl(self, value):
        self.url = value

    def getseries(self):
        return self.series

    def setseries(self, value):
        self.series = value

    def getcategory(self):
        return self.category

    def setcategory(self, value):
        self.category = value

    def getmodel(self):
        return self.model

    def setmodel(self, value):
        self.model = value

    def getpath(self):
        return self.path

    def setpath(self, value):
        self.path = value

    def getrelease(self):
        return self.release

    def setrelease(self, value):
        if value != "":
            value = int(time.mktime(time.strptime(value, '%d-%b-%Y')))
        self.release = value

    def getendofsale(self):
        return self.endofsale

    def setendofsale(self, value):
        if value != "":
            value = int(time.mktime(time.strptime(value, '%d-%b-%Y')))
        self.endofsale = value

    def getenfodsupport(self):
        return self.enfodsupport

    def setenfodsupport(self, value):
        if value != "":
            value = int(time.mktime(time.strptime(value, '%d-%b-%Y')))
        self.enfodsupport = value

    def getdownloads(self):
        return self.downloads

    def setdownloads(self, value):
        self.downloads = value

    _vendor = property(getvendor, setvendor)
    _url = property(geturl, seturl)
    _series = property(getseries, setseries)
    _category = property(getcategory, setcategory)
    _model = property(getmodel, setmodel)
    _path = property(getpath, setpath)
    _release = property(getrelease, setrelease)
    _endofsale = property(getendofsale, setendofsale)
    _enfodsupport = property(getenfodsupport, setenfodsupport)
    _downloads = property(getdownloads, setdownloads)


class DownloadInfo:
    latest = "none"
    filename = "none"
    size = "none"
    md5 = "none"


class AllReleases:
    all = "none"
