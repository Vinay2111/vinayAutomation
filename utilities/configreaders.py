from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
print(config.get("basic info","website_used"))

