from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1345359606:AAFLEs3oY4kenF75PyWsse2-lnCnHXTvCYU"
	APP_ID = 1383845
	API_HASH = "0e3d2c299cc3c5cc26c283cecd2eb97c"
	OWNER_ID = "1131653685" #ID of bot owner
	AUTH_CHANNEL = [-1001266398622]
	DESTINATION_FOLDER = "TORHUNTER" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nscope = drive\nroot_folder_id = 19JWUztITYFMI4ouFIWxczTj-MsrKBsmw\ntoken = {"access_token":"ya29.a0AfH6SMDAsu_t7bnyVjskDNxsXZGM-VFGV19Y2dliBbDoF0tX8UZY37Y0CIf0tyZwLhaA-fdDW8X95Hx8bg0uQCefZPKm6hXAXjhPCMgG0-ZE0cM50ruv0bBopKVr2fTYxP066DetE_qtX7v6pfkWR7psuavDyiqW7aqIcQTghoE","token_type":"Bearer","refresh_token":"1//09jiQRmiVDpuOCgYIARAAGAkSNwF-L9IrXEuo4u7ep_PD8f5aUYfSOHsPdjQlNJIPPtjQX3DO5KUXJHlNltIiZ1IS7t4w4dDuC9M","expiry":"2020-12-12T16:30:09.8369024+05:30"}\nteam_drive = 0ADOQtaG3VrFxUk9PVA"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
