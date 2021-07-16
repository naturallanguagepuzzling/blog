#!/usr/bin/env python


## 2021/07/12. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/07/11 Sunday Puzzle:
## https://www.npr.org/2021/07/11/1014959492/sunday-puzzle-two-consonants
## That puzzle:
"""
This week's challenge comes from listener Peter Collins, of Ann Arbor, Mich.
Think of a country. Embedded in consecutive letters is a well-known brand name.
The first, second, eighth and ninth letters of the country, in order, spell a
former competitor of that brand. Name the country and the brands.
"""

import pandas as pd
from slugify import slugify


## List of countries; some are represented more than once, with variant names;
countries = [
    'Afghanistan', 'Aland Islands', 'Albania', 'Algeria','American Samoa',
    'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
    'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Plurinational State of Bolivia',
    'Bolivia', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina',
    'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory',
    'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde',
    'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands',
    'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island',
    'Cocos Islands', 'Keeling Islands', 'Colombia', 'Comoros', 'Congo',
    'Democratic Republic of the Congo', 'Cook Islands', 'Costa Rica',
    "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czechia',
    'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
    'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
    'Eswatini', 'Ethiopia', 'Falkland Islands', 'Malvinas', 'Faroe Islands',
    'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia',
    'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany',
    'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe',
    'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana',
    'Haiti', 'Heard Island and McDonald Islands', 'Holy See', 'Honduras',
    'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran',
    'Islamic Republic of Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel',
    'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya',
    'Kiribati', 'Korea', "Democratic People's Republic of Korea",
    'Republic of Korea', 'Kuwait', 'Kyrgyzstan', 'Ivory Coast'
    "Lao People's Democratic Republic", 'Laos', 'Latvia', 'Lebanon', 'Lesotho',
    'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao',
    'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
    'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte',
    'Mexico', 'Micronesia', 'Federated States of Micronesia', 'Moldova',
    'Republic of Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat',
    'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal',
    'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger',
    'Nigeria', 'Niue', 'Norfolk Island', 'North Macedonia',
    'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',
    'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
    'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',
    'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy',
    'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis',
    'Saint Lucia', 'Saint Martin', 'Saint Pierre and Miquelon',
    'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
    'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
    'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia',
    'Solomon Islands', 'Somalia', 'South Africa', "Republic of Côte d'Ivoire",
    'South Georgia and the South Sandwich Islands', 'South Sudan', 'Spain',
    'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Sweden',
    'Switzerland', 'Syrian Arab Republic', 'Taiwan', 'Republic of China',
    'Tajikistan', 'Tanzania', 'United Republic of Tanzania', 'Thailand',
    'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago',
    'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu',
    'Uganda', 'Ukraine', 'United Arab Emirates',
    'United Kingdom of Great Britain and Northern Ireland',
    'United States of America', 'United States Minor Outlying Islands',
    'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela',
    'Bolivarian Republic of Venezuela', 'Viet Nam', 'Virgin Islands',
    'British Virgin Islands', 'U.S. Virgin Islands', 'Wallis and Futuna',
    'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']


