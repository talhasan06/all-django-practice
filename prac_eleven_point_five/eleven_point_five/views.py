from django.shortcuts import render

# Create your views here.
def index(request):
    meals = [
        {
        "strMeal": "BeaverTails",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg", 
        "idMeal": "52928",
        "reciepe": "Fried dough topped with cinnamon and sugar resembling the tail of a beaver. Originated in Killaloe, Ontario, it is a sweet treat often found at outdoor winter events around Canada."
        },
        {
            "strMeal": "Breakfast Potatoes", 
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",  
            "reciepe": "A hearty breakfast side dish made by pan frying potatoes seasoned with onions, bell peppers, paprika, garlic powder, salt, and pepper. Often enjoyed with eggs and meat."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923", 
            "reciepe": "A sweet and sticky tart pastry from Canada filled with butter, sugar, eggs, raisins, and other ingredients baked in a tart shell. A classic treat often served around the holidays." 
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "reciepe": "Smoked meat sandwich originating from Montreal. Made by curing beef brisket with spices and smoke. Usually served stacked high on rye bread with mustard."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924", 
            "reciepe": "No-bake dessert bars named after Nanaimo, British Columbia with three layers - a wafer and nut crumb base, a custard flavor buttercream middle, and a chocolate ganache top."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930", 
            "reciepe": "A French-Canadian layered casserole dish made with ground beef, sweet corn, and mashed potatoes. Often served as a hearty family meal." 
        },
        {  
            "strMeal": "Pouding chomeur",  
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "reciepe": "A warm Quebec specialty dessert with maple syrup poured over a cake batter baked with a sugar and butter syrup to create a gooey and sticky sweet treat."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804", 
            "reciepe": "Iconic Canadian fast food dish consisting of french fries topped with cheese curds and hot gravy. Originated in rural Quebec in the 1950s."
        }, 
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "reciepe": "Type of meat pie from Nova Scotia made from grated and rinsed potatoes along with onion, meat, and spices baked into a hearty casserole."
        },
        {
            "strMeal": "Split Pea Soup", 
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg", 
            "idMeal": "52925",
            "reciepe": "Thick soup made by boiling split peas along with various vegetables like carrots, onions, potatoes and herbs. Often includes a ham bone."
        }
    ]
    return render(request,'index.html',{'meals':meals})