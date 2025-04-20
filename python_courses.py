# stimated_population = 15
# tehran_information = f"Tehran is Iran capital city. Tehran contains {stimated_population} milions people"

# # print(tehran_information)


building_information = {
  "location" : "Zaeferaniyeh",
  "No" : 125,
  "area" : 1000
}

dtails_building_information = "{location}, {No} and {area} are properties of building_information".format_map(building_information).ljust(80, "😀")

# print(dtails_building_information, "just for test")

main_street = "Ghds"
converted_street_name = main_street.maketrans("Gh", "Qo")
translate_street_name = main_street.translate(converted_street_name)
print(translate_street_name)


print(dtails_building_information.partition(","))
print(dtails_building_information.rfind("😀"))
print(dtails_building_information.rindex("😀"))


last_building_information = "{location}, {No} and {area} are properties of building_information".format_map(building_information).rjust(20, "😮")
print(last_building_information)

print(last_building_information.rsplit(" "))


iran_capital_city = "                  Tehran is Iran capital city.    kkk.                       "
print(iran_capital_city.rstrip())
print(iran_capital_city.strip())
print(iran_capital_city.swapcase())