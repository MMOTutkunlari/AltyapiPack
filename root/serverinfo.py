import app
app.ServerName = None

SERVER1 = {
	"name" : "MMO Tutkunlari",
	"host" : "192.168.1.111",
	"auth" : 11900,
	"ch1" : 13900,
	"ch2" : 13910,
}

STATE_NONE = "..."
					
STATE_DICT = {
	0 : "....",
	1 : "NORM",
	2 : "BUSY",
	3 : "FULL"
}

SERVER01_CHANNEL_DICT = {
	1: {"key":11, "name":"CH1", "ip":SERVER1["host"], "tcp_port":SERVER1["ch1"], "udp_port":SERVER1["ch1"], "state":STATE_NONE,},
	2: {"key":12, "name":"CH2", "ip":SERVER1["host"], "tcp_port":SERVER1["ch2"], "udp_port":SERVER1["ch2"], "state":STATE_NONE,},
}

REGION_NAME_DICT = {
	0 : SERVER1["name"],		
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":SERVER1["host"], "port":SERVER1["auth"], },

	}		
}

REGION_DICT = {
	0 : {
		1 : { "name" :SERVER1["name"], "channel" : SERVER01_CHANNEL_DICT, },						
	},
}

MARKADDR_DICT = {
	10 : { "ip" : SERVER1["host"], "tcp_port" : SERVER1["ch1"], "mark" : "10.tga", "symbol_path" : "10", },
}