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
    postcodes: list[str];
    country_id: int;
    country: str;
    admin1: str;
    admin2: str;
    admin3: str;
    admin4: str;

class geoResults:  
    results: list[geolocale];  

class currentWeather:
        temperature: float;
        windspeed: float;
        winddirection: float;
        weathercode: int;
        is_day: int | bool;
        time: str;

class weatherDataTypesHourly: 
    time: list[str];
    temperature_2m: list[float];
    relativehumidity_2m: list[float];
    dewpoint_2m: list[float];
    apparent_temperature: list[float];
    pressure_msl: list[float];
    surface_pressure: list[float];
    cloudcover: list[float];
    cloudcover_low: list[float];
    cloudcover_mid: list[float];
    cloudcover_high: list[float];
    windspeed_10m: list[float];
    windspeed_80m: list[float];
    windspeed_120m: list[float];
    windspeed_180m: list[float];
    winddirection_10m: list[float];
    winddirection_80m: list[float];
    winddirection_120m: list[float];
    winddirection_180m: list[float];
    windgusts_10m: list[float];
    shortwave_radiation: list[float];
    direction_radiation: list[float];
    direction_normal_irradiance: list[float];
    diffuse_radiation: list[float];
    vapor_pressure_deficit: list[float];
    cape: list[float];
    evapotranspiration: list[float];
    et0_fao_evapotranspiration: list[float];
    precipitation: list[float];
    snowfall: list[float];
    precipitation_probability: list[float];
    rain: list[float];
    showers: list[float];
    weathercode: list[float];
    snow_depth: list[float];
    freezlinglevel_height: list[float];
    visibility: list[float];
    soil_temperature_0cm: list[float];
    soil_temperature_6cm: list[float];
    soil_temperature_18cm: list[float];
    soil_temperature_54cm: list[float];
    soil_moisture_0_1cm: list[float];
    soil_moisture_1_3cm: list[float];
    soil_moisture_3_9cm: list[float];
    soil_moisture_9_27cm: list[float];
    soil_moisture_27_81cm: list[float];
    is_day: list[float];


class weatherDataTypesDaily: 
    time: list[str];
    temperature_2m_max: list[float];
    temperature_2m_min: list[float];
    apparent_temperature_max: list[float];
    apparent_temperature_min: list[float];
    precipitation_sum: list[float];
    rain_sum: list[float];
    showers_sum: list[float];
    snowfall_sum: list[float];
    precipitation_hours: list[float];
    precipitation_probability_max: list[float];
    precipitation_probability_min: list[float];
    precipitation_probability_mean: list[float];
    weathercode: list[float];
    sunrise: list[float];
    sunset: list[float];
    windspeed_10m_max: list[float];
    windgusts_10m_max: list[float];
    winddirection_10m_dominant: list[float];
    shortwave_radiation_sum: list[float];
    et0_fao_evapotranspiration: list[float];
    uv_index_max: list[float];
    uv_index_clear_sky_max: list[float];


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
    
class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self