from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1345359606:AAFLEs3oY4kenF75PyWsse2-lnCnHXTvCYU"
	APP_ID = 1383845
	API_HASH = "0e3d2c299cc3c5cc26c283cecd2eb97c"
	OWNER_ID = "1131653685" #ID of bot owner
	AUTH_CHANNEL = [-1001266398622]
	DESTINATION_FOLDER = "Gdrive bot" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nscope = drive\nroot_folder_id = 1ugGQR35PZbG5SjNv53XGWvlj3LZO8aCP\ntoken = {"access_token":"ya29.a0AfH6SMBb1KthGGArvJDOHuOy_Vew_BPVWG34NDKwkQ1ygVWwt-OIhh5x7y98WKbV95n5m4Xbnnr-fcBt9rLv_HxKs25HG_ScWXpi1OtSw3rg19Y6JNnoTsheCgT9IYvdyhKYFruWFZR680ODVgzBSQdPeQvUgXm3CRXLVlgCxng","token_type":"Bearer","refresh_token":"1//09m-3YTLywwFtCgYIARAAGAkSNwF-L9IrXUc3DNs3d_BgskfZ2QYYjcGIzCvITifoht-Xd8VbZp_rxQbd6eHg2XvLrp2KBk6hGt8","expiry":"2020-12-12T16:52:08.8696738+05:30"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
