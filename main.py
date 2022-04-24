import setup
import retard_speech

""""
Variables
"""
client = setup.get_client()
retard_list = ['thierrybaudet', 'berend210']


"""
Functions
"""
# Function to test if the client object is working.
# Retrieves the user @realWingmans which happens to be our bot.
def test_main():
    response = client.get_user(username='realWingmans')
    print(response)




""""
Executables
"""
#test_main()


