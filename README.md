The script uses coinmarketcap API and pulls selected info for a list of coins. In the current example it pulls volume_24h for top 5000 coins. 
You may set this script to run every 24h and it will dump all the data in the CSV file. Every time it will add new column with the timestamp and the respective volumes for each coin from the list. 

Steps:
1. Get your API token on coinmarketcap and paste it into the relevant places in the script

2. Run script "Create_file.py" to setup a CSV 
3. Run script "Coinmarketap.py" to fill CSV with data and automate its launch every 24h
4. Set up relevant triggers for coins (I.e. spike in volume) and consider these coins for your crypto portfolio
5. Profit! 

Would be happy to hear your ideas  on further improvements as this is my first script:)  

#crypto #coinmarketcap
