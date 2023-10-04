from bs4 import BeautifulSoup
import requests
import re
import time

def get_cats():

    animal = requests.get("https://www.laanimalservices.com/search/pets?items_per_page=24&field_species[28]=28&sort_order=ASC").text
    friends = requests.get("https://bestfriends.org/adopt/adopt-our-sanctuary/cats?title=&field_animal_primary_breed_target_id=All&field_animal_secondary_breed_target_id=All&field_animal_age_value=All&field_animal_size_value=All&field_animal_color_target_id=All&field_animal_sex_value=All&sort_by=field_rg_created_date_value&page=10").text
    monica = requests.get("https://petharbor.com/results.asp?searchtype=ADOPT&start=4&nopod=1&grid=1&friends=1&samaritans=1&nosuccess=0&rows=12&imgres=detail&tWidth=300&view=sysadm.v_snmn&nobreedreq=1&nomax=1&nocustom=1&fontface=sans-serif&fontsize=12&text=2f2d2c&link=00619b&vlink=00619b&alink=fd7e14&col_hdr_fg=ffffff&col_hdr_bg=009da6&miles=20&shelterlist=%27SNMN%27&atype=&where=type_CAT&PAGE=1").text
    pet = requests.get("https://www.adoptapet.com/pet-search?speciesId=2&radius=35&postalCode=90230&city=Los+Angeles&state=CA&caredForBy[0]=shelter&needHomeFast=true").text
    animal_soup = BeautifulSoup(animal, "lxml")
    friends_soup = BeautifulSoup(friends, "lxml")
    monica_soup = BeautifulSoup(monica, "lxml")
    pet_soup = BeautifulSoup(pet, "lxml")

    animal_results = animal_soup.find_all("a", class_ = "pet-results__pet")
    friends_results = friends_soup.find_all("div", class_ = "card")
    monica_results = monica_soup.find_all("div", class_ = "gridResult")
    pet_results = pet_soup.find_all("a", class_ = "relative")

    for cat4 in pet_results:
        name = cat4.find("p", class_ = "font-bold").text.strip()
        info = cat4["href"]
        pet_shelter = requests.get(info).text
        pet_shelter_soup = BeautifulSoup(pet_shelter, "lxml")
        pet_shelter_results = pet_shelter_soup.find("span", class_ = "link-content-kin-teal-2")
        shelter = pet_shelter_results.text
        print(f"{shelter}:\nCat: {name}\nMore Info: {info}\n")

    for cat1 in animal_results:
        name = cat1.find("div", class_ = "pet-results__pet-name").text
        info = "https://www.laanimalservices.com" + cat1["href"]
        shelter = "LA Animal Services"
        print(f"{shelter}:\nCat: {name}\nMore Info: {info}\n")

    for cat2 in friends_results:
        name = cat2.find("span").text
        info = "https://www.bestfriends.org" + cat2.a["href"]
        shelter = "Best Friends"
        print(f"{shelter}:\nCat: {name}\nMore Info: {info}\n")

    for cat3 in monica_results:
        name = cat3.find("div", class_ = "gridText").text
        name, number = name.split(" ")
        number = number[1:-2]
        info = "https://petharbor.com/pet.asp?uaid=SNMN." + number
        shelter = "Santa Monica Pet Harbor"
        print(f"{shelter}:\nCat: {name}\nMore Info: {info}\n")


if __name__ == "__main__":
    while True:
        get_cats()
        time.sleep(60)

