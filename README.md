# google-earth-geojson
Utility for exporting images from Google Earth Pro using GeoJSON files

WORK IN PROGRESS

## What is it?

Sometimes there's a need to get historical satellite images for a certain area. Most of the services use geoJSON files for specifying the area of interest. Google Earth Pro makes it possible to browse high quality satellite images manually and for free. This utility will make it possible to gather historical satellite images automatically using geoJSON files as the AOI reference.

## TODO:

- [x] Implement a script to convert geojson files to .geprint (Google Earth Pro screenshot utility)
- [ ] Implement GUI automation with pyautogui
- [ ] Implement generating a sequence of .geprint files with dates given as parameters
- [ ] Implement GUI automation for a sequence of .geprint files
- [ ] Implement automatic GIF from the sequence of images taken
- [ ] Implement automatic difference calculation for the sequence of images