# ## Totally ugly and unvetted list that should be stored in a txt or csv but
# ## I'm pasting it here to keep things simple. I cobbled this list together
# ## from various online lists of top US brands, top worldwide brands, etc.
brands = [
    '20th Television', '3', '3M', '7-Eleven', 'ABB', 'ABC', 'ABN Amro',
    'ADNOC', 'ADP', 'AIA', 'AIG', 'ANZ', 'AOL', 'ARMCO', 'ASML', 'AT&T',
    'AT&T Technologies', 'AXA', 'AbbVie', 'Abbott', 'Abbott Laboratories',
    'Abbott Labs', 'Accenture', 'Acer', 'Activision Blizzard', 'Adidas',
    'Adobe', 'Aetna', 'Aflac', 'Airbus', 'Airtel', 'Alcoa', 'Aldi',
    'Alibaba.com', 'Allianz', 'Allstate', 'Altria Group', 'Amazon.com',
    'Amerada Hess', 'American Airlines', 'American Can', 'American Express',
    'American Standard', 'AmerisourceBergen', 'Amoco',
    'Anaconda', 'Anheuser-Busch', 'Anta', 'Anthem', 'Apple', 'Apple Computer',
    'Applied Materials', 'Archer Daniels Midland', 'Armour', 'Asda', 'Ashland',
    'AstraZeneca', 'Atlantic Richfield', 'Auchan', 'Audi', 'AutoZone', 'Aviva',
    'Avon', 'BAE Systems', 'BANCA INTESA', 'BANCO DO BRASIL',
    'BANK OF NEW YORK', 'BANK OF SCOTLAND', 'BANK OF TOKYO-MITSUBISHI UFJ',
    'BASF', 'BBC', 'BBVA', 'BD', 'BDO Global', 'BHP', 'BMO', 'BMW',
    'BNP Paribas', 'BNSF', 'BNY Mellon', 'BOE', 'BP', 'BP America', 'BRADESCO',
    'BT', 'BUICK', 'Baidu', 'Banco do Brasil', 'Bank of America',
    'Bank of Beijing', 'Bank of China', 'Bank of Communications',
    'Barclays', 'Baxter International', 'Bayer', 'Bayer Corporation',
    'Beatrice', 'Bechtel', 'Becks', 'Bell', 'BellSouth Corp',
    'Bendix', 'Benson and Hedges', 'Best Buy', 'Bestfoods',
    'Bethlehem Steel', 'Black & Decker', 'Blackrock',
    'Bloomberg', 'Boeing', 'Borden Chemical', 'Bosch', 'Bouygues',
    'Bridgestone', 'Bristol-Myers Squibb', 'British Airways', 'Broadcom',
    'Brookfield', 'Budweiser', 'Bulgari', 'Burlington Industries Equity',
    'C&S Wholesale Grocers', 'CANADIAN IMPERIAL BANK OF COMMERCE', 'CBS',
    'CCCC', 'CFLD', 'CHASE', 'CIBC', 'CJ Group', 'CNBM', 'CNOOC',
    'CNP Assurances', 'COACH', 'COMMERZBANK', 'COMMONWEALTH BANK OF AUSTRALIA',
    'CPIC', 'CRCC', 'CRECG', 'CREDIT AGRICOLE', 'CRRC',
    'CSCEC', 'CVS', 'Cadbury', 'Cadillac', 'Campbell Soup', "Campbell's",
    'Canada Life', 'Canadian National Railway', 'Canon', 'Capgemini',
    'Capital One', 'Cardinal Health', 'Cargill', 'Carmax', 'Carrefour',
    'Cartier', 'Caterpillar', 'Celanese', 'Centene Corporation', 'Centurylink',
    'Champion International', 'Chanel', 'Chase', 'Chevrolet', 'Chevron',
    'ChevronTexaco', 'China CITIC Bank', 'China Construction Bank',
    'China Everbright Bank', 'China Life', 'China Minsheng Bank',
    'China Mobile', 'China Post', 'China Telecom', 'China Unicom',
    'Chiquita Brands Intl.', 'Chow Tai Fook', 'Chrysler', 'Chubb',
    'Cigna', 'Cingular', 'Circle K', 'Cisco', 'Citgo Petroleum', 'Citi',
    'Claro', 'Clinique', 'Coastal', 'Coca-Cola', 'Cognizant', 'Coles',
    'Colgate', 'Comcast', 'Commonwealth Bank', 'ConAgra Foods', 'Conch',
    'Conoco', 'ConocoPhillips', 'Continental Group', 'Corona', 'Costco',
    'Country Garden', 'Cox Enterprises', 'Credit Suisse', 'Credit Agricole',
    'Credit Mutuel', 'Cummins', 'D.R. Horton', 'DBS', 'DHL', 'Daikin',
    'Daiwa House', 'Dana', 'Danaher', 'Danone', 'Deere', 'Dell',
    'Dell Technologies', 'Deloitte', 'Delta',
    'Deutsche Bank', 'Deutsche Telekom', 'Diesel', 'Digital Equipment',
    'Dior', 'Discover', 'Disney', 'Dollar General', "Domino's Pizza", 'Dove',
    'Dow Chemical', 'DuPont', "Dunkin'", 'E.ON', 'EA', 'EDF', 'EMC', 'ESPN',
    'EY', 'Eastman Kodak', 'Edeka', 'El Corte Ingl√©s', 'Electronic Arts',
    'Emerson Electric', 'Emirates', 'Enel', 'Engie', 'Eni', 'Enterprise',
    'Enterprise Holdings', 'Equinor', 'Ericsson', 'Ernst & Young', 'Esmark',
    'Est√©e Lauder', 'Etisalat', 'Evergrande', 'Express Scripts', 'Exxon Mobil',
    'ExxonMobil', 'FIS', 'FMC', 'FORTIS', 'FREDDIE MAC', 'Facebook', 'FedEx',
    'Ferrari', 'Fidelity Investments', 'Firestone Tire & Rubber', 'Ford',
    'Ford Motor', 'Fort James', 'Fortune Brands', 'Fox', 'Fresenius',
    'Fubon Financial', 'Fujitsu Group', 'GE', 'GEICO', 'GS Group', 'GUCCI',
    'Gap', 'Garnier', 'Gatorade', 'Gazprom', 'Geely', 'General Dynamics',
    'General Electric', 'General Foods', 'General Mills', 'General Motors',
    'General Telephone & Electronics', 'Generali', 'Generali Group', 'Genesco',
    'Georgia-Pacific', 'Gillette', 'GlaxoSmithKline', 'Goldman Sachs',
    'Goodrich', 'Goodyear', 'Goodyear Tire & Rubber', 'Google', 'Gree',
    'Greenland', 'Grumman', 'Gucci', 'Guerlain', 'Gujing Gong Jiu',
    'Gulf & Western Industries', 'Gulf Oil', 'H&M', 'H-E-B', 'H.J. Heinz',
    'HBO', 'HDFC Bank', 'HP', 'HPE', 'HSBC', 'HYPOVEREINSBANK', 'Haidilao',
    'Haier', 'Halifax', 'Hanson Industries NA', 'Harley-Davidson',
    'Head & Shoulders', 'Hearst', 'Heineken', 'Heinz', 'Hennessy', 'Hermes',
    "Hershey's", 'Hertz', 'Hewlett-Packard', 'Hikvision', 'Hilton', 'Hitachi',
    'Hoechst Celanese', 'Home Depot', 'Honda', 'Honeywell',
    'Honeywell Intl.', 'Hua Xia Bank', 'Huawei', 'Huggies', 'Humana', 'Hyatt',
    'Hyundai', 'Hyundai Group', 'IBM', 'ICBC', 'IKEA', 'ING', 'ITT Industries',
    'Iberdrola', 'Indian Oil', 'Industrial Bank', 'Infosys', 'Instagram',
    'Intel', 'International Paper', 'Intesa Sanpaolo',
    'Intl. Business Machines', 'JD.com', 'JP MORGAN', 'JP Morgan', 'JR',
    'Japan Airlines', 'Japan Post Holdings', 'Jeep', 'Jio', 'John Deere',
    'Johnson & Johnson', 'KB Financial Group', 'KEPCO', 'KFC', 'KPMG',
    "Kellogg's", 'Kia', 'Kimberly-Clark', 'Kleenex', 'Koch Industries', 'Kodak',
    'Kraft', 'Kroger', 'L&M', "L'Oreal", 'LENNAR', 'LG', 'LG Group', 'LIC',
    'LTV', 'LUKOIL', 'La Poste', 'Land Rover', "Lay's", 'Lego', 'Lehman Bros',
    'Lenovo', "Levi's", 'Lexus', 'Lidl', 'LinkedIn', 'Litton Industries',
    'Lloyds Bank', 'Loblaws', 'Lockheed Martin', 'Logan', 'Longfor Properties',
    'Louis Vuitton', "Lowe's", 'Lufthansa', 'Lukoil', 'Luzhou Laojiao',
    'Lyondell Chemical', 'MCC', 'MSCI', 'MTV', 'MUFG', 'Maersk',
    'Mahindra Group', 'Manulife', 'Manulife Financial', 'Marathon Oil',
    'Marks & Spencer', 'Marlboro', 'Mars',
    'Marshalls', 'Martin Marietta', 'Marubeni', 'Mastercard', 'McCain',
    "McDonald's", 'McDonnell Douglas', 'McKesson', 'McKinsey', 'McLane',
    'Medtronic', 'Meijer', 'Meituan', 'Mengniu', 'Mercadona', 'Mercedes-Benz',
    'Merck', 'Merck & Co', 'Merrill', 'Merrill Lynch', 'Metlife', 'Metro',
    'Michelin', 'Micron Technology', 'Microsoft', 'Midea', 'Mitsubishi Group',
    'Mitsui', 'Mizuho', 'Mizuho Financial Group', 'Mobil', 'Monsanto',
    'Monster', 'Morgan Stanley', 'Motorola', 'Moutai', 'Movistar', 'Munich Re',
    'NBC', 'NCR', 'NEC', 'NORDEA', 'NTT DoCoMo', 'NTT Group',
    'Nabisco Group Holdings', 'NatWest', 'National Austalia Bank',
    'National Intergroup', 'Navistar International', 'Nescafe', 'Nestle',
    'NetEase', 'Netflix', 'New China Life (NCL)', 'News Corp', 'Nike', 'Nikon',
    'Nintendo', 'Nippon Life Insurance', 'Nissan', 'Nivea', 'Nokia', 'Nordea',
    'North American Philips', 'Northrop Grumman', 'Novartis', 'Nvidia', 'O2',
    'OCBC Bank', 'Occidental Petroleum', 'OfficeMax', 'Old Mutual', 'Olin',
    'Olympus', 'Omega', 'Optum', 'Oracle', 'Orange', 'Owens-Illinois', 'PICC',
    'PNC', 'PPG Industries', 'PTT', 'PWC', 'Pall Mall', 'Pampers', 'Panasonic',
    'Pantene', 'PayPal', 'Pemex', 'Pepsi', 'PepsiCo', 'PetroChina', 'Petronas',
    'Peugeot', 'Pfizer', 'Philips', 'Pilot Flying J', 'Ping An', 'Pizza Hut',
    'Playstation', 'Poly Real Estate',
    'Porsche', 'Postal Savings Bank', 'Poste Italiane', 'Power China', 'Prada',
    'PricewaterhouseCoopers', 'Procter & Gamble', 'Progressive',
    'Prudential', 'Publix', 'Publix Super Markets', 'Purina', 'PwC', 'QNB',
    'Quaker Oats', 'Qualcomm', 'RBC', 'RCA', 'RWE', 'Rabobank', 'Rakuten',
    'Ralston Purina', 'Rapid-American', 'Raytheon', 'Raytheon Technologies',
    'Red Bull', 'Reliance', 'Renault', 'Republic Steel', 'Reyes Holdings',
    'Reynolds Metals', 'Roche', 'Rockwell Automation', 'Rogers', 'Rolex',
    'Ross Dress For Less', 'Royal Bank of Scotland', 'Ryerson Tull',
    'S&P Global', 'SABIC', 'SANTANDER', 'SAP', 'SF Express', 'SFR', 'SK Group',
    'STANDARD BANK OF SOUTH AFRICA', 'SUEZ Environment', 'SUMITOMO MITSUI',
    'Saab', 'Safran', "Sainsbury's", 'Saint-Gobain', 'Salesforce', "Sam's Club",
    'Samsung', 'Samsung Group', 'Sanofi', 'Santander',
    'Sara Lee', 'Saudi Aramco', 'Sber', 'Scotiabank', 'Sealed Air', 'Sephora',
    'Servicenow', 'Shanghai Pudong Development Bank', 'Sharp', 'Shell',
    'Shell Oil', 'Sherwin-Williams', 'Shinhan Financial Group', 'Siemens',
    'Siemens Group', 'Signal Companies', 'Singer', 'Sinopec', 'SiriusXM',
    'Sky', 'Smirnoff', 'Sodexo', 'SoftBank', 'Sompo Japan Nipponkoa', 'Sony',
    'Spectrum', 'Sperry', 'Spotify', 'Sprint', 'Sprite', 'Standard Chartered',
    'Starbucks', 'State Bank of India', 'State Farm', 'State Grid',
    'Stella Artois', 'Stone Container', 'Subaru', 'Subway', 'Sumitomo Group',
    'Sun', 'Sunac', 'Suning', 'Sunoco', 'Swiss Re', 'Swisscom', 'Symantec',
    'Sysco', 'T (Deutsche Telekom)', 'TATA Group', 'TD', 'TEPCO', 'TIM',
    'TJ Maxx', 'TORONTO-DOMINION BANK', 'TRW', 'TSMC', 'Taco Bell', 'Taobao',
    'Target', 'Tata', 'Telecom Italia', 'Teledyne', 'Telefonica', 'Telenor',
    'Telia', 'Telstra', 'Telus', 'Tencent', 'Tenneco Automotive', 'Tesco',
    'Tesla', 'Texaco', 'Texas Instruments', 'Textron', 'The Home Depot',
    'The North Face', 'Thermo Fisher Scientific', 'Thomson Reuters', 'Tide',
    'Tiffany & Co.', 'Tim Hortons', 'Time Warner', 'TimeWarner', 'Tmall',
    'Tokio Marine', 'Total', 'Toyota', 'Travelers', 'Truist',
    'Tyson', 'U.S. Bank', 'U.S. Steel', 'UBS', 'UNICREDIT', 'UNIQLO', 'UOB',
    'UPS', 'US BANCORP', 'Uber', 'Unicharm Corp', 'Unilever U.S.',
    'Union Carbide', 'Union Pacific', 'Uniroyal', 'Unisys', 'United Airlines',
    'United Technologies', 'UnitedHealthcare', 'Universal', 'Unocal', 'VISA',
    'VMWARE', 'VW (Volkswagen)', 'Valero', 'Vanke', 'Verizon', 'Victoria',
    "Victoria's Secret", 'Viettel', 'Vinci', 'Vodafone', 'Volkswagen', 'Volvo',
    'WACHOVIA CORP', 'WESTPAC', 'Wal-Mart', 'Walgreens', 'Walmart',
    'Warner Bros', 'Washington Mutual', 'Wawa', 'WeChat', 'Wellpoint',
    'Wells Fargo', 'Weyerhaeuser', 'Whirlpool', 'Whole Foods', 'Wipro',
    'Woolworths', 'Wrigley', "Wrigley's", 'Wuliangye', 'Wyeth', 'Xbox', 'Xerox',
    'Xfinity', 'Xiaomi', 'Yahoo!', 'Yahoo! Group', 'Yanghe', 'Yili',
    'Yonghui Superstores', 'YouTube', 'Youku', 'ZARA', 'Zalando', 'Zara',
    'Zurich', 'accenture', 'adidas', 'booking.com', 'eBay', 'movistar']


## tokenize string, convert to nearest ASCII, remove whitespace and non-letters
def clean_string(ugly):
    ugly = ugly.split(" ")
    ugly = [slugify(g) for g in ugly]
    ugly = "".join(ugly)
    clean = "".join([l for l in ugly if l.isalpha()])
    return clean


def main():
    cs = [clean_string(ct) for ct in countries if clean_string(ct)]
    cs = [ct for ct in cs if len(ct) > 8]
    bs = [clean_string(br) for br in brands if clean_string(br)]
    bs = [br for br in bs if len(br) > 2]
    for c in cs:
        for b in bs:
            if b in c:
                rival = c[0]+c[1]+c[7]+c[8]
                if rival in bs:
                    print(c+" & "+b+" & "+rival)


if __name__ == "__main__":
    main()



"""
SOLUTION:
saudiarabia & audi & saab
"""
