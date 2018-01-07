# GeodesyGina Website Code

This code is used to build the [Geodesy Gina Website](http://geodesygina.com/) using [Pelican](http://docs.getpelican.com/en/stable/).  

### Installing the code:
1. Fork this repository
2. Install dependencies:

        pip install -r requirements.txt

### To generate new content:
1. Make changes to rst files in content folder, or add new rst file.
2. Type:

        pelican content

### To view the new content on your local machine:
1. Change to content directory:

        cd content/

2. Start your local server:

        python -m pelican.server

3. Go to your internet brower and type the following url:

        http://localhost:8000/
