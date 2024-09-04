import streamlit as st
import pickle

#set the title and an image for the web app, we host and with link can access over internet
st.title("Welcome to Franck's Titanic App :ship:")
st.image("Titanic Ship.jpeg")

#load the pre-trained model
#with helps us process efficiently the memory usage, the RAM usage

with open('titanicpickle.pkl', 'rb') as pickle_file:
    pickle_load_file = pickle.load(pickle_file)

#the pickle file is the brain, that helps me predict
#we need to get the pickle file into the directory
#download from jupyter notebook, and drag into VScode streamlit directory (titanicpickle.pkl)

#creating a function to make predictions
def PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    prediction = pickle_load_file.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
    #we need double square brackets, so that system knows it is a list
    print(prediction) #it will print 0 or 1
    return prediction

def main():
    st.title('Titanic Prediction App')
    #design the front end form for user, input fields
    # this is commented to show chatgpt code below
    # Pclass = st.text_input('Passenger Class')
    # Sex = st.text_input('Sex')
    # Age = st.text_input('Age')
    # SibSp = st.text_input('Siblinds aboard')
    # Parch = st.text_input('Parent Child Relationship')
    # Fare = st.text_input('Fare')
    # Embarked = st.text_input('Port of Embarcation')
    
    st.sidebar.header('Input Features')

    # Collect user inputs
    Pclass = st.sidebar.selectbox('Passenger Class', (1, 2, 3), help="Select passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)")
    Sex = st.text_input('Sex')
    Age = st.sidebar.slider('Age', 0, 100, 30, help="Select passenger age")
    SibSp = st.sidebar.number_input('Number of Siblings/Spouses Aboard', min_value=0, max_value=10, value=0, help="Input number of siblings/spouses aboard")
    Parch = st.sidebar.number_input('Number of Parents/Children Aboard', min_value=0, max_value=10, value=0, help="Input number of parents/children aboard")
    Fare = st.sidebar.slider('Ticket Fare', 0.0, 500.0, 32.0, help="Input ticket fare")
    Embarked = st.text_input('Port of Embarcation')

    
    result = " "



    #This code ensures that when the button "Predict" is clicked, the prediction function should be executed
    if st.button('Predict'):
        #convert inputs into appropriate data types
        Pclass = int(Pclass)
        Age = float(Age)
        SibSp = int(SibSp)
        Parch = int(Parch)
        Fare = float(Fare)

        result = PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)

    st.success(f"The output is: {result}")

#calling the function to execute the code in its body
main()
