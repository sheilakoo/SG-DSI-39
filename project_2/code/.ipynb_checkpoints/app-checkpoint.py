{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a55f516c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "\n",
    "\n",
    "def main():\n",
    "    style = \"\"\"<div style='background-color:pink; padding:12px'>\n",
    "              <h1 style='color:black'>House Price Prediction App</h1>\n",
    "       </div>\"\"\"\n",
    "    st.markdown(style, unsafe_allow_html=True)\n",
    "    left, right = st.columns((2,2))\n",
    "    longitude = left.number_input('Enter the Longitude in negative number',\n",
    "                                  step =1.0, format=\"%.2f\", value=-21.34)\n",
    "    latitude = right.number_input('Enter the Latitude in positive number',\n",
    "                                  step=1.0, format='%.2f', value= 35.84)\n",
    "    housing_median_age = left.number_input('Enter the median age of the building',\n",
    "                                           step=1.0, format='%.1f', value=25.0)\n",
    "    total_rooms = right.number_input('How many rooms are there in the house?',\n",
    "                                     step=1.0, format='%.1f', value=56.0)\n",
    "    total_bedrooms = left.number_input('How many bedrooms are there in the house?',\n",
    "                                       step=1.0, format='%.1f', value=15.0)\n",
    "    population = right.number_input('Population of people within a block',\n",
    "                                    step=1.0, format='%.1f', value=250.0)\n",
    "    households = left.number_input('Poplulation of a household',  step=1.0,\n",
    "                                   format='%.1f',value=43.0)\n",
    "    median_income = right.number_input('Median_income of a household in Dollars',\n",
    "                                       step=1.0, format='%.1f', value=3000.0)    \n",
    "    ocean_proximity = st.selectbox('How close to the sea is the house?',\n",
    "                    ('<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND'))\n",
    "    button = st.button('Predict')\n",
    "    \n",
    "    # if button is pressed\n",
    "    if button:\n",
    "        \n",
    "        # make prediction\n",
    "        result = predict(longitude, latitude, housing_median_age,\n",
    "                         total_rooms,total_bedrooms, population,\n",
    "                         households, median_income, ocean_proximity)\n",
    "        st.success(f'The value of the house is ${result}')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
