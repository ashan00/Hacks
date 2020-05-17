import requests

file = open("API_Key.txt", "r")
key = file.read()


#Intro to user
print("Hey, this program will help determine if you are inhibiting an symptoms of COVID-19")
print("Please provide a 'yes' or 'no' answer to the following prompts")
print("\nDisclaimer: The information is retrieved from the World Health Organization. The results may not be accurate. \nRefer to a doctor or physician for assurance")

i = 1
while i == 1:
    # symptoms where the user should stop and call 911
    question1 = input("\nAre you showing any symptoms of difficult breathing, severe chest pain, dizziness or confusion? ")

    if question1.lower() == 'no':
        # (severe symptoms)
        i = 2

        while i == 2:
            #question for severe symptoms
            question2 = input("\nAre you showing any signs of a fever, dry cough or tiredness? ")
            # (mild symptoms):
            mild_symptoms = ["aches and pains", "sore throat", "diarrhea", "conjunctivitis","headache", "loss of taste or smell", "a rash on skin", "discolouration of fingers or toes"]

            if question2.lower() == 'yes' or question2.lower() == 'no':

                i = 3
                while i == 3:
                    # question for mild symptoms
                    print("\nAre you showing any of the following signs: ")
                    print(mild_symptoms)
                    question3 = input("")

                    #Analyze Results
                    if question2.lower() =='yes' and question3.lower() =='yes':
                        print("You are showing both severe and mild symptoms that could potentially be a result of COVID-19.")
                        i = 4
                    elif question2.lower() =='yes' and question3.lower() =='no':
                        print("The symptoms you're facing are severe and could potentially be a result of COVID-19.")
                        i = 4
                    elif question2.lower() =='no' and question3.lower() =='yes':
                        print("The symptoms you're facing are mild and could potentially be a result of COVID-19.")
                        i = 4
                    elif question2.lower() =='no' and question3.lower() =='no':
                        print("You are not showing any known symptoms of COVID-19.")
                        i = 4
                    else:
                        print("Invalid Response. Please answer with 'yes' or 'no'")
                        del question3

            else:
                print("Invalid Response. Please answer with 'yes' or 'no'")
                del question2

    elif question1.lower() == 'yes':
        print ("\nPlease Call 911 to medical attention ASAP!!!")
        i = 3

    else:
        print ("Invalid Response. Please answer with 'yes' or 'no'")
        del question1

#will determine nearest hospital to the user
response = input("\nWould you like to find locate any nearby clinics or hospitals? Yes/No ")
if response.lower() == "yes":
    #input for address
    address = input("What's your address?\n")
    address.strip()

    #longitude and latitude of user
    address_data = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + address + ",+CA&key=" + key)

    #conversion of data
    address_data = address_data.json()

    #user location
    user_lat = address_data["results"][0]["geometry"]["location"]["lat"]
    user_lng = address_data["results"][0]["geometry"]["location"]["lng"]

    #print(user_lat)
    #print(user_lng)

    #data for nearby hospitals
    data = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(user_lat) + "," + str(user_lng) + "&radius=1000&type=hospital&key="+ key)

    #conversion of data
    data = data.json()
    i = 0

    hospitals = data["results"][i]["name"]
    count = 0
    try:
        print("The following are nearby clinics and hospitals you may want to seek out to. \n ")
        for names in hospitals:
            count += 1
        while i < count:
            hospitals = data["results"][i]["name"]
            print (hospitals)
            i += 1
    except IndexError:
        print("")

print("\nThank you for using our service! STAY SAFE!!!")
file.close()