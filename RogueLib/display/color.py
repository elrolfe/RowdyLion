from enum import Enum

# Define colors
class Color(Enum):
	ALICE_BLUE = 0XF0F8FF
	ANTIQUE_WHITE = 0XFAEBD7
	AQUA = 0X00FFFF
	AQUA_MARINE = 0X7FFFD4
	AZURE = 0XF0FFFF
	BEIGE = 0XF5F5DC
	BISQUE = 0XFFE4C4
	BLACK = 0X000000
	BLANCHED_ALMOND = 0XFFEBCD
	BLUE = 0X0000FF
	BLUE_VIOLET = 0X8A2BE2
	BROWN = 0XA52A2A
	BURLY_WOOD = 0XDEB887
	CADET_BLUE = 0X5F9EA0
	CHARTREUSE = 0X7FFF00
	CHOCOLATE = 0XD2691E
	CORAL = 0XFF7F50
	CORNFLOWER_BLUE = 0X6495ED
	CORNSILK = 0XFFF8DC
	CRIMSON = 0XDC143C
	CYAN = 0X00FFFF
	DARK_BLUE = 0X00008B
	DARK_CYAN = 0X008B8B
	DARK_GOLDENROD = 0XB8860B
	DARK_GRAY = 0XA9A9A9
	DARK_GREY = 0XA9A9A9
	DARK_GREEN = 0X006400
	DARK_KHAKI = 0XBDB76B
	DARK_MAGENTA = 0X8B008B
	DARK_OLIVE_GREEN = 0X556B2F
	DARK_ORANGE = 0XFF8C00
	DARK_ORCHID = 0X9932CC
	DARK_RED = 0X8B0000
	DARK_SALMON = 0XE9967A
	DARK_SEA_GREEN = 0X8FBC8F
	DARK_SLATE_BLUE = 0X483D8B
	DARK_SLATE_GRAY = 0X2F4F4F
	DARK_SLATE_GREY = 0X2F4F4F
	DARK_TURQUOISE = 0X00CED1
	DARK_VIOLET = 0X9400D3
	DEEP_PINK = 0XFF1493
	DEEP_SKY_BLUE = 0X00BFFF
	DIM_GRAY = 0X696969
	DIM_GREY = 0X696969
	DODGER_BLUE = 0X1E90FF
	FIRE_BRICK = 0XB22222
	FLORAL_WHITE = 0XFFFAF0
	FOREST_GREEN = 0X228B22
	FUCHSIA = 0XFF00FF
	GAINSBORO = 0XDCDCDC
	GHOST_WHITE = 0XF8F8FF
	GOLD = 0XFFD700
	GOLDENROD = 0XDAA520
	GRAY = 0X808080
	GREY = 0X808080
	GREEN = 0X008000
	GREEN_YELLOW = 0XADFF2F
	HONEYDEW = 0XF0FFF0
	HOT_PINK = 0XFF69BF
	INDIAN_RED = 0XCD5C5C
	INDIGO = 0X4B0082
	IVORY = 0XFFFFF0
	KHAKI = 0XF0E68C
	LAVENDER = 0XE6E6FA
	LAVENDER_BLUSH = 0XFFF0F5
	LAWN_GREEN = 0X7CFC00
	LEMON_CHIFFON = 0XFFFACD
	LIGHT_BLUE = 0XADD8E6
	LIGHT_CORAL = 0XF08080
	LIGHT_CYAN = 0XE0FFFF
	LIGHT_GOLDENROD_YELLOW = 0XFAFAD2
	LIGHT_GRAY = 0XD3D3D3
	LIGHT_GREY = 0XD3D3D3
	LIGHT_GREEN = 0X90EE90
	LIGHT_PINK = 0XFFB6C1
	LIGHT_SALMON = 0XFFA07A
	LIGHT_SEA_GREEN = 0X20B2AA
	LIGHT_SKY_BLUE = 0X87CEFA
	LIGHT_SLATE_GRAY = 0X778899
	LIGHT_SLATE_GREY = 0X778899
	LIGHT_STEEL_BLUE = 0XB0C4DE
	LIGHT_YELLOW = 0XFFFFE0
	LIME = 0X00FF00
	LIME_GREEN = 0X32CD32
	LINEN = 0XFAF0E6
	MAGENTA = 0XFF00FF
	MAROON = 0X800000
	MEDIUM_AQUA_MARINE = 0X66CDAA
	MEDIUM_BLUE = 0X0000CD
	MEDIUM_ORCHID = 0XBA55D3
	MEDIUM_PURPLE = 0X9370DB
	MEDIUM_SEA_GREEN = 0X3CB371
	MEDIUM_SLATE_BLUE = 0X7B68EE
	MEDIUM_SPRING_GREEN = 0X00FA9A
	MEDIUM_TURQUOISE = 0X48D1CC
	MEDIUM_VIOLET_RED = 0XC71585
	MIDNIGHT_BLUE = 0X191970
	MINT_CREAM = 0XF5FFFA
	MISTY_ROSE = 0XFFE4E1
	MOCCASIN = 0XFFE4B5
	NAVAJO_WHITE = 0XFFDEAD
	NAVY = 0X000080
	OLD_LACE = 0XFDF5E6
	OLIVE = 0X808000
	OLIVE_DRAB = 0X6B8E23
	ORANGE = 0XFFA500
	ORANGE_RED = 0XFF4500
	ORCHID = 0XDA70D6
	PALE_GOLDENROD = 0XEEE8AA
	PALE_GREEN = 0X98FB98
	PALE_TURQUOISE = 0XAFEEEE
	PALE_VIOLET_RED = 0XDB7093
	PAPAYA_WHIP = 0XFFEFD5
	PEACH_PUFF = 0XFFDAB9
	PERU = 0XCD853F
	PINK = 0XFFC0CB
	PLUM = 0XDDA0DD
	POWDER_BLUE = 0XB0E0E6
	PURPLE = 0X800080
	REBECCA_PURPLE = 0X663399
	RED = 0XFF0000
	ROSY_BROWN = 0XBC8F8F
	ROYAL_BLUE = 0X4169E1
	SADDLE_BROWN = 0X8B4513
	SALMON = 0XFA8072
	SANDY_BROWN = 0XF4A460
	SEA_GREEN = 0X2E8B57
	SEA_SHELL = 0XFFF5EE
	SIENNA = 0XA0522D
	SILVER = 0XC0C0C0
	SKY_BLUE = 0X87CEEB
	SLATE_BLUE = 0X6A5ACD
	SLATE_GRAY = 0X708090
	SLATE_GREY = 0X708090
	SNOW = 0XFFFAFA
	SPRING_GREEN = 0X00FF7F
	STEEL_BLUE = 0X4682B4
	TAN = 0XD2B48C
	TEAL = 0X008080
	THISTLE = 0XD8BFD8
	TOMATO = 0XFF6347
	TURQUOISE = 0X40E0D0
	VIOLET = 0XEE82EE
	WHEAT = 0XF5DEB3
	WHITE = 0XFFFFFF
	WHITE_SMOKE = 0XF5F5F5
	YELLOW = 0XFFFF00
	YELLOW_GREEN = 0X9ACD32