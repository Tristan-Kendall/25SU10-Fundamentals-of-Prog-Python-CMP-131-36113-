#stored variables
warm_water = float(1.5)
tbsp_yeast = float(1)
all_purp_flour = float(4.5)
tbsp_oil = float(2)

#calculating
one_loaf = (warm_water + tbsp_yeast + all_purp_flour + tbsp_oil)
question = (int(input("How many loaves do you want to make?")))

#printing result
print("You need", 
      warm_water * question, "cups of warm water, ",
      tbsp_yeast * question, "tablespoons of yeast, ",
      all_purp_flour * question, "cups of all-purpose flour, ",
      "and", 
      tbsp_oil * question, "tablespoons of oil."
      )
