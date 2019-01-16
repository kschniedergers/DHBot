from bs4 import BeautifulSoup
import requests


class DHMenuScraper:
    menuLink = "https://nutrition.sa.ucsc.edu/menuSamp.asp?"
    dHallCodes = {
        "nineten" : "locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall",
        "cowellstevenson" : "locationNum=05&locationName=Cowell+Stevenson+Dining+Hall"
    }

    def __init__(self):
        return

    def getFullMenu(self, dHall, mealNum):

        fullUrl = self.menuLink + self.dHallCodes[dHall]
        page = requests.get(fullUrl)

        soup = BeautifulSoup(page.text, 'html.parser')
        # finds the correct table for the meal
        meal = soup.find_all('div', class_='menusampmeals')[mealNum]

        # variables for loop to find the meals
        current = meal
        firstTableFound = True

        while current is not None:
            # print(current)
            if current.name == 'table':
                if firstTableFound:
                    firstTableFound = False
                else:
                    # we are done
                    break

            current = current.parent


        rawMeals = current.find_all('div', class_='menusamprecipes')

        finalMeals = []

        for meal in rawMeals:
            finalMeals.append(meal.string)

        return finalMeals