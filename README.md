# Celestial_Dragon

Welcome to the year 2912, where your data science skills are needed to solve a cosmic mystery. We've received a transmission from four light years away and things aren't looking good. The Celestial Dragon was an interstellar passenger liner launched a month ago. 
With almost 13,000 passengers on board, the vessel set out on its maiden voyage 
transporting emigrants from our solar system to three newly habitable exoplanets 
orbiting nearby stars.
While rounding Alpha Centauri en route to its first destination—the torrid 55 
Cancri E—the unwary Celestial Dragon collided with a space-time anomaly hidden 
within a dust cloud. Though the ship stayed intact, almost half of the passengers 
were transported to an alternate dimension!
Your task is to predict whether a passenger was transported to an alternate 
dimension during the Celestial Dragon’s collision with the space-time anomaly.

train.csv - Personal records for about two-thirds (~8700) of the passengers, to be 
used as training data.

PassengerId - A unique Id for each passenger. Each Id takes the form gggg_pp 
where gggg indicates a group the passenger is travelling with and pp is their 
number within the group. People in a group are often family members, but not 
always.

HomePlanet - The planet the passenger departed from, typically their planet of 
permanent residence.

CryoSleep - Indicates whether the passenger elected to be put into suspended 
animation for the duration of the voyage. Passengers in cryosleep are confined to 
their cabins.

Cabin - The cabin number where the passenger is staying. Takes the form 
deck/num/side, where side can be either P for Port or S for Starboard.
Destination - The planet the passenger will be debarking to.

Age - The age of the passenger.

VIP - Whether the passenger has paid for special VIP service during the voyage.
RoomService, FoodCourt, ShoppingMall, Spa, VRDeck - Amount the passenger has 
billed at each of the Celestial Dragon’s many luxury amenities.

Name - The first and last names of the passenger.

Transported - Whether the passenger was transported to another dimension. This 
is the target, the column you are trying to predict.

test.csv - Personal records for the remaining one-third (~4300) of the passengers, 
to be used as test data. Your task is to predict the value of Transported for the 
passengers in this set.

sample_submission.csv - A submission file in the correct format.

PassengerId - Id for each passenger in the test set.

Transported - The target. For each passenger, predict either True or False
