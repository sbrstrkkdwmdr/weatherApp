class geolocale: 
    id: int;
    name: str;
    latitude: float;
    longitude: float;
    elevation: float;
    feature_code: str;
    country_code: str;
    admin1_id: int;
    admin3_id: int;
    admin4_id: int;
    timezone: str;
    population: int;
    postcodes: list; # of strings
    country_id: int;
    country: str;
    admin1: str;
    admin2: str;
    admin3: str;
    admin4: str;

class geoResults:  
    results: list; # of geoLocale 

class currentWeather:
        temperature: float;
        windspeed: float;
        winddirection: float;
        weathercode: int;
        is_day: int | bool;
        time: str;

class weatherDataTypesHourly: 
    time: list;
    temperature_2m: list;
    relativehumidity_2m: list;
    dewpoint_2m: list;
    apparent_temperature: list;
    pressure_msl: list;
    surface_pressure: list;
    cloudcover: list;
    cloudcover_low: list;
    cloudcover_mid: list;
    cloudcover_high: list;
    windspeed_10m: list;
    windspeed_80m: list;
    windspeed_120m: list;
    windspeed_180m: list;
    winddirection_10m: list;
    winddirection_80m: list;
    winddirection_120m: list;
    winddirection_180m: list;
    windgusts_10m: list;
    shortwave_radiation: list;
    direction_radiation: list;
    direction_normal_irradiance: list;
    diffuse_radiation: list;
    vapor_pressure_deficit: list;
    cape: list;
    evapotranspiration: list;
    et0_fao_evapotranspiration: list;
    precipitation: list;
    snowfall: list;
    precipitation_probability: list;
    rain: list;
    showers: list;
    weathercode: list;
    snow_depth: list;
    freezlinglevel_height: list;
    visibility: list;
    soil_temperature_0cm: list;
    soil_temperature_6cm: list;
    soil_temperature_18cm: list;
    soil_temperature_54cm: list;
    soil_moisture_0_1cm: list;
    soil_moisture_1_3cm: list;
    soil_moisture_3_9cm: list;
    soil_moisture_9_27cm: list;
    soil_moisture_27_81cm: list;
    is_day: list;


class weatherDataTypesDaily: 
    time: list;
    temperature_2m_max: list;
    temperature_2m_min: list;
    apparent_temperature_max: list;
    apparent_temperature_min: list;
    precipitation_sum: list;
    rain_sum: list;
    showers_sum: list;
    snowfall_sum: list;
    precipitation_hours: list;
    precipitation_probability_max: list;
    precipitation_probability_min: list;
    precipitation_probability_mean: list;
    weathercode: list;
    sunrise: list;
    sunset: list;
    windspeed_10m_max: list;
    windgusts_10m_max: list;
    winddirection_10m_dominant: list;
    shortwave_radiation_sum: list;
    et0_fao_evapotranspiration: list;
    uv_index_max: list;
    uv_index_clear_sky_max: list;


class weatherDataUnitsHourly: 
    time: str;
    temperature_2m: str;
    relativehumidity_2m: str;
    dewpoint_2m: str;
    apparent_temperature: str;
    pressure_msl: str;
    surface_pressure: str;
    cloudcover: str;
    cloudcover_low: str;
    cloudcover_mid: str;
    cloudcover_high: str;
    windspeed_10m: str;
    windspeed_80m: str;
    windspeed_120m: str;
    windspeed_180m: str;
    winddirection_10m: str;
    winddirection_80m: str;
    winddirection_120m: str;
    winddirection_180m: str;
    windgusts_10m: str;
    shortwave_radiation: str;
    direction_radiation: str;
    direction_normal_irradiance: str;
    diffuse_radiation: str;
    vapor_pressure_deficit: str;
    cape: str;
    evapotranspiration: str;
    et0_fao_evapotranspiration: str;
    precipitation: str;
    snowfall: str;
    precipitation_probability: str;
    rain: str;
    showers: str;
    weathercode: str;
    snow_depth: str;
    freezlinglevel_height: str;
    visibility: str;
    soil_temperature_0cm: str;
    soil_temperature_6cm: str;
    soil_temperature_18cm: str;
    soil_temperature_54cm: str;
    soil_moisture_0_1cm: str;
    soil_moisture_1_3cm: str;
    soil_moisture_3_9cm: str;
    soil_moisture_9_27cm: str;
    soil_moisture_27_81cm: str;
    is_day: str;


class weatherDataUnitsDaily: 
    temperature_2m_max: str;
    temperature_2m_min: str;
    apparent_temperature_max: str;
    apparent_temperature_min: str;
    precipitation_sum: str;
    rain_sum: str;
    showers_sum: str;
    snowfall_sum: str;
    precipitation_hours: str;
    precipitation_probability_max: str;
    precipitation_probability_min: str;
    precipitation_probability_mean: str;
    weathercode: str;
    sunrise: str;
    sunset: str;
    windspeed_10m_max: str;
    windgusts_10m_max: str;
    winddirection_10m_dominant: str;
    shortwave_radiation_sum: str;
    et0_fao_evapotranspiration: str;
    uv_index_max: str;
    uv_index_clear_sky_max: str;

class weatherData: 
    latitude: float;
    longitude: float;
    generationtime_ms: float;
    utc_offset_seconds: int;
    timezone: str;
    timezone_abbreviation: str;
    elevation: float;
    current_weather: currentWeather;
    hourly: weatherDataTypesHourly;
    hourly_units: weatherDataUnitsHourly;
    daily: weatherDataTypesDaily;
    daily_units: weatherDataUnitsDaily;
    error: bool;
    reason: str;