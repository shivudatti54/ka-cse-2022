jsx
// TemperatureConverter.js (The Parent)
import React, { useState } from 'react';
import TemperatureInput from './TemperatureInput';

function TemperatureConverter() {
const [temperature, setTemperature] = useState('');
const [scale, setScale] = useState('c'); // Default scale

// Function to handle Celsius changes
const handleCelsiusChange = (value) => {
setTemperature(value);
setScale('c');
};

// Function to handle Fahrenheit changes
const handleFahrenheitChange = (value) => {
setTemperature(value);
setScale('f');
};

// Conversion functions
function toCelsius(fahrenheit) {
return ((fahrenheit - 32) _ 5) / 9;
}
function toFahrenheit(celsius) {
return (celsius _ 9) / 5 + 32;
}

// Logic to derive the values for both inputs
const celsiusValue = scale === 'f' ? tryConvert(temperature, toCelsius) : temperature;
const fahrenheitValue = scale === 'c' ? tryConvert(temperature, toFahrenheit) : temperature;

return (
<div>
<TemperatureInput
        scale="C"
        temperature={celsiusValue}
        onTemperatureChange={handleCelsiusChange} />
<TemperatureInput
        scale="F"
        temperature={fahrenheitValue}
        onTemperatureChange={handleFahrenheitChange} />
</div>
);
}
export default TemperatureConverter;
