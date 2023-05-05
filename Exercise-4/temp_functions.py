def fahr_to_celsius(temp_fahrenheit):
    """
    Function for converting temperature in Fahrenheit to Celsius.
    
    Parameters
    ----------
    temp_fahrenheit: <numerical>
        Temperature in Fahrenheit
    
    Returns
    -------
    <float>
        converted temperature in Celsius.
    """
    # Convert the value to Celsius using the equation below     
    converted_temp = (temp_fahrenheit - 32) / 1.8
    # Return the result 
    return converted_temp


def temp_classifier(temp_celsius):
    """
    Function for classfying temperature into 4 classes returning values 0, 1, 2, 3 depending on the input temperature in Celsius.
    
    Parameters
    ----------
    temp_celsius: <numerical>
    
    Returns
    -------
    <interger>
        classified value
    """
    # Check if the temperature is below negative 2 then return 0
    if temp_celsius < -2:
        return 0
    # Check if the temperature is equal or above negative 2 AND below 2, then return integer 1
    elif (temp_celsius >= -2) and (temp_celsius < 2):
        return 1
    # Check if the temperature is equal or above 2 AND below 15, then return interger 2
    elif (temp_celsius >= 2) and (temp_celsius < 15):
        return 2
    # Check if the temperature is equal or below 15, then return integer 3
    elif (temp_celsius >= 15): 
        return 3