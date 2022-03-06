import json

test = {'res': [{'businesses': [{'id': '5B92XhcMTS1YymGx3qpB9w', 'alias': 'uncle-afs-agoura-hills', 'name': "Uncle Af's", 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/CoamHi3DHUOixwPOhTEcUg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/uncle-afs-agoura-hills?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 656, 'categories': [{'alias': 'sandwiches', 'title': 'Sandwiches'}, {'alias': 'salad', 'title': 'Salad'}, {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'}], 'rating': 5, 'coordinates': {'latitude': 34.1570154, 'longitude': -118.7563608}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 'location': {'address1': '5905 Kanan Rd', 'address2': None, 'address3': '', 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['5905 Kanan Rd', 'Agoura Hills, CA 91301']}, 'phone': '+18185843556', 'display_phone': '(818) 584-3556', 'distance': 838.4256063009796}, {'id': 'A21AmZFG5OQloYLaS7xnzg', 'alias': 'lal-mirch-indian-restaurant-agoura-hills-2', 'name': 'Lal Mirch Indian Restaurant', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/EhOVQ8KWhgTwIkpJgARyhg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/lal-mirch-indian-restaurant-agoura-hills-2?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 832, 'categories': [{'alias': 'indpak', 'title': 'Indian'}], 'rating': 4.5, 'coordinates': {'latitude': 34.1479288, 'longitude': -118.7605167}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 'location': {'address1': '5146 Kanan Rd', 'address2': '', 'address3': '', 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['5146 Kanan Rd', 'Agoura Hills, CA 91301']}, 'phone': '+18185327532', 'display_phone': '(818) 532-7532', 'distance': 504.8841302474077}, {'id': 'Xoc9VDZXU0kkiRc_6Xw58Q', 'alias': 'lure-fish-house-westlake-village', 'name': 'Lure Fish House', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/O_2tSZrC9qrSI646UEVSMg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/lure-fish-house-westlake-village?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 2499, 'categories': [{'alias': 'seafood', 'title': 'Seafood'}, {'alias': 'cocktailbars', 'title': 'Cocktail Bars'}, {'alias': 'wine_bars', 'title': 'Wine Bars'}], 'rating': 4.5, 'coordinates': {'latitude': 34.151, 'longitude': -118.80227}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 'location': {'address1': '30970 Russell Ranch Rd', 'address2': '', 'address3': '', 'city': 'Westlake Village', 'zip_code': '91362', 'country': 'US', 'state': 'CA', 'display_address': ['30970 Russell Ranch Rd', 'Westlake Village, CA 91362']}, 'phone': '+18186516611', 'display_phone': '(818) 651-6611', 'distance': 3601.135144839797}, {'id': 'Oogri3PnYxBvqtiqaNWfyg', 'alias': 'tifa-chocolate-and-gelato-agoura-hills-3', 'name': 'Tifa Chocolate & Gelato', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/FF_Ne4Jri3c-w8LM4tAXGw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/tifa-chocolate-and-gelato-agoura-hills-3?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 483, 'categories': [{'alias': 'chocolate', 'title': 'Chocolatiers & Shops'}, {'alias': 'icecream', 'title': 'Ice Cream & Frozen Yogurt'}], 'rating': 4.5, 'coordinates': {'latitude': 34.1448527, 'longitude': -118.7545433}, 'transactions': [], 'price': '$$', 'location': {'address1': '28888 Roadside Dr', 'address2': '', 'address3': '', 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['28888 Roadside Dr', 'Agoura Hills, CA 91301']}, 'phone': '+18188790685', 'display_phone': '(818) 879-0685', 'distance': 1117.6864475750156}, {'id': 'dMNQchp74yTINss8qsIz6Q', 'alias': 'italia-deli-and-bakery-agoura-hills', 'name': 'Italia Deli & Bakery', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/TuwiVdDhbJcb_5LlIOCjvg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/italia-deli-and-bakery-agoura-hills?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 715, 'categories': [{'alias': 'delis', 'title': 'Delis'}, {'alias': 'grocery', 'title': 'Grocery'}, {'alias': 'italian', 'title': 'Italian'}], 'rating': 4.5, 'coordinates': {'latitude': 34.1531499188827, 'longitude': -118.757597263375}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '5657 Kanan Rd', 'address2': '', 'address3': '', 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['5657 Kanan Rd', 'Agoura Hills, CA 91301']}, 'phone': '+18189914838', 'display_phone': '(818) 991-4838', 'distance': 514.4994591933438}, {'id': 'hly_R_JR8LXbukp_-glaDw', 'alias': 'carrara-pastries-agoura-hills', 'name': 'Carrara Pastries', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/2D4h1qmRpgn5TYO6utkyfQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/carrara-pastries-agoura-hills?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 441, 'categories': [{'alias': 'bakeries', 'title': 'Bakeries'}, {'alias': 'desserts', 'title': 'Desserts'}, {'alias': 'coffee', 'title': 'Coffee & Tea'}], 'rating': 4.5, 'coordinates': {'latitude': 34.1442978463423, 'longitude': -118.755306685416}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '28914 Roadside Dr', 'address2': 'Ste 107', 'address3': '', 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['28914 Roadside Dr', 'Ste 107', 'Agoura Hills, CA 91301']}, 'phone': '+18186619006', 'display_phone': '(818) 661-9006', 'distance': 1114.3944583066639}, {'id': 'zeV-cwGvnXZ54RjOo7XvXA', 'alias': 'anarbagh-indian-restaurant-westlake-village', 'name': 'Anarbagh Indian Restaurant', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/xmFiGf1Cm-J6d0kAeubWqg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/anarbagh-indian-restaurant-westlake-village?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 655, 'categories': [{'alias': 'indpak', 'title': 'Indian'}], 'rating': 4.5, 'coordinates': {'latitude': 34.15568840533415, 'longitude': -118.7933634082523}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 'location': {'address1': '30853 E Thousand Oaks Blvd', 'address2': None, 'address3': '', 'city': 'Westlake Village', 'zip_code': '91362', 'country': 'US', 'state': 'CA', 'display_address': ['30853 E Thousand Oaks Blvd', 'Westlake Village, CA 91362']}, 'phone': '+18189912128', 'display_phone': '(818) 991-2128', 'distance': 2804.449245753969}, {'id': 'Pv58L33fTIHYFs9hBnnZEg', 'alias': 'old-place-cornell', 'name': 'Old Place', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/0L6nvFWWTUbTuh77gEak3w/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/old-place-cornell?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 1125, 'categories': [{'alias': 'tradamerican', 'title': 'American (Traditional)'}, {'alias': 'steak', 'title': 'Steakhouses'}], 'rating': 4.5, 'coordinates': {'latitude': 34.114552, 'longitude': -118.778234}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '29983 Mulholland Hwy', 'address2': '', 'address3': '', 'city': 'Cornell', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['29983 Mulholland Hwy', 'Cornell, CA 91301']}, 'phone': '+18187069001', 'display_phone': '(818) 706-9001', 'distance': 4370.464628182815}, {'id': 'YXGlXuRFeEbTDgkLEOU3Ow', 'alias': 'mandarin-lotus-agoura-hills', 'name': 'Mandarin Lotus', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/SXsvhBJR9_nPApzyPc5k-g/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/mandarin-lotus-agoura-hills?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 457, 'categories': [{'alias': 'chinese', 'title': 'Chinese'}, {'alias': 'asianfusion', 'title': 'Asian Fusion'}, {'alias': 'gluten_free', 'title': 'Gluten-Free'}], 'rating': 4.5, 'coordinates': {'latitude': 34.144847317156, 'longitude': -118.76275539839}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '5015 Kanan Rd', 'address2': '', 'address3': '', 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['5015 Kanan Rd', 'Agoura Hills, CA 91301']}, 'phone': '+18189919831', 'display_phone': '(818) 991-9831', 'distance': 782.3582384878188}, {'id': '5NkNvC-iosvaoGVMdbK-mg', 'alias': 'plata-taqueria-and-cantina-agoura-hills', 'name': 'Plata Taqueria & Cantina', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/xWNTyFZkGH7bIAEDM9s5fQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/plata-taqueria-and-cantina-agoura-hills?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 641, 'categories': [{'alias': 'cocktailbars', 'title': 'Cocktail Bars'}, {'alias': 'mexican', 'title': 'Mexican'}], 'rating': 4, 'coordinates': {'latitude': 34.1442468, 'longitude': -118.7542527}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '28914 Roadside Dr', 'address2': 'Ste 110', 'address3': '', 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['28914 Roadside Dr', 'Ste 110', 'Agoura Hills, CA 91301']}, 'phone': '+18187359982', 'display_phone': '(818) 735-9982', 'distance': 1184.2466713204178}, {'id': 'b3mKbHTJm4f-etxAEwNv_A', 'alias': 'malibu-wine-hikes-malibu', 'name': 'Malibu Wine Hikes', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/65Z9uexeVhhyJCs4KkD5Vw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/malibu-wine-hikes-malibu?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 1130, 'categories': [{'alias': 'hiking', 'title': 'Hiking'}, {'alias': 'winetastingroom', 'title': 'Wine Tasting Room'}], 'rating': 5, 'coordinates': {'latitude': 34.09897, 'longitude': -118.83317}, 'transactions': [], 'location': {'address1': '32111 Mulholland Hwy', 'address2': None, 'address3': '', 'city': 'Malibu', 'zip_code': '90265', 'country': 'US', 'state': 'CA', 'display_address': ['32111 Mulholland Hwy', 'Malibu, CA 90265']}, 'phone': '+18185784077', 'display_phone': '(818) 578-4077', 'distance': 8811.892275910375}, {'id': 'JLMs2kt6c5rN7ty6v3hn9A', 'alias': 'vincitore-italian-restaurant-agoura-hills', 'name': 'Vincitore Italian Restaurant', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/u7ljqyGqnv4zaWLBhD--UQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/vincitore-italian-restaurant-agoura-hills?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 315, 'categories': [{'alias': 'italian', 'title': 'Italian'}, {'alias': 'gluten_free', 'title': 'Gluten-Free'}, {'alias': 'pizza', 'title': 'Pizza'}], 'rating': 4.5, 'coordinates': {'latitude': 34.156719, 'longitude': -118.757753}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 'location': {'address1': '5869 Kanan Rd', 'address2': '', 'address3': '', 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['5869 Kanan Rd', 'Agoura Hills, CA 91301']}, 'phone': '+18187062200', 'display_phone': '(818) 706-2200', 'distance': 738.3277469772419}, {'id': 'Vmru9PIUMbjF2oweWaMC3Q', 'alias': 'cuckoo-rooster-agoura-hills', 'name': 'Cuckoo Rooster', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/0CdvbiSDPr0jkIGhYHyCtA/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/cuckoo-rooster-agoura-hills?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 293, 'categories': [{'alias': 'chickenshop', 'title': 'Chicken Shop'}, {'alias': 'chicken_wings', 'title': 'Chicken Wings'}], 'rating': 4.5, 'coordinates': {'latitude': 34.15311617, 'longitude': -118.759162}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '5653 Kanan Rd', 'address2': None, 'address3': '', 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['5653 Kanan Rd', 'Agoura Hills, CA 91301']}, 'phone': '+18188519566', 'display_phone': '(818) 851-9566', 'distance': 386.5953617830401}, {'id': '4-IQtK-3P_Vd6c1WFr3TUw', 'alias': 'solé-soups-agoura-hills-6', 'name': 'SoLé SoupS', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/4sWlOrgn6w_fQ5371wOcIg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/sol%C3%A9-soups-agoura-hills-6?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 222, 'categories': [{'alias': 'soup', 'title': 'Soup'}, {'alias': 'salad', 'title': 'Salad'}, {'alias': 'pastashops', 'title': 'Pasta Shops'}], 'rating': 4.5, 'coordinates': {'latitude': 34.1434257, 'longitude': -118.7512937}, 'transactions': ['delivery', 'pickup'], 'price': '$', 'location': {'address1': '28708 Roadside Dr', 'address2': 'Ste H', 'address3': None, 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['28708 Roadside Dr', 'Ste H', 'Agoura Hills, CA 91301']}, 'phone': '+18183091787', 'display_phone': '(818) 309-1787', 'distance': 1445.688342441987}, {'id': 'PLkr4pOEFnrwZ8JrHryQ9g', 'alias': 'tifa-chocolate-and-gelato-westlake-village', 'name': 'Tifa Chocolate & Gelato', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/BU7q7Q71rmFI-5_gdVfM5Q/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/tifa-chocolate-and-gelato-westlake-village?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 261, 'categories': [{'alias': 'desserts', 'title': 'Desserts'}, {'alias': 'gelato', 'title': 'Gelato'}], 'rating': 5, 'coordinates': {'latitude': 34.147988, 'longitude': -118.795841}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '30760 Russell Ranch Rd', 'address2': 'Ste A', 'address3': '', 'city': 'Westlake Village', 'zip_code': '91362', 'country': 'US', 'state': 'CA', 'display_address': ['30760 Russell Ranch Rd', 'Ste A', 'Westlake Village, CA 91362']}, 'phone': '+18057961893', 'display_phone': '(805) 796-1893', 'distance': 3031.197460833151}, {'id': '1T-i8pJyoxCOnXvh0NLMJA', 'alias': 'mediterranean-pita-grill-westlake-village-3', 'name': 'Mediterranean Pita Grill', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/zL-Zcs1jsws2WWHelZn-Qw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/mediterranean-pita-grill-westlake-village-3?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 746, 'categories': [{'alias': 'mediterranean', 'title': 'Mediterranean'}, {'alias': 'lebanese', 'title': 'Lebanese'}], 'rating': 4.5, 'coordinates': {'latitude': 34.1554026482396, 'longitude': -118.794719555152}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 'location': {'address1': '5790 E Lindero Canyon Rd', 'address2': '', 'address3': '', 'city': 'Westlake Village', 'zip_code': '91362', 'country': 'US', 'state': 'CA', 'display_address': ['5790 E Lindero Canyon Rd', 'Westlake Village, CA 91362']}, 'phone': '+18188791279', 'display_phone': '(818) 879-1279', 'distance': 2923.4307589339264}, {'id': 'AEejJpRUJnP_cW7cv5YPiw', 'alias': 'moody-rooster-westlake-village', 'name': 'Moody Rooster', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/IbjZLVNlYZoHI-4k-dinqg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/moody-rooster-westlake-village?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 624, 'categories': [{'alias': 'newamerican', 'title': 'American (New)'}, {'alias': 'seafood', 'title': 'Seafood'}, {'alias': 'bars', 'title': 'Bars'}], 'rating': 4.5, 'coordinates': {'latitude': 34.151416, 'longitude': -118.823317}, 'transactions': ['delivery', 'restaurant_reservation'], 'price': '$$', 'location': {'address1': '2900 Townsgate Rd', 'address2': 'Ste 113', 'address3': None, 'city': 'Westlake Village', 'zip_code': '91361', 'country': 'US', 'state': 'CA', 'display_address': ['2900 Townsgate Rd', 'Ste 113', 'Westlake Village, CA 91361']}, 'phone': '+18053703131', 'display_phone': '(805) 370-3131', 'distance': 5528.780677668498}, {'id': 'w3H8-7ppQ8f7OoFrKr1jBQ', 'alias': 'eloong-dumplings-westlake-village-3', 'name': 'eLoong Dumplings', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/UQ7T8-B82BCkFagL7EQfVw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/eloong-dumplings-westlake-village-3?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 775, 'categories': [{'alias': 'chinese', 'title': 'Chinese'}], 'rating': 4, 'coordinates': {'latitude': 34.1551998, 'longitude': -118.792175}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 'location': {'address1': '30843 Thousand Oaks Blvd', 'address2': None, 'address3': None, 'city': 'Westlake Village', 'zip_code': '91362', 'country': 'US', 'state': 'CA', 'display_address': ['30843 Thousand Oaks Blvd', 'Westlake Village, CA 91362']}, 'phone': '+18185327668', 'display_phone': '(818) 532-7668', 'distance': 2752.0631383832447}, {'id': 'ozrqAIT2ok444zLopsKthA', 'alias': 'maral-cuisine-agoura-hills', 'name': 'Maral Cuisine', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/gLa_w0QxClXpQx_vSfkFFg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/maral-cuisine-agoura-hills?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 322, 'categories': [{'alias': 'mideastern', 'title': 'Middle Eastern'}, {'alias': 'persian', 'title': 'Persian/Iranian'}], 'rating': 4.5, 'coordinates': {'latitude': 34.156176, 'longitude': -118.7564156}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 'location': {'address1': '5843 Kanan Rd', 'address2': None, 'address3': '', 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['5843 Kanan Rd', 'Agoura Hills, CA 91301']}, 'phone': '+18188899495', 'display_phone': '(818) 889-9495', 'distance': 770.958151396959}, {'id': 'ro_zbo12yaMISXU_2AZvOw', 'alias': 'hatch-cafe-and-market-agoura-hills-2', 'name': 'Hatch Cafe & Market', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/4dWti2bbug4o6iLLweJURw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/hatch-cafe-and-market-agoura-hills-2?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 263, 'categories': [{'alias': 'sandwiches', 'title': 'Sandwiches'}, {'alias': 'salad', 'title': 'Salad'}, {'alias': 'cafes', 'title': 'Cafes'}], 'rating': 4.5, 'coordinates': {'latitude': 34.1551167931364, 'longitude': -118.788515016995}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '30651 Thousand Oaks Blvd', 'address2': '', 'address3': None, 'city': 'Agoura Hills', 'zip_code': '91301', 'country': 'US', 'state': 'CA', 'display_address': ['30651 Thousand Oaks Blvd', 'Agoura Hills, CA 91301']}, 'phone': '+18185759000', 'display_phone': '(818) 575-9000', 'distance': 2353.8444774806185}], 'total': 601, 'region': {'center': {'longitude': -118.76323699951172, 'latitude': 34.151871943680234}}}, {'businesses': [{'id': 'd0MDUX9gUR1gC7rmOsS0FQ', 'alias': 'blue-springs-cafe-highland', 'name': 'Blue Springs Cafe', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/Yw81qZNOM2BHFWIbj77hZA/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/blue-springs-cafe-highland?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 228, 'categories': [{'alias': 'tradamerican', 'title': 'American (Traditional)'}], 'rating': 4, 'coordinates': {'latitude': 38.78353, 'longitude': -89.63212}, 'transactions': [], 'price': '$$', 'location': {'address1': '3505 George St', 'address2': '', 'address3': '', 'city': 'Highland', 'zip_code': '62249', 'country': 'US', 'state': 'IL', 'display_address': ['3505 George St', 'Highland, IL 62249']}, 'phone': '+16186545788', 'display_phone': '(618) 654-5788', 'distance': 14566.138896752269}, {'id': 'mQAuvROJT-t8q7aTK5i01g', 'alias': 'weezys-hamel-2', 'name': "Weezy's", 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/lROplIM7EfiLX-leCmRbnQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/weezys-hamel-2?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 40, 'categories': [{'alias': 'bars', 'title': 'Bars'}, {'alias': 'tradamerican', 'title': 'American (Traditional)'}], 'rating': 4.5, 'coordinates': {'latitude': 38.8883870402121, 'longitude': -89.845167373327}, 'transactions': [], 'price': '$', 'location': {'address1': '108 S Old Us Rt 66', 'address2': '', 'address3': '', 'city': 'Hamel', 'zip_code': '62046', 'country': 'US', 'state': 'IL', 'display_address': ['108 S Old Us Rt 66', 'Hamel, IL 62046']}, 'phone': '+16186332228', 'display_phone': '(618) 633-2228', 'distance': 9401.883171368185}, {'id': 'vKw-2Kzc3xLUyGm6g1TFeA', 'alias': 'yellowdog-cafe-and-bar-worden', 'name': 'Yellowdog Cafe & Bar', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/SX9x4u3DQfWUOuJQUjB8ig/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/yellowdog-cafe-and-bar-worden?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 17, 'categories': [{'alias': 'newamerican', 'title': 'American (New)'}, {'alias': 'burgers', 'title': 'Burgers'}, {'alias': 'bars', 'title': 'Bars'}], 'rating': 4.5, 'coordinates': {'latitude': 38.931301, 'longitude': -89.838478}, 'transactions': [], 'price': '$$', 'location': {'address1': '124 E Wall St', 'address2': '', 'address3': '', 'city': 'Worden', 'zip_code': '62097', 'country': 'US', 'state': 'IL', 'display_address': ['124 E Wall St', 'Worden, IL 62097']}, 'phone': '+16184593663', 'display_phone': '(618) 459-3663', 'distance': 10163.515299386845}, {'id': 'zkdKou1wiV3EJCPXczU9SA', 'alias': 'diamond-mineral-springs-highland', 'name': 'Diamond Mineral Springs', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/d1SSAcVq0t-_3LiULBUKuA/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/diamond-mineral-springs-highland?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 25, 'categories': [{'alias': 'tradamerican', 'title': 'American (Traditional)'}], 'rating': 3.5, 'coordinates': {'latitude': 38.830418, 'longitude': -89.670023}, 'transactions': [], 'price': '$$', 'location': {'address1': '1 W Pocahontas Rd', 'address2': '', 'address3': '', 'city': 'Highland', 'zip_code': '62249', 'country': 'US', 'state': 'IL', 'display_address': ['1 W Pocahontas Rd', 'Highland, IL 62249']}, 'phone': '+16186752655', 'display_phone': '(618) 675-2655', 'distance': 8447.08992207648}, {'id': 'TeWi_LQGOIU-PT6TJE6wOQ', 'alias': 'country-inn-cafe-and-motel-livingston', 'name': 'Country Inn Cafe & Motel', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/6UWi7aeqwpjMz42ZB7AnEg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/country-inn-cafe-and-motel-livingston?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 12, 'categories': [{'alias': 'hotels', 'title': 'Hotels'}, {'alias': 'tradamerican', 'title': 'American (Traditional)'}, {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'}], 'rating': 4.5, 'coordinates': {'latitude': 38.966653, 'longitude': -89.757396}, 'transactions': [], 'price': '$', 'location': {'address1': '536 Veterans Memorial Dr', 'address2': '', 'address3': '', 'city': 'Livingston', 'zip_code': '62058', 'country': 'US', 'state': 'IL', 'display_address': ['536 Veterans Memorial Dr', 'Livingston, IL 62058']}, 'phone': '+16186372600', 'display_phone': '(618) 637-2600', 'distance': 9152.024258772275}, {'id': '9ANsv9F1LfKXju4FcAmv-w', 'alias': 'the-marine-diner-marine', 'name': 'The Marine Diner', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/5AxxAbXang5cVf3OBfdE-Q/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/the-marine-diner-marine?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 11, 'categories': [{'alias': 'icecream', 'title': 'Ice Cream & Frozen Yogurt'}, {'alias': 'salad', 'title': 'Salad'}, {'alias': 'tradamerican', 'title': 'American (Traditional)'}], 'rating': 4.5, 'coordinates': {'latitude': 38.786325, 'longitude': -89.7798877}, 'transactions': [], 'location': {'address1': '302 W Division St', 'address2': None, 'address3': '', 'city': 'Marine', 'zip_code': '62061', 'country': 'US', 'state': 'IL', 'display_address': ['302 W Division St', 'Marine, IL 62061']}, 'phone': '+16188872046', 'display_phone': '(618) 887-2046', 'distance': 11695.970773920058}, {'id': 'SBjuU_pzIc1MzNlO_ORZTw', 'alias': 'the-other-place-on-the-hill-hamel', 'name': 'The Other Place On the Hill', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/KFzawahchSDXpXAhWeW3Pg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/the-other-place-on-the-hill-hamel?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 14, 'categories': [{'alias': 'italian', 'title': 'Italian'}, {'alias': 'pizza', 'title': 'Pizza'}], 'rating': 4, 'coordinates': {'latitude': 38.888965, 'longitude': -89.8332995}, 'transactions': [], 'price': '$$', 'location': {'address1': '9180 State Rte 140', 'address2': '', 'address3': '', 'city': 'hamel', 'zip_code': '62097', 'country': 'US', 'state': 'IL', 'display_address': ['9180 State Rte 140', 'hamel, IL 62097']}, 'phone': '+16186332500', 'display_phone': '(618) 633-2500', 'distance': 8377.457293577521}, {'id': 'PONZjvKIkz9bNmqcJffNEg', 'alias': 'twistee-treat-diner-at-the-pink-elephant-livingston', 'name': 'Twistee Treat Diner at The Pink Elephant', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/UvoFQdUic8NL0O103rOL6A/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/twistee-treat-diner-at-the-pink-elephant-livingston?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 4, 'categories': [{'alias': 'icecream', 'title': 'Ice Cream & Frozen Yogurt'}, {'alias': 'tradamerican', 'title': 'American (Traditional)'}], 'rating': 5, 'coordinates': {'latitude': 38.960611, 'longitude': -89.76473}, 'transactions': [], 'location': {'address1': '908 Veterans Memorial Dr', 'address2': '', 'address3': None, 'city': 'Livingston', 'zip_code': '62058', 'country': 'US', 'state': 'IL', 'display_address': ['908 Veterans Memorial Dr', 'Livingston, IL 62058']}, 'phone': '+16186372544', 'display_phone': '(618) 637-2544', 'distance': 8652.640166264166}, {'id': 'NcpI4wMps-il_XptcQp1jg', 'alias': 'maedges-bar-and-grill-alhambra', 'name': "Maedge's Bar & Grill", 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/TaWZkweGdkGb98jLTkdkVg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/maedges-bar-and-grill-alhambra?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 6, 'categories': [{'alias': 'tradamerican', 'title': 'American (Traditional)'}, {'alias': 'bars', 'title': 'Bars'}], 'rating': 3, 'coordinates': {'latitude': 38.888357, 'longitude': -89.726422}, 'transactions': [], 'price': '$', 'location': {'address1': '709 E Main St', 'address2': '', 'address3': '', 'city': 'Alhambra', 'zip_code': '62001', 'country': 'US', 'state': 'IL', 'display_address': ['709 E Main St', 'Alhambra, IL 62001']}, 'phone': '+16184886400', 'display_phone': '(618) 488-6400', 'distance': 919.3463544157581}, {'id': '3Kz4LncueBdqn7gPNVW5iA', 'alias': 'route-66-creamery-hamel', 'name': 'Route 66 Creamery', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/d46aVaqNDA5QJMQPci5D4Q/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/route-66-creamery-hamel?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 9, 'categories': [{'alias': 'desserts', 'title': 'Desserts'}, {'alias': 'icecream', 'title': 'Ice Cream & Frozen Yogurt'}], 'rating': 3.5, 'coordinates': {'latitude': 38.8889723, 'longitude': -89.8447858}, 'transactions': [], 'location': {'address1': '11 S Old Rte 66', 'address2': '', 'address3': None, 'city': 'Hamel', 'zip_code': '62046', 'country': 'US', 'state': 'IL', 'display_address': ['11 S Old Rte 66', 'Hamel, IL 62046']}, 'phone': '+16186332688', 'display_phone': '(618) 633-2688', 'distance': 9420.273547641278}, {'id': 'o8TuB7pH0ffv8UdtRT0arw', 'alias': 'phyls-chet-and-roses-tavern-marine', 'name': "Phyl's Chet & Rose's Tavern", 'image_url': '', 'is_closed': False, 'url': 'https://www.yelp.com/biz/phyls-chet-and-roses-tavern-marine?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 3, 'categories': [{'alias': 'bars', 'title': 'Bars'}], 'rating': 4.5, 'coordinates': {'latitude': 38.7883741, 'longitude': -89.7778649}, 'transactions': [], 'price': '$', 'location': {'address1': '204 N Duncan St', 'address2': '', 'address3': '', 'city': 'Marine', 'zip_code': '62061', 'country': 'US', 'state': 'IL', 'display_address': ['204 N Duncan St', 'Marine, IL 62061']}, 'phone': '+16188874067', 'display_phone': '(618) 887-4067', 'distance': 11425.593232078581}, {'id': 'mukZfb2JR3VmDWcyNMVY-w', 'alias': 'the-back-porch-highland', 'name': 'The Back Porch', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/wDBFC29QS5b2Mx-3BeE2eA/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/the-back-porch-highland?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 11, 'categories': [{'alias': 'newamerican', 'title': 'American (New)'}], 'rating': 3, 'coordinates': {'latitude': 38.8305282592773, 'longitude': -89.6698532104492}, 'transactions': [], 'price': '$$', 'location': {'address1': '1 W Pocahontas Rd', 'address2': '', 'address3': '', 'city': 'Highland', 'zip_code': '62249', 'country': 'US', 'state': 'IL', 'display_address': ['1 W Pocahontas Rd', 'Highland, IL 62249']}, 'phone': '+16186752655', 'display_phone': '(618) 675-2655', 'distance': 8430.052273142457}, {'id': 'Ps8UMPkme6Sx75FtBafKEg', 'alias': 'decamp-station-staunton-2', 'name': 'DeCamp Station', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/P3TLcfB0UtjegVIq9AnoPQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/decamp-station-staunton-2?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 4, 'categories': [{'alias': 'bars', 'title': 'Bars'}], 'rating': 5, 'coordinates': {'latitude': 38.97585, 'longitude': -89.80161}, 'transactions': [], 'price': '$', 'location': {'address1': '8767 State Rte 4', 'address2': '', 'address3': '', 'city': 'Staunton', 'zip_code': '62088', 'country': 'US', 'state': 'IL', 'display_address': ['8767 State Rte 4', 'Staunton, IL 62088']}, 'phone': '+16186372951', 'display_phone': '(618) 637-2951', 'distance': 11455.129351901667}, {'id': 'Eq6N0YYdL11m_Y62aA_APw', 'alias': 'bonnie-and-klides-bar-and-grill-livingston', 'name': 'Bonnie & Klides Bar & Grill', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/0udviQON_pQ1syI9f85dRw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/bonnie-and-klides-bar-and-grill-livingston?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 1, 'categories': [{'alias': 'tradamerican', 'title': 'American (Traditional)'}, {'alias': 'bars', 'title': 'Bars'}], 'rating': 5, 'coordinates': {'latitude': 38.96764, 'longitude': -89.76461}, 'transactions': [], 'location': {'address1': '595 Livingston Ave', 'address2': '', 'address3': None, 'city': 'Livingston', 'zip_code': '62058', 'country': 'US', 'state': 'IL', 'display_address': ['595 Livingston Ave', 'Livingston, IL 62058']}, 'phone': '+16186372699', 'display_phone': '(618) 637-2699', 'distance': 9397.270802186707}, {'id': 'UesP1GuLVXhn-_Xbnx8D7A', 'alias': 'mcdonalds-hamel', 'name': "McDonald's", 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/ylN2_RkbnFV6m5AfdjDeUQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/mcdonalds-hamel?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 13, 'categories': [{'alias': 'coffee', 'title': 'Coffee & Tea'}, {'alias': 'burgers', 'title': 'Burgers'}, {'alias': 'hotdogs', 'title': 'Fast Food'}], 'rating': 2, 'coordinates': {'latitude': 38.8900307357214, 'longitude': -89.8347732424736}, 'transactions': [], 'price': '$', 'location': {'address1': '9191 State Route140', 'address2': None, 'address3': None, 'city': 'Hamel', 'zip_code': '62046', 'country': 'US', 'state': 'IL', 'display_address': ['9191 State Route140', 'Hamel, IL 62046']}, 'phone': '+16186332131', 'display_phone': '(618) 633-2131', 'distance': 8510.33626172447}, {'id': 'f_6cI4MdPem_48WgD1Ofcw', 'alias': 'clara-bs-kitchen-table-belleville', 'name': "Clara B's Kitchen Table", 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/-H2JYArfWuCwnw3ucPZHVQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/clara-bs-kitchen-table-belleville?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 5, 'categories': [{'alias': 'foodtrucks', 'title': 'Food Trucks'}, {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'}], 'rating': 5, 'coordinates': {'latitude': 38.5134231, 'longitude': -89.98252889999999}, 'transactions': [], 'location': {'address1': '106 E Main St', 'address2': '', 'address3': None, 'city': 'Belleville', 'zip_code': '62220', 'country': 'US', 'state': 'IL', 'display_address': ['106 E Main St', 'Belleville, IL 62220']}, 'phone': '+16184161812', 'display_phone': '(618) 416-1812', 'distance': 46598.62399621284}, {'id': 'W61WeIkwGivzH2SrExjuVA', 'alias': 'oak-brook-golf-club-edwardsville', 'name': 'Oak Brook Golf Club', 'image_url': '', 'is_closed': False, 'url': 'https://www.yelp.com/biz/oak-brook-golf-club-edwardsville?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 2, 'categories': [{'alias': 'golf', 'title': 'Golf'}], 'rating': 1, 'coordinates': {'latitude': 38.8301124572754, 'longitude': -89.8358459472656}, 'transactions': [], 'location': {'address1': '9157 Fruit Rd', 'address2': '', 'address3': '', 'city': 'Edwardsville', 'zip_code': '62025', 'country': 'US', 'state': 'IL', 'display_address': ['9157 Fruit Rd', 'Edwardsville, IL 62025']}, 'phone': '+16186565600', 'display_phone': '(618) 656-5600', 'distance': 10557.127995699087}, {'id': '2ikHPAiK-H2OCDhaZAshCQ', 'alias': 'savor-the-southwest-saint-peters', 'name': 'Savor The Southwest', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/Iv52CHO6R_7BGaxDE0vmQw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/savor-the-southwest-saint-peters?adjust_creative=nJ_epROMJ_WNWbvgdx_sQg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=nJ_epROMJ_WNWbvgdx_sQg', 'review_count': 3, 'categories': [{'alias': 'tex-mex', 'title': 'Tex-Mex'}, {'alias': 'foodtrucks', 'title': 'Food Trucks'}], 'rating': 2, 'coordinates': {'latitude': 38.74144, 'longitude': -90.6369717}, 'transactions': [], 'location': {'address1': '6209 Mid Rivers Mall Dr', 'address2': 'Ste 105', 'address3': '', 'city': 'Saint Peters', 'zip_code': '63304', 'country': 'US', 'state': 'MO', 'display_address': ['6209 Mid Rivers Mall Dr', 'Ste 105', 'Saint Peters, MO 63304']}, 'phone': '+16363239580', 'display_phone': '(636) 323-9580', 'distance': 79648.43063496123}], 'total': 18, 'region': {'center': {'longitude': -89.73658561706543, 'latitude': 38.88595471412341}}}]}


x = json.dumps(test)

y = json.loads(x)

# print(y["res"][1])

res = y["res"]

aliases = []

for item in res:
    businesses = item["businesses"]
    # print(businesses)
    for business in businesses:
        # print(business["categories"])
        categories = business["categories"]
        new_list = []
        for category in categories:
            # print(category)
            my_tuple = (category["alias"], category["title"])
            # print(my_tuple)
            new_list.append(my_tuple)
        aliases.append(new_list)


for item in aliases:
    print(item)





# print(y["res"][0]["businesses"][0]["categories"])
#aliases [(alias, title)]
