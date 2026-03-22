This is a demonstration of the geospatial full-stack development work of Zach Dorminey. This web app is a Django app that utilizes a custom PostGIS backend.
This is intended to be used for demonstration purposes only, and therefore the code is not shared on my GitHub repo. It is still in development phase. My beta python package [basal and bark](https://github.com/ZachDorm/basal_and_bark) is implemented in this app as well. The goal is to implement a custom python package with other well known packages for full-stack geospatial development skills to be on full display.
A few important notes of design ideas implemented in this work sample:


This specific app utilizes the Django web development framework with a custom PostGIS database backend that replaces the default PostgreSQL backend.

This app handles spatial and non-spatial data. Users can upload data, as well as data that has been uploaded by the developer.

This app is containerized using Docker, where a conda environment has been curated for this app to specifically build the environment with the proper requirements for this geospatial app. The Windows Subsystem for Linux (WSL) was utilized for development of this app.

Example of some of its capabilites:

The homescreen has a navigation menu with buttons corresponding to various tools throughout the app. The tool shown here is the shapefile upload tool that returns a table with the attribute information of each feature when a file is uploaded.
https://github.com/user-attachments/assets/e55c1dad-28c4-4c7c-8f95-771eb8a819b9


Showing the file upload:
https://github.com/user-attachments/assets/028d6dc5-8a22-4b71-b47d-e44774a58aa0


Mapping capabilities, including Google Earth Engine are plugged into this app:
https://github.com/user-attachments/assets/4efa5bc0-37c2-4b2f-9be1-ec828790c532

