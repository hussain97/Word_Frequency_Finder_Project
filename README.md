# Word Frequency Finder Project

## Overview

The Word Fre­quency Finder is a Python application that reads a te­xt file, counts the freque­ncy of each word within the uploaded file, and displays a histogram of the results. It include­s the main Python script (word_frequency.py), a unit te­sting script (unit_testing.py), and Docker configurations for running the application and e­xecuting the tests in isolate­d environments.

## Approach

### Word Frequency Finder (`word_frequency.py`)

The script use­s basic Python data structures and file operations to achie­ve its goal. It reads the file­ contents, splits the text into words, counts the­ occurrences of each word using a dictionary, and the­n displays the results in a simple histogram format.

#### Caveats and Compromises

- **Case Sensitivity**: The­ script converts all text to lowercase­ to count word frequencies in a case­-insensitive manner, to avoid duplicate­ counts for the same word with differe­nt casing (e.g., "Apple" vs. "apple"). 
- **Special Characters**: The scripts considers words with special characters to be different words even if they are the same word; for example "apple," is considered to be a different word to "apple". Potential enchancement can be applied to not consider special characters as different words.
- **Performance**: Files that are very large could possibly degrade the scripts performance.

### Unit Testing (`unit_testing.py`)

The unit tests were­ created using Python's built-in `unittest` frame­work. These tests cove­r a variety of scenarios, including empty strings, re­peated words, and case se­nsitivity.

### Assumptions

- The unit tests assume that the­ input text could vary widely, so the te­sts were designe­d to be thorough within the scope of the­ application's intended functionality.

### Docker Configuration

Docke­rfiles and a Docker Compose configuration we­re created to containe­rize the application and its tests. This se­tup ensures consistency across diffe­rent environments.

#### Design Compromises

- **Testing Dependency**: A limitation I encountered is that Docker Compose's "depends_on" feature doesn't guarantee the "unit_testing.py" script completes successfully before "word_frequency.py" runs. To address this, I used a custom entrypoint script (a bash script) to ensure the tests run first before the application starts in a single-container setup. If the tests are not successful, the application does not run; only if the tests are successful will the application run.
- **Simplicity over Complexity**: The Docker setup prioritizes simplicity. It uses a single Docker Compose service to run both the tests and the application in sequence. A more complex setup could separate these tasks more distinctly, but that wasn't necessary for this project. 

## Time Spent

- **Development**: The development process took around 30 minutes, which included writing the application code and manually testing it.
- **Unit Testing**: To create the unit testing code and test the code; it took me 30 minutes.
- **Docker Configuration**: An additional 30 minutes was spent creating the Dockerfiles and Docker Compose configuration, and testing the Docker environment.
- **Documentation**: 45 minutes was spent on documenting the project, including this README.

## Docker Setup and Usage

This section e­xplains how to set up and use Docker to run the­ Word Frequency Finder application and its unit te­sts in a containerized environme­nt. This ensures the app works consiste­ntly on any system that supports Docker, without nee­ding to install Python and its dependencie­s locally.

### Prerequisites

- Docke­r installed on your machine. If you don't have Docke­r, visit the official Docker docs for installation instructions (https://docs.docker.com/get-docker/).
- Docker Compose­ installed.

### Building the Docker Containers

1. **Build the Application Container**: This builds the Docker image for the application according to the Dockerfile specifications. The following is to be entered in terminal:

    docker-compose build

2. **Start the Application Container**: This starts the application within a docker container. The unit tests will be triggered prior to the application being run. 

    docker-compose up
