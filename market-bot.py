import discord
import asyncio
import random
import time

client = discord.Client() 

# list of words which triggers it
bannedWords = ["trade", "exchanges", "tradeogre", "sell turtlecoin", "buy turtlecoin", "sell trtl", "buy trtl", "tradesatoshi", "trde", "trae", "tradesat", 
				"wen lambo", "wen moon", "trade-", "when moon", "when lambo", "fiat", "pr1ce", "usd", "euro", "inr", "binance", "altcoin", "sats", 
				"to down", "ts down", "tradesatoshi down", "tradeogre down", "ogre down", "sats down", "exhcnage", "pump and dump", "dump", 
				"eur", "gbp", "ruble", "but turtlecoin", "but trtl", "moons", "hitbtc", "trtl be worth", "trtl worth", "exhcnag,e"
				"airdrop", "shitcoin", "shitcion", "shitconi", "gewi", "gwei", "mine and sell", "down trend", "resistance line", "bearish", "bullish",
				"to da moon", "pump and dump", "pump & dump", "pumped and dumped", "pumped & dumped", "pump n dump", "pumped n dumped" , "cmc", "coin market cap",
				"ico ", "ipo ", "stop loss", "mkid", "tether", "trading", "trend line", "buy wall", "sell wall", "buy order", "sell order", "buy trlt", "sell trlt", 
				"wtb", "wts", "Bitfinex", "Kraken", "Coinbase", "coinone", "Bitstamp", "Bithumb", "Bittrex", "Quoine", "Gemini", "bitFlyer", "BTC-e", "Poloniex", 
				"exx ", "livecoin", "exmo", "korbit", "cex.io", "tidex", "vaultoro", "itbit", "cryptopia", "yobit", "lakebtc", "kucoin", "btc-alpha", 
				"quadrigacx", "localbitcoins", "coinfloor", "bitx", "coinexchange", "okcoin", "gatecoin", "coinmate", "bitso", "acx", "idex", "cryptobridge", 
				"btcc", "bitfex", "virwox", "bleutrade", "abucoins", "paymium",  "flowbtc", "gate.io", "bitkonan", "cryptox", "cryptonit", "go4cryptos", "c-cex",
				"novaexchange", "coincoz", "btctrade", "vircurex", "allcoin", "coinsecure",  "indacoin", "bitmarket", "braziliex", "coinnest", "dsx", 
				"localturtlecoin", "localmonero", "local bitcoin", "local bitcoins", "localbitcoin", "stocks.exchange", "wen lamb0", "when lamb0", "wen l@mbo", 
				"when l@mbo", "wen l@mb0", "when l@mb0", "indacion", "indaocin", "satoshis", "ogre", "tr@de", "tr2de", "elliot wave", "when buy in", "mt. gox",
				" mt. gox", "mtgox", "mt gox", "pesos", "pesps", "trtl sell", "tlt sell", "turtlecoin sell", "trtl buy", "trlt buy", "turtlecoin buy",
				"1sat", "1 sat", "buy turtle", "sell turtle", "crypto exchange", "cryptocurrency exchange", "crypto currency exchange", "sellin", "buyin",
				"selin", "pumpin", "dumpin", "sellwall", "buywall", "selwall", " ts", "s@t", "0 sat", "0sat", "0stas", "stas", "st@s", "btc volume", 
				"btc volue", "btc volube", "wen buy in", "wen sell out", "wen but in", "when but in", "pr!ce", "binnance", "buy btc", "buy bct", "buy bticoin", 
				"buy bitcion", "buy btiocin", "buy bitocin", "coin offering", "inital coin offering", "crypto investing", "crypto invensting", "crypto investments",
				"investment", "investment", "investing", "invensting", "dividends", "dividens", "profit, dividends and gains", "profit dividens and gains",
				"mark3t", "xchange", "m@rket", "m@rk3t", "initial coin offering", "exchnage", "mkt", "xchnage", "bitfenix", "ccex", "exchamge", "buy some", "but some",
				"bynance", "turtle cost", "cost turtle", "cost of turtle", "buy high sell low", "buy hi sell low", "sell high buy low", "sell hi buy low", "trtl price", 
				"price of trtl", "price trtl", "price of turtle", "turtle price", "price turtle", "price of rtrl", "coin price", "price of coin", "price coin", "2 sats",
				"2 sat", "3 sat", "3 sats", "4 sat", "4 sats", "2sat", "3sat", "4sat", "5sat", "5 sat", "6sat", "6 sat", "7sat", "7 sat", "8sat", "8 sat",
				"9sat", "9 sat", "price of the coin", "price of the trtl", "price of the turtle", "pricce for the coin", "price for the trtl", "price for the turtle",
				"price for coin", "price for trtl", "price for turtle", "gamble turtle", "gamble trtl", "gamble rtrl", "trtl gamble", "turtle gamble" ]

