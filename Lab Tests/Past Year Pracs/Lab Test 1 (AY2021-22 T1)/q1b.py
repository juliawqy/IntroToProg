# Name:
# Email ID:

def is_official_language(country, language):
    # Replace the code below with your implementation.

    Belgium = ["Belgium", "Dutch, French, German"]
    Canada = ["Canada", "English, French"]
    Philippines = ["Philippines", "English, Filipino"]
    Singapore = ["Singapore", "Chinese, English, Malay, Tamil"]

    countries = [Belgium, Canada, Philippines, Singapore]
    
    for country_index in range(4):
        if country == countries[country_index][0]:
            if countries[country_index][1].find(language) != -1:
                return True
            else:
                return False