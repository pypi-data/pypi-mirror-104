# GHS Hazard pictograms

Based on [GHS_hazard_pictograms](https://en.wikipedia.org/wiki/GHS_hazard_pictograms) Wikipedia article

# Install 

pip install ghs_hazard_pictogram

# Usage

```python
>>>from ghs_hazard_pictogram import Hazard
>>>Hazard.all() # List all hazards
>>>Hazard(code='class8') # Return hazard with code 'class8'
>>>Hazard.search('division') # Return hazard with attribute containing 'division' case insesitive
>>>Hazard(code='class8').get_pictogram() # returns full path to the svg file
```

# Licence

This code is licenced under MIT, and the content is licenced under Creative Commons.

# Bug or request

Please create an issue on [Github](https://github.com/fmeurou/ghs_hazard_pictogram)