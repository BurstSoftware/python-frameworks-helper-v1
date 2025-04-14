import streamlit as st

# Define the frameworks and their descriptions organized by category
frameworks_data = {
    "Web Development Frameworks": {
        "Django": "A high-level, full-stack framework with ORM, authentication, and admin panel.",
        "Flask": "A lightweight micro-framework, highly customizable with extensions.",
        "FastAPI": "A modern, high-performance framework for APIs with async support.",
        "Tornado": "An asynchronous web framework for handling long-lived connections.",
        "Bottle": "An ultra-lightweight micro-framework with no external dependencies.",
        "Pyramid": "A flexible framework that scales from small to large apps.",
        "CherryPy": "A minimalist framework integrating with Python’s object-oriented nature.",
        "Sanic": "An async web framework built for speed, inspired by Flask.",
        "Falcon": "A bare-bones framework for high-performance REST APIs.",
        "Masonite": "A modern framework with ORM and command-line tools.",
        "Hug": "A simplified API framework with minimal boilerplate.",
        "Quart": "An async-compatible reimplementation of Flask.",
        "Starlette": "A lightweight ASGI framework, the foundation for FastAPI."
    },
    "Data Science and Machine Learning Frameworks": {
        "TensorFlow": "A comprehensive framework for deep learning and large-scale ML.",
        "PyTorch": "A dynamic computation graph-based framework for research and production.",
        "scikit-learn": "A general-purpose ML library for classification, regression, etc.",
        "Keras": "A high-level API for neural networks, integrated into TensorFlow.",
        "Pandas": "A data manipulation and analysis library with DataFrames.",
        "NumPy": "A core library for numerical computing with arrays.",
        "SciPy": "A scientific computing library built on NumPy.",
        "XGBoost": "An optimized gradient boosting framework for ML.",
        "LightGBM": "A fast, distributed gradient boosting framework.",
        "CatBoost": "A gradient boosting library with categorical feature support.",
        "Theano": "An older deep learning framework for symbolic math.",
        "Statsmodels": "A statistical modeling library for data exploration.",
        "Dask": "A parallel computing library for scaling Pandas/NumPy.",
        "Ray": "A distributed computing framework for scalable ML."
    },
    "Automation and Scripting Frameworks": {
        "Ansible": "An IT automation tool for configuration and deployment.",
        "Robot Framework": "A keyword-driven test automation framework.",
        "Fabric": "A high-level library for system admin tasks over SSH.",
        "SaltStack": "A configuration management and remote execution framework.",
        "Invoke": "A Pythonic task execution tool for CLI scripts.",
        "PyAutoGUI": "A GUI automation library for mouse/keyboard control.",
        "Schedule": "A simple library for scheduling repetitive tasks.",
        "Celery": "A distributed task queue for asynchronous task execution."
    },
    "GUI Development Frameworks": {
        "Tkinter": "Python’s standard GUI library, simple and lightweight.",
        "PyQt": "A rich, cross-platform GUI framework based on Qt.",
        "Kivy": "A framework for multitouch, cross-platform apps.",
        "wxPython": "A cross-platform GUI toolkit with native look and feel.",
        "PySide": "Official Python bindings for Qt, an alternative to PyQt.",
        "Dear PyGui": "A fast, GPU-accelerated GUI framework.",
        "Toga": "A cross-platform GUI toolkit for native apps.",
        "PySimpleGUI": "A simplified wrapper for rapid GUI prototyping.",
        "Eel": "A framework for desktop apps with HTML/CSS/JS frontends."
    },
    "Game Development Frameworks": {
        "Pygame": "A popular library for 2D game development.",
        "Pyglet": "A cross-platform library for games and multimedia.",
        "Arcade": "A modern 2D game development library.",
        "Panda3D": "A full-featured 3D game engine.",
        "Ren’Py": "A visual novel engine for storytelling games.",
        "Cocos2d": "A framework for 2D games and graphics."
    },
    "Networking and Asynchronous Frameworks": {
        "Twisted": "An event-driven networking engine.",
        "asyncio": "A standard library for async code.",
        "AIOHTTP": "An async HTTP client/server framework.",
        "Gevent": "A coroutine-based concurrency library.",
        "Eventlet": "A concurrent networking library.",
        "SocketIO": "A real-time communication library."
    },
    "Testing Frameworks": {
        "pytest": "A robust testing framework with plugins.",
        "unittest": "Python’s built-in testing framework.",
        "nose2": "An extension of unittest with additional features.",
        "doctest": "A module for testing docstring examples.",
        "Hypothesis": "A property-based testing framework.",
        "Tox": "A tool for testing across multiple environments.",
        "Behave": "A BDD framework for plain-language tests."
    },
    "Microservices and API Development Frameworks": {
        "Nameko": "A microservices framework with RPC support.",
        "Connexion": "A Swagger/OpenAPI framework for Flask.",
        "APIStar": "A lightweight API framework.",
        "Vibora": "A discontinued but notable fast async framework.",
        "Responder": "A modern API framework with async support."
    },
    "Scientific Computing and Visualization Frameworks": {
        "Matplotlib": "A foundational plotting library.",
        "Seaborn": "A statistical data visualization library.",
        "Plotly": "An interactive graphing library.",
        "Bokeh": "A framework for web-ready plots.",
        "SymPy": "A symbolic mathematics library.",
        "NetworkX": "A library for network and graph analysis.",
        "Holoviews": "A high-level visualization framework."
    },
    "Database and ORM Frameworks": {
        "SQLAlchemy": "A powerful ORM and SQL toolkit.",
        "Peewee": "A lightweight ORM for simple operations.",
        "Django ORM": "Django’s built-in ORM.",
        "Tortoise ORM": "An async ORM for asyncio frameworks.",
        "PonyORM": "An intuitive ORM with Pythonic syntax.",
        "Gino": "A lightweight async ORM."
    },
    "Cloud and DevOps Frameworks": {
        "Boto3": "AWS SDK for Python.",
        "Google Cloud SDK": "Python libraries for Google Cloud.",
        "Apache Libcloud": "A unified cloud management interface.",
        "Pulumi": "An infrastructure-as-code framework.",
        "OpenStack": "A cloud OS with Python APIs."
    },
    "Security and Penetration Testing Frameworks": {
        "Scapy": "A packet manipulation framework.",
        "Impacket": "A library for network protocol classes.",
        "Pwntools": "A framework for exploit development.",
        "PyCrypto": "A legacy cryptographic library.",
        "Cryptography": "A modern cryptographic library."
    },
    "Natural Language Processing (NLP) Frameworks": {
        "NLTK": "A comprehensive library for text processing.",
        "spaCy": "An industrial-strength NLP library.",
        "TextBlob": "A simplified NLP library.",
        "Gensim": "A framework for topic modeling.",
        "Hugging Face Transformers": "A state-of-the-art NLP framework."
    },
    "Mobile App Development Frameworks": {
        "Kivy": "A cross-platform framework for mobile apps.",
        "BeeWare": "A suite for native mobile app development.",
        "Buildozer": "A tool for packaging Kivy apps."
    },
    "Content Management and Blogging Frameworks": {
        "Wagtail": "A modern CMS built on Django.",
        "Mezzanine": "A Django-based CMS with blogging features.",
        "Pelican": "A static site generator for blogs.",
        "Lektor": "A static CMS with an admin interface."
    },
    "IoT and Hardware Frameworks": {
        "MicroPython": "A lightweight Python for microcontrollers.",
        "PySerial": "A library for serial port communication.",
        "RPi.GPIO": "A framework for Raspberry Pi GPIO.",
        "Adafruit CircuitPython": "A framework for microcontroller programming.",
        "Paho MQTT": "A Python client for MQTT protocol."
    },
    "Real-Time and Streaming Frameworks": {
        "Faust": "A stream processing library.",
        "Streamz": "A framework for real-time data pipelines.",
        "Pulsar": "A Python client for Apache Pulsar.",
        "Dramatiq": "A task queue system.",
        "RQ": "A simple job queuing library."
    },
    "Computer Vision Frameworks": {
        "OpenCV": "A comprehensive library for computer vision.",
        "Pillow": "A library for basic image manipulation.",
        "SimpleCV": "A wrapper over OpenCV for prototyping.",
        "imageio": "A library for image data formats.",
        "Mahotas": "A fast computer vision library."
    },
    "Audio and Signal Processing Frameworks": {
        "Librosa": "A library for music and audio analysis.",
        "PyDub": "A high-level audio manipulation library.",
        "Audiotools": "A collection of audio tools.",
        "PyAudio": "A library for audio recording/playback.",
        "Madmom": "A framework for real-time audio processing."
    },
    "Blockchain and Cryptocurrency Frameworks": {
        "Web3.py": "A library for Ethereum blockchain interaction.",
        "Brownie": "A framework for Ethereum smart contracts.",
        "PyCryptodome": "A cryptographic library for blockchain.",
        "Blockcypher": "A Python SDK for blockchain APIs."
    },
    "Geospatial and Mapping Frameworks": {
        "GeoPandas": "An extension of Pandas for geospatial data.",
        "Folium": "A library for interactive maps.",
        "Cartopy": "A geospatial mapping library.",
        "Shapely": "A library for geometric objects.",
        "Pyproj": "A tool for cartographic projections."
    },
    "Robotics Frameworks": {
        "ROS (rospy)": "A framework for robot software development.",
        "PyRobot": "A lightweight robotics framework.",
        "Robotics Toolbox": "A library for robot kinematics.",
        "PyBullet": "A physics simulation framework."
    },
    "Workflow and Pipeline Frameworks": {
        "Airflow": "A workflow orchestration platform.",
        "Luigi": "A framework for batch job pipelines.",
        "Prefect": "A modern workflow management system.",
        "Kedro": "A framework for data science pipelines.",
        "Dagster": "A data orchestration framework."
    },
    "Simulation and Modeling Frameworks": {
        "SimPy": "A discrete-event simulation framework.",
        "DEAP": "A framework for evolutionary computation.",
        "Mesa": "An agent-based modeling framework.",
        "Pyomo": "An optimization modeling language.",
        "Brian2": "A simulator for spiking neural networks."
    },
    "E-commerce and Business Frameworks": {
        "Saleor": "A Django-based e-commerce framework.",
        "Shuup": "An open-source e-commerce platform.",
        "Oscar": "A domain-driven e-commerce solution."
    },
    "Educational and Interactive Learning Frameworks": {
        "Brython": "A Python implementation for the browser.",
        "Trinket": "A framework for interactive Python code.",
        "Mu": "A simple Python editor for beginners."
    },
    "Documentation and Static Analysis Frameworks": {
        "Sphinx": "A documentation generator for Python.",
        "Pydocstyle": "A tool for docstring conventions.",
        "Flake8": "A linting framework for style enforcement.",
        "Mypy": "A static type checker for Python."
    },
    "Reinforcement Learning Frameworks": {
        "Stable-Baselines3": "Reliable RL algorithms with PyTorch.",
        "RLlib": "A scalable RL library.",
        "Gym": "A toolkit for RL environments.",
        "Dopamine": "A research-oriented RL framework.",
        "TF-Agents": "A TensorFlow-based RL library."
    },
    "Privacy and Anonymity Frameworks": {
        "Torpy": "A Tor client for anonymous networking.",
        "PySyft": "A framework for privacy-preserving ML.",
        "Opacus": "A PyTorch library for differential privacy.",
        "Anonypylib": "A library for data anonymization."
    },
    "Quantum Computing Frameworks": {
        "Qiskit": "IBM’s framework for quantum computing.",
        "Cirq": "Google’s quantum circuit framework.",
        "PennyLane": "A library for quantum ML.",
        "PyQuil": "A framework for quantum programming.",
        "ProjectQ": "A quantum computing framework."
    },
    "Social Media and Web Interaction Frameworks": {
        "Tweepy": "A library for Twitter API access.",
        "PRAW": "A Python Reddit API wrapper.",
        "Instapy": "An Instagram automation framework.",
        "Selenium": "A web automation and testing tool.",
        "MechanicalSoup": "A lightweight web scraping library."
    },
    "Workflow Automation for Creative Tools": {
        "PyAutoCAD": "A library for AutoCAD automation.",
        "Blender Python API": "A scripting interface for Blender.",
        "PyNuke": "A Python API for Nuke.",
        "Krita Scripting": "A Python API for Krita."
    },
    "Synthetic Data Generation Frameworks": {
        "Faker": "A library for generating fake data.",
        "SDV": "A framework for synthetic tabular data.",
        "Synthpop": "A tool for synthetic population generation.",
        "Pydbgen": "A library for random database tables."
    },
    "Ethical Hacking and Red Teaming Frameworks": {
        "SQLmap": "An automated SQL injection tool.",
        "Metasploit (pymetasploit3)": "Python bindings for Metasploit.",
        "Nmap (python-nmap)": "A Python interface for Nmap.",
        "Fsociety": "A collection of hacking tools."
    },
    "Data Compression and File Handling Frameworks": {
        "PyZMQ": "Python bindings for ZeroMQ messaging.",
        "Brotli": "A library for Brotli compression.",
        "Py7zr": "A library for 7z archives.",
        "Zipfile": "A standard library for ZIP files."
    },
    "Text-to-Speech and Speech Recognition Frameworks": {
        "gTTS": "A Google Text-to-Speech library.",
        "Pyttsx3": "An offline text-to-speech library.",
        "SpeechRecognition": "A library for speech recognition.",
        "Vosk": "An offline speech recognition toolkit."
    },
    "Game AI and Procedural Content Generation Frameworks": {
        "NEAT-Python": "A framework for evolving game AI.",
        "Arcade Learning Environment": "A framework for Atari games.",
        "PCGRL": "A RL-based framework for game levels."
    },
    "Low-Code and Rapid Development Frameworks": {
        "Streamlit": "A framework for data apps.",
        "Anvil": "A low-code web app platform.",
        "PyWebIO": "A library for interactive web apps."
    },
    "Distributed Systems and Messaging Frameworks": {
        "Dask.distributed": "A distributed computing extension.",
        "PyZMQ": "A messaging library (repeated).",
        "RabbitMQ (pika)": "A Python client for RabbitMQ.",
        "Kafka-Python": "A Python client for Kafka.",
        "Nameko": "A microservices framework (repeated)."
    },
    "Animation and Motion Graphics Frameworks": {
        "Manim": "A mathematical animation engine.",
        "Pyglet": "A library for animations (repeated).",
        "MoviePy": "A library for video editing.",
        "Gizeh": "A vector graphics library."
    },
    "Healthcare and Medical Imaging Frameworks": {
        "Pydicom": "A library for DICOM files.",
        "Nibabel": "A library for neuroimaging data.",
        "ITK": "A framework for medical image processing.",
        "Monai": "A PyTorch-based medical imaging framework."
    },
    "Energy and Environmental Modeling Frameworks": {
        "PyPSA": "A framework for power system analysis.",
        "Pvlib-python": "A library for photovoltaic systems.",
        "Climlab": "A framework for climate modeling.",
        "Windpowerlib": "A library for wind power modeling."
    },
    "Educational Simulation Frameworks": {
        "PyGame Zero": "A simplified game framework.",
        "EduPython": "An educational Python environment.",
        "Turtle": "A standard library for graphics."
    },
    "API Testing and Mocking Frameworks": {
        "Requests-Mock": "A library for mocking HTTP requests.",
        "HTTPretty": "An HTTP client mocking tool.",
        "Responses": "A library for mocking responses.",
        "Tavern": "An API testing framework."
    },
    "Code Refactoring and Optimization Frameworks": {
        "Black": "A code formatting framework.",
        "isort": "A library for sorting imports.",
        "Autopep8": "A tool for PEP 8 formatting.",
        "Pyupgrade": "A tool for upgrading syntax."
    },
    "Natural Disaster and Risk Analysis Frameworks": {
        "HazPy": "A framework for seismic hazard analysis.",
        "PyEarthquake": "A library for earthquake data.",
        "OpenQuake": "A platform for seismic risk modeling."
    },
    "Astronomy and Space Science Frameworks": {
        "AstroPy": "A core library for astronomy.",
        "SunPy": "A framework for solar physics.",
        "Poliastro": "A library for astrodynamics.",
        "Skyfield": "A tool for astronomical computations."
    },
    "Chemistry and Molecular Modeling Frameworks": {
        "RDKit": "A cheminformatics toolkit.",
        "Open Babel": "A chemical file format library.",
        "PySCF": "A framework for quantum chemistry.",
        "Chemlab": "A library for molecular visualization."
    },
    "Supply Chain and Logistics Frameworks": {
        "Pyomo": "An optimization framework (repeated).",
        "OR-Tools": "A library for routing and optimization.",
        "PuLP": "A linear programming library.",
        "SimPy": "A simulation framework (repeated)."
    },
    "Augmented Analytics Frameworks": {
        "H2O.ai": "An automated ML platform.",
        "Auto-sklearn": "An automated ML toolkit.",
        "TPOT": "A pipeline optimization tool.",
        "PyCaret": "A low-code ML library."
    },
    "Digital Forensics Frameworks": {
        "Volatility": "A memory forensics framework.",
        "Pytsk": "A file system forensics library.",
        "DFIRWizard": "A forensics automation framework.",
        "Autopsy": "A forensic platform with Python plugins."
    },
    "Synthetic Biology Frameworks": {
        "PySCeS": "A simulator for cellular systems.",
        "Tellurium": "A systems biology framework.",
        "Antimony": "A synthetic biology modeling tool."
    },
    "Music Composition and Analysis Frameworks": {
        "Music21": "A toolkit for musicology.",
        "Mingus": "A library for music theory.",
        "Abjad": "A framework for music composition.",
        "FoxDot": "A live-coding music framework."
    },
    "Legal Tech and Document Analysis Frameworks": {
        "LexNLP": "An NLP library for legal texts.",
        "DocTR": "A framework for document text recognition.",
        "PyPDF2": "A library for PDF manipulation."
    },
    "Urban Planning and Smart Cities Frameworks": {
        "UrbanSim": "A platform for urban simulation.",
        "SUMOPy": "A traffic modeling extension.",
        "CityEnergyAnalyst": "An energy modeling framework."
    },
    "Materials Science Frameworks": {
        "ASE": "An atomic simulation environment.",
        "Pymatgen": "A materials analysis library.",
        "Matplotlib": "A plotting library (repeated)."
    },
    "Behavioral Analysis Frameworks": {
        "PsychoPy": "A framework for psychology experiments.",
        "OpenSesame": "An experiment-building framework.",
        "Nengo": "A neural simulation framework."
    },
    "Cryptanalysis Frameworks": {
        "Cryptography": "A cryptographic library (repeated).",
        "PyCryptanalysis": "A library for cipher analysis.",
        "SageMath": "A mathematical software with cryptanalysis."
    },
    "Oceanography and Marine Science Frameworks": {
        "PyNIO": "A library for scientific data formats.",
        "PyFerret": "A data visualization tool.",
        "Oceans": "A utility collection for oceanography.",
        "Xarray": "A framework for multi-dimensional arrays."
    },
    "Sports Analytics Frameworks": {
        "Sportsipy": "A library for sports statistics.",
        "PyBall": "A basketball data API wrapper.",
        "Trueskill": "A rating system for matchmaking.",
        "OpenStats": "A statistical analysis tool."
    },
    "Food Science and Nutrition Frameworks": {
        "Nutripy": "A library for nutritional analysis.",
        "FoodData Central": "A USDA database client.",
        "PyMeal": "A framework for meal planning."
    },
    "Wearable Tech and Fitness Frameworks": {
        "Fitparse": "A library for FIT file parsing.",
        "PyHealth": "A framework for healthcare data.",
        "Activityio": "A library for activity data."
    },
    "Archaeology and Historical Data Frameworks": {
        "ArchPy": "A framework for archaeological data.",
        "PyChron": "A library for geochronology.",
        "HistPy": "A toolkit for historical data."
    },
    "Fashion and Textile Design Frameworks": {
        "Fashion-MNIST": "A dataset for fashion ML.",
        "PyPattern": "A library for textile patterns.",
        "Seamly2D": "A pattern-making software."
    },
    "Neuroscience Frameworks": {
        "MNE-Python": "A framework for MEG/EEG data.",
        "BluePyOpt": "An optimization framework.",
        "NEURON": "A simulation environment."
    },
    "Gaming Simulation Frameworks": {
        "PySC2": "A StarCraft II interface.",
        "OpenSpiel": "A game environment collection.",
        "PLE": "A learning environment for games."
    },
    "Agriculture and Farming Frameworks": {
        "PyCrop": "A library for crop simulation.",
        "Agrisat": "A framework for satellite data.",
        "FarmOS": "A farm management software."
    },
    "Art Conservation and Restoration Frameworks": {
        "PyArtRestoration": "A library for art conservation.",
        "Gmic-py": "A library for art enhancement.",
        "ArtPy": "A toolkit for art metadata."
    },
    "Aerospace and Flight Simulation Frameworks": {
        "AeroPy": "A library for aerodynamics.",
        "JSBSim": "A flight dynamics model.",
        "PyFlight": "A framework for flight planning.",
        "AirSim": "A simulator for drones."
    },
    "Political Science and Election Analysis Frameworks": {
        "PyVote": "A library for voting systems.",
        "GerryChain": "A framework for redistricting.",
        "PolPy": "A toolkit for political data."
    },
    "Paleontology and Fossil Analysis Frameworks": {
        "PyRate": "A framework for fossil analysis.",
        "PaleoPy": "A library for paleoclimate data.",
        "Divvy": "A tool for diversification analysis."
    },
    "Retail and Customer Analytics Frameworks": {
        "PyRetail": "A library for sales forecasting.",
        "CustomerPy": "A framework for customer analysis.",
        "Basket": "A market basket analysis tool."
    },
    "Journalism and Media Analysis Frameworks": {
        "Newspaper3k": "A library for article extraction.",
        "PyMediainfo": "A framework for media metadata.",
        "Textacy": "An NLP library for media text."
    },
    "Transportation and Traffic Analysis Frameworks": {
        "TraffPy": "A library for traffic simulation.",
        "PyTrans": "A framework for transit modeling.",
        "OSMnx": "A tool for street network analysis."
    },
    "Veterinary Science Frameworks": {
        "VetPy": "A library for epidemiology.",
        "PyAnimal": "A framework for behavior analysis.",
        "BioVet": "A toolkit for biological data."
    },
    "Cryptocurrency Trading Frameworks": {
        "CCXT": "A cryptocurrency trading library.",
        "Freqtrade": "A crypto trading bot framework.",
        "PyAlgoTrade": "An algorithmic trading library."
    },
    "Photonics and Optics Frameworks": {
        "PyOptics": "A library for optical design.",
        "LightPipes": "A framework for light propagation.",
        "PyFresnel": "A tool for diffraction calculations."
    },
    "Exoplanet and Astrobiology Frameworks": {
        "ExoPy": "A library for exoplanet modeling.",
        "Batma": "A framework for atmosphere analysis.",
        "AstroBioPy": "A toolkit for habitability analysis."
    },
    "Hydrology and Water Resource Frameworks": {
        "PyHSPF": "A hydrological simulation interface.",
        "HydroPy": "A library for water resource modeling.",
        "PySWMM": "A wrapper for storm water modeling.",
        "FloPy": "A framework for groundwater modeling."
    },
    "Linguistic and Phonetics Frameworks": {
        "Pyphon": "A library for phonetic transcription.",
        "LingPy": "A framework for linguistics.",
        "Praat-Py": "A phonetics analysis interface.",
        "PhonemePy": "A tool for phoneme segmentation."
    },
    "Ethical AI and Fairness Frameworks": {
        "Fairlearn": "A library for fairness in ML.",
        "AIF360": "A framework for bias detection.",
        "EthicML": "A toolkit for ethical ML evaluation."
    },
    "Satellite and Remote Sensing Frameworks": {
        "Rasterio": "A library for raster data.",
        "PySAT": "A framework for satellite analysis.",
        "Sentinelsat": "A tool for Sentinel imagery.",
        "Pyresample": "A library for resampling data."
    },
    "Gaming Hardware and Emulation Frameworks": {
        "PyNES": "A framework for NES emulation.",
        "PyPSX": "A library for PlayStation emulation.",
        "PyGamepad": "A framework for game controllers."
    },
    "Industrial Automation Frameworks": {
        "PyModbus": "A Modbus protocol implementation.",
        "Opcua": "A library for OPC UA communication.",
        "PyPLC": "A framework for PLC programming."
    },
    "Time Series Analysis Frameworks": {
        "Prophet": "A forecasting framework by Facebook.",
        "Statsmodels.tsa": "A time series analysis module.",
        "PyTS": "A library for time series classification.",
        "Darts": "A framework for forecasting models."
    },
    "Augmented Writing and Text Generation Frameworks": {
        "TextGenRNN": "A text generation library.",
        "Grok": "A text generation framework.",
        "PyMarkov": "A Markov chain text generator."
    },
    "Cybersecurity Visualization Frameworks": {
        "PyVis": "A library for network visualizations.",
        "NetGraph": "A tool for network plotting.",
        "PyShark": "A wrapper for Wireshark visualization."
    },
    "Virtual Assistant Frameworks": {
        "Mycroft": "An open-source voice assistant.",
        "JARVIS": "A lightweight virtual assistant.",
        "PyAssistant": "A modular assistant framework."
    },
    "Graph Theory and Network Analysis Frameworks": {
        "Graph-tool": "An efficient graph library.",
        "igraph": "A high-performance graph library.",
        "Snap.py": "A network analysis wrapper.",
        "PyGraphviz": "A graph visualization interface."
    },
    "Synthetic Media Frameworks": {
        "PyFakeWebcam": "A virtual webcam library.",
        "SV2TTS": "A voice cloning framework.",
        "DeepFaceLab": "A face-swapping framework.",
        "PyGan": "A simplified GAN framework."
    },
    "Ergonomics and Human Factors Frameworks": {
        "PyErgo": "A library for ergonomic analysis.",
        "HumanPy": "A framework for movement modeling.",
        "PyPosture": "A tool for posture analysis."
    },
    "Photonics and Laser Technology Frameworks": {
        "PyLaser": "A library for laser simulation.",
        "PyNLO": "A framework for nonlinear optics.",
        "OptiPy": "A toolkit for optical design."
    },
    "Cultural Heritage Frameworks": {
        "PyHeritage": "A library for heritage data.",
        "Archivematica": "A digital preservation system.",
        "PyMuse": "A framework for museum data."
    },
    "Crowdsourcing and Collaborative Frameworks": {
        "PyBossa": "A crowdsourcing framework.",
        "CrowdPy": "A library for response aggregation.",
        "TurPy": "A Mechanical Turk client."
    },
    "Synthetic Chemistry Frameworks": {
        "ChemPy": "A library for chemical kinetics.",
        "AutoDockTools": "A framework for drug design.",
        "Pybel": "A wrapper for Open Babel."
    },
    "Smart Home and IoT Integration Frameworks": {
        "Home Assistant": "A home automation platform.",
        "PyZigBee": "A library for ZigBee devices.",
        "PyMiLight": "A framework for smart bulbs."
    },
    "Behavioral Economics Frameworks": {
        "EconPy": "A library for behavioral economics.",
        "PyBEAM": "A framework for Bayesian estimation.",
        "ChoicePy": "A toolkit for choice modeling."
    },
    "Planetary Science Frameworks": {
        "PyPlanets": "A library for planetary calculations.",
        "SpicePy": "A wrapper for NASA’s SPICE toolkit.",
        "PyMars": "A framework for Mars analysis."
    },
    "Volcanology and Geothermal Frameworks": {
        "PyVolc": "A library for volcanic modeling.",
        "ToughIO": "An interface for geothermal simulation.",
        "PySeismo": "A framework for seismic data."
    },
    "Culinary Arts and Recipe Automation Frameworks": {
        "PyCuisine": "A library for recipe parsing.",
        "FlavorPy": "A framework for flavor pairing.",
        "CookPy": "A toolkit for cooking automation."
    },
    "Textile Manufacturing Frameworks": {
        "TexPy": "A library for textile patterns.",
        "PyLoom": "A framework for loom modeling.",
        "FiberPy": "A tool for fiber analysis."
    },
    "Oceanography Instrumentation Frameworks": {
        "PyOcean": "A library for sensor data.",
        "SeaPy": "A framework for underwater vehicles.",
        "PyADCP": "A tool for ADCP data."
    },
    "Sleep Science Frameworks": {
        "PySleep": "A library for sleep analysis.",
        "SleepPy": "A framework for sensor data.",
        "YASA": "A package for sleep scoring."
    },
    "Synthetic Ecosystems Frameworks": {
        "EcoPy": "A library for ecological modeling.",
        "PyEcoSim": "A framework for ecosystem simulation.",
        "BioNetPy": "A tool for biological networks."
    },
    "Haptics and Tactile Feedback Frameworks": {
        "PyHaptics": "A library for haptic simulation.",
        "HapPy": "A framework for tactile design.",
        "PyTouch": "A tool for touch sensor data."
    },
    "Heritage Language Preservation Frameworks": {
        "PyLangPreserve": "A library for language documentation.",
        "ELAN-Py": "An interface for linguistic annotation.",
        "PyLexis": "A framework for lexical analysis."
    },
    "Extreme Weather Frameworks": {
        "PyStorm": "A library for storm tracking.",
        "HurrPy": "A framework for hurricane modeling.",
        "PyTornado": "A tool for tornado analysis."
    },
    "Space Weather Frameworks": {
        "PySpaceWeather": "A library for solar wind analysis.",
        "SunPy": "A framework for space weather (repeated).",
        "PyAurora": "A tool for auroral simulation."
    },
    "Glaciology and Ice Dynamics Frameworks": {
        "PyGlacier": "A library for glacier simulation.",
        "OGGM": "A framework for glacier modeling.",
        "PyIce": "A tool for ice sheet dynamics."
    },
    "Olfactory and Scent Analysis Frameworks": {
        "PySmell": "A library for scent classification.",
        "ScentPy": "A framework for chemical modeling.",
        "OlfactPy": "A tool for sensor integration."
    },
    "Forensic Anthropology Frameworks": {
        "PyForensicAnthro": "A library for skeletal analysis.",
        "BonePy": "A framework for 3D bone modeling.",
        "AnthroPy": "A toolkit for anthropological data."
    },
    "Synthetic Psychology Frameworks": {
        "PsyPy": "A library for psychological simulation.",
        "CogPy": "A framework for cognitive modeling.",
        "PyMind": "A tool for behavior prediction."
    },
    "Urban Soundscape Frameworks": {
        "PySoundscape": "A library for noise analysis.",
        "AcoustiPy": "A framework for acoustic modeling.",
        "SoundPy": "A tool for environmental audio."
    },
    "Paleoclimate Frameworks": {
        "PyPaleoClimate": "A library for climate reconstruction.",
        "ClimaPy": "A framework for proxy modeling.",
        "PaleoPy": "A tool for paleoclimate visualization (repeated)."
    },
    "Microfluidics Frameworks": {
        "PyMicrofluidics": "A library for channel design.",
        "FluidPy": "A framework for fluid dynamics.",
        "MicroPy": "A tool for microscale processes."
    },
    "Synthetic Sociology Frameworks": {
        "SocPy": "A library for sociological modeling.",
        "PySociety": "A framework for social simulation.",
        "AgentPy": "A tool for agent-based modeling."
    },
    "Astrogeology Frameworks": {
        "PyAstroGeo": "A library for planetary geology.",
        "CraterPy": "A framework for crater detection.",
        "GeoPyMars": "A tool for Mars geology."
    },
    "Neuromorphic Computing Frameworks": {
        "PyNEST": "An interface for neural simulation.",
        "BindsNET": "A framework for spiking networks.",
        "PyNN": "A tool for neuromorphic integration."
    },
    "Soil Science and Agronomy Frameworks": {
        "PySoil": "A library for soil analysis.",
        "SoilPy": "A framework for moisture simulation.",
        "AgroPy": "A tool for crop-soil studies."
    },
    "Chronobiology Frameworks": {
        "PyChronoBio": "A library for circadian analysis.",
        "BioRhythmPy": "A framework for biological clocks.",
        "ChronoPy": "A tool for phase analysis."
    },
    "Synthetic Geography Frameworks": {
        "GeoSynthPy": "A library for landscape generation.",
        "PyGeoSim": "A framework for spatial simulation.",
        "SpatialPy": "A tool for geographic modeling."
    },
    "Optogenetics Frameworks": {
        "PyOpto": "A library for optogenetic modeling.",
        "OptoPy": "A framework for light-based control.",
        "NeuroOptoPy": "A tool for neural integration."
    },
    "Psychometrics Frameworks": {
        "PyPsych": "A library for psychometric analysis.",
        "PsyMetricPy": "A framework for test scoring.",
        "FactorPy": "A tool for factor analysis."
    },
    "Atmospheric Chemistry Frameworks": {
        "PyAtmoChem": "A library for chemistry simulations.",
        "ChemPy": "A framework for atmospheric modeling (repeated).",
        "AirPy": "A tool for air quality analysis."
    },
    "Synthetic Oceanography Frameworks": {
        "PyOceanSim": "A library for ocean simulation.",
        "MarinePy": "A framework for marine ecosystems.",
        "OceanSynthPy": "A tool for synthetic datasets."
    },
    "Exogeology Frameworks": {
        "ExoGeoPy": "A library for exoplanet geology.",
        "PyLunar": "A framework for lunar modeling.",
        "AstroRockPy": "A tool for rocky exoplanets."
    },
    "Taste and Flavor Science Frameworks": {
        "PyTaste": "A library for taste modeling.",
        "FlavorChemPy": "A framework for flavor analysis.",
        "TasteSynthPy": "A tool for flavor generation."
    },
    "Synthetic Anthropology Frameworks": {
        "AnthroSynthPy": "A library for cultural simulation.",
        "PyCulture": "A framework for cultural diffusion.",
        "EthnoPy": "A tool for ethnographic analysis."
    },
    "Hydrometeorology Frameworks": {
        "PyHydroMet": "A library for rainfall modeling.",
        "MetPy": "A framework for weather analysis.",
        "RainPy": "A tool for precipitation simulation."
    },
    "Synthetic Neurology Frameworks": {
        "NeuroSynthPy": "A library for neural simulation.",
        "PyBrainSim": "A framework for brain activity.",
        "SynthNeuroPy": "A tool for synthetic neural data."
    },
    "Petrology Frameworks": {
        "PyPetro": "A library for petrological analysis.",
        "RockPy": "A framework for rock simulation.",
        "PetroSynthPy": "A tool for synthetic petrology."
    },
    "Synthetic Epidemiology Frameworks": {
        "EpiPy": "A library for outbreak simulation.",
        "PyEpidemic": "A framework for disease modeling.",
        "SynthEpiPy": "A tool for synthetic datasets."
    },
    "Acoustical Engineering Frameworks": {
        "PyAcoustics": "A library for acoustic processing.",
        "AcouPy": "A framework for sound wave modeling.",
        "SoundFieldPy": "A tool for spatial audio."
    },
    "Synthetic Demography Frameworks": {
        "DemoPy": "A library for demographic modeling.",
        "PyPopulation": "A framework for population simulation.",
        "SynthDemoPy": "A tool for synthetic demographics."
    },
    "Chronostratigraphy Frameworks": {
        "PyChronoStrat": "A library for stratigraphic analysis.",
        "StratPy": "A framework for fossil layers.",
        "TimeScalePy": "A tool for geological timelines."
    },
    "Synthetic Paleontology Frameworks": {
        "PaleoSynthPy": "A library for fossil simulation.",
        "PyFossil": "A framework for ecosystem modeling.",
        "ExtinctPy": "A tool for extinction analysis."
    },
    "Behavioral Neuroscience Frameworks": {
        "BehavNeuroPy": "A library for neuroscience experiments.",
        "PyBehavior": "A framework for behavior modeling.",
        "NeuroBehavPy": "A tool for data integration."
    },
    "Synthetic Climatology Frameworks": {
        "ClimaSynthPy": "A library for climate simulation.",
        "PyClimateSim": "A framework for climate dynamics.",
        "SynthClimaPy": "A tool for synthetic datasets."
    },
}

# Streamlit app
st.title("Python Frameworks Explorer")
st.write("Choose a framework category to view its associated frameworks and descriptions.")

# Display dropdown for categories at the top of the main app
category = st.selectbox("Select a Category", list(frameworks_data.keys()))

# Display a list of frameworks and their descriptions for the selected category
if category:
    st.subheader(f"Frameworks in {category}")
    frameworks = frameworks_data[category]
    
    # Iterate through each framework and display its name and description
    for framework, description in frameworks.items():
        st.markdown(f"**{framework}**")
        st.write(description)
        st.markdown("---")  # Add a horizontal line for separation between frameworks