# list of responses
wordlist = ["Heyo, please move to the server linked in <https://tinyurl.com/ybas4twh>, we don't like it here.", 
			"If you could move to the server linked in <https://tinyurl.com/ybas4twh>, that'd be great! We don't enjoy that here.", 
			"Please move this discussion to the server linked in <https://tinyurl.com/ybas4twh>, we like to keep this server focused on support and development. Thank you! <:t_smile:405478442599972874>",
			":rotating_light: MARKET TALK DETECTED :rotating_light: Please move to the server linked in <https://tinyurl.com/ybas4twh>, we don't like that here. :rotating_light:"]

#help reply
help = "Available commands - `^git` and `^todo`"

# github repo
git = "https://github.com/Sajo811/turtlecoin-market-linker"

# todo list
todo = "https://github.com/Sajo811/turtlecoin-market-linker/projects/1"

# supreme power
super = "WHEN WEB WALLET"

# manual warn's response
manres = "Hey, we don't like market-related talk in here. Join the server linked in <https://tinyurl.com/ybas4twh> to discuss about it."

# tip me repsonse
tip = "Hey, thanks for the thought! If you tip me, it all goes to RainBorg. If you want to tip my creator, tip `@Sajo8#2953`. Once again, thank you! <:t_smile:405478442599972874>"

@client.event 
async def on_ready():
	print("With me around, ain't gonna be no market talk!") 

lastMessageTimes = []
maxResponses = 4
timeFrameWindow = 15

def shouldPrint():
	currentTime = time.time()

	global lastMessageTimes
	# remove any messages that haven't occured in the last timeFrameWindow seconds
	lastMessageTimes = [x for x in lastMessageTimes if not currentTime - x > timeFrameWindow]

	# check if we've had over maxResponses in the last timeFrameWindow
	if len(lastMessageTimes) >= maxResponses:
		return False
	return True

@client.event
async def on_message(message):
	# convert it to lower
	msg = message.content.lower()

	# check if message incl. banned words. if so, spit a response
	if any(word.lower() in msg for word in bannedWords):
		if shouldPrint():
			lastMessageTimes.append(time.time())
			await client.send_message(message.channel, message.author.mention + " " + random.choice(wordlist))
		else:
			print("Ignoring message, have responded too many times in timeframe")

	# command to see if message *is* something and then responds if true
	if msg == "^help":
		if shouldPrint():
			lastMessageTimes.append(time.time())
			await client.send_message(message.channel, message.author.mention + " " + help)
		else:
			print("Ignoring message, have responded too many times in timeframe")

	if msg == "^git":
		if shouldPrint():
			lastMessageTimes.append(time.time())
			await client.send_message(message.channel, message.author.mention + " " + git)
		else:
			print("Ignoring message, have responded too many times in timeframe")

	if msg == "^todo":
		if shouldPrint():
			lastMessageTimes.append(time.time())
			await client.send_message(message.channel, message.author.mention + " " + todo)
		else:
			print("Ignoring message, have responded too many times in timeframe")

	#commmand which can only be run by person whose user id matches this one here
	if msg == "^super":
		if message.author.id == "235707623985512451":
			await client.send_message(message.channel, message.author.mention + " " + super)
		return  

	# command to manually warn person
	if msg.startswith("^warn"): 
		if message.author.id == "235707623985512451":
			# get userid of person
			user = message.mentions[0]
			await client.send_message(message.channel, user.mention + " " + manres)
	else:
		return

	if msg == "^tip":
		if shouldPrint():
			lastMessageTimes.append(time.time())
			await client.send_message(message.channel, message.author.mention + " " + tip)
		else:
			print("Ignoring message, have responded too many times in timeframe")

client.run("token")
