from enum import Enum

class Size(Enum):
    FULL = "full"
    COMPACT = "compact"

class Providers(Enum):
    oanda_fxp = 'oanda_fxp'
    
class Intervals(Enum):
    sec05 =  1 #5 second candlesticks, minute alignment
    sec10 =  2 #10 second candlesticks, minute alignment
    sec15 =  3 #15 second candlesticks, minute alignment
    sec30 =  4 #30 second candlesticks, minute alignment
    min01 =  5 #1 minute candlesticks, minute alignment
    min02 =  6 #2 minute candlesticks, hour alignment
    min04 =  7 #4 minute candlesticks, hour alignment
    min05 =  8 #5 minute candlesticks, hour alignment
    min10 =  9 #10 minute candlesticks, hour alignment
    min15 =  10 #15 minute candlesticks, hour alignment
    min30 =  11 #30 minute candlesticks, hour alignment
    min60 =  12 #1 hour candlesticks, hour alignment
    hour1 =  13 #2 hour candlesticks, day alignment
    hour2 =  14 #3 hour candlesticks, day alignment
    hour3 =  15 #4 hour candlesticks, day alignment
    hour4 =  16 #6 hour candlesticks, day alignment
    hour6 =  17 #8 hour candlesticks, day alignment
    hour8 =  18 #12 hour candlesticks, day alignment
    daily =  19 #1 day candlesticks, day alignment
    wekly =  20 #1 week candlesticks, aligned to start of week
    mntly =  21 #1 month candlesticks, aligned to first day of the month

class ForexPairs(Enum):
	aud_cad	=	1
	aud_chf	=	2
	aud_jpy	=	3
	aud_nzd	=	4
	aud_usd	=	5
	cad_chf	=	6
	cad_jpy	=	7
	chf_jpy	=	8
	eur_aud	=	9
	eur_cad	=	10
	eur_chf	=	11
	eur_gbp	=	12
	eur_jpy	=	13
	eur_nzd	=	14
	eur_usd	=	15
	gbp_aud	=	16
	gbp_cad	=	17
	gbp_chf	=	18
	gbp_jpy	=	19
	gbp_nzd	=	20
	gbp_usd	=	21
	nzd_jpy	=	22
	nzd_usd	=	23
	usd_cad	=	24
	usd_chf	=	25
	usd_jpy	=	26
	usd_sgd	=	27