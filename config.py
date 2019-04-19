class _config:
    class ConfigError(TypeError):
        pass

    class ConfigCaseError(ConfigError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise (self.ConfigError, "Can't change config.%s" % name)
        if not name.isupper():
            raise (self.ConfigCaseError, 'config name "%s" is not all uppercase' % name)
        self.__dict__[name] = value

config = _config()

config.localConfig = [
    {
        "targetScanPath": "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient",
        "projectPath" : "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\dy_PCClient.vcxproj",
        "outputPath" : "E:\\unused_cpp.txt",
        "type" : ".cpp"
    },
    {
        "targetScanPath": "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\QML",
        "projectPath" : "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\QML\qml.qrc",
        "outputPath" : "E:\\unused_qml.txt",
        "type" : ".qml"
    },
    {
        "targetScanPath": "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\IMG",
        "projectPath" : "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\IMG\img.qrc",
        "outputPath" : "E:\\unused_img.txt",
        "type" : ".png|.gif|.ico"
    },
]